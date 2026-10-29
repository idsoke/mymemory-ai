---
title: Odoo CRM: Predictive Lead Scoring (PLS)
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

Probabilitas otomatis dihitung dengan **Naive Bayes** berdasarkan histori lead won/lost per Sales Team. Field yang dipakai secara default: `stage_id`, `state_id`, `country_id`, `phone_state`, `email_state`, `source_id`, `lang_id`, `tag_ids` (dapat diatur via wizard `crm.lead.pls.update`).

```mermaid
flowchart LR
    subgraph LEARN["Pembelajaran"]
        direction TB
        H1["Lead menjadi Won / Lost"] --> H2["_handle_won_lost()<br/>_pls_increment_frequencies()"]
        H3["Rebuild penuh<br/>_pls_prepare_update_frequency_table(rebuild=True)"] --> H4
        H2 --> H4[("crm.lead.scoring.frequency<br/>(variable, value, won_count, lost_count, team)")]
    end

    subgraph PREDICT["Prediksi"]
        direction TB
        C1["Cron: _cron_update_automated_probabilities()"] --> C2
        C3["Create / write lead"] --> C2["_compute_probabilities()"]
        C2 --> C4["_pls_get_naive_bayes_probabilities()<br/>P(won) = Π P(field=value|won) · P(won)<br/>dinormalisasi dengan P(lost)"]
        C4 --> C5["automated_probability"]
        C5 --> C6{"is_automated_probability?<br/>(probability belum diubah manual)"}
        C6 -- Ya --> C7["probability = automated_probability"]
        C6 -- Tidak --> C8["probability tetap (manual)<br/>tombol action_set_automated_probability()"]
    end

    H4 --> C4
```

Nilai 0.1 ditambahkan pada `won_count`/`lost_count` untuk menghindari frekuensi nol.

---

_Sumber: dokumentasi_crm_odoo.md §8_
