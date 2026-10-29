---
title: Operasional mymemory-ai (sync, config, catatan WSL)
tags: mymemory,ops,wsl,cron
project: mymemory
updated: 2026-10-30
---

- Registrasi MCP: ~/.claude.json -> mcpServers.mymemory (stdio, .venv/bin/python server.py). Backup lama: ~/.claude.json.bak-mymemory.
  CLI `claude mcp add` gagal di shell: "claude native binary not installed".
- Sync: sync.sh (git add data, commit jika berubah, push ke origin main). Cron tiap 30 menit, log di sync.log.
- Cron di WSL hanya jalan selama WSL hidup. Push via SSH; key berpassphrase bisa membuat push cron gagal (commit tetap lokal).
- Setelah ubah registrasi, restart Claude Code agar tool memori termuat.

- Update 2026-10-30: remote dipindah ke HTTPS (https://github.com/idsoke/mymemory-ai.git) dengan credential helper lokal `gh auth git-credential`, karena SSH key id_ed25519 berpassphrase dan tidak ada ssh-agent sehingga push dari cron gagal.

- Mirror Windows: sync.sh menyalin data/ ke /mnt/d/dokumentasi/odoo/mymemory (rsync --delete, hanya subfolder itu). Satu arah: edit di Windows akan tertimpa.
