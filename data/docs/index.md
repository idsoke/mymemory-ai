---
title: Index dokumentasi mymemory
tags: index,meta
project: meta
updated: 2026-10-30
---

Daftar semua dokumentasi: yang sudah ada dan yang direncanakan.
Update catatan ini setiap kali menambah atau menyelesaikan dokumentasi.
Status: [x] sudah dibuat · [ ] rencana

## Sudah dibuat

### mymemory (sistem memori)
- [x] mymemory.overview: apa itu mymemory-ai, lokasi, daftar tool
- [x] mymemory.design: keputusan desain (teks, FTS, graph, alasan belum pakai vektor)
- [x] mymemory.ops: registrasi MCP, sync/cron, catatan WSL, remote HTTPS

### odoo
- [x] odoo.workspace: lokasi source Odoo, folder skills/, konvensi id

### Dokumentasi modul Odoo 20.0 (file di Windows, belum diimpor ke memori)
Lokasi: D:\dokumentasi\odoo (WSL: /mnt/d/dokumentasi/odoo), masing-masing ada versi .md dan .html
- [x] dokumentasi_sales_odoo: arsitektur, ERD, siklus Sales Order, alur end-to-end, CRM→Quotation
- [x] dokumentasi_crm_odoo: arsitektur, ERD, siklus Lead→Opportunity→Won/Lost, sumber lead
- [x] dokumentasi_inventory_odoo: lokasi/quant/move, ERD, warehouse, siklus transfer
- [x] dokumentasi_accounting_odoo: ERD, move_type & jurnal, siklus invoice, payment_state
- [x] dokumentasi_pos_odoo: backend↔frontend kasir, ERD, siklus pos.session & pos.order

## Rencana

### odoo: dasar & lingkungan
- [ ] odoo.dev.setup: cara menjalankan odoo-bin lokal (config, database, addons_path)
- [ ] odoo.arch.orm: ORM (models, fields, _inherit, compute, onchange, constraints)
- [ ] odoo.arch.module: struktur modul (__manifest__, security, views, data)
- [ ] odoo.skills: ringkasan folder skills/ (guidelines, review, security, git, web)

### odoo: model inti
- [ ] odoo.res.partner: kontak/pelanggan/vendor
- [ ] odoo.product: product.template vs product.product
- [ ] odoo.sale.order: sales order dan state-nya (sebagian ada di dokumentasi_sales_odoo)
- [ ] odoo.stock.picking: transfer gudang, stock.move (sebagian ada di dokumentasi_inventory_odoo)
- [ ] odoo.account.move: invoice/bill/jurnal (sebagian ada di dokumentasi_accounting_odoo)

### odoo: alur bisnis
- [ ] odoo.flow.sale-to-invoice: quotation → SO → delivery → invoice → payment (sebagian ada di dokumentasi_sales_odoo)
- [ ] odoo.flow.purchase-to-bill: RFQ → PO → receipt → vendor bill

### mymemory: pengembangan
- [ ] mymemory.feature.autosave: hook Claude Code untuk simpan ringkasan otomatis
- [ ] mymemory.feature.graph-view: export graph.html untuk visualisasi
- [ ] mymemory.feature.vector: pencarian semantik (sqlite-vec + embedding lokal)

## Kopian Windows
Semua catatan memori dicerminkan otomatis oleh sync.sh ke D:\dokumentasi\odoo\mymemory (satu arah; jangan edit di sana).
