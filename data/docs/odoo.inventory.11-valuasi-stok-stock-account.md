---
title: Odoo Inventory: Valuasi Stok (stock_account)
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TB
    A["Kategori produk / Perusahaan"] --> B{"cost_method"}
    B -- standard --> B1["Standard Price<br/>(biaya tetap)"]
    B -- average --> B2["Average Cost (AVCO)<br/>dihitung ulang tiap barang masuk"]
    B -- fifo --> B3["FIFO<br/>(stock_account)"]

    A --> C{"Inventory Valuation<br/>(property_valuation / company.inventory_valuation)"}
    C -- "periodic (default)" --> C1["Periodic (at closing):<br/>jurnal valuasi dibuat saat closing<br/>action_close_stock_valuation()<br/>cron 'Inventory Valuation Closing'"]
    C -- real_time --> C2["Perpetual (at invoicing):<br/>jurnal valuasi otomatis saat<br/>produk ditagih / di-bill"]

    M["stock.move done"] --> V["Nilai move (value)<br/>+ product.value"]
    V --> C1
    V --> C2
```

Akun yang dipakai: **Stock Valuation Account**, **Stock Journal**, dan akun selisih harga (*price difference*) dari kategori produk atau default perusahaan.

---

_Sumber: dokumentasi_inventory_odoo.md §11_
