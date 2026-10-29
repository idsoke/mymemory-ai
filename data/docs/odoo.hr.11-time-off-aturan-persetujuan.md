---
title: Odoo HR: Time Off: Aturan Persetujuan
tags: odoo,hr,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TB
    T{"leave_validation_type<br/>(di jenis cuti)"}
    T -- no_validation --> A0["Langsung Approved"]
    T -- hr --> A1["Disetujui oleh HR Responsible<br/>(Time Off Officer)"]
    T -- manager --> A2["Disetujui oleh Time Off Approver<br/>(employee.leave_manager_id)"]
    T -- both --> A3["1. Approver → validate1 (Second Approval)<br/>2. HR Officer → validate"]

    O["Officer (group_hr_holidays_user)"] -.->|"bisa validasi<br/>dalam satu langkah"| A3
    X["_check_approval_update()<br/>cek hak user per perubahan state"] -.-> T
```

Hari wajib masuk (`hr.leave.mandatory.day`) bisa diatur agar karyawan tidak bisa mengajukan cuti pada tanggal tersebut. Libur nasional bisa diimpor lewat wizard `load.public.holiday.wizard` atau dibuat otomatis oleh cron.

---

_Sumber: dokumentasi_hr_odoo.md §11_
