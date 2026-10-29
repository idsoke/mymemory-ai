---
title: Odoo CRM: Hak Akses (Security Groups)
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

CRM memakai grup dari `sales_team`:

```mermaid
flowchart BT
    U["base.group_user<br/>Internal User"]
    S1["sales_team.group_sale_salesman<br/>User: Own Documents Only"]
    S2["sales_team.group_sale_salesman_all_leads<br/>User: All Documents"]
    S3["sales_team.group_sale_manager<br/>Administrator"]
    GL["crm.group_use_lead<br/>Fitur 'Leads' (tahap kualifikasi)"]
    GR["crm.group_use_recurring_revenues<br/>Fitur Recurring Revenue"]

    U --> S1 --> S2 --> S3
    GL -. opsional .- S1
    GR -. opsional .- S1
```

| Grup | Akses ke `crm.lead` |
|---|---|
| Own Documents Only | Baca/tulis/buat lead miliknya sendiri atau yang belum ada salesperson (tanpa hapus) |
| All Documents | Baca/tulis/buat semua lead (tanpa hapus) |
| Administrator | CRUD semua lead + konfigurasi (stage, team, tag, lost reason, PLS) |

Semua grup juga dibatasi aturan multi-company: `company_id in company_ids + [False]`.

---

_Sumber: dokumentasi_crm_odoo.md §10_
