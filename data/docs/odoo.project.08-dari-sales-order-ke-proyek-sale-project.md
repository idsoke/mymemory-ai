---
title: Odoo Project & Timesheet: Dari Sales Order ke Proyek (sale_project)
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

Produk jasa punya `service_tracking` yang menentukan apa yang dibuat saat SO dikonfirmasi.

```mermaid
flowchart TD
    SO["Sales Order dikonfirmasi<br/>_action_confirm()"] --> GEN["order_line._timesheet_service_generation()"]
    GEN --> T{"product.service_tracking"}
    T -- "no" --> N["Tidak ada yang dibuat"]
    T -- "task_global_project" --> A["Task di proyek yang sudah ada<br/>(product.project_id)"]
    T -- "project_only" --> B["Proyek baru<br/>(bisa dari project_template_id)"]
    T -- "task_in_project" --> C["Proyek baru + task per baris SO"]
    A & B & C --> L["sale_line_id terhubung ke task/proyek"]
```

**Kebijakan penagihan jasa** (`service_policy` di produk):

| Nilai | Arti | invoice_policy |
|---|---|---|
| `ordered_prepaid` | Prepaid / harga tetap | `order` |
| `delivered_milestones` | Berdasarkan milestone (jika fitur milestone aktif) | `delivery` |
| `delivered_timesheet` | Berdasarkan timesheet (`sale_timesheet`) | `delivery` |
| `delivered_manual` | Berdasarkan delivery manual | `delivery` |

---

_Sumber: dokumentasi_project_odoo.md §8_
