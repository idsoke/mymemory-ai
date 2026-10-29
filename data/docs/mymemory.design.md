---
title: Keputusan desain mymemory-ai
tags: mymemory,design
project: mymemory
updated: 2026-10-30
---

- Sumber kebenaran = file teks: data/docs/<id>.md (header key: value + body markdown) dan data/relations.jsonl (edge src/rel/dst, terurut agar diff git rapi).
- index.db = indeks SQLite FTS5, dibangun ulang saat startup, tidak di-commit.
- Pencarian: kata kunci di-quote (aman untuk `sale.order`), AND dulu lalu fallback OR.
- Graph: relasi berarah; `neighbors` menelusuri dua arah sampai depth 3.
- Hemat token berasal dari retrieval (ambil potongan relevan saja), bukan dari visualisasi.
- Vektor/embeddings sengaja belum dipakai; tambahkan (mis. sqlite-vec) jika pencarian bahasa bebas sering meleset.
- Visualisasi graph hanya untuk manusia, opsional, belum dibuat.
- Ukuran: ribuan catatan < ~20 MB; tidak hilang saat logout Claude karena berupa file lokal.
