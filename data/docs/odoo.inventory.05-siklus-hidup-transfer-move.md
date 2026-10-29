---
title: Odoo Inventory: Siklus Hidup Transfer & Move
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    [*] --> draft : Transfer dibuat
    draft --> confirmed : action_confirm()<br/>(Mark as To Do)
    draft --> waiting : Menunggu move lain<br/>(chain multi-step / MTO)
    waiting --> confirmed : Move sebelumnya done
    confirmed --> assigned : action_assign()<br/>stok tersedia & direservasi
    confirmed --> confirmed : Stok kurang<br/>(Check Availability gagal)
    assigned --> done : button_validate()
    confirmed --> done : button_validate()<br/>(paksa / tanpa reservasi)
    draft --> cancel : action_cancel()
    confirmed --> cancel : action_cancel()
    assigned --> cancel : action_cancel()
    done --> [*]
    cancel --> [*]
```

| State picking | Label | Arti |
|---|---|---|
| `draft` | Draft | Belum dikonfirmasi |
| `waiting` | Waiting Another Operation | Menunggu transfer lain selesai |
| `confirmed` | Waiting | Menunggu stok tersedia |
| `assigned` | Ready | Stok sudah direservasi, siap diproses |
| `done` | Done | Selesai, quant sudah diperbarui |
| `cancel` | Cancelled | Dibatalkan |

`stock.move` punya state tambahan **`partially_available`**. Kebijakan pengiriman (`move_type`): **direct** = kirim sebagian dengan backorder, **one** = kirim saat semua produk siap.

---

_Sumber: dokumentasi_inventory_odoo.md §5_
