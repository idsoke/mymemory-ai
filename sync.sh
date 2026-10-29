#!/usr/bin/env bash
# Commit and push changes under data/. Run by cron; safe to run by hand.
set -euo pipefail
cd "$(dirname "$0")"

# The docs listed in docs_import.json (D:\dokumentasi\odoo, D:\dokumentasi\nakama)
# are the source of truth for their notes: refresh them first. A failed import
# must not stop the sync.
.venv/bin/python import_docs.py || echo "import_docs gagal (exit $?), sync tetap jalan"

# Readable per-project copies on Windows (docs_import.json "mirrors"). One-way:
# edits made there are overwritten; edit the source docs or use the MCP tools.
# Set MYMEMORY_MIRROR= (empty) to disable.
.venv/bin/python mirror.py || echo "mirror gagal (exit $?), sync tetap jalan"

git add data
if ! git diff --cached --quiet; then
  git commit -q -m "memory: sync $(date '+%Y-%m-%d %H:%M')"
fi
if git remote get-url origin >/dev/null 2>&1; then
  git push -q origin main
fi
