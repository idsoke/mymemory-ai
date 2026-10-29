---
title: Odoo Website & eCommerce (modul): ringkasan & daftar bagian
tags: odoo,ecommerce,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **eCommerce** (`addons/website_sale`) di atas modul **Website**, beserta penghubungnya (`website_sale_stock`, `website_sale_loyalty`, `website_sale_collect`) dalam bentuk diagram.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_website_sale_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Model data (ERD)
3. Katalog: publikasi produk, kategori & harga
4. Keranjang (cart) = `sale.order` draft
5. Alur checkout (checkout steps)
6. Pembayaran & konfirmasi order
7. Alur end-to-end: kunjungan → order → pengiriman → invoice
8. Stok di toko online
9. Abandoned cart & email otomatis
10. Pengaturan & hak akses
11. Ringkasan file penting

---

## Bagian di memori
- `odoo.ecommerce.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.ecommerce.02-model-data-erd`: Model Data (ERD)
- `odoo.ecommerce.03-katalog-publikasi-produk-kategori-harga`: Katalog: Publikasi Produk, Kategori & Harga
- `odoo.ecommerce.04-keranjang-cart-sale-order-draft`: Keranjang (Cart) = sale.order Draft
- `odoo.ecommerce.05-alur-checkout-checkout-steps`: Alur Checkout (Checkout Steps)
- `odoo.ecommerce.06-pembayaran-konfirmasi-order`: Pembayaran & Konfirmasi Order
- `odoo.ecommerce.07-alur-end-to-end`: Alur End-to-End
- `odoo.ecommerce.08-stok-di-toko-online`: Stok di Toko Online
- `odoo.ecommerce.09-abandoned-cart-email-otomatis`: Abandoned Cart & Email Otomatis
- `odoo.ecommerce.10-pengaturan-hak-akses`: Pengaturan & Hak Akses
- `odoo.ecommerce.11-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_website_sale_odoo.md (versi HTML: dokumentasi_website_sale_odoo.html)_
