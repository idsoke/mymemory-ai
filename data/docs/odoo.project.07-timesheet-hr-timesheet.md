---
title: Odoo Project & Timesheet: Timesheet (hr_timesheet)
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

Timesheet adalah `account.analytic.line` yang punya `project_id`. Biayanya dihitung dari tarif karyawan.

```mermaid
sequenceDiagram
    autonumber
    participant EMP as Karyawan
    participant TS as account.analytic.line
    participant TASK as project.task
    participant PRJ as project.project
    participant AA as account.analytic.account

    EMP->>TS: catat jam (unit_amount) pada task
    TS->>TS: _timesheet_postprocess():<br/>amount = -(jam × employee.hourly_cost)
    TS->>AA: account_id = analytic account proyek
    TS->>TASK: effective_hours, remaining_hours, progress
    TASK->>PRJ: total waktu proyek vs allocated_hours
    Note over PRJ,AA: Proyek dengan allow_timesheets wajib punya analytic account,<br/>dibuat otomatis lewat _create_analytic_account()
```

```mermaid
flowchart LR
    AH["allocated_hours<br/>(task / proyek)"] --> RH["remaining_hours =<br/>allocated − effective"]
    EH["effective_hours<br/>(jam timesheet task)"] --> RH
    SUB["subtask_effective_hours"] --> TOT["total_hours_spent"]
    EH --> TOT
    RH --> OV{"Negatif?"}
    OV -- "Ya" --> OT["overtime / is_project_overtime"]
```

- Satuan input: `timesheet_encode_method` = `hours` (jam/menit) atau `days` (hari/setengah hari).
- `internal_project_id` di perusahaan: proyek internal untuk jam non-proyek (cuti, pelatihan, rapat).

---

_Sumber: dokumentasi_project_odoo.md §7_
