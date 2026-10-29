---
title: Odoo HR (modul): ringkasan & daftar bagian
tags: odoo,hr,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan tiga modul HR dalam bentuk diagram: **Employees** (`addons/hr`), **Attendances** (`addons/hr_attendance`), dan **Time Off** (`addons/hr_holidays`), beserta modul dasar `hr_work_entry`.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_hr_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. **Employees**: model data (ERD)
3. **Employees**: Employee & Version (riwayat data kontrak)
4. **Employees**: siklus karyawan (onboarding → departure)
5. **Attendances**: model data
6. **Attendances**: alur check-in / check-out
7. **Attendances**: validasi, auto check-out & time rules (lembur)
8. **Time Off**: model data
9. **Time Off**: alokasi (reguler & accrual)
10. **Time Off**: siklus pengajuan cuti
11. **Time Off**: aturan persetujuan
12. Cron
13. Hak akses
14. Ringkasan file penting

---

## Bagian di memori
- `odoo.hr.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.hr.02-employees-model-data-erd`: Employees: Model Data (ERD)
- `odoo.hr.03-employees-employee-version`: Employees: Employee & Version
- `odoo.hr.04-employees-siklus-karyawan`: Employees: Siklus Karyawan
- `odoo.hr.05-attendances-model-data`: Attendances: Model Data
- `odoo.hr.06-attendances-alur-check-in-check-out`: Attendances: Alur Check-in / Check-out
- `odoo.hr.07-attendances-validasi-auto-check-out-time-rules`: Attendances: Validasi, Auto Check-out & Time Rules
- `odoo.hr.08-time-off-model-data`: Time Off: Model Data
- `odoo.hr.09-time-off-alokasi-reguler-accrual`: Time Off: Alokasi (Reguler & Accrual)
- `odoo.hr.10-time-off-siklus-pengajuan-cuti`: Time Off: Siklus Pengajuan Cuti
- `odoo.hr.11-time-off-aturan-persetujuan`: Time Off: Aturan Persetujuan
- `odoo.hr.12-cron`: Cron
- `odoo.hr.13-hak-akses`: Hak Akses
- `odoo.hr.14-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_hr_odoo.md (versi HTML: dokumentasi_hr_odoo.html)_
