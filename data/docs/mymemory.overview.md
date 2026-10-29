---
title: mymemory-ai: memori lokal berbasis MCP
tags: mymemory,mcp,memory
project: mymemory
updated: 2026-10-30
---

Sistem memori lokal (knowledge graph) untuk asisten AI, diekspos sebagai MCP server.
- Lokasi: /home/idris/mymemory-ai (repo GitHub public idsoke/mymemory-ai, lisensi MIT, dijadikan public 2026-10-30). Riwayat nama repo: idsoke/mymemory-ai → idsoke/odoo-mymemory-ai → kembali idsoke/mymemory-ai (2026-10-30, karena dipakai lebih dari satu proyek).
- Server: server.py (Python, mcp SDK 2.3 `MCPServer`, nama server "mymemory-ai", venv di .venv)
- Tools: search, get_doc, list_docs, save_doc, append_doc, delete_doc, link, unlink, neighbors
- Proyek: odoo (odoo.workspace) dan nakama (nakama.workspace). Filter `project` di search memisahkan hasil.
- Dibuat: 2026-10-30

- Mulai dari catatan `index` untuk melihat semua dokumentasi dan rencana.
