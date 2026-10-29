---
title: Odoo Inventory: Konsep Inti: Lokasi, Quant, Move
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

Odoo memakai **double-entry inventory**: setiap pergerakan barang adalah perpindahan dari satu lokasi ke lokasi lain. Stok tidak pernah "muncul" atau "hilang", hanya berpindah antar lokasi (termasuk lokasi virtual).

```mermaid
flowchart LR
    V["Partners/Vendors<br/>usage = supplier"] -->|"Receipt"| S["WH/Stock<br/>usage = internal"]
    S -->|"Delivery"| C["Partners/Customers<br/>usage = customer"]
    S -->|"Internal Transfer"| S2["WH/Stock/Rak-A<br/>usage = internal"]
    S <-->|"Inventory Adjustment"| I["Virtual/Inventory adjustment<br/>usage = inventory"]
    S -->|"Scrap"| SC["Virtual/Scrap<br/>usage = inventory"]
    S <-->|"Konsumsi / Hasil produksi"| P["Virtual/Production<br/>usage = production"]
    S -->|"Antar gudang"| T["Transit<br/>usage = transit"]

    Q[("stock.quant<br/>qty per produk + lokasi<br/>+ lot + package + owner")]
    S -.-> Q
    S2 -.-> Q
```

- **`stock.quant`** hanya ada untuk lokasi `internal` (dan `transit`): ini adalah stok fisik.
- **`stock.move`** = rencana/perpindahan per produk. **`stock.move.line`** = detail aktual (lokasi spesifik, lot/serial, package).

---

_Sumber: dokumentasi_inventory_odoo.md §2_
