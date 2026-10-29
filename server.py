"""odoo-mymemory-ai: local knowledge-graph memory exposed over MCP.

Source of truth is plain text under data/ (versioned in git):
  data/docs/<id>.md       one note per node, with a small "key: value" header
  data/relations.jsonl    one {"src", "rel", "dst"} edge per line, sorted

index.db is a disposable SQLite FTS5 index rebuilt from data/ at startup.
"""

import datetime
import json
import re
import sqlite3
from pathlib import Path

from mcp.server.mcpserver import MCPServer

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "data" / "docs"
RELATIONS = ROOT / "data" / "relations.jsonl"
INDEX = ROOT / "index.db"

ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
HEADER_KEYS = ("title", "tags", "project", "updated")


def check_id(id: str) -> str:
    if not ID_RE.match(id):
        raise ValueError(f"invalid id {id!r}: use letters, digits, '.', '_' or '-' (e.g. 'sale.order')")
    return id


def write_doc(id: str, meta: dict, body: str) -> None:
    header = "\n".join(f"{k}: {meta.get(k, '')}" for k in HEADER_KEYS)
    (DOCS / f"{id}.md").write_text(f"---\n{header}\n---\n\n{body.strip()}\n")


def read_doc(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    meta = {}
    if text.startswith("---\n") and "\n---\n" in text[4:]:
        header, body = text[4:].split("\n---\n", 1)
        for line in header.splitlines():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
        return meta, body.strip()
    return meta, text.strip()


def load_relations() -> set[tuple[str, str, str]]:
    if not RELATIONS.exists():
        return set()
    edges = set()
    for line in RELATIONS.read_text().splitlines():
        if line.strip():
            e = json.loads(line)
            edges.add((e["src"], e["rel"], e["dst"]))
    return edges


def save_relations(edges: set[tuple[str, str, str]]) -> None:
    lines = [json.dumps({"src": s, "rel": r, "dst": d}, ensure_ascii=False) for s, r, d in sorted(edges)]
    RELATIONS.write_text("\n".join(lines) + ("\n" if lines else ""))


def open_index() -> sqlite3.Connection:
    DOCS.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(INDEX, check_same_thread=False)
    db.executescript("""
        DROP TABLE IF EXISTS docs_fts;
        CREATE VIRTUAL TABLE docs_fts USING fts5(id, title, tags, project, body, tokenize='unicode61');
    """)
    for path in DOCS.glob("*.md"):
        index_doc(db, path.stem, *read_doc(path))
    db.commit()
    return db


def index_doc(db: sqlite3.Connection, id: str, meta: dict, body: str) -> None:
    db.execute("DELETE FROM docs_fts WHERE id = ?", (id,))
    db.execute(
        "INSERT INTO docs_fts (id, title, tags, project, body) VALUES (?, ?, ?, ?, ?)",
        (id, meta.get("title", ""), meta.get("tags", ""), meta.get("project", ""), body),
    )


def fts_query(text: str, op: str) -> str:
    # Quote each term so input like "sale.order" or "a-b" is not parsed as FTS syntax.
    terms = [t.replace('"', '""') for t in text.split() if t.strip()]
    return f" {op} ".join(f'"{t}"' for t in terms)


db = open_index()

mcp = MCPServer(
    "odoo-mymemory-ai",
    instructions=(
        "Persistent local memory (knowledge graph) shared across sessions. "
        "Before exploring a codebase or topic, call `search` to reuse what is already known. "
        "After learning something durable (how a module works, a decision, a gotcha), "
        "store it with `save_doc` and connect related nodes with `link`. "
        "Use stable ids such as 'odoo.sale.order' or 'odoo.flow.invoice'. Keep notes concise."
    ),
)


@mcp.tool()
def save_doc(id: str, title: str, body: str, tags: str = "", project: str = "") -> str:
    """Create or replace a note (graph node). body is markdown; tags is comma-separated."""
    check_id(id)
    meta = {"title": title, "tags": tags, "project": project, "updated": datetime.date.today().isoformat()}
    write_doc(id, meta, body)
    index_doc(db, id, meta, body)
    db.commit()
    return f"saved {id}"


@mcp.tool()
def append_doc(id: str, text: str) -> str:
    """Append text to an existing note without rewriting it."""
    path = DOCS / f"{check_id(id)}.md"
    if not path.exists():
        raise ValueError(f"no note {id!r}; create it with save_doc")
    meta, body = read_doc(path)
    meta["updated"] = datetime.date.today().isoformat()
    body = f"{body}\n\n{text.strip()}"
    write_doc(id, meta, body)
    index_doc(db, id, meta, body)
    db.commit()
    return f"appended to {id}"


@mcp.tool()
def get_doc(id: str) -> dict:
    """Read one note in full, plus its direct relations."""
    path = DOCS / f"{check_id(id)}.md"
    if not path.exists():
        raise ValueError(f"no note {id!r}")
    meta, body = read_doc(path)
    return {"id": id, **meta, "body": body, "relations": neighbors(id)}


@mcp.tool()
def search(query: str, limit: int = 8, project: str = "") -> list[dict]:
    """Full-text search over notes. Returns ids, titles and short snippets (not full bodies)."""
    sql = (
        "SELECT id, title, tags, snippet(docs_fts, 4, '[', ']', '…', 24) FROM docs_fts "
        "WHERE docs_fts MATCH ?" + (" AND project = ?" if project else "") + " ORDER BY rank LIMIT ?"
    )
    for op in ("AND", "OR"):  # fall back to any-term match when all-terms finds nothing
        q = fts_query(query, op)
        if not q:
            return []
        params = (q, project, limit) if project else (q, limit)
        rows = db.execute(sql, params).fetchall()
        if rows:
            break
    return [{"id": r[0], "title": r[1], "tags": r[2], "snippet": r[3]} for r in rows]


@mcp.tool()
def list_docs(project: str = "", tag: str = "") -> list[dict]:
    """List all notes (id + title), optionally filtered by project or tag."""
    out = []
    for path in sorted(DOCS.glob("*.md")):
        meta, _ = read_doc(path)
        if project and meta.get("project") != project:
            continue
        if tag and tag not in [t.strip() for t in meta.get("tags", "").split(",")]:
            continue
        out.append({"id": path.stem, "title": meta.get("title", ""), "updated": meta.get("updated", "")})
    return out


@mcp.tool()
def delete_doc(id: str) -> str:
    """Delete a note and every relation touching it."""
    path = DOCS / f"{check_id(id)}.md"
    path.unlink(missing_ok=True)
    db.execute("DELETE FROM docs_fts WHERE id = ?", (id,))
    db.commit()
    save_relations({e for e in load_relations() if id not in (e[0], e[2])})
    return f"deleted {id}"


@mcp.tool()
def link(src: str, rel: str, dst: str) -> str:
    """Add a directed relation src --rel--> dst, e.g. ('odoo.sale.order', 'creates', 'odoo.stock.picking')."""
    check_id(src), check_id(dst)
    edges = load_relations()
    edges.add((src, rel.strip(), dst))
    save_relations(edges)
    return f"{src} --{rel}--> {dst}"


@mcp.tool()
def unlink(src: str, rel: str, dst: str) -> str:
    """Remove a relation."""
    edges = load_relations()
    edges.discard((src, rel.strip(), dst))
    save_relations(edges)
    return f"removed {src} --{rel}--> {dst}"


@mcp.tool()
def neighbors(id: str, depth: int = 1) -> list[dict]:
    """Relations around a node, following edges in both directions up to `depth` hops (max 3)."""
    edges = load_relations()
    seen, frontier, found = {id}, {id}, set()
    for _ in range(max(1, min(depth, 3))):
        nxt = set()
        for s, r, d in edges:
            if s in frontier or d in frontier:
                found.add((s, r, d))
                nxt |= {s, d} - seen
        seen |= nxt
        frontier = nxt
    return [{"src": s, "rel": r, "dst": d} for s, r, d in sorted(found)]


if __name__ == "__main__":
    mcp.run()
