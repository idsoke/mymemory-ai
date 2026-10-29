---
title: Odoo CRM: Ringkasan File Penting
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `crm/models/crm_lead.py` | Model utama `crm.lead`: konversi, won/lost, merge, mail gateway, PLS |
| `crm/models/crm_stage.py` | `crm.stage` dan daftar `AVAILABLE_PRIORITIES` |
| `crm/models/crm_team.py` | Ekstensi `crm.team`: alias email, Lead Assignment |
| `crm/models/crm_team_member.py` | Kuota & domain penugasan per anggota |
| `crm/models/crm_lead_scoring_frequency.py` | Tabel frekuensi PLS |
| `crm/models/crm_lost_reason.py` | Alasan lost |
| `crm/models/crm_recurring_plan.py` | Rencana recurring revenue (bulanan, tahunan, dll.) |
| `crm/models/res_config_settings.py` | Pengaturan CRM |
| `crm/data/ir_cron_data.xml` | Cron Lead Assignment |
| `crm/data/crm_lead_prediction_data.xml` | Field PLS default + cron update probabilitas |
| `crm/data/crm_stage_data.xml` | Stage bawaan |
| `crm/wizard/*` | Wizard konversi, merge, lost, PLS |
| `crm/security/crm_security.xml`, `crm/security/ir.access.csv` | Grup, record rule & hak akses |

_Sumber: dokumentasi_crm_odoo.md §11_
