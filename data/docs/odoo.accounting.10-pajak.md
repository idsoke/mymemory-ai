---
title: Odoo Accounting / Invoicing: Pajak
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart LR
    P["Produk<br/>taxes_id / supplier_taxes_id"] --> L["Baris invoice<br/>tax_ids"]
    FP["Fiscal Position<br/>(mapping pajak & akun<br/>per partner/negara)"] -->|"map_tax()"| L
    L --> C["account.tax<br/>_get_tax_details / compute_all"]
    C --> T1{"amount_type"}
    T1 -- percent --> R1["% dari harga"]
    T1 -- fixed --> R2["Nominal tetap per unit"]
    T1 -- division --> R3["Percentage Tax Included<br/>(dibagi)"]
    T1 -- group --> R4["Gabungan beberapa pajak"]
    R1 & R2 & R3 & R4 --> TL["Baris pajak (display_type = tax)<br/>tax_line_id, akun dari repartition line"]
    TL --> TR["Laporan pajak<br/>(tax tags / account.report)"]
```

Pengaturan *price include* per pajak menentukan apakah harga produk sudah termasuk pajak. Cash rounding (`account.cash.rounding`) bisa menambah baris pembulatan.

---

_Sumber: dokumentasi_accounting_odoo.md §10_
