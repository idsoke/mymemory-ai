---
title: Odoo Manufacturing: Bill of Materials: Manufacture vs Kit
tags: odoo,mrp,dokumentasi
project: odoo
updated: 2026-10-30
---

Field `type` di `mrp.bom` menentukan perilaku BoM.

```mermaid
flowchart TB
    BOM{"mrp.bom.type"}
    BOM -- "normal<br/>Manufacture this product" --> N1["Dipakai untuk membuat MO"]
    N1 --> N2["Komponen dikonsumsi,<br/>produk jadi masuk stok"]
    N2 --> N3["Operasi → Work Order<br/>(jika grup Work Orders aktif)"]

    BOM -- "phantom<br/>Kit" --> K1["Tidak ada MO"]
    K1 --> K2["Saat SO/PO/transfer dibuat,<br/>produk kit dipecah (explode)<br/>menjadi move per komponen"]
    K2 --> K3["Stok yang bergerak adalah<br/>komponennya, bukan kit"]

    SUB["bom_line.child_bom_id<br/>komponen yang punya BoM sendiri"] -.->|"multi-level BoM"| N1
    BP["byproduct_ids<br/>(grup By-Products)"] -.->|"produk sampingan,<br/>cost_share"| N2
```

**Pemilihan BoM:** `mrp.bom._bom_find()` mencari BoM yang cocok dengan varian produk, perusahaan, dan (jika diisi) `picking_type_id`. BoM khusus varian (`product_id` terisi) didahulukan dari BoM template.

---

_Sumber: dokumentasi_mrp_odoo.md §3_
