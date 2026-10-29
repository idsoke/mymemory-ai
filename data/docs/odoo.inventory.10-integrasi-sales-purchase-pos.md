---
title: Odoo Inventory: Integrasi: Sales, Purchase, POS
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart LR
    SO["Sales Order<br/>(sale)"] -->|"sale_stock:<br/>_action_launch_stock_rule()"| REF1["stock.reference<br/>(nama SO)"]
    REF1 --> OUTP["Delivery Order<br/>WH/OUT"]
    OUTP -->|"qty_delivered"| SO

    PO["Purchase Order<br/>(purchase)"] -->|"purchase_stock:<br/>_create_picking()"| INP["Receipt<br/>WH/IN"]
    INP -->|"qty_received"| PO
    RULE["Reordering rule / MTO<br/>route Buy"] -->|"_run_buy()"| PO

    POS["Order POS<br/>(point_of_sale)"] -->|"pos_stock"| PST{"update_stock_at_closing?"}
    PST -- "Tidak (real time)" --> PP1["Picking per order<br/>_create_order_picking()"]
    PST -- "Ya" --> PP2["Picking gabungan saat sesi ditutup<br/>_create_picking_at_end_of_session()"]
```

Di `pos_stock`, picking tetap dibuat real time (walau `update_stock_at_closing` aktif) untuk order yang di-invoice pada perusahaan dengan anglo-saxon accounting, atau refund dari order yang dikirim belakangan.

---

_Sumber: dokumentasi_inventory_odoo.md §10_
