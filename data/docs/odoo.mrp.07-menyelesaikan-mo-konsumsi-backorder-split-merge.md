---
title: Odoo Manufacturing: Menyelesaikan MO: Konsumsi, Backorder, Split & Merge
tags: odoo,mrp,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TD
    START(["button_mark_done()"]) --> SAN["Pemeriksaan dasar<br/>(lot/serial, qty)"]
    SAN --> CONS{"Konsumsi komponen<br/>sesuai BoM?<br/>_get_consumption_issues()"}
    CONS -- "Tidak" --> WIZ1["Wizard mrp.consumption.warning<br/>konfirmasi / kembalikan ke BoM"]
    WIZ1 --> BACK
    CONS -- "Ya" --> BACK{"qty_producing lebih kecil<br/>dari product_qty?"}
    BACK -- "Tidak" --> POST
    BACK -- "Ya" --> TYPE{"picking_type.create_backorder"}
    TYPE -- "ask" --> WIZ2["Wizard mrp.production.backorder<br/>buat backorder / tidak"]
    TYPE -- "always" --> BO["Backorder MO otomatis<br/>(nama .../002)"]
    TYPE -- "never" --> POST
    WIZ2 --> POST
    BO --> POST
    POST["_post_inventory():<br/>move komponen & hasil → done"] --> FINISH(["MO done"])
```

**Fitur lain di MO:**

| Aksi | Method / wizard | Fungsi |
|---|---|---|
| Ubah jumlah | `change.production.qty` | Mengubah `product_qty` MO yang sudah dikonfirmasi |
| Split | `action_split()` → `mrp.production.split` | Memecah MO menjadi beberapa MO |
| Merge | `action_merge()` | Menggabungkan MO dengan produk & BoM sama |
| Lock/Unlock | `action_toggle_is_locked()` | Kunci qty setelah done (default terkunci kecuali grup *Unlocked by default*) |
| Nomor seri massal | `mrp.production.serial.numbers` | Generate serial untuk produk jadi |
| Generate BoM | `action_generate_bom()` | Membuat BoM dari MO tanpa BoM |

---

_Sumber: dokumentasi_mrp_odoo.md §7_
