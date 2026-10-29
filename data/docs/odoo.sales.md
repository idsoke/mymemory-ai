---
title: Odoo Sales (modul): ringkasan & daftar bagian
tags: odoo,sales,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **Sales** (`addons/sale`, versi manifest `1.2`) beserta modul penghubungnya (`sale_crm`, `sale_management`, `sale_stock`) dalam bentuk diagram.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_sales_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Model data (ERD)
3. Siklus hidup Sales Order
4. Alur end-to-end: Opportunity → Quotation → Sales Order → Invoice
5. Dari CRM ke Quotation (`sale_crm`)
6. Konfirmasi order & portal pelanggan
7. Status invoice (`invoice_status`) & kebijakan invoice
8. Membuat invoice (termasuk Down Payment)
9. Integrasi pengiriman (`sale_stock`)
10. Cron & hak akses
11. Ringkasan file penting

---

## Bagian di memori
- `odoo.sales.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.sales.02-model-data-erd`: Model Data (ERD)
- `odoo.sales.03-siklus-hidup-sales-order`: Siklus Hidup Sales Order
- `odoo.sales.04-alur-end-to-end`: Alur End-to-End
- `odoo.sales.05-dari-crm-ke-quotation-sale-crm`: Dari CRM ke Quotation (sale_crm)
- `odoo.sales.06-konfirmasi-order-portal-pelanggan`: Konfirmasi Order & Portal Pelanggan
- `odoo.sales.07-status-invoice-kebijakan-invoice`: Status Invoice & Kebijakan Invoice
- `odoo.sales.08-membuat-invoice-termasuk-down-payment`: Membuat Invoice (termasuk Down Payment)
- `odoo.sales.09-integrasi-pengiriman-sale-stock`: Integrasi Pengiriman (sale_stock)
- `odoo.sales.10-cron-hak-akses`: Cron & Hak Akses
- `odoo.sales.11-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_sales_odoo.md (versi HTML: dokumentasi_sales_odoo.html)_
