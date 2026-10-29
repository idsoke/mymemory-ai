---
title: Odoo Website & eCommerce: Alur Checkout (Checkout Steps)
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

Urutan langkah disimpan di model `website.checkout.step` (`website_sale/data/website_checkout_step_data.xml`), sehingga bisa disesuaikan per website.

```mermaid
flowchart LR
    S1["Order<br/>/shop/cart<br/>(seq 0)"] --> S2["Address<br/>/shop/address<br/>(seq 125)"]
    S2 --> S3["Address: ringkasan & delivery<br/>/shop/checkout<br/>(seq 250)"]
    S3 --> S4["Extra Info<br/>/shop/extra_info<br/>(seq 500, opsional)"]
    S4 --> S5["Payment<br/>/shop/payment<br/>(seq 999)"]
    S5 --> S6["Payment Confirmation<br/>/shop/payment/transaction<br/>(seq 1500)"]
    S6 --> S7["/shop/payment/validate"]
    S7 --> S8["Thank you<br/>/shop/confirmation"]
```

- **Akun pelanggan** (`account_on_checkout`): `optional` (boleh guest), `disabled` (selalu guest), `mandatory` (wajib login).
- **Extra Info** hanya tampil jika view `website_sale.extra_info` aktif.
- **Pengiriman**: daftar metode dari `/shop/delivery_methods`, harga dari `/shop/get_delivery_rate`, dipilih via `/shop/set_delivery_method` (modul `delivery`).
- **Express checkout** (`/shop/express_checkout`): alamat & pembayaran langsung dari dompet digital (Google Pay/Apple Pay, tergantung provider).

---

_Sumber: dokumentasi_website_sale_odoo.md §5_
