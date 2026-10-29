---
title: Odoo Point of Sale (modul): ringkasan & daftar bagian
tags: odoo,pos,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **Point of Sale** (`addons/point_of_sale`, versi manifest `1.0.2`) dalam bentuk diagram.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_pos_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Arsitektur aplikasi (backend ↔ frontend kasir)
3. Model data (ERD)
4. Siklus hidup Sesi POS (`pos.session`)
5. Siklus hidup Order POS (`pos.order`)
6. Alur transaksi kasir (end-to-end)
7. Sinkronisasi order dari UI (`sync_from_ui`)
8. Pembayaran & metode pembayaran
9. Penutupan sesi & jurnal akuntansi
10. Invoice & refund
11. Cron (tugas terjadwal)
12. Hak akses (Security Groups)
13. Ringkasan file penting

---

## Bagian di memori
- `odoo.pos.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.pos.02-arsitektur-aplikasi-backend-frontend-kasir`: Arsitektur Aplikasi (Backend ↔ Frontend Kasir)
- `odoo.pos.03-model-data-erd`: Model Data (ERD)
- `odoo.pos.04-siklus-hidup-sesi-pos-pos-session`: Siklus Hidup Sesi POS (pos.session)
- `odoo.pos.05-siklus-hidup-order-pos-pos-order`: Siklus Hidup Order POS (pos.order)
- `odoo.pos.06-alur-transaksi-kasir-end-to-end`: Alur Transaksi Kasir (End-to-End)
- `odoo.pos.07-sinkronisasi-order-dari-ui-sync-from-ui`: Sinkronisasi Order dari UI (sync_from_ui)
- `odoo.pos.08-pembayaran-metode-pembayaran`: Pembayaran & Metode Pembayaran
- `odoo.pos.09-penutupan-sesi-jurnal-akuntansi`: Penutupan Sesi & Jurnal Akuntansi
- `odoo.pos.10-invoice-refund`: Invoice & Refund
- `odoo.pos.11-cron-tugas-terjadwal`: Cron (Tugas Terjadwal)
- `odoo.pos.12-hak-akses-security-groups`: Hak Akses (Security Groups)
- `odoo.pos.13-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_pos_odoo.md (versi HTML: dokumentasi_pos_odoo.html)_
