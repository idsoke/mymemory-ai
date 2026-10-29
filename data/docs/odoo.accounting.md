---
title: Odoo Accounting / Invoicing (modul): ringkasan & daftar bagian
tags: odoo,accounting,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **Accounting/Invoicing** (`addons/account`) dalam bentuk diagram, termasuk bagaimana Sales, Purchase, POS, dan Inventory menghasilkan jurnal.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_accounting_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Model data (ERD)
3. Jenis dokumen (`move_type`) & jurnal
4. Siklus hidup Journal Entry / Invoice
5. Status pembayaran (`payment_state`)
6. Alur Invoice → Payment → Rekonsiliasi
7. Register Payment & `account.payment`
8. Rekonsiliasi (partial & full)
9. Credit Note / Reversal
10. Pajak
11. Jurnal otomatis dari modul lain
12. Lock date, keamanan data & cron
13. Hak akses
14. Ringkasan file penting

---

## Bagian di memori
- `odoo.accounting.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.accounting.02-model-data-erd`: Model Data (ERD)
- `odoo.accounting.03-jenis-dokumen-move-type-jurnal`: Jenis Dokumen (move_type) & Jurnal
- `odoo.accounting.04-siklus-hidup-journal-entry-invoice`: Siklus Hidup Journal Entry / Invoice
- `odoo.accounting.05-status-pembayaran-payment-state`: Status Pembayaran (payment_state)
- `odoo.accounting.06-alur-invoice-payment-rekonsiliasi`: Alur Invoice → Payment → Rekonsiliasi
- `odoo.accounting.07-register-payment-account-payment`: Register Payment & account.payment
- `odoo.accounting.08-rekonsiliasi-partial-full`: Rekonsiliasi (Partial & Full)
- `odoo.accounting.09-credit-note-reversal`: Credit Note / Reversal
- `odoo.accounting.10-pajak`: Pajak
- `odoo.accounting.11-jurnal-otomatis-dari-modul-lain`: Jurnal Otomatis dari Modul Lain
- `odoo.accounting.12-lock-date-keamanan-data-cron`: Lock Date, Keamanan Data & Cron
- `odoo.accounting.13-hak-akses`: Hak Akses
- `odoo.accounting.14-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_accounting_odoo.md (versi HTML: dokumentasi_accounting_odoo.html)_
