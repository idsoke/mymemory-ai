---
title: Odoo Inventory: Validasi Transfer & Backorder
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TB
    A(["button_validate()"]) --> B{"Picking masih draft?"}
    B -- Ya --> B1["action_confirm()<br/>qty dikerjakan = demand"]
    B -- Tidak --> C
    B1 --> C["_sanity_check()<br/>lot/serial wajib, qty valid"]
    C --> D["_pre_action_done_hook()<br/>wizard pra-validasi"]
    D --> D1{"Qty < demand?"}
    D1 -- Ya --> W1["Wizard stock.backorder.confirmation:<br/>Create Backorder / No Backorder"]
    D1 -- Tidak --> D2{"Qty = 0 di semua baris?"}
    D2 -- Ya --> W2["Wizard stock.zero.demand.confirmation"]
    D2 -- Tidak --> E
    W1 --> E["_action_done()"]
    W2 --> E
    E --> F["stock.move._action_done()<br/>stock.move.line._action_done()"]
    F --> G["stock.quant._update_available_quantity()<br/>lokasi asal −qty, lokasi tujuan +qty"]
    G --> H{"Backorder?"}
    H -- Ya --> I["_create_backorder()<br/>picking baru untuk sisa qty"]
    H -- Tidak --> J
    I --> J["_push_apply()<br/>jalankan push rule berikutnya"]
    J --> K["Move tujuan (move_dest_ids)<br/>bisa direservasi"]
    K --> L(["state = done, date_done = now"])
```

**Reservasi** (`action_assign` → `stock.move._action_assign`): menaikkan `reserved_quantity` di quant sesuai **removal strategy** lokasi/kategori produk (FIFO, LIFO, Closest, Least Packages, FEFO).

---

_Sumber: dokumentasi_inventory_odoo.md §6_
