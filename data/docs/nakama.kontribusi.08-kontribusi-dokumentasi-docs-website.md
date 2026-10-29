---
title: Nakama Aturan Kontribusi: Kontribusi dokumentasi (docs/website)
tags: nakama,kontribusi,dokumentasi
project: nakama
updated: 2026-10-30
---

User docs ada di `docs/website/content/docs/` (MDX). Audiens: operator dan
pengguna chat — bukan kontributor teknis. Prioritas isi: **Why** (masalah apa
yang diselesaikan) -> **Value** (apa yang jadi lebih baik) -> **How to use**
(langkah UI, role, screenshot). Detail teknis kontributor taruh di
`AGENTS.md`, bukan di docs user.

Langkah menambah/ubah halaman:
1. Edit/tambah MDX di `docs/website/content/docs/`
2. Daftarkan halaman di `docs/website/content/docs/meta.json`
3. Cross-link dari halaman hub `docs/website/content/docs/docs.mdx`
4. Screenshot di `docs/website/public/screenshots/`
   (`![alt](/screenshots/foo.png)`); script capture di
   `docs/website/scripts/`
5. Verifikasi: `bun run build:docs`

_Sumber: ATURAN-KONTRIBUSI.md §8_
