---
title: Odoo Point of Sale: Ringkasan File Penting
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `point_of_sale/models/pos_config.py` | Konfigurasi POS, buka UI, validasi sebelum sesi, sequence |
| `point_of_sale/models/pos_session.py` | Sesi: opening/closing control, `load_data()`, jurnal penutupan, cron harian |
| `point_of_sale/models/pos_order.py` | Order: `sync_from_ui()`, pembayaran, invoice, refund, cron order |
| `point_of_sale/models/pos_order_line.py` | Baris order, combo, refund line |
| `point_of_sale/models/pos_payment.py`, `pos_payment_method.py` | Pembayaran & metode bayar |
| `point_of_sale/models/pos_load_mixin.py` | Mekanisme pemuatan data ke frontend |
| `point_of_sale/models/pos_bus_mixin.py` | Notifikasi realtime antar perangkat |
| `point_of_sale/models/pos_preset.py` | Preset (Dine in / Takeaway / Delivery) |
| `point_of_sale/models/pos_prep_order.py`, `pos_prep_line.py` | Order persiapan (dapur / bar) |
| `point_of_sale/controllers/` | Route `/pos/ui` dan lainnya |
| `point_of_sale/static/src/app/` | Aplikasi kasir OWL (screens, store, services, models) |
| `point_of_sale/data/ir_cron_data.xml` | Definisi cron |
| `point_of_sale/security/point_of_sale_security.xml` | Grup & record rule |
| `point_of_sale/wizard/*` | Wizard pembayaran, invoice, laporan |

_Sumber: dokumentasi_pos_odoo.md §13_
