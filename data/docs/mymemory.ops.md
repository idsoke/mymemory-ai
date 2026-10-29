---
title: Operasional odoo-mymemory-ai (sync, config, catatan WSL)
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

- Update 2026-10-30: repo GitHub diganti nama menjadi idsoke/odoo-mymemory-ai; remote origin sekarang https://github.com/idsoke/odoo-mymemory-ai.git. Folder lokal tetap /home/idris/mymemory-ai (dipakai .venv, crontab, dan ~/.claude.json).

- Update 2026-10-30: impor otomatis dokumentasi Odoo (opsi A). Sumber kebenaran = D:\dokumentasi\odoo\dokumentasi_*_odoo.md. sync.sh menjalankan import_docs.py dulu (pemetaan file → id di docs_import.json), lalu mirror dan commit. Catatan odoo.<modul>* jangan diedit lewat save_doc karena akan tertimpa impor berikutnya; edit file MD sumbernya. server.py me-refresh indeks FTS sebelum tiap search, jadi hasil impor langsung bisa dicari tanpa restart. Catatan index (daftar dokumentasi) tetap diperbarui manual.

- Mirror Windows: sync.sh menyalin data/ ke /mnt/d/dokumentasi/odoo/mymemory (rsync --delete, hanya subfolder itu). Satu arah: edit di Windows akan tertimpa.

- Update 2026-10-30: multi-proyek (Odoo + Nakama). docs_import.json sekarang punya daftar "sources" (per sumber: source_dir, pattern, project, title_prefix, sections "numbered" untuk `## N. Judul` atau "h2" untuk semua `## `, workspace + relasi) dan "mirrors". Nakama: D:\dokumentasi\nakama\*.md (kecuali README.md) → nakama.<dok>, relasi nakama.workspace --punya_dokumen-->. `import_docs.py --only nakama` untuk satu sumber.
- Mirror sekarang lewat mirror.py (bukan rsync): per folder hanya project yang dipilih. D:\dokumentasi\odoo\mymemory = semua kecuali project nakama; D:\dokumentasi\nakama\mymemory = project nakama + meta (index). Satu arah; MYMEMORY_MIRROR= (kosong) mematikan semua mirror.
- Rencana 2026-10-30: repo diganti nama kembali ke idsoke/mymemory-ai karena tidak lagi khusus Odoo (menunggu user menjalankan rename; GitHub me-redirect nama lama).
