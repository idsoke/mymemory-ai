---
title: Odoo HR: Employees: Employee & Version
tags: odoo,hr,dokumentasi
project: odoo
updated: 2026-10-30
---

`hr.employee` memakai **`_inherits = {'hr.version': 'version_id'}`**. Field seperti departemen, jabatan, jadwal kerja, gaji, tanggal kontrak, dan data pribadi dibaca/ditulis ke versi yang aktif. Setiap perubahan bisa disimpan sebagai **versi baru dengan tanggal efektif**, sehingga riwayatnya tidak hilang.

```mermaid
flowchart LR
    E["hr.employee<br/>(Budi)"]
    E -->|"version_ids"| V1["hr.version<br/>date_version: 2024-01-01<br/>Job: Staff, Wage: 8 jt<br/>contract 2024-01-01 → 2024-12-31"]
    E -->|"version_ids"| V2["hr.version<br/>date_version: 2025-01-01<br/>Job: Senior Staff, Wage: 10 jt"]
    E -->|"version_ids"| V3["hr.version<br/>date_version: 2026-07-01<br/>Dept: Sales, Wage: 12 jt"]
    E ==>|"current_version_id<br/>(berlaku hari ini)"| V3
    E -.->|"version_id<br/>(versi yang sedang dibaca/ditulis,<br/>bisa diganti lewat context)"| V2

    W["Wizard<br/>hr.employee.create.version.wizard"] -->|"Buat versi baru<br/>per tanggal efektif"| E
    T["contract_template_id<br/>(template kontrak)"] -.-> V3
```

---

_Sumber: dokumentasi_hr_odoo.md §3_
