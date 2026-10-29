---
title: Odoo Point of Sale: Cron (Tugas Terjadwal)
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

| Nama | Method | Interval | Fungsi |
|---|---|---|---|
| POS: Product Snooze cleanup | `pos.snooze._cron_clean_records()` | 1 hari | Hapus data produk "snooze" yang sudah kedaluwarsa |
| POS: Process Order Tasks | `pos.order._cron_process_pos_orders()` | 5 menit | Membuat & mengirim PDF invoice yang ditunda (`defer_invoice_pdf`) |
| POS: Auto Order Invoicing | `pos.session._cron_generate_invoice_period()` | 10 menit | Validasi akuntansi harian untuk sesi dengan closing mode **Daily** |

---

_Sumber: dokumentasi_pos_odoo.md §11_
