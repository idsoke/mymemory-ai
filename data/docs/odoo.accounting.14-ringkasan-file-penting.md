---
title: Odoo Accounting / Invoicing: Ringkasan File Penting
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `account/models/account_move.py` | `account.move`: invoice/bill/entry, posting, payment state, reversal, pengiriman |
| `account/models/account_move_line.py` | Baris jurnal, rekonsiliasi, selisih kurs |
| `account/models/account_payment.py` | `account.payment` dan jurnal pembayarannya |
| `account/models/account_partial_reconcile.py`, `account_full_reconcile.py` | Data rekonsiliasi |
| `account/models/account_bank_statement_line.py` | Transaksi bank |
| `account/models/account_reconcile_model.py` | Aturan rekonsiliasi |
| `account/models/account_tax.py` | Perhitungan pajak |
| `account/models/account_journal.py`, `account_account.py` | Jurnal & chart of accounts |
| `account/models/company.py` | Lock date, pengaturan akuntansi & valuasi stok perusahaan |
| `account/models/chart_template.py` | Instalasi chart of accounts (dipakai `l10n_*`) |
| `account/wizard/account_payment_register.py` | Wizard Register Payment |
| `account/wizard/account_move_reversal.py` | Wizard Credit Note / Reversal |
| `account/data/service_cron.xml` | Definisi cron |
| `account/security/account_security.xml` | Grup & record rule |

_Sumber: dokumentasi_accounting_odoo.md §14_
