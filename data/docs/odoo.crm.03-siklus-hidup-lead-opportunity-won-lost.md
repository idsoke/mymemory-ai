---
title: Odoo CRM: Siklus Hidup Lead → Opportunity → Won / Lost
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

Status *won/lost* dihitung di field `won_status`:

- **Won** = lead berada di stage dengan `is_won = True` (probabilitas 100%).
- **Lost** = `active = False` **dan** `probability = 0`.
- **Pending** = selain itu.

Stage bawaan (`data/crm_stage_data.xml`): **New (1) → Qualified (2) → Proposition (3) → Won (70)**.

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Lead : Dibuat (manual / email / website / IAP)<br/>type = lead
    [*] --> New : Dibuat langsung sebagai opportunity<br/>(jika grup "Leads" tidak aktif)

    Lead --> New : action_convert_to_opportunity()<br/>type = opportunity
    Lead --> Lost : action_set_lost()

    state Pipeline {
        New --> Qualified
        Qualified --> Proposition
        Proposition --> Qualified
    }

    Pipeline --> Won : action_set_won()<br/>stage.is_won = True, probability = 100
    Pipeline --> Lost : action_set_lost()<br/>active = False, probability = 0
    Lost --> Pipeline : action_restore()<br/>probability = automated_probability
    Won --> Pipeline : Pindah ke stage non-won
    Won --> [*]
    Lost --> [*]
    note right of Pipeline : type = opportunity
```

---

_Sumber: dokumentasi_crm_odoo.md §3_
