---
title: Odoo Inventory: Ringkasan File Penting
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `stock/models/stock_warehouse.py` | Warehouse, pembuatan lokasi/route/rule otomatis |
| `stock/models/stock_location.py` | `stock.location` dan `stock.route` |
| `stock/models/stock_picking.py` | Transfer: konfirmasi, reservasi, validasi, backorder |
| `stock/models/stock_picking_type.py` | Operation type |
| `stock/models/stock_move.py` | Move: confirm, assign, done, push, scrap |
| `stock/models/stock_move_line.py` | Detail operasi (lot, package, lokasi) |
| `stock/models/stock_quant.py` | Stok on hand, reservasi, inventory adjustment |
| `stock/models/stock_rule.py` | Procurement, pull/push rule, scheduler |
| `stock/models/stock_orderpoint.py` | Reordering rules / replenishment |
| `stock/models/stock_reference.py` | Penghubung dokumen asal ↔ move |
| `stock/models/stock_picking_batch.py` | Batch & wave transfer |
| `stock/models/product_strategy.py` | Putaway rule & removal strategy |
| `stock/wizard/*` | Backorder, replenish, label, inventory, put in pack, dll. |
| `stock/data/stock_data.xml`, `stock_sequence_data.xml` | Lokasi virtual, removal strategy, cron scheduler |
| `stock/security/stock_security.xml` | Grup & record rule |
| `stock_account/models/*` | Valuasi stok, metode biaya |

_Sumber: dokumentasi_inventory_odoo.md §13_
