---
title: Odoo Website & eCommerce: Arsitektur & Dependensi Modul
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

`website_sale` bergantung pada `website`, `sale`, `website_payment`, `website_mail`, `portal_rating`, `digest`, `delivery`, dan `html_builder`. Order online adalah **Sales Order biasa** dengan `website_id` terisi.

```mermaid
flowchart LR
    website["website<br/>halaman, menu, visitor"] --> WS(["website_sale<br/>Toko online, cart, checkout"])
    sale["sale<br/>Sales Order"] --> WS
    wp["website_payment<br/>payment provider"] --> WS
    delivery["delivery<br/>metode pengiriman"] --> WS
    mail["website_mail / portal_rating"] --> WS

    subgraph EXT["Modul yang memperluas eCommerce"]
        direction TB
        website_sale_stock["website_sale_stock<br/>Stok & delivery (auto_install)"]
        website_sale_loyalty["website_sale_loyalty<br/>Kupon, promo, gift card"]
        website_sale_collect["website_sale_collect<br/>Click & collect di toko"]
        website_sale_mrp["website_sale_mrp<br/>Stok produk kit"]
        website_sale_slides["website_sale_slides<br/>Jual kursus eLearning"]
        website_sale_mass_mailing["website_sale_mass_mailing<br/>Newsletter di checkout"]
    end
    WS --> EXT
```

---

_Sumber: dokumentasi_website_sale_odoo.md §1_
