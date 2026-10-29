---
title: Odoo Point of Sale: Arsitektur Aplikasi (Backend ↔ Frontend Kasir)
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

UI kasir adalah aplikasi **OWL (JavaScript)** di `static/src/app`, berjalan di browser dan bisa bekerja **offline**. Saat dibuka, semua data master dimuat sekali lewat `pos.session.load_data()`. Setiap model yang ikut dimuat mewarisi `pos.load.mixin`. Order disimpan lokal (IndexedDB) lalu dikirim ke server lewat `pos.order.sync_from_ui()`. Notifikasi antar-perangkat memakai bus (`pos.bus.mixin`).

```mermaid
flowchart LR
    subgraph FE["Frontend POS (browser / tablet) — static/src/app"]
        direction TB
        SCR["Screens<br/>ProductScreen · PaymentScreen<br/>ReceiptScreen · TicketScreen<br/>PartnerList · TipScreen"]
        STORE["PosStore + models (JS)<br/>data lokal / IndexedDB"]
        SW["service_worker.js<br/>(mode offline)"]
        HW["Hardware<br/>printer · barcode · timbangan<br/>cash drawer · payment terminal"]
        CD["Customer Display"]
        SCR <--> STORE
        STORE --- SW
        SCR --> HW
        STORE --> CD
    end

    subgraph BE["Backend Odoo (Python)"]
        direction TB
        CTRL["controllers/main.py<br/>/pos/ui/{config_id} (web client POS)"]
        LOAD["pos.session.load_data()<br/>pos.load.mixin._load_pos_data_*"]
        SYNC["pos.order.sync_from_ui()"]
        BUS["pos.bus.mixin<br/>notifikasi realtime"]
        DB[("PostgreSQL")]
        CTRL --> LOAD --> DB
        SYNC --> DB
    end

    CTRL -- "1) Buka /pos/ui" --> SCR
    LOAD -- "2) Data master<br/>(produk, harga, pajak, partner, ...)" --> STORE
    STORE -- "3) Order lunas / draft (RPC)" --> SYNC
    SYNC -- "4) id & data order tersimpan" --> STORE
    BUS -. sinkronisasi antar perangkat .-> STORE
```

---

_Sumber: dokumentasi_pos_odoo.md §2_
