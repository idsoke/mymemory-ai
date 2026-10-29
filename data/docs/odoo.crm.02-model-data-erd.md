---
title: Odoo CRM: Model Data (ERD)
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

Model utama adalah `crm.lead`, yang menyimpan **lead** maupun **opportunity** (dibedakan oleh field `type`).

```mermaid
erDiagram
    CRM_LEAD {
        char name "Judul opportunity"
        selection type "lead | opportunity"
        selection priority "0-3 bintang"
        float probability "Probabilitas (%)"
        float automated_probability "Hasil PLS"
        monetary expected_revenue
        monetary prorated_revenue "expected x probability"
        monetary recurring_revenue
        selection won_status "won | lost | pending"
        boolean active "False = arsip/lost"
        char email_from
        char phone
        char contact_name
        char partner_name
        datetime date_deadline "Expected closing"
        datetime date_closed
        datetime date_conversion
    }
    CRM_STAGE {
        char name
        int sequence
        boolean is_won
        boolean fold
        int rotting_threshold_days
        text requirements
    }
    CRM_TEAM {
        char name
        boolean use_leads
        boolean use_opportunities
        char assignment_domain
        int assignment_max
        boolean assignment_optout
    }
    CRM_TEAM_MEMBER {
        char assignment_domain
        char assignment_domain_preferred
        int assignment_max "Kapasitas per 30 hari"
    }
    CRM_TAG {
        char name
        int color
    }
    CRM_LOST_REASON {
        char name
        boolean active
    }
    CRM_RECURRING_PLAN {
        char name
        int number_of_months
    }
    CRM_LEAD_SCORING_FREQUENCY {
        char variable
        char value
        float won_count
        float lost_count
    }
    RES_PARTNER {
        char name
        char email
        boolean is_company
    }
    RES_USERS {
        char name
    }
    CALENDAR_EVENT {
        char name
        datetime start
    }
    UTM {
        char campaign_medium_source
    }
    RES_COMPANY {
        char name
    }

    CRM_LEAD }o--|| CRM_STAGE : stage_id
    CRM_LEAD }o--o| CRM_TEAM : team_id
    CRM_LEAD }o--o| RES_USERS : "user_id (Salesperson)"
    CRM_LEAD }o--o| RES_PARTNER : partner_id
    CRM_LEAD }o--o{ CRM_TAG : tag_ids
    CRM_LEAD }o--o| CRM_LOST_REASON : lost_reason_id
    CRM_LEAD }o--o| CRM_RECURRING_PLAN : recurring_plan
    CRM_LEAD ||--o{ CALENDAR_EVENT : calendar_event_ids
    CRM_LEAD }o--o| UTM : "campaign / medium / source"
    CRM_LEAD }o--o| RES_COMPANY : company_id
    CRM_STAGE }o--o{ CRM_TEAM : team_ids
    CRM_TEAM ||--o{ CRM_TEAM_MEMBER : crm_team_member_ids
    CRM_TEAM_MEMBER }o--|| RES_USERS : user_id
    CRM_LEAD_SCORING_FREQUENCY }o--o| CRM_TEAM : team_id
```

**Model wizard (TransientModel):**

| Model | File | Fungsi |
|---|---|---|
| `crm.lead2opportunity.partner.mass` | `wizard/crm_lead_to_opportunity_mass.py` | Konversi massal (Convert / Convert & Merge) |
| `crm.merge.opportunity` | `wizard/crm_merge_opportunities.py` | Menggabungkan lead/opportunity duplikat |
| `crm.lead.lost` | `wizard/crm_lead_lost.py` | Menandai lost + alasan |
| `crm.lead.pls.update` | `wizard/crm_lead_pls_update.py` | Pengaturan field & tanggal mulai PLS |

---

_Sumber: dokumentasi_crm_odoo.md §2_
