---
title: Odoo Website & eCommerce: Ringkasan File Penting
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

| File | Isi |
|---|---|
| `website_sale/controllers/main.py` | Route `/shop`, produk, checkout, alamat, payment, confirmation |
| `website_sale/controllers/cart.py` | `/shop/cart`, add, update, quick add |
| `website_sale/controllers/delivery.py` | Metode & tarif pengiriman, express checkout |
| `website_sale/controllers/payment.py` | `/shop/payment/transaction` |
| `website_sale/models/sale_order.py` | Logika cart: `_cart_add`, `_cart_update_line_quantity`, abandoned |
| `website_sale/models/website.py` | Pengaturan toko, `_create_cart`, checkout steps |
| `website_sale/models/website_checkout_step.py` | Model langkah checkout |
| `website_sale/models/product_template.py` | Publikasi, kategori, ribbon, out-of-stock |
| `website_sale/models/payment_transaction.py` | Post-process transaksi website |
| `sale/models/payment_transaction.py` | `_check_amount_and_confirm_order()`, invoice otomatis |
| `website_sale/data/ir_cron_data.xml` | Cron abandoned cart, rating, rekomendasi, stok |
| `website_sale_stock/` | Cek stok cart & delivery |

_Sumber: dokumentasi_website_sale_odoo.md §11_
