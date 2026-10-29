---
title: Odoo HR: Attendances: Validasi, Auto Check-out & Time Rules
tags: odoo,hr,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TB
    A[("hr.attendance")] --> V{"attendance_validation<br/>(perusahaan)"}
    V -- no_validation --> V1["Otomatis validated"]
    V -- manual_validation --> V2["draft → manager validate / refuse"]
    V -- tolerance_validation --> V3["Perlu persetujuan hanya jika<br/>di luar toleransi jam"]

    A --> AC{"auto_check_out?"}
    AC -- "tolerance" --> AC1["Cron: check-out otomatis setelah<br/>jam kerja + toleransi"]
    AC -- "specific_time" --> AC2["Cron: check-out otomatis<br/>pada jam tertentu"]

    A --> AB{"absence_management?"}
    AB -- Ya --> AB1["Cron: deteksi karyawan tidak hadir<br/>tanpa cuti"]

    A --> TR["Cron harian & mingguan:<br/>evaluasi hr.time.rule"]
    TR --> TR1{"threshold_operator"}
    TR1 -- exceed --> OT["Jam kerja > jadwal/expected_hours<br/>→ attendance overtime<br/>(source_attendance_id,<br/>work_entry_type_id, amount_rate)"]
    TR1 -- less_than --> UT["Jam kerja < jadwal<br/>→ undertime"]
    OT --> OT2["Bisa dikonversi jadi hak cuti<br/>(hr_holidays_attendance)"]
```

Time rule bisa dibatasi per hari (Senin–Minggu, hari libur), jam (`timing_start`–`timing_stop`), karyawan (`employee_domain`), dan negara. Toleransi bisa dibedakan untuk karyawan (`employee_tolerance`) dan perusahaan (`employer_tolerance`).

---

_Sumber: dokumentasi_hr_odoo.md §7_
