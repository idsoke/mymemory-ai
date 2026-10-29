---
title: Odoo HR: Ringkasan File Penting
tags: odoo,hr,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `hr/models/hr_employee.py` | `hr.employee`, `_inherits` ke `hr.version`, presensi, hierarki manager |
| `hr/models/hr_version.py` | Riwayat data karyawan: kontrak, gaji, jabatan, jadwal, data pribadi |
| `hr/models/hr_department.py`, `hr_job.py` | Departemen & jabatan |
| `hr/models/hr_employee_departure.py` | Proses karyawan keluar |
| `hr/models/mail_activity_plan.py` | Onboarding/offboarding plan |
| `hr/security/hr_security.xml` | Grup & record rule Employees |
| `hr_work_entry/models/hr_work_entry_type.py`, `hr_time_rule.py` | Jenis work entry & time rule |
| `hr_attendance/models/hr_attendance.py` | Check-in/out, validasi, lembur |
| `hr_attendance/models/hr_employee.py` | `_attendance_action_change()`, status presensi |
| `hr_attendance/models/res_company.py` | Kiosk, auto check-out, validasi, absence management |
| `hr_attendance/controllers/main.py` | Endpoint kiosk & systray |
| `hr_holidays/models/hr_work_entry_type.py` | Pengaturan jenis cuti |
| `hr_holidays/models/hr_leave.py` | Pengajuan cuti, persetujuan, efek ke kalender |
| `hr_holidays/models/hr_leave_allocation.py` | Alokasi & accrual |
| `hr_holidays/models/hr_leave_accrual_plan*.py` | Accrual plan & level |
| `hr_holidays/data/ir_cron_data.xml` | Cron Time Off |

_Sumber: dokumentasi_hr_odoo.md §14_
