---
title: Nakama Fitur Tersedia: Tools bawaan
tags: nakama,fitur,dokumentasi
project: nakama
updated: 2026-10-30
---

| Tool | Fungsi |
|---|---|
| `read_file`, `search_files`, `ripgrep` | Baca dan cari file di workspace agent |
| `bash` | Shell di workspace profile |
| `web_search`, `web_fetch` | Cari dan ambil halaman web |
| `knowledge_base_search` | Cari di knowledge base |
| `email` | Akses mailbox |
| `update-profile-memory`, `archive-profile-memory` | Kelola memori |
| `save-artifact` | Simpan file hasil kerja ke `artifacts/` |
| `sub_agent` | Delegasi ke agent lain |
| `coding-agent` | Serahkan tugas coding ke Codex, Claude Code, OpenCode, pi, atau Cursor Agent |
| `agent-browser` | Kendalikan browser untuk situs yang perlu login |
| `create-profile` | Super Bot membuat profile baru (dengan konfirmasi) |
| `skill_manage` | Buat, ubah, hapus skill |

Tool read/search berjalan paralel. Tool yang mengubah data berjalan berurutan.

Custom tools: file `.js` atau `.py` di `~/.nakama/tools/`.

**Tool Playground** (`/system/playground/:toolId`): admin bisa menjalankan tool secara langsung untuk tes.

Doc: `builtin-tools`, `tool-reference`.

_Sumber: 02-fitur-tersedia.md §3_
