---
title: Odoo Manufacturing (modul): ringkasan & daftar bagian
tags: odoo,mrp,dokumentasi,modul
project: odoo
updated: 2026-10-30
---

Dokumentasi ini menjelaskan modul **Manufacturing** (`addons/mrp`) beserta modul penghubungnya (`mrp_account`, `sale_mrp`, `purchase_mrp`, `mrp_subcontracting`) dalam bentuk diagram.
Semua diagram ditulis dengan **Mermaid**, sehingga bisa dibaca langsung di GitHub, GitLab, VS Code (ekstensi *Markdown Preview Mermaid*), Obsidian, atau di file HTML pendamping (`dokumentasi_mrp_odoo.html`) yang bisa mengekspor tiap diagram ke PNG/JPG.

**Isi:**

1. Arsitektur & dependensi modul
2. Model data (ERD)
3. Bill of Materials: Manufacture vs Kit
4. Siklus hidup Manufacturing Order
5. Alur end-to-end: kebutuhan → MO → produksi → stok
6. Work Order & Work Center
7. Menyelesaikan MO: konsumsi, backorder, split & merge
8. Langkah gudang (1/2/3 step) & route Manufacture
9. Biaya produksi (`mrp_account`)
10. Unbuild & scrap
11. Pengaturan & hak akses
12. Ringkasan file penting

---

## Bagian di memori
- `odoo.mrp.01-arsitektur-dependensi-modul`: Arsitektur & Dependensi Modul
- `odoo.mrp.02-model-data-erd`: Model Data (ERD)
- `odoo.mrp.03-bill-of-materials-manufacture-vs-kit`: Bill of Materials: Manufacture vs Kit
- `odoo.mrp.04-siklus-hidup-manufacturing-order`: Siklus Hidup Manufacturing Order
- `odoo.mrp.05-alur-end-to-end`: Alur End-to-End
- `odoo.mrp.06-work-order-work-center`: Work Order & Work Center
- `odoo.mrp.07-menyelesaikan-mo-konsumsi-backorder-split-merge`: Menyelesaikan MO: Konsumsi, Backorder, Split & Merge
- `odoo.mrp.08-langkah-gudang-route-manufacture`: Langkah Gudang & Route Manufacture
- `odoo.mrp.09-biaya-produksi-mrp-account`: Biaya Produksi (mrp_account)
- `odoo.mrp.10-unbuild-scrap`: Unbuild & Scrap
- `odoo.mrp.11-pengaturan-hak-akses`: Pengaturan & Hak Akses
- `odoo.mrp.12-ringkasan-file-penting`: Ringkasan File Penting

_Sumber: D:\dokumentasi\odoo\dokumentasi_mrp_odoo.md (versi HTML: dokumentasi_mrp_odoo.html)_
