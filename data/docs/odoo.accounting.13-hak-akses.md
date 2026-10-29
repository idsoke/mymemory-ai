---
title: Odoo Accounting / Invoicing: Hak Akses
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart BT
    U["base.group_user"]
    RO["account.group_account_readonly<br/>Readonly (Auditor)"]
    INV["account.group_account_invoice<br/>Invoicing (Billing)"]
    BAS["account.group_account_basic<br/>Basic"]
    USR["account.group_account_user<br/>Full Accounting Features"]
    MGR["account.group_account_manager<br/>Administrator"]

    U --> INV --> BAS --> USR
    U --> RO --> USR
    INV --> MGR

    F1["group_account_secured<br/>Inalterability"]
    F2["group_cash_rounding"]
    F3["group_validate_bank_account"]
    F4["group_delivery_invoice_address"]
    F1 & F2 & F3 & F4 -. fitur .- INV
```

| Grup | Hak |
|---|---|
| Invoicing | Buat & posting invoice/bill, register payment |
| Readonly | Lihat semua data akuntansi tanpa mengubah |
| Full Accounting Features | Fitur akuntansi lengkap (jurnal, rekonsiliasi, laporan) |
| Administrator | Konfigurasi (chart of accounts, pajak, jurnal, lock date). Secara teknis hanya mewarisi grup Invoicing; untuk fitur akuntansi lengkap biasanya juga diberi Full Accounting Features |

---

_Sumber: dokumentasi_accounting_odoo.md §13_
