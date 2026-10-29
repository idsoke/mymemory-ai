---
title: Nakama Fitur Tersedia: Usage dan biaya token
tags: nakama,fitur,dokumentasi
project: nakama
updated: 2026-10-30
---

| Fitur | Penjelasan | Doc |
|---|---|---|
| Badge per balasan | Setiap balasan menampilkan token input/output dan biaya (USD). | `changelog` |
| Popover konteks | Menampilkan bagian context window yang sudah terpakai. | `changelog` |
| Hitung token | Token diambil dari laporan provider. Jika provider tidak melapor, Nakama memakai estimasi (±4 karakter = 1 token) dan menandai balasan `estimated`. | — |
| Hitung biaya | Token × harga per 1 juta token (input, cached input, output). Harga dari katalog model, harga custom model yang diisi user, atau tabel gambar. Model tanpa harga resmi tidak menampilkan biaya. | `providers` |
| Ledger per org | Disimpan per org: total, per model, per agent/user, per hari (30 hari), dan per bulan. | — |
| Halaman Status | Request, token, dan biaya: total, per model, per hari. | — |
| Usage summary org | Pemakaian harian dan peringkat agent dan member menurut jumlah request. | — |
| Kuota bulanan | Admin set batas token dan/atau turn per bulan dan persen peringatan (default 80%). Jika habis, request ditolak (HTTP 429). | — |
| Biaya gambar | `generate_image` dicatat dengan cara yang sama seperti chat. | `image-generation` |

_Sumber: 02-fitur-tersedia.md §11_
