---
title: Odoo Project & Timesheet: Penagihan Berdasarkan Timesheet (sale_timesheet)
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
sequenceDiagram
    autonumber
    participant TS as Timesheet
    participant SOL as sale.order.line
    participant SO as sale.order
    participant INV as account.move

    TS->>SOL: so_line ditentukan dari task/proyek<br/>(atau pemetaan karyawan → SOL)
    TS->>TS: billable_type<br/>(04_billable_time, 02_billable_fixed, ...)
    SOL->>SOL: qty_delivered += jam<br/>(qty_delivered_method = timesheet)
    SO->>INV: Create Invoice
    INV-->>TS: reinvoice_move_id = invoice<br/>(timesheet terkunci dari edit)
```

**Pricing proyek** (`pricing_type` di `project.project`):

| Nilai | Arti |
|---|---|
| `task_rate` | Tarif mengikuti SOL di task |
| `fixed_rate` | Satu SOL (tarif) untuk seluruh proyek |
| `employee_rate` | Tarif per karyawan (`project.sale.line.employee.map`) |

---

_Sumber: dokumentasi_project_odoo.md §9_
