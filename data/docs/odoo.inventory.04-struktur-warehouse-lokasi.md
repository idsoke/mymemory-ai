---
title: Odoo Inventory: Struktur Warehouse & Lokasi
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

Saat warehouse dibuat, Odoo otomatis membuat lokasi, operation type, route, dan rule sesuai jumlah langkah penerimaan dan pengiriman.

```mermaid
flowchart TB
    WH["Warehouse WH<br/>(view: WH)"]
    WH --> STK["WH/Stock<br/>lot_stock_id"]
    WH --> INP["WH/Input<br/>(2-3 langkah terima)"]
    WH --> QC["WH/Quality Control<br/>(3 langkah terima)"]
    WH --> PCK["WH/Packing Zone<br/>(3 langkah kirim)"]
    WH --> OUT["WH/Output<br/>(2-3 langkah kirim)"]

    subgraph REC["Penerimaan (reception_steps)"]
        direction LR
        R1["one_step:<br/>Vendor → Stock"]
        R2["two_steps:<br/>Vendor → Input → Stock"]
        R3["three_steps:<br/>Vendor → Input → QC → Stock"]
    end

    subgraph DEL["Pengiriman (delivery_steps)"]
        direction LR
        D1["ship_only:<br/>Stock → Customer"]
        D2["pick_ship:<br/>Stock → Output → Customer"]
        D3["pick_pack_ship:<br/>Stock → Packing → Output → Customer"]
    end

    WH -.-> REC
    WH -.-> DEL
```

Operation type yang dibuat: **Receipts** (`incoming`), **Delivery Orders** (`outgoing`), **Internal Transfers**, **Pick**, **Pack**, **Storage**, **Quality Control**, dll. sesuai konfigurasi.

---

_Sumber: dokumentasi_inventory_odoo.md §4_
