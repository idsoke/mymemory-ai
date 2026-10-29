---
title: Odoo Point of Sale: Siklus Hidup Order POS (pos.order)
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    [*] --> draft : Order dibuat di UI kasir<br/>(disimpan lokal, disinkron sebagai draft)
    draft --> paid : Pembayaran lengkap<br/>action_pos_order_paid()
    draft --> cancel : action_pos_order_cancel()
    paid --> done : Sesi divalidasi / ditutup<br/>(masuk jurnal sesi atau invoice)
    done --> [*]
    cancel --> [*]

    note right of paid
        to_invoice = True → invoice
        dibuat langsung saat paid
        (_generate_order_invoice)
    end note
```

| State | Label | Arti |
|---|---|---|
| `draft` | New | Order belum lunas (mis. meja restoran yang masih terbuka) |
| `paid` | Paid | Sudah lunas, belum ada jurnal akuntansi sesi |
| `done` | Posted | Sudah tercatat di jurnal akuntansi |
| `cancel` | Cancelled | Dibatalkan |

---

_Sumber: dokumentasi_pos_odoo.md §5_
