---
title: Odoo Inventory (modul): ringkasan & daftar bagian
tags: odoo,inventory,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **Inventory** (`addons/stock`) beserta modul penghubungnya (`sale_stock`, `purchase_stock`, `pos_stock`, `stock_account`) dalam bentuk diagram.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_inventory_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Konsep inti: Lokasi, Quant, Move
3. Model data (ERD)
4. Struktur Warehouse & lokasi
5. Siklus hidup Transfer (`stock.picking`) & Move (`stock.move`)
6. Validasi transfer & backorder
7. Procurement: Route & Rule (pull / push)
8. Replenishment (Reordering Rules)
9. Inventory Adjustment & Scrap
10. Integrasi: Sales, Purchase, POS
11. Valuasi stok (`stock_account`)
12. Cron & hak akses
13. Ringkasan file penting

---

## Bagian di memori
- `odoo.inventory.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.inventory.02-konsep-inti-lokasi-quant-move`: Konsep Inti: Lokasi, Quant, Move
- `odoo.inventory.03-model-data-erd`: Model Data (ERD)
- `odoo.inventory.04-struktur-warehouse-lokasi`: Struktur Warehouse & Lokasi
- `odoo.inventory.05-siklus-hidup-transfer-move`: Siklus Hidup Transfer & Move
- `odoo.inventory.06-validasi-transfer-backorder`: Validasi Transfer & Backorder
- `odoo.inventory.07-procurement-route-rule`: Procurement: Route & Rule
- `odoo.inventory.08-replenishment-reordering-rules`: Replenishment (Reordering Rules)
- `odoo.inventory.09-inventory-adjustment-scrap`: Inventory Adjustment & Scrap
- `odoo.inventory.10-integrasi-sales-purchase-pos`: Integrasi: Sales, Purchase, POS
- `odoo.inventory.11-valuasi-stok-stock-account`: Valuasi Stok (stock_account)
- `odoo.inventory.12-cron-hak-akses`: Cron & Hak Akses
- `odoo.inventory.13-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_inventory_odoo.md (versi HTML: dokumentasi_inventory_odoo.html)_
