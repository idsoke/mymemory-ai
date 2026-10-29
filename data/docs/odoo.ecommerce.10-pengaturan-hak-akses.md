---
title: Odoo Website & eCommerce: Pengaturan & Hak Akses
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

| Pengaturan | Field |
|---|---|
| Akses toko | `ecommerce_access`: `everyone` / `logged_in` |
| Akun pelanggan | `account_on_checkout` |
| Sembunyikan tombol beli | `prevent_sale`, `prevent_sale_for` |
| Pricelist default | `website.pricelist_id` |
| Jual saat stok habis (default produk baru) | `default_allow_out_of_stock_order` |
| Tampilkan stok | `default_show_availability`, `default_available_threshold` |
| Salesperson & tim | `website.salesperson_id`, `website.salesteam_id` |

**Grup fitur** (`website_sale/security/res_groups.xml`):

```mermaid
flowchart LR
    G1["group_product_price_comparison<br/>Harga pembanding (coret)"]
    G2["group_automate_suggested_products<br/>Produk opsional/aksesori otomatis"]
    G3["group_product_feed<br/>Product feed (Google Merchant, dll.)"]
    G4["group_unpublish_out_of_stock<br/>Unpublish produk habis"]
    SAL["Hak akses data tetap dari<br/>sales_team & website<br/>(Salesman, Website Designer)"]
    G1 & G2 & G3 & G4 -. fitur .- SAL
```

---

_Sumber: dokumentasi_website_sale_odoo.md §10_
