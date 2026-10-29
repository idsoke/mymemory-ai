---
title: Odoo Project & Timesheet: Stage vs State pada Task
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

Task punya dua dimensi status yang berbeda:

```mermaid
flowchart LR
    subgraph STG["stage_id: project.task.type"]
        direction LR
        S1["New"] --> S2["In Progress"] --> S3["Review"] --> S4["Done (fold)"]
    end
    subgraph ST["state: status kerja"]
        direction TB
        A["01_in_progress"]
        B["02_changes_requested"]
        C["03_approved"]
        D["04_waiting_normal<br/>(diblokir task lain)"]
        E["1_done / 1_canceled<br/>(CLOSED_STATES)"]
    end
    STG -. "stage = kolom kanban,<br/>dapat diatur per proyek" .- ST
```

- **Stage** (`stage_id`) = kolom kanban; bebas didefinisikan dan bisa dipakai bersama oleh beberapa proyek (`project_ids`).
- **State** (`state`) = status kerja task. Saat task pindah stage, state yang belum tertutup kembali ke `01_in_progress`.
- **Personal stage** (`personal_stage_type_id`) = kanban pribadi tiap user (Inbox, Today, …), tidak memengaruhi stage proyek.

---

_Sumber: dokumentasi_project_odoo.md §3_
