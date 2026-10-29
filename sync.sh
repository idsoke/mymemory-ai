#!/usr/bin/env bash
# Commit and push changes under data/. Run by cron; safe to run by hand.
set -euo pipefail
cd "$(dirname "$0")"

# Readable copy on Windows (D:\dokumentasi\odoo\mymemory). One-way mirror:
# edits made there are overwritten; edit through the MCP tools instead.
MIRROR=/mnt/d/dokumentasi/odoo/mymemory
if [ -d "$(dirname "$MIRROR")" ]; then
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
