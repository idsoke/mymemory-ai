---
title: Odoo Manufacturing: Ringkasan File Penting
tags: odoo,mrp,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `mrp/models/mrp_production.py` | `mrp.production`: state, konfirmasi, mark done, backorder, split/merge |
| `mrp/models/mrp_bom.py` | `mrp.bom`, `mrp.bom.line`, `mrp.bom.byproduct`, explode & `_bom_find()` |
| `mrp/models/mrp_routing.py` | `mrp.routing.workcenter` (operasi) |
| `mrp/models/mrp_workorder.py` | `mrp.workorder`: start/pause/finish, dependensi |
| `mrp/models/mrp_workcenter.py` | Work center, log produktivitas, OEE, kapasitas |
| `mrp/models/mrp_unbuild.py` | Unbuild order |
| `mrp/models/stock_rule.py` | `_run_manufacture()`: MO dari procurement |
| `mrp/models/stock_warehouse.py` | `manufacture_steps`, route & lokasi pre/post-production |
| `mrp/wizard/` | Consumption warning, backorder, split, ubah qty, serial |
| `mrp/security/mrp_security.xml` | Grup & record rule |
| `mrp_account/models/mrp_production.py` | `_cal_price()`, `_post_labour()`, WIP |

_Sumber: dokumentasi_mrp_odoo.md §12_
