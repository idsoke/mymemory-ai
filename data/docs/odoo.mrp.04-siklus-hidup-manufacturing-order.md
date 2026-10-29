---
title: Odoo Manufacturing: Siklus Hidup Manufacturing Order
tags: odoo,mrp,dokumentasi
project: odoo
updated: 2026-10-30
---

`state` dihitung otomatis (`_compute_state`) dari status move dan work order.

```mermaid
stateDiagram-v2
    [*] --> draft
    draft --> confirmed : action_confirm()
    confirmed --> progress : komponen mulai dipick atau WO dimulai
    progress --> to_close : semua WO done/cancel
    confirmed --> done : button_mark_done()
    progress --> done : button_mark_done()
    to_close --> done : button_mark_done()
    draft --> cancel : action_cancel()
    confirmed --> cancel : action_cancel()
    progress --> cancel : action_cancel()
    done --> [*]
    cancel --> [*]
```

**Kesiapan bahan** (`reservation_state`, terpisah dari `state`):

| Nilai | Arti |
|---|---|
| `confirmed` | Waiting: komponen belum tersedia |
| `assigned` | Ready: komponen tersedia (semua, atau operasi pertama jika `ready_to_produce = asap`) |
| `waiting` | Waiting Another Operation: menunggu transfer sebelumnya (mis. pick komponen) |

---

_Sumber: dokumentasi_mrp_odoo.md §4_
