---
title: Odoo Manufacturing: Pengaturan & Hak Akses
tags: odoo,mrp,dokumentasi
project: odoo
updated: 2026-10-30
---

**Pengaturan** (`res.config.settings`):

| Opsi | Field / grup |
|---|---|
| Work Orders | `group_mrp_routings` → `mrp.group_mrp_routings` |
| By-Products | `group_mrp_byproducts` → `mrp.group_mrp_byproducts` |
| Unlock MO secara default | `group_unlocked_by_default` → `mrp.group_unlocked_by_default` |
| MPS, PLM, Quality | `module_mrp_mps`, `module_mrp_plm`, `module_quality_control` (Enterprise) |
| Subcontracting | `module_mrp_subcontracting` |

```mermaid
flowchart BT
    SU["stock.group_stock_user"]
    MU["mrp.group_mrp_user<br/>User"]
    MM["mrp.group_mrp_manager<br/>Administrator"]
    SU --> MU --> MM

    F1["mrp.group_mrp_routings<br/>Work Orders"]
    F2["mrp.group_mrp_byproducts<br/>By-Products"]
    F3["mrp.group_unlocked_by_default"]
    F1 & F2 & F3 -. fitur .- MU
```

---

_Sumber: dokumentasi_mrp_odoo.md §11_
