---
title: Odoo POS Restaurant: Pengaturan
tags: odoo,pos-restaurant,dokumentasi
project: odoo
updated: 2026-10-30
---

| Pengaturan | Field | Keterangan |
|---|---|---|
| Is a Bar/Restaurant | `pos.config.module_pos_restaurant` | Aktifkan mode restoran |
| Floors | `floor_ids` | Lantai yang dilayani POS ini |
| Default Screen | `default_screen` | `tables` (denah) atau `register` (langsung kasir, cocok untuk bar) |
| Course Allocation | `use_course_allocation` | Otomatis membagi item ke course |
| Show Items on Fired Course Ticket | `use_show_items_on_course_ticket` | Tampilkan item lagi di tiket fire course |
| Preparation Printers | `preparation_printer_ids` (core POS) | Printer dapur/bar per kategori |
| Tips / Tip after payment | `iface_tipproduct`, `set_tip_after_payment` (core POS) | Tip, termasuk tip setelah otorisasi kartu |
| Presets | `pos.preset` + `use_guest` | Dine in / Takeaway / Delivery; wajib isi jumlah tamu |

Saat POS restoran baru dibuat, `_setup_default_floor()` membuat lantai dan meja default. Ada skenario onboarding **restaurant** dan **bar** (`load_onboarding_restaurant_scenario`, `load_onboarding_bar_scenario`).

---

_Sumber: dokumentasi_pos_restaurant_odoo.md §10_
