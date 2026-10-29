---
title: Odoo HR: Cron
tags: odoo,hr,dokumentasi
project: odoo
updated: 2026-10-30
---

| Modul | Nama | Fungsi |
|---|---|---|
| hr_attendance | Attendance: Automatically check-out employees | `_cron_auto_check_out()` |
| hr_attendance | Attendance: Detect Absences for employees | `_cron_absence_detection()` |
| hr_attendance | Attendance: Process daily time rules | `_cron_process_day_undertime_rules()` |
| hr_attendance | Attendance: Process weekly time rules | `_cron_process_week_time_rules()` |
| hr_holidays | Accrual Time Off: Updates the number of time off | `_update_accrual()` pada alokasi accrual |
| hr_holidays | Time Off: Cancel invalid leaves | `_cancel_invalid_leaves()` |
| hr_holidays | Time Off: Generate Public Holidays | `_cron_generate_public_holidays()` |
| hr_holidays | Time Off: Process daily / weekly time rules | Time rule untuk cuti |

---

_Sumber: dokumentasi_hr_odoo.md §12_
