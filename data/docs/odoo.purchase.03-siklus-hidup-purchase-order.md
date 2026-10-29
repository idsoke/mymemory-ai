---
title: Odoo Purchase: Siklus Hidup Purchase Order
tags: odoo,purchase,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    state "to approve" as to_approve
    [*] --> draft : Buat RFQ<br/>(manual / otomatis dari route Buy)
    draft --> sent : action_rfq_send()<br/>(email ke vendor)
    draft --> purchase : button_confirm()<br/>(persetujuan cukup)
    sent --> purchase : button_confirm()
    draft --> to_approve : button_confirm()<br/>(perlu persetujuan manager)
    sent --> to_approve : button_confirm()
    to_approve --> purchase : button_approve()<br/>(Purchase Manager)
    draft --> cancel : button_cancel()
    sent --> cancel : button_cancel()
    to_approve --> cancel : button_cancel()
    purchase --> cancel : button_cancel()<br/>(ditolak jika locked<br/>atau sudah ada bill posted)
    cancel --> draft : button_draft()
    purchase --> purchase : button_lock() / button_unlock()
```

| State | Label | Arti |
|---|---|---|
| `draft` | RFQ | Request for Quotation, bisa diubah |
| `sent` | RFQ Sent | RFQ sudah dikirim ke vendor |
| `to approve` | To Approve | Menunggu persetujuan manager (double validation) |
| `purchase` | Purchase Order | PO dikonfirmasi; receipt dibuat (`purchase_stock`) |
| `cancel` | Cancelled | Dibatalkan |

Seperti Sales, status "Locked/Done" lama diganti field **`locked`**. Jika pengaturan **Lock Confirmed Orders** (`po_lock = lock`) aktif, PO langsung terkunci setelah disetujui. Field `acknowledged` menandai vendor sudah mengonfirmasi PO (`action_acknowledge`).

---

_Sumber: dokumentasi_purchase_odoo.md §3_
