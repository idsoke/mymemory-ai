---
title: Odoo Inventory: Cron & Hak Akses
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

**Cron:**

| Nama | Model | Interval | Fungsi |
|---|---|---|---|
| Procurement: run scheduler | `stock.rule` | 1 hari | Jalankan reordering rule otomatis & reservasi ulang move |
| Account: Inventory Valuation Closing | `res.company` (modul `account`) | — | Jurnal valuasi periodik (`_cron_post_stock_valuation`) |

**Grup akses & fitur:**

```mermaid
flowchart BT
    U["base.group_user"]
    SU["stock.group_stock_user<br/>User"]
    SM["stock.group_stock_manager<br/>Administrator"]
    U --> SU --> SM

    F1["group_stock_multi_locations<br/>Storage Locations"]
    F2["group_stock_multi_warehouses<br/>Multi-Warehouses"]
    F3["group_adv_location<br/>Multi-Step Routes"]
    F4["group_production_lot<br/>Lots & Serial Numbers"]
    F5["group_tracking_lot<br/>Packages"]
    F6["group_tracking_owner<br/>Consignment"]
    F7["group_stock_picking_batch<br/>Batch / Wave Transfers"]
    F8["group_stock_sign_delivery<br/>Signature"]
    F1 & F2 & F3 & F4 -. fitur .- SU
    F5 & F6 & F7 & F8 -. fitur .- SU
```

---

_Sumber: dokumentasi_inventory_odoo.md §12_
