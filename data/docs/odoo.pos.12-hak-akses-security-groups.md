---
title: Odoo Point of Sale: Hak Akses (Security Groups)
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart BT
    U["base.group_user<br/>Internal User"]
    PU["point_of_sale.group_pos_user<br/>User"]
    PM["point_of_sale.group_pos_manager<br/>Administrator"]
    PR["point_of_sale.group_pos_preset<br/>Preset Menu"]

    U --> PU --> PM
    PR -. opsional .- PU
```

| Grup | Hak |
|---|---|
| User | Membuka sesi, membuat order, pembayaran, cash in/out, melihat order |
| Administrator | Semua hak User + konfigurasi POS, metode pembayaran, kategori, laporan; bisa membatasi perubahan harga (`restrict_price_control`) |

Setiap `pos.config` juga punya `group_pos_user_id` dan `group_pos_manager_id` untuk menentukan grup yang dipakai.

---

_Sumber: dokumentasi_pos_odoo.md §12_
