---
title: Odoo Project & Timesheet: Arsitektur & Dependensi Modul
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

`project` bergantung pada `analytic`, `mail`, `portal_rating`, dan `resource`. Ia **tidak** bergantung pada HR. Pencatatan waktu (timesheet) ditambahkan oleh `hr_timesheet`.

```mermaid
flowchart LR
    analytic["analytic"] --> PRJ(["project<br/>Proyek, task, stage, milestone"])
    mail["mail / portal_rating"] --> PRJ
    resource["resource"] --> PRJ

    PRJ --> HT(["hr_timesheet<br/>Timesheet = account.analytic.line"])
    hr["hr"] --> HT

    subgraph SALE["Penghubung ke Sales"]
        direction TB
        sale_project["sale_project<br/>SO → proyek/task, milestone billing<br/>(auto: sale_management + project_account)"]
        sale_timesheet["sale_timesheet<br/>Tagih berdasarkan timesheet<br/>(auto_install)"]
    end
    PRJ --> sale_project
    sale_project --> sale_timesheet
    HT --> sale_timesheet

    subgraph EXT["Modul lain"]
        direction TB
        project_todo["project_todo<br/>To-Do pribadi"]
        project_timesheet_holidays["project_timesheet_holidays<br/>Cuti → timesheet otomatis"]
        project_mrp["project_mrp<br/>MO terkait proyek"]
        project_purchase["project_purchase<br/>PO terkait proyek"]
    end
    PRJ --> EXT
```

---

_Sumber: dokumentasi_project_odoo.md §1_
