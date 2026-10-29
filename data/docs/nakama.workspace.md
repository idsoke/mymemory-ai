---
title: Workspace Nakama lokal
tags: nakama,workspace
project: nakama
updated: 2026-10-30
---

- Source Nakama (fork idsoke/nakama, upstream ahmadrosid/nakama) di /home/idris/nakama. Bun monorepo: apps/{server,web,cli,desktop,platform/*}, packages/{core,agent,db,client}. Aturan agent: AGENTS.md + CONTRIBUTING.md.
- Remote: origin = idsoke/nakama (fork), upstream = ahmadrosid/nakama. Update source: `git fetch --all && git checkout main && git merge --ff-only upstream/main && bun install`.
- Dokumentasi (MD + HTML) di D:\dokumentasi\nakama: 01-ringkasan, 02-fitur-tersedia, 03-roadmap, ATURAN-KONTRIBUSI, SETUP-LOKAL. Semua *.md (kecuali README.md) diimpor otomatis oleh import_docs.py sebagai nakama.<dok> + nakama.<dok>.NN-<bagian> (pecah per heading `## `).
- alur-proses.html: diagram animasi 9 tab (chat & tools, agent & skills, file & ekstensi, org & operasi, usage & biaya, channel & integrasi, keamanan & deploy, Super Nakama, roadmap). Tidak diimpor (HTML).
- Catatan nakama.<dok>* jangan diedit lewat save_doc: akan tertimpa impor berikutnya. Edit file MD sumbernya.
- Memori ini dipakai bersama dengan Odoo. Saat bekerja di Nakama, cari dengan project="nakama" dan pakai id berawalan `nakama.` (mis. nakama.flow.chat, nakama.server.agent-service).
- Mirror baca-saja: D:\dokumentasi\nakama\mymemory (hanya catatan project nakama + index).
