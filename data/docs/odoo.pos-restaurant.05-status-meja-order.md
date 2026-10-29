---
title: Odoo POS Restaurant: Status Meja & Order
tags: odoo,pos-restaurant,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Kosong
    Kosong --> Terisi : Pilih meja → order draft dibuat<br/>(table_id, customer_count)
    Terisi --> Terisi : Tambah item / kirim ke dapur<br/>(order tetap draft, disinkron)
    Terisi --> Kosong : Order dibayar (paid)<br/>atau dipindah ke meja lain
    Terisi --> Kosong : Order dibatalkan / dihapus

    state Terisi {
        [*] --> BelumDikirim
        BelumDikirim --> DiDapur : Tombol Order
        DiDapur --> BelumDikirim : Item baru ditambahkan<br/>(badge perubahan)
    }
```

Di server, order restoran yang masih `draft` dicari berdasarkan `uuid` **atau** `table_id` + `state = draft` + `config_id` (`pos.order._get_open_order`). Dengan begitu beberapa perangkat yang membuka meja yang sama memakai order yang sama.

---

_Sumber: dokumentasi_pos_restaurant_odoo.md §5_
