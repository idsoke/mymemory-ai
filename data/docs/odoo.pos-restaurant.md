---
title: Odoo POS Restaurant (modul): ringkasan & daftar bagian
tags: odoo,pos-restaurant,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **POS Restaurant** (`addons/pos_restaurant`) dalam bentuk diagram. Modul ini mengubah Point of Sale menjadi kasir restoran/bar: denah lantai, meja, jumlah tamu, kirim order ke dapur, course, transfer/gabung meja, dan split bill.
Dokumentasi dasar POS (sesi, order, pembayaran, akuntansi) ada di `dokumentasi_pos_odoo.md`.

Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_pos_restaurant_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Model data (ERD)
3. Alur layanan restoran (end-to-end)
4. Floor plan & meja
5. Status meja & order
6. Kirim order ke dapur (Preparation)
7. Course (urutan hidangan)
8. Transfer & gabung order / meja
9. Split bill
10. Pengaturan
11. Ringkasan file penting

---

## Bagian di memori
- `odoo.pos-restaurant.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.pos-restaurant.02-model-data-erd`: Model Data (ERD)
- `odoo.pos-restaurant.03-alur-layanan-restoran-end-to-end`: Alur Layanan Restoran (End-to-End)
- `odoo.pos-restaurant.04-floor-plan-meja`: Floor Plan & Meja
- `odoo.pos-restaurant.05-status-meja-order`: Status Meja & Order
- `odoo.pos-restaurant.06-kirim-order-ke-dapur-preparation`: Kirim Order ke Dapur (Preparation)
- `odoo.pos-restaurant.07-course-urutan-hidangan`: Course (Urutan Hidangan)
- `odoo.pos-restaurant.08-transfer-gabung-order-meja`: Transfer & Gabung Order / Meja
- `odoo.pos-restaurant.09-split-bill`: Split Bill
- `odoo.pos-restaurant.10-pengaturan`: Pengaturan
- `odoo.pos-restaurant.11-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_pos_restaurant_odoo.md (versi HTML: dokumentasi_pos_restaurant_odoo.html)_
