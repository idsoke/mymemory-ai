---
title: Odoo Sales: Siklus Hidup Sales Order
tags: odoo,sales,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    [*] --> draft : Buat quotation
    draft --> sent : action_quotation_send()<br/>(email ke customer)
    draft --> sale : action_confirm()
    sent --> sale : action_confirm()<br/>atau customer tanda tangan/bayar di portal
    draft --> cancel : action_cancel()
    sent --> cancel : action_cancel()
    sale --> cancel : action_cancel()<br/>(ditolak jika locked)
    cancel --> draft : action_draft()
    sale --> sale : action_lock() / action_unlock()

    note right of sale
        Jika "Lock Confirmed Sales" aktif
        (sale.group_auto_done_setting),
        order langsung locked setelah konfirmasi
    end note
```

| State | Label | Arti |
|---|---|---|
| `draft` | Quotation | Penawaran, bisa diubah bebas |
| `sent` | Quotation Sent | Penawaran sudah dikirim ke customer |
| `sale` | Sales Order | Sudah dikonfirmasi, memicu pengiriman/invoice |
| `cancel` | Cancelled | Dibatalkan; invoice draft terkait ikut dibatalkan |

Field `locked` menggantikan state "Locked/Done" versi lama. Order yang locked tidak bisa diubah atau dibatalkan sebelum di-unlock.

---

_Sumber: dokumentasi_sales_odoo.md §3_
