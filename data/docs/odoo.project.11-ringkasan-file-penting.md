---
title: Odoo Project & Timesheet: Ringkasan File Penting
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `project/models/project_project.py` | `project.project`: visibilitas, fitur, template, analytic |
| `project/models/project_task.py` | `project.task`: stage/state, dependensi, sub-task, `CLOSED_STATES` |
| `project/models/project_task_type.py` | Stage task, rating, auto validation |
| `project/models/project_milestone.py` | Milestone |
| `project/models/project_update.py` | Project update & status |
| `project/models/project_task_recurrence.py` | Recurring task |
| `project/models/project_collaborator.py` | Project sharing ke portal |
| `hr_timesheet/models/account_analytic_line.py` | Timesheet, biaya (`_timesheet_postprocess`) |
| `hr_timesheet/models/project_task.py` | Jam efektif, sisa, progress |
| `hr_timesheet/models/project_project.py` | `allow_timesheets`, analytic account otomatis |
| `sale_project/models/sale_order_line.py` | `_timesheet_service_generation()`: proyek/task dari SO |
| `sale_project/models/product_template.py` | `service_tracking`, `service_policy` |
| `sale_timesheet/models/account_analytic_line.py` | `so_line`, billable type, invoice |
| `sale_timesheet/models/project_project.py` | `pricing_type`, `billing_type` |

_Sumber: dokumentasi_project_odoo.md §11_
