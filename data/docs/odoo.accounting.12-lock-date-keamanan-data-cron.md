---
title: Odoo Accounting / Invoicing: Lock Date, Keamanan Data & Cron
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

**Lock date** (`res.company`): `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`, dan `hard_lock_date` (tidak bisa dibuka lagi). Pengecualian sementara bisa diberikan lewat `account.lock_exception`.

**Inalterability:** jurnal dengan *secure entries* mencatat `inalterable_hash` pada setiap entri yang diposting, sehingga data tidak bisa diubah tanpa ketahuan (wizard `account.secure.entries.wizard`).

**Cron** (`account/data/service_cron.xml`):

| Nama | Fungsi |
|---|---|
| Account: Post draft entries with auto_post enabled and accounting date up to today | Posting otomatis entri draft yang `auto_post` dan tanggalnya ≤ hari ini |
| Send invoices automatically | `_cron_account_move_send()`: kirim invoice di antrean pengiriman |
| Account: Inventory Valuation Closing | `res.company._cron_post_stock_valuation()`: jurnal valuasi stok periodik |

---

_Sumber: dokumentasi_accounting_odoo.md §12_
