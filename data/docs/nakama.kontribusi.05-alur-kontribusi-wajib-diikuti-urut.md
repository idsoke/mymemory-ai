---
title: Nakama Aturan Kontribusi: Alur kontribusi (WAJIB diikuti urut)
tags: nakama,kontribusi,dokumentasi
project: nakama
updated: 2026-10-30
---

1. **Klaim issue dulu, jangan langsung coding.** Komentar di issue dan tunggu
   di-assign. Assignee adalah satu-satunya sinyal buat kontributor lain —
   branch di fork sendiri tidak terlihat dari repo utama, jadi dua orang bisa
   tanpa sadar mengerjakan fitur yang sama.
   Sebelum mulai, cek juga PR terbuka untuk nomor issue tersebut:
   ```bash
   gh pr list --repo ahmadrosid/nakama --search "<nomor-issue>"
   ```
2. Branch dari `main` (boleh dari fork sendiri, lalu branch).
3. Satu concern per PR (jangan gabungkan beberapa perubahan tak berkaitan).
4. Push dan buka PR:
   ```bash
   git push -u origin HEAD
   gh pr create
   ```
5. Isi PR harus menyebutkan: apa yang berubah, apa yang sudah diverifikasi,
   risiko yang tersisa.
6. CI harus lulus sebelum merge.
7. **Jangan ubah `AGENTS.md`, `README.md`, atau `ARCHITECTURE.md`** kecuali
   perubahan memang spesifik tentang file-file itu.

_Sumber: ATURAN-KONTRIBUSI.md §5_
