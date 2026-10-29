---
title: Odoo Project & Timesheet (modul): ringkasan & daftar bagian
tags: odoo,project,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **Project** (`addons/project`) dan **Timesheet** (`addons/hr_timesheet`), beserta penghubung ke Sales (`sale_project`, `sale_timesheet`), dalam bentuk diagram.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_project_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Model data (ERD)
3. Stage vs State pada task
4. Siklus hidup task & dependensi
5. Visibilitas proyek & project sharing (portal)
6. Milestone, project update & recurring task
7. Timesheet (`hr_timesheet`)
8. Dari Sales Order ke proyek (`sale_project`)
9. Penagihan berdasarkan timesheet (`sale_timesheet`)
10. Pengaturan, cron & hak akses
11. Ringkasan file penting

---

## Bagian di memori
- `odoo.project.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.project.02-model-data-erd`: Model Data (ERD)
- `odoo.project.03-stage-vs-state-pada-task`: Stage vs State pada Task
- `odoo.project.04-siklus-hidup-task-dependensi`: Siklus Hidup Task & Dependensi
- `odoo.project.05-visibilitas-proyek-project-sharing`: Visibilitas Proyek & Project Sharing
- `odoo.project.06-milestone-project-update-recurring-task`: Milestone, Project Update & Recurring Task
- `odoo.project.07-timesheet-hr-timesheet`: Timesheet (hr_timesheet)
- `odoo.project.08-dari-sales-order-ke-proyek-sale-project`: Dari Sales Order ke Proyek (sale_project)
- `odoo.project.09-penagihan-berdasarkan-timesheet-sale-timesheet`: Penagihan Berdasarkan Timesheet (sale_timesheet)
- `odoo.project.10-pengaturan-cron-hak-akses`: Pengaturan, Cron & Hak Akses
- `odoo.project.11-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_project_odoo.md (versi HTML: dokumentasi_project_odoo.html)_
