---
title: Index dokumentasi mymemory
tags: index,meta
project: meta
updated: 2026-10-30
---

Daftar semua dokumentasi: yang sudah ada dan yang direncanakan.
Update catatan ini setiap kali menambah atau menyelesaikan dokumentasi.
Status: [x] sudah dibuat · [ ] rencana
Proyek: odoo, nakama (cari dengan filter project agar hasil tidak tercampur).

## Sudah dibuat

### mymemory (sistem memori)
- [x] mymemory.overview: apa itu mymemory-ai, lokasi, daftar tool
- [x] mymemory.design: keputusan desain (teks, FTS, graph, alasan belum pakai vektor)
- [x] mymemory.ops: registrasi MCP, sync/cron, catatan WSL, remote HTTPS, multi-proyek

### odoo
- [x] odoo.workspace: lokasi source Odoo, folder skills/, konvensi id

### Modul Odoo 20.0 (diimpor dari D:\dokumentasi\odoo, 2026-10-30)
Tiap modul punya catatan ringkasan + catatan per bagian (`odoo.<modul>.NN-...`). Buka catatan modul untuk daftar bagiannya.
- [x] odoo.sales: Sales (11 bagian)
- [x] odoo.crm: CRM (11 bagian)
- [x] odoo.inventory: Inventory (13 bagian)
- [x] odoo.accounting: Accounting / Invoicing (14 bagian)
- [x] odoo.pos: Point of Sale (13 bagian)
- [x] odoo.purchase: Purchase (11 bagian)
- [x] odoo.pos-restaurant: POS Restaurant (11 bagian)
- [x] odoo.hr: HR: Employees, Attendances, Time Off (14 bagian)
- [x] odoo.mrp: Manufacturing (12 bagian)
- [x] odoo.project: Project & Timesheet (11 bagian)
- [x] odoo.ecommerce: Website & eCommerce (11 bagian)
- [x] odoo.overview: gambaran besar & alur antar modul (10 bagian)

### nakama
- [x] nakama.workspace: lokasi source, remote fork/upstream, dokumentasi, konvensi id

### Dokumentasi Nakama v0.4.61 (diimpor dari D:\dokumentasi\nakama, 2026-10-30)
Tiap dokumen punya catatan ringkasan + catatan per bagian (`nakama.<dok>.NN-...`).
- [x] nakama.ringkasan: apa itu Nakama, konsep, arsitektur, cara menjalankan (5 bagian)
- [x] nakama.fitur: fitur yang sudah dibuat, termasuk usage & biaya token (12 bagian)
- [x] nakama.roadmap: fitur yang akan dikembangkan per stage now/next/later (5 bagian)
- [x] nakama.kontribusi: aturan kontribusi ke ahmadrosid/nakama (10 bagian)
- [x] nakama.setup-lokal: catatan setup lokal di WSL (5 bagian)

## Rencana

### odoo: dasar & lingkungan
- [ ] odoo.dev.setup: cara menjalankan odoo-bin lokal (config, database, addons_path)
- [ ] odoo.arch.orm: ORM (models, fields, _inherit, compute, onchange, constraints)
- [ ] odoo.arch.module: struktur modul (__manifest__, security, views, data)
- [ ] odoo.skills: ringkasan folder skills/ (guidelines, review, security, git, web)

### odoo: model inti
- [ ] odoo.res.partner: kontak/pelanggan/vendor
- [ ] odoo.product: product.template vs product.product
- [ ] odoo.sale.order: sales order dan state-nya (sebagian tercakup: odoo.sales.03, odoo.sales.04)
- [ ] odoo.stock.picking: transfer gudang, stock.move (sebagian tercakup: odoo.inventory.05, odoo.inventory.06)
- [ ] odoo.account.move: invoice/bill/jurnal (sebagian tercakup: odoo.accounting.03, odoo.accounting.04)

### odoo: alur bisnis
- [ ] odoo.flow.sale-to-invoice: quotation → SO → delivery → invoice → payment (sebagian tercakup: odoo.sales.04, odoo.accounting.06, odoo.overview.03)
- [ ] odoo.flow.purchase-to-bill: RFQ → PO → receipt → vendor bill (sebagian tercakup: odoo.purchase.04, odoo.overview.04)

### nakama: kode
- [ ] nakama.server.agent-service: AgentService, buildChatSession, generateReply
- [ ] nakama.agent.tool-loop: tool loop, parallelSafe, compaction
- [ ] nakama.db.schema: tabel utama dan org_id (packages/db/sql/schema.sql)
- [ ] nakama.flow.chat: alur request chat dari web sampai SSE (sebagian tercakup: alur-proses.html tab 1)
- [ ] nakama.usage: usage tracking, pricing, kuota (sebagian tercakup: nakama.fitur.11)

### mymemory: pengembangan
- [ ] mymemory.feature.autosave: hook Claude Code untuk simpan ringkasan otomatis
- [ ] mymemory.feature.graph-view: export graph.html untuk visualisasi
- [ ] mymemory.feature.vector: pencarian semantik (sqlite-vec + embedding lokal)

## Kopian Windows
Dicerminkan otomatis oleh sync.sh (mirror.py), satu arah; jangan edit di sana:
- D:\dokumentasi\odoo\mymemory: semua catatan kecuali project nakama
- D:\dokumentasi\nakama\mymemory: catatan project nakama + index
