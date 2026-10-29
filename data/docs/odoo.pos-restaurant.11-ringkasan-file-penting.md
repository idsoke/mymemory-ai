---
title: Odoo POS Restaurant: Ringkasan File Penting
tags: odoo,pos-restaurant,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `pos_restaurant/models/pos_restaurant.py` | `restaurant.floor` & `restaurant.table` |
| `pos_restaurant/models/pos_config.py` | Pengaturan restoran, simpan/muat floor plan, data demo |
| `pos_restaurant/models/pos_order.py` | `table_id`, `customer_count`, `course_ids`, `_get_open_order` per meja |
| `pos_restaurant/models/pos_course.py`, `restaurant_order_course.py` | Course master & course per order |
| `pos_restaurant/static/src/app/services/pos_store.js` | Logika utama: meja, kirim ke dapur, transfer, merge, course |
| `pos_restaurant/static/src/app/screens/floor_screen/` | Denah & editor floor plan |
| `pos_restaurant/static/src/app/screens/split_bill_screen/` | Split bill |
| `pos_restaurant/data/scenarios/` | Preset & data skenario restoran |
| `point_of_sale/models/pos_prep_order.py`, `pos_printer.py` | Order persiapan & printer (core POS) |

_Sumber: dokumentasi_pos_restaurant_odoo.md §11_
