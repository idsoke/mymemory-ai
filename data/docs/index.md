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

## Rencana

### odoo: dasar & lingkungan
- [ ] odoo.dev.setup: cara menjalankan odoo-bin lokal (config, database, addons_path)
- [ ] odoo.arch.orm: ORM (models, fields, _inherit, compute, onchange, constraints)
- [ ] odoo.arch.module: struktur modul (__manifest__, security, views, data)
- [ ] odoo.skills: ringkasan folder skills/ (guidelines, review, security, git, web)

### odoo: model inti
- [ ] odoo.res.partner: kontak/pelanggan/vendor
- [ ] odoo.product: product.template vs product.product
- [ ] odoo.sale.order: sales order dan state-nya
- [ ] odoo.stock.picking: transfer gudang, stock.move
- [ ] odoo.account.move: invoice/bill/jurnal

### odoo: alur bisnis
- [ ] odoo.flow.sale-to-invoice: quotation → SO → delivery → invoice → payment
- [ ] odoo.flow.purchase-to-bill: RFQ → PO → receipt → vendor bill

### mymemory: pengembangan
- [ ] mymemory.feature.autosave: hook Claude Code untuk simpan ringkasan otomatis
- [ ] mymemory.feature.graph-view: export graph.html untuk visualisasi
- [ ] mymemory.feature.vector: pencarian semantik (sqlite-vec + embedding lokal)
