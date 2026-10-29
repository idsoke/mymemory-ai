"""Import project docs (e.g. D:\\dokumentasi\\<project>\\*.md) into data/ as notes.

docs_import.json lists one or more sources; the markdown files in each
source_dir are the source of truth. Each file becomes one summary note (<id>)
plus one note per section (<id>.NN-<slug>). A source's "sections" picks how a
file is split: "numbered" uses "## N. Heading" lines, "h2" uses every "## "
heading outside code fences, numbered in order. Notes are rewritten only when
their content changes, section notes that no longer exist in the source are
deleted (with every relation touching them), and the structural relations
(index/berisi, <workspace>/<workspace_rel>, <id>/punya_bagian) are kept in sync.

Run by sync.sh before committing; safe to run by hand:
    .venv/bin/python import_docs.py [--dry-run] [--only NAME]
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "docs_import.json"
HEADER_KEYS = ("title", "tags", "project", "updated")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.replace("`", "").lower()).strip("-")


def render(meta: dict, body: str) -> str:
    # Same layout as server.write_doc.
    header = "\n".join(f"{k}: {meta.get(k, '')}" for k in HEADER_KEYS)
    return f"---\n{header}\n---\n\n{body.strip()}\n"


def without_updated(text: str) -> str:
    return re.sub(r"^updated:.*$", "", text, count=1, flags=re.M)


def load_sources(config: dict) -> list[dict]:
    # The first format had one source at the top level; keep reading it.
    if "sources" in config:
        return config["sources"]
    return [{"name": "odoo", **config}]


def default_entry(name: str, text: str, source: dict) -> dict:
    """Entry for a source file missing from the source's docs map."""
    match = re.fullmatch(source.get("key_regex", r"(.+)\.md"), name)
    key = match.group(1) if match else Path(name).stem
    prefix = source.get("title_prefix", "")
    h1 = text.split("\n", 1)[0].lstrip("# ").strip()
    label = re.sub(r"^Dokumentasi( Modul)?\s+", "", h1)
    if prefix:
        label = re.split(rf"\s+[—-]\s+{re.escape(prefix)}", label)[0]
    label = label.strip() or key
    return {"id": f"{source['project']}.{slug(key)}", "label": label, "tag": slug(key)}


def split_sections(text: str, mode: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Return (intro, [(number, heading, body)]) with the H1 line removed."""
    if mode == "numbered":
        parts = re.split(r"^## (\d+)\. (.+)$", text, flags=re.M)
        intro = parts[0].split("\n", 1)[1].strip() if "\n" in parts[0] else ""
        sections = [(parts[i], parts[i + 1].strip(), parts[i + 2].strip()) for i in range(1, len(parts), 3)]
        return intro, sections

    lines = text.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    intro, sections, fence = [], [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith("## "):
            heading = re.sub(r"^[\d.]+\s+", "", line[3:].strip()) or line[3:].strip()
            sections.append([str(len(sections) + 1), heading, []])
        elif sections:
            sections[-1][2].append(line)
        else:
            intro.append(line)
    return "\n".join(intro).strip(), [(n, h, "\n".join(b).strip()) for n, h, b in sections]


def build_notes(src: Path, entry: dict, source: dict) -> dict[str, tuple[dict, str]]:
    """Return {note_id: (meta_without_updated, body)} for one source file."""
    note_id, label, tag = entry["id"], entry["label"], entry["tag"]
    project, prefix = source["project"], source.get("title_prefix", "")
    intro, sections = split_sections(src.read_text(encoding="utf-8"), source.get("sections", "numbered"))

    notes, listing = {}, []
    for num, heading, body in sections:
        plain = heading.replace("`", "")
        sid = f"{note_id}.{int(num):02d}-{slug(heading)}"
        meta = {"title": f"{prefix} {label}: {plain}".strip(), "tags": f"{project},{tag},dokumentasi", "project": project}
        notes[sid] = (meta, f"{body}\n\n_Sumber: {src.name} §{num}_")
        listing.append(f"- `{sid}`: {plain}")

    where = f"{source.get('windows_dir', source['source_dir'])}\\{src.name}"
    if source.get("html", False):
        where += f" (versi HTML: {src.name[:-3]}.html)"
    body = intro + "\n\n## Bagian di memori\n" + "\n".join(listing)
    body += f"\n\n_Sumber: {where}_"
    fields = {"prefix": prefix, "label": label, "project": project, "tag": tag}
    meta = {
        "title": entry.get("title") or source.get("summary_title", "{prefix} {label}").format(**fields).strip(),
        "tags": source.get("summary_tags", "{project},{tag},dokumentasi").format(**fields),
        "project": project,
    }
    notes[note_id] = (meta, body)
    return notes


def load_relations(path: Path) -> set[tuple[str, str, str]]:
    if not path.exists():
        return set()
    return {(e["src"], e["rel"], e["dst"]) for e in map(json.loads, filter(str.strip, path.read_text().splitlines()))}


def save_relations(path: Path, edges: set[tuple[str, str, str]]) -> None:
    # Same format as server.save_relations.
    lines = [json.dumps({"src": s, "rel": r, "dst": d}, ensure_ascii=False) for s, r, d in sorted(edges)]
    path.write_text("\n".join(lines) + ("\n" if lines else ""))


def import_source(source: dict, docs_dir: Path, edges: set, today: str, dry_run: bool) -> tuple[list[str], list[str]]:
    """Import one source, updating edges in place. Return (changes, unmapped)."""
    changes, unmapped = [], []
    source_dir = Path(source["source_dir"])
    if not source_dir.is_dir():
        print(f"import_docs [{source['name']}]: {source_dir} tidak ditemukan, dilewati")
        return changes, unmapped

    exclude = set(source.get("exclude", []))
    for src in sorted(source_dir.glob(source.get("pattern", "*.md"))):
        if src.name in exclude:
            continue
        entry = source.get("docs", {}).get(src.name)
        if entry is None:
            entry = default_entry(src.name, src.read_text(encoding="utf-8"), source)
            unmapped.append(f"{src.name} -> {entry['id']} (label {entry['label']!r})")
        note_id = entry["id"]
        notes = build_notes(src, entry, source)

        for nid, (meta, body) in notes.items():
            path = docs_dir / f"{nid}.md"
            old = path.read_text(encoding="utf-8") if path.exists() else None
            text = render({**meta, "updated": today}, body)
            if old is not None and without_updated(old) == without_updated(text):
                continue
            changes.append(f"{'ubah' if old is not None else 'tambah'}: {nid}")
            if not dry_run:
                path.write_text(text, encoding="utf-8")

        # Section notes of this doc that disappeared from the source. A section
        # whose heading changed keeps its number, so its hand-made relations
        # move to the new id; otherwise they are dropped with the note.
        by_number = {nid[len(note_id) + 1:][:2]: nid for nid in notes if nid != note_id}
        for path in docs_dir.glob(f"{note_id}.[0-9][0-9]-*.md"):
            old_id = path.stem
            if old_id in notes:
                continue
            touching = {e for e in edges if old_id in (e[0], e[2])}
            manual = {e for e in touching if e[1] != "punya_bagian"}
            edges -= touching
            successor = by_number.get(old_id[len(note_id) + 1:][:2])
            if successor:
                rename = lambda x: successor if x == old_id else x  # noqa: E731
                edges |= {(rename(s), r, rename(d)) for s, r, d in manual}
                note = f" (relasi dipindah ke {successor})" if manual else ""
            else:
                lost = "; ".join(sorted(f"{s} --{r}--> {d}" for s, r, d in manual))
                note = f" (relasi ikut terhapus: {lost})" if manual else ""
            changes.append(f"hapus: {old_id}{note}")
            if not dry_run:
                path.unlink()

        sections = {nid for nid in notes if nid != note_id}
        edges -= {e for e in edges if e[0] == note_id and e[1] == "punya_bagian" and e[2] not in sections}
        edges |= {(note_id, "punya_bagian", sid) for sid in sections}
        edges.add(("index", "berisi", note_id))
        if source.get("workspace") and entry.get("module", True):
            edges.add((source["workspace"], source.get("workspace_rel", "punya_dokumen"), note_id))
    return changes, unmapped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true", help="show what would change without writing")
    ap.add_argument("--only", help="import only the source with this name")
    ap.add_argument("--data-dir", default=str(ROOT / "data"), help="data directory (default: ./data)")
    args = ap.parse_args()

    if not CONFIG.exists():
        print(f"import_docs: {CONFIG.name} tidak ada, impor dilewati")
        return 0
    sources = [s for s in load_sources(json.loads(CONFIG.read_text())) if not args.only or s["name"] == args.only]
    data = Path(args.data_dir)
    docs_dir, rel_path = data / "docs", data / "relations.jsonl"

    today = datetime.date.today().isoformat()
    edges = load_relations(rel_path)
    new_edges = set(edges)
    prefix = "import_docs (dry-run)" if args.dry_run else "import_docs"

    for source in sources:
        changes, unmapped = import_source(source, docs_dir, new_edges, today, args.dry_run)
        label = f"{prefix} [{source['name']}]"
        if changes and unmapped:
            # Only worth mentioning when something happened; tune id/label in docs_import.json.
            print(f"{label}: belum ada di docs_import.json, memakai id otomatis: {', '.join(unmapped)}")
        if changes:
            print(f"{label}: {len(changes)} perubahan")
            for line in changes:
                print(f"  {line}")
        else:
            print(f"{label}: tidak ada perubahan")

    if new_edges != edges:
        added, removed = len(new_edges - edges), len(edges - new_edges)
        print(f"{prefix}: relasi +{added} -{removed}")
        if not args.dry_run:
            save_relations(rel_path, new_edges)
    return 0


if __name__ == "__main__":
    sys.exit(main())
