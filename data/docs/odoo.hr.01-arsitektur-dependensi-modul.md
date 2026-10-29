---
title: Odoo HR: Arsitektur & Dependensi Modul
tags: odoo,hr,dokumentasi
project: odoo
updated: 2026-10-30
---

Perubahan besar di Odoo 20.0:

- **`hr.contract` tidak ada lagi.** Data kontrak (tanggal kontrak, gaji, jadwal kerja, tipe karyawan) disimpan di **`hr.version`**, yaitu riwayat versi data karyawan per tanggal efektif.
- **`hr.leave.type` tidak ada lagi.** Jenis cuti adalah **`hr.work.entry.type`** (dari `hr_work_entry`) yang diberi pengaturan time off.
- **`hr.time.rule`** (di `hr_work_entry`) adalah aturan umum untuk lembur/kurang jam, dipakai bersama oleh Attendances dan Time Off.

```mermaid
flowchart LR
    subgraph BASE["Dasar"]
        direction TB
        resource["resource<br/>Jadwal kerja & libur"]
        auth_signup
        base_setup
        digest
    end

    HR(["hr<br/>Employees"])
    WE(["hr_work_entry<br/>Work Entry Type & Time Rule"])
    ATT(["hr_attendance<br/>Attendances"])
    HOL(["hr_holidays<br/>Time Off"])
    CAL["hr_calendar"]

    BASE --> HR
    HR --> WE
    WE --> ATT
    WE --> HOL
    CAL --> HOL
    BG["barcodes,<br/>base_geolocalize"] --> ATT

    subgraph EXT["Modul lain di atasnya"]
        direction TB
        hr_holidays_attendance["hr_holidays_attendance<br/>Lembur → cuti"]
        hr_timesheet["hr_timesheet"]
        hr_expense["hr_expense"]
        hr_recruitment["hr_recruitment"]
        hr_skills["hr_skills"]
        payroll["hr_payroll (Enterprise)"]
    end
    HR --> EXT
```

---

_Sumber: dokumentasi_hr_odoo.md §1_
