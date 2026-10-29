---
title: Odoo Website & eCommerce: Katalog: Publikasi Produk, Kategori & Harga
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TB
    P["product.template<br/>sale_ok = True"] --> PUB{"is_published?"}
    PUB -- "Tidak" --> HID["Tidak tampil di /shop"]
    PUB -- "Ya" --> SHOP["Tampil di /shop"]
    SHOP --> CAT["Dikelompokkan oleh<br/>public_categ_ids (kategori eCommerce)"]
    SHOP --> ORD["Urutan: website_sequence /<br/>shop_default_sort website"]
    SHOP --> RIB["Label: website_ribbon_id"]
    SHOP --> PRICE["Harga dari pricelist website<br/>(/shop/change_pricelist)"]
    PRICE --> TAX["Tampil termasuk / tanpa pajak<br/>(show_line_subtotals_tax_selection)"]
    SHOP --> VAR["Varian dipilih di halaman produk<br/>(/shop/config/product)"]
```

Halaman utama: `/shop` (daftar produk, filter, pencarian), `/shop/<product>` (detail produk), `/shop/compare` (perbandingan), `/shop/wishlist` (wishlist).

---

_Sumber: dokumentasi_website_sale_odoo.md §3_
