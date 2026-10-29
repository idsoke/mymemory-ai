---
title: Odoo CRM: Konversi Lead menjadi Opportunity
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

Di Odoo 20.0 konversi **satu lead** dilakukan langsung lewat tombol *Convert to Opportunity* (`action_convert_to_opportunity()`), tanpa wizard. Konversi **banyak lead** memakai wizard `crm.lead2opportunity.partner.mass`.

```mermaid
sequenceDiagram
    autonumber
    actor S as Salesperson
    participant L as crm.lead
    participant P as res.partner

    S->>L: Tombol "Convert to Opportunity"<br/>action_convert_to_opportunity()
    L->>L: convert_opportunity(partner_id)
    Note right of L: Lewati jika lead tidak aktif atau sudah Won
    L->>L: _convert_opportunity_data()<br/>type = opportunity, date_conversion = now<br/>stage = _stage_find(team) jika belum ada
    L->>P: _find_matching_partner()<br/>cari partner dari email_from
    alt Partner ditemukan
        P-->>L: partner_id = partner yang cocok
    else Tidak ada partner
        L->>P: _create_customer()<br/>dari contact_name / partner_name / email
        P-->>L: partner_id = partner baru
    end
    L-->>S: Form Opportunity di pipeline
```

**Konversi massal** (`crm.lead2opportunity.partner.mass`):

```mermaid
flowchart LR
    A["Pilih banyak lead<br/>(list view → Action)"] --> B["Wizard Convert to Opportunities"]
    B --> C{"Conversion Action"}
    C -- "convert" --> D["convert_opportunity()<br/>untuk tiap lead"]
    C -- "convert_and_merge" --> E["Gabungkan duplikat<br/>(_get_lead_duplicates by partner/email)<br/>lalu konversi"]
    D --> F["_handle_salesmen_assignment(user_ids, team_id)<br/>round-robin: L1→S1, L2→S2, ..., L5→S1"]
    E --> F
    F --> G{"link_to_matching_customer?"}
    G -- Ya --> H["_handle_partner_assignment()<br/>cari / buat customer"]
    G -- Tidak --> I(["Selesai"])
    H --> I
```

---

_Sumber: dokumentasi_crm_odoo.md §5_
