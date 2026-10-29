---
title: Odoo Project & Timesheet: Siklus Hidup Task & Dependensi
tags: odoo,project,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    state "01_in_progress" as in_progress
    state "02_changes_requested" as changes_requested
    state "03_approved" as approved
    state "04_waiting_normal" as waiting
    state "1_done" as done
    state "1_canceled" as canceled
    [*] --> in_progress
    in_progress --> changes_requested : reviewer minta revisi
    changes_requested --> in_progress
    in_progress --> approved
    approved --> done
    in_progress --> done
    in_progress --> waiting : ada depend_on_ids yang belum selesai
    waiting --> in_progress : semua task pendahulu ditutup
    in_progress --> canceled
    done --> [*]
    canceled --> [*]

```

**Rating pelanggan:** jika stage punya `rating_active` dan `auto_validation_state`, balasan rating positif dari pelanggan mengubah state menjadi `03_approved`; rating netral/negatif menjadi `02_changes_requested`.

---

_Sumber: dokumentasi_project_odoo.md §4_
