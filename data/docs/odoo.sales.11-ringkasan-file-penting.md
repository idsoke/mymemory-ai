---
title: Odoo Sales: Ringkasan File Penting
tags: odoo,sales,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `sale/models/sale_order.py` | `sale.order`: state, konfirmasi, lock, cancel, invoice status, pembuatan invoice |
| `sale/models/sale_order_line.py` | Baris order: qty delivered/invoiced, invoice policy, harga, pajak |
| `sale/wizard/sale_make_invoice_advance.py` | Wizard Create Invoice / Down Payment |
| `sale/models/payment_transaction.py` | Konfirmasi otomatis setelah pembayaran online |
| `sale/controllers/portal.py` | Portal customer: lihat, tanda tangan, bayar quotation |
| `sale/data/ir_cron.xml` | Definisi cron |
| `sale/security/res_groups.xml` | Grup fitur Sales |
| `sale_crm/models/crm_lead.py` | Tombol New Quotation, jumlah quotation/order, update expected revenue |
| `sale_management/models/sale_order_template.py` | Template quotation |
| `sale_stock/models/sale_order_line.py` | Procurement & delivery dari SO |

_Sumber: dokumentasi_sales_odoo.md §11_
