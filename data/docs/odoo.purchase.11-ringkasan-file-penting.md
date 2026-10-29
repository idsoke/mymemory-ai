---
title: Odoo Purchase: Ringkasan File Penting
tags: odoo,purchase,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `purchase/models/purchase_order.py` | `purchase.order`: state, konfirmasi, approval, lock, cancel, bill |
| `purchase/models/purchase_order_line.py` | Qty received/invoiced, harga dari vendor, baris bill |
| `purchase/models/product.py` | `purchase_method` (bill control) |
| `purchase/models/purchase_bill_line_match.py` | Pencocokan PO ↔ bill |
| `purchase/models/res_company.py` | Pengaturan approval & lock |
| `purchase/wizard/bill_to_po_wizard.py` | Tautkan bill ke PO |
| `purchase/data/ir_cron_data.xml` | Cron reminder |
| `purchase/security/purchase_security.xml` | Grup & record rule |
| `purchase_stock/models/purchase_order.py` | Pembuatan receipt saat approve |
| `purchase_stock/models/stock_rule.py` | `_run_buy()`: RFQ otomatis |
| `product/models/product_supplierinfo.py` | Harga & lead time vendor |
| `purchase_requisition/` | Purchase agreement / blanket order |

_Sumber: dokumentasi_purchase_odoo.md §11_
