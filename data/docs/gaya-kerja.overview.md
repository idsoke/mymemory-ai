---
title: Tes Gaya Kerja Big Five: ringkasan proyek
tags: gaya-kerja,big-five,psikotes,vercel,dokumentasi
project: gaya-kerja
updated: 2026-11-04
---

Prototipe tes Big Five (IPIP 50 soal) untuk pencari kerja di Indonesia.

- Live: https://gaya-kerja.vercel.app (akun Vercel `idsoke`, proyek `gaya-kerja`)
- Sumber: `~/gaya-kerja/index.html`, file statis tunggal. Redeploy: `vercel deploy --prod` dari folder itu.
- Dokumentasi lengkap: `~/gaya-kerja/docs/riwayat-chat-2026-11-04.md`. `docs/` dikecualikan dari deploy lewat `.vercelignore`.
- Skor per dimensi 10-50: rendah 10-23, sedang 24-36, tinggi 37-50. Soal negatif memakai `6 - jawaban`. Skor tidak dibandingkan dengan orang lain.
- Jawaban hanya di `localStorage`, tanpa akun atau backend.
- Keputusan: mulai B2C, posisikan sebagai refleksi diri dan latihan, bukan psikotes resmi. Hindari MBTI, klaim tanpa sumber, dan janji pasti lolos.
- Belum selesai: tinjauan psikolog, uji 10-20 pencari kerja, validasi terjemahan, laporan berbayar, autentikasi MCP Vercel.
- Gotcha: wrapper `grep` dan `claude` di shell error `claude native binary not installed`; pakai `/usr/bin/grep`. Bagikan hanya URL production karena URL deployment panjang dialihkan proteksi Vercel.
