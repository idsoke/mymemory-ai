---
title: Odoo Inventory: Procurement: Route & Rule
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

Kebutuhan barang (dari SO, orderpoint, MTO, dll.) dinyatakan sebagai **procurement**, lalu `stock.rule.run()` mencari rule yang cocok dan menjalankannya.

```mermaid
flowchart TB
    SRC["Sumber kebutuhan:<br/>Sales Order · Reordering Rule ·<br/>MTO dari move lain · Manual Replenish"] --> PROC["Procurement<br/>(produk, qty, lokasi tujuan, values)"]
    PROC --> RUN["stock.rule.run(procurements)"]
    RUN --> GR["_get_rule()<br/>cari rule berdasarkan:<br/>1. route di procurement/SO line<br/>2. route produk & kategori<br/>3. route warehouse<br/>+ lokasi tujuan (naik ke parent)"]
    GR --> ACT{"rule.action"}
    ACT -- pull --> PULL["_run_pull()<br/>buat stock.move<br/>dari location_src_id → location_dest_id"]
    ACT -- buy --> BUY["purchase_stock: _run_buy()<br/>buat / tambah RFQ"]
    ACT -- manufacture --> MFG["mrp: _run_manufacture()<br/>buat Manufacturing Order"]
    PULL --> PM{"procure_method"}
    PM -- make_to_stock --> MTS["Ambil dari stok<br/>(menunggu reservasi)"]
    PM -- make_to_order --> MTO["Buat procurement baru<br/>di lokasi sumber (rekursif)"]
    PM -- mts_else_mto --> MIX["Pakai stok jika ada,<br/>sisanya MTO"]
    MTO --> RUN

    DONE["Move selesai di lokasi X"] --> PUSH["_push_apply()<br/>cari push rule untuk lokasi X"]
    PUSH --> PUSH2["Buat move lanjutan<br/>(auto: manual / transparent)"]
```

---

_Sumber: dokumentasi_inventory_odoo.md §7_
