---
title: Odoo Website & eCommerce: Stok di Toko Online
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

Field stok ada di `product.template` (`website_sale`); pengecekan stok aktual dilakukan oleh `website_sale_stock` (auto install bila `stock` terpasang).

```mermaid
flowchart TD
    Q["Qty tersedia di gudang website"] --> A{"allow_out_of_stock_order?"}
    A -- "Ya (default)" --> OK["Tetap bisa dibeli<br/>(backorder)"]
    A -- "Tidak" --> LIM["Qty di cart dibatasi stok;<br/>tombol beli nonaktif saat habis"]
    LIM --> MSG["out_of_stock_message<br/>+ notifikasi stok kembali<br/>(/shop/add/stock_notification)"]
    Q --> SHOW{"show_availability?"}
    SHOW -- "Ya" --> TH["Tampilkan sisa stok jika<br/>di bawah available_threshold"]
```

---

_Sumber: dokumentasi_website_sale_odoo.md §8_
