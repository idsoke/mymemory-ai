---
title: Odoo Project & Timesheet: Milestone, Project Update & Recurring Task
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart LR
    subgraph MS["Milestone (allow_milestones)"]
        direction TB
        M1["project.milestone<br/>deadline"] --> M2["Task dikaitkan (milestone_id)"]
        M2 --> M3["is_reached = True<br/>(ditandai manual; tombol tersedia<br/>saat semua task tertutup)"]
        M3 -.->|"sale_project"| M4["Billing berdasarkan milestone"]
    end
    subgraph UP["Project Update"]
        direction TB
        U1["project.update<br/>status + progress + catatan"] --> U2["last_update_status proyek<br/>on_track / at_risk / off_track /<br/>on_hold / done"]
    end
    subgraph RC["Recurring task (allow_recurring_tasks)"]
        direction TB
        R1["Task dengan recurrence_id<br/>tiap N hari/minggu/bulan/tahun"] --> R2["Task terakhir ditutup<br/>(state 1_done / 1_canceled)"]
        R2 --> R3["_create_next_occurrences():<br/>salinan task berikutnya"]
    end
```

**Template proyek:** proyek dengan `is_template = True` dipakai sebagai cetakan; proyek baru dibuat via `action_create_from_template()` (task dan stage ikut disalin).

---

_Sumber: dokumentasi_project_odoo.md §6_
