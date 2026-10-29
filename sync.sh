#!/usr/bin/env bash
# Commit and push changes under data/. Run by cron; safe to run by hand.
set -euo pipefail
cd "$(dirname "$0")"

# D:\dokumentasi\odoo\dokumentasi_*_odoo.md is the source of truth for the
# Odoo module notes: refresh them first. A failed import must not stop the sync.
.venv/bin/python import_docs.py || echo "import_docs gagal (exit $?), sync tetap jalan"

# Readable copy on Windows (D:\dokumentasi\odoo\mymemory). One-way mirror:
# edits made there are overwritten; edit the source docs or use the MCP tools.
# Override with MYMEMORY_MIRROR=/some/dir, or set it empty to disable.
MIRROR="${MYMEMORY_MIRROR-/mnt/d/dokumentasi/odoo/mymemory}"
if [ -n "$MIRROR" ] && [ -d "$(dirname "$MIRROR")" ]; then
  mkdir -p "$MIRROR"
  rsync -rt --delete data/ "$MIRROR/"
fi

git add data
if ! git diff --cached --quiet; then
  git commit -q -m "memory: sync $(date '+%Y-%m-%d %H:%M')"
fi
if git remote get-url origin >/dev/null 2>&1; then
  git push -q origin main
fi
