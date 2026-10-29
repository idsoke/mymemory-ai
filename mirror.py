"""Copy notes to readable per-project folders (e.g. D:\\dokumentasi\\odoo\\mymemory).

docs_import.json "mirrors" lists the targets. Each target gets the notes whose
"project:" header is in "projects", or not in "exclude_projects", plus the
relations that touch those notes. One-way: files in a target that are not
mirrored notes are deleted, so edits made there are overwritten.

Set MYMEMORY_MIRROR= (empty) to disable every mirror. Run by sync.sh:
    .venv/bin/python mirror.py [--dry-run]
"""

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "docs_import.json"
DATA = ROOT / "data"


def project_of(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n") and "\n---\n" in text[4:]:
        for line in text[4:].split("\n---\n", 1)[0].splitlines():
            key, _, value = line.partition(":")
            if key.strip() == "project":
                return value.strip()
    return ""


def wanted(project: str, target: dict) -> bool:
    if "projects" in target:
        return project in target["projects"]
    return project not in target.get("exclude_projects", [])


def write_if_changed(path: Path, text: str, dry_run: bool) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    if not dry_run:
        path.write_text(text, encoding="utf-8")
    return True


def mirror(target: dict, dry_run: bool) -> None:
    out = Path(target["dir"])
    if not out.parent.is_dir():
        print(f"mirror: {out.parent} tidak ada, {out} dilewati")
        return
    docs = {p.stem: p for p in (DATA / "docs").glob("*.md") if wanted(project_of(p), target)}
    if not dry_run:
        (out / "docs").mkdir(parents=True, exist_ok=True)

    written = sum(
        write_if_changed(out / "docs" / p.name, p.read_text(encoding="utf-8"), dry_run) for p in docs.values()
    )
    removed = 0
    for old in (out / "docs").glob("*") if (out / "docs").is_dir() else []:
        if old.is_file() and not old.name.startswith(".") and (old.stem not in docs or old.suffix != ".md"):
            removed += 1
            if not dry_run:
                old.unlink()

    lines = (DATA / "relations.jsonl").read_text(encoding="utf-8").splitlines()
    edges = [json.loads(line) for line in lines if line.strip()]
    kept = [json.dumps(e, ensure_ascii=False) for e in edges if e["src"] in docs or e["dst"] in docs]
    rel_changed = write_if_changed(out / "relations.jsonl", "\n".join(kept) + ("\n" if kept else ""), dry_run)
    print(f"mirror {out}: {len(docs)} catatan, {written} ditulis, {removed} dihapus, relasi {'diubah' if rel_changed else 'sama'}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true", help="show what would change without writing")
    args = ap.parse_args()
    if os.environ.get("MYMEMORY_MIRROR", None) == "":
        print("mirror: MYMEMORY_MIRROR kosong, mirror dimatikan")
        return 0
    targets = json.loads(CONFIG.read_text()).get("mirrors", []) if CONFIG.exists() else []
    for target in targets:
        mirror(target, args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
