---
title: Odoo CRM: Sumber Masuknya Lead
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TB
    U1["Salesperson<br/>(input manual / Quick Create Kanban)"]
    U2["Email ke alias Sales Team<br/>mis. sales@perusahaan.com"]
    U3["Form Kontak Website<br/>(website_crm)"]
    U4["Livechat<br/>/lead command (crm_livechat)"]
    U5["Lead Generation IAP<br/>(crm_iap_mine, website_crm_iap_reveal)"]
    U6["Event / Survey / Mass Mailing<br/>(event_crm, survey_crm)"]
    U7["Import CSV / Excel"]

    MG["mail gateway<br/>crm.lead.message_new()"]
    LEAD[("crm.lead")]
    ASG{"Ada user_id?"}
    AUTO["_assign_userless_lead_in_team()<br/>atau cron Lead Assignment"]
    DONE["Lead siap ditindaklanjuti<br/>(aktivitas, email, meeting)"]

    U2 --> MG --> LEAD
    U1 --> LEAD
    U3 --> LEAD
    U4 --> LEAD
    U5 --> LEAD
    U6 --> LEAD
    U7 --> LEAD
    LEAD --> ASG
    ASG -- Tidak --> AUTO --> DONE
    ASG -- Ya --> DONE
```

Pada `message_new()`, default salesperson **dikosongkan** (`default_user_id=False`) agar penugasan dilakukan oleh aturan otomatis, bukan oleh user gateway (root). Nama lead diambil dari subjek email, `email_from` dari pengirim.

---

_Sumber: dokumentasi_crm_odoo.md §4_
