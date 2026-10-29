"""Import the diagram docs (dokumentasi_*_odoo.md) into data/ as notes.

The markdown files in docs_import.json's source_dir are the source of truth.
Each file becomes one summary note (<id>) plus one note per "## N. Heading"
section (<id>.NN-<slug>). Notes are rewritten only when their content changes,
section notes that no longer exist in the source are deleted (with every
relation touching them), and the structural relations (index/berisi,
odoo.workspace/punya_modul, <id>/punya_bagian) are kept in sync.

Run by sync.sh before committing; safe to run by hand:
    .venv/bin/python import_docs.py [--dry-run]
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


def default_entry(name: str, text: str) -> dict:
    """Entry for a source file missing from docs_import.json."""
    key = re.fullmatch(r"dokumentasi_(.+)_odoo\.md", name).group(1)
    h1 = text.split("\n", 1)[0].lstrip("# ").strip()
    label = re.sub(r"^Dokumentasi( Modul)?\s+", "", h1)
    label = re.split(r"\s+[—-]\s+Odoo", label)[0].strip() or key
    return {"id": f"odoo.{key.replace('_', '-')}", "label": label, "tag": key.replace("_", "-")}


def build_notes(src: Path, entry: dict) -> dict[str, tuple[dict, str]]:
    """Return {note_id: (meta_without_updated, body)} for one source file."""
    text = src.read_text(encoding="utf-8")
    note_id, label, tag = entry["id"], entry["label"], entry["tag"]
    parts = re.split(r"^## (\d+)\. (.+)$", text, flags=re.M)
    intro = parts[0].split("\n", 1)[1].strip() if "\n" in parts[0] else ""

    notes, listing = {}, []
    for i in range(1, len(parts), 3):
        num, heading, body = parts[i], parts[i + 1].strip(), parts[i + 2].strip()
        plain = heading.replace("`", "")
        sid = f"{note_id}.{int(num):02d}-{slug(heading)}"
        meta = {"title": f"Odoo {label}: {plain}", "tags": f"odoo,{tag},dokumentasi", "project": "odoo"}
        notes[sid] = (meta, f"{body}\n\n_Sumber: {src.name} §{num}_")
        listing.append(f"- `{sid}`: {plain}")

    html = src.name[:-3] + ".html"
    body = intro + "\n\n## Bagian di memori\n" + "\n".join(listing)
    body += f"\n\n_Sumber: D:\\dokumentasi\\odoo\\{src.name} (versi HTML: {html})_"
    meta = {
        "title": entry.get("title") or f"Odoo {label} (modul): ringkasan & daftar bagian",
        "tags": f"odoo,{tag},dokumentasi,modul",
        "project": "odoo",
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true", help="show what would change without writing")
    ap.add_argument("--source-dir", help="override source_dir from docs_import.json")
    ap.add_argument("--data-dir", default=str(ROOT / "data"), help="data directory (default: ./data)")
    args = ap.parse_args()

    if not CONFIG.exists():
        print(f"import_docs: {CONFIG.name} tidak ada, impor dilewati")
        return 0
    config = json.loads(CONFIG.read_text())
    source_dir = Path(args.source_dir or config["source_dir"])
    data = Path(args.data_dir)
    docs_dir, rel_path = data / "docs", data / "relations.jsonl"
    if not source_dir.is_dir():
        print(f"import_docs: {source_dir} tidak ditemukan, impor dilewati")
        return 0

    today = datetime.date.today().isoformat()
    edges = load_relations(rel_path)
    new_edges = set(edges)
    changes, unmapped = [], []

    for src in sorted(source_dir.glob(config.get("pattern", "dokumentasi_*_odoo.md"))):
        entry = config["docs"].get(src.name)
        if entry is None:
            entry = default_entry(src.name, src.read_text(encoding="utf-8"))
            unmapped.append(f"{src.name} -> {entry['id']} (label {entry['label']!r})")
        note_id = entry["id"]
        notes = build_notes(src, entry)

        for nid, (meta, body) in notes.items():
            path = docs_dir / f"{nid}.md"
            old = path.read_text(encoding="utf-8") if path.exists() else None
            text = render({**meta, "updated": today}, body)
            if old is not None and without_updated(old) == without_updated(text):
                continue
            changes.append(f"{'ubah' if old is not None else 'tambah'}: {nid}")
            if not args.dry_run:
                path.write_text(text, encoding="utf-8")

        # Section notes of this doc that disappeared from the source. A section
        # whose heading changed keeps its number, so its hand-made relations
        # move to the new id; otherwise they are dropped with the note.
        by_number = {nid[len(note_id) + 1:][:2]: nid for nid in notes if nid != note_id}
        for path in docs_dir.glob(f"{note_id}.[0-9][0-9]-*.md"):
            old_id = path.stem
            if old_id in notes:
                continue
            touching = {e for e in new_edges if old_id in (e[0], e[2])}
            manual = {e for e in touching if e[1] != "punya_bagian"}
            new_edges -= touching
            successor = by_number.get(old_id[len(note_id) + 1:][:2])
            if successor:
                rename = lambda x: successor if x == old_id else x  # noqa: E731
                new_edges |= {(rename(s), r, rename(d)) for s, r, d in manual}
                note = f" (relasi dipindah ke {successor})" if manual else ""
            else:
                lost = "; ".join(sorted(f"{s} --{r}--> {d}" for s, r, d in manual))
                note = f" (relasi ikut terhapus: {lost})" if manual else ""
            changes.append(f"hapus: {old_id}{note}")
            if not args.dry_run:
                path.unlink()

        sections = {nid for nid in notes if nid != note_id}
        new_edges -= {e for e in new_edges if e[0] == note_id and e[1] == "punya_bagian" and e[2] not in sections}
        new_edges |= {(note_id, "punya_bagian", sid) for sid in sections}
        new_edges.add(("index", "berisi", note_id))
        if entry.get("module", True):
            new_edges.add(("odoo.workspace", "punya_modul", note_id))

    if new_edges != edges:
        added, removed = len(new_edges - edges), len(edges - new_edges)
        changes.append(f"relasi: +{added} -{removed}")
        if not args.dry_run:
            save_relations(rel_path, new_edges)

    prefix = "import_docs (dry-run)" if args.dry_run else "import_docs"
    if changes and unmapped:
        # Only worth mentioning when something happened; tune id/label in docs_import.json.
        print(f"{prefix}: belum ada di docs_import.json, memakai id otomatis: {', '.join(unmapped)}")
    if changes:
        print(f"{prefix}: {len(changes)} perubahan")
        for line in changes:
            print(f"  {line}")
    else:
        print(f"{prefix}: tidak ada perubahan")
    return 0


if __name__ == "__main__":
    sys.exit(main())
