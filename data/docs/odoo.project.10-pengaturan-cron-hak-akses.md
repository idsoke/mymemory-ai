---
title: Odoo Project & Timesheet: Pengaturan, Cron & Hak Akses
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

**Fitur proyek** (diaktifkan per proyek, butuh grup):

| Field proyek | Grup |
|---|---|
| `allow_task_dependencies` | `project.group_project_task_dependencies` |
| `allow_milestones` | `project.group_project_milestone` |
| `allow_recurring_tasks` | `project.group_project_recurring_tasks` |
| Stage proyek (`stage_id`) | `project.group_project_stages` |

**Cron:** `Project Stage: Send rating` (`project/data/ir_cron_data.xml`) mengirim permintaan rating untuk task di stage yang `rating_active`. Pengingat timesheet diatur di `hr_timesheet` (`reminder_user_allow`, `reminder_allow`).

```mermaid
flowchart BT
    U["base.group_user"]
    PU["project.group_project_user<br/>User"]
    PM["project.group_project_manager<br/>Administrator"]
    U --> PU --> PM

    TU["hr_timesheet.group_hr_timesheet_user<br/>Timesheet: data sendiri"]
    TA["hr_timesheet.group_hr_timesheet_approver<br/>Timesheet: semua data"]
    TM["hr_timesheet.group_timesheet_manager<br/>Administrator<br/>(+ hr.group_hr_user)"]
    U --> TU --> TA --> TM
```

---

_Sumber: dokumentasi_project_odoo.md §10_
