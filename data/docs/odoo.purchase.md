---
title: Odoo Purchase (modul): ringkasan & daftar bagian
tags: odoo,purchase,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **Purchase** (`addons/purchase`) beserta modul penghubungnya (`purchase_stock`, `purchase_requisition`, `purchase_alternative`) dalam bentuk diagram.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_purchase_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Model data (ERD)
3. Siklus hidup Purchase Order
4. Alur end-to-end: RFQ → PO → Receipt → Bill → Payment
5. Konfirmasi & persetujuan dua tingkat
6. Penerimaan barang (`purchase_stock`)
7. Vendor Bill & Bill Control
8. Pembelian otomatis dari Inventory (route Buy)
9. Harga vendor (`product.supplierinfo`)
10. Cron, pengaturan & hak akses
11. Ringkasan file penting

---

## Bagian di memori
- `odoo.purchase.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.purchase.02-model-data-erd`: Model Data (ERD)
- `odoo.purchase.03-siklus-hidup-purchase-order`: Siklus Hidup Purchase Order
- `odoo.purchase.04-alur-end-to-end`: Alur End-to-End
- `odoo.purchase.05-konfirmasi-persetujuan-dua-tingkat`: Konfirmasi & Persetujuan Dua Tingkat
- `odoo.purchase.06-penerimaan-barang-purchase-stock`: Penerimaan Barang (purchase_stock)
- `odoo.purchase.07-vendor-bill-bill-control`: Vendor Bill & Bill Control
- `odoo.purchase.08-pembelian-otomatis-dari-inventory-route-buy`: Pembelian Otomatis dari Inventory (Route Buy)
- `odoo.purchase.09-harga-vendor-product-supplierinfo`: Harga Vendor (product.supplierinfo)
- `odoo.purchase.10-cron-pengaturan-hak-akses`: Cron, Pengaturan & Hak Akses
- `odoo.purchase.11-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_purchase_odoo.md (versi HTML: dokumentasi_purchase_odoo.html)_
