---
title: Nakama Setup Lokal: Alur kerja untuk kontribusi berikutnya (sesuai CONTRIBUTING.md)
tags: nakama,setup,dokumentasi
project: nakama
updated: 2026-10-30
---

1. Pilih/klaim issue di `ahmadrosid/nakama`, komentar dan tunggu di-assign.
2. Sinkron `main` sebelum mulai:
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```
3. Buat branch baru: `git checkout -b <tipe>/<deskripsi-singkat>`
4. Sebelum push, jalankan:
   ```bash
   bun run check   # lint
   bun run fix     # auto-fix
   bun run knip    # unused code (CI gagal kalau ada temuan)
   bun test
   ```
5. Push & buka PR ke repo asli:
   ```bash
   git push -u origin HEAD
   gh pr create --repo ahmadrosid/nakama
   ```

Detail lengkap aturan kontribusi ada di `ATURAN-KONTRIBUSI.md` (file
terpisah di folder ini).

_Sumber: SETUP-LOKAL.md §4_
