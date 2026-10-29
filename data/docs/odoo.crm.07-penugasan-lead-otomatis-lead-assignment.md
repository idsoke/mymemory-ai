---
title: Odoo CRM: Penugasan Lead Otomatis (Lead Assignment)
tags: odoo,crm,dokumentasi
project: odoo
updated: 2026-10-30
---

Diaktifkan di **CRM → Configuration → Settings → Rule-Based Assignment**. Bisa manual (tombol *Assign Leads*) atau otomatis via cron **"CRM: Lead Assignment"** (`crm.team._cron_assign_leads()`, default tiap 1 hari).

```mermaid
flowchart TB
    START(["Cron _cron_assign_leads()<br/>atau tombol action_assign_leads()"]) --> T["Ambil Sales Team aktif<br/>(assignment_optout = False)"]
    T --> D["Untuk tiap team: cari lead tanpa team<br/>sesuai team.assignment_domain<br/>(dibuat ≤ 7 hari terakhir)"]
    D --> DUP["Gabungkan duplikat<br/>(_merge_opportunity)"]
    DUP --> TA["Set team_id ke lead"]
    TA --> M["Untuk tiap anggota (crm.team.member)<br/>hitung kuota = assignment_max / 30<br/>dikurangi lead yg sudah diterima"]
    M --> PR{"Cocok<br/>assignment_domain_preferred?"}
    PR -- Ya --> P1["Prioritaskan ke member tsb"]
    PR -- Tidak --> P2["Cocokkan assignment_domain member"]
    P1 --> RR["Distribusi berbobot (random weighted)<br/>berdasarkan sisa kuota"]
    P2 --> RR
    RR --> U["Set user_id<br/>+ konversi ke opportunity<br/>(_assign_and_convert_leads)"]
    U --> FINISH(["Selesai / notifikasi"])
```

Aturan member (`assignment_rules`): **Always in rotation**, **In rotation, with a limit**, **Out of rotation**.

---

_Sumber: dokumentasi_crm_odoo.md §7_
