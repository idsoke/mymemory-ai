---
title: Odoo Sales: Status Invoice & Kebijakan Invoice
tags: odoo,sales,dokumentasi
project: odoo
updated: 2026-10-30
---

Setiap baris punya `invoice_policy` dari produk:

- **Ordered quantities (`order`)**: yang ditagih = qty dipesan − qty sudah ditagih.
- **Delivered quantities (`delivery`)**: yang ditagih = qty terkirim − qty sudah ditagih.

`qty_delivered` diisi sesuai `qty_delivered_method`: `manual` (diisi tangan), `analytic` (dari expense), ditambah `stock_move` (dari pengiriman, `sale_stock`) dan `timesheet` (`sale_timesheet`).

```mermaid
flowchart TB
    A{"state SO = sale?"} -- Tidak --> NO["invoice_status = no<br/>(Nothing to Invoice)"]
    A -- Ya --> B{"invoicing_closed?"}
    B -- Ya --> INV["invoiced"]
    B -- Tidak --> C["Baca invoice_status tiap baris<br/>(kecuali down payment & section/note)"]
    C --> D{"Ada baris 'to invoice'?"}
    D -- Ya --> E{"Hanya baris khusus<br/>(diskon/ongkir/promo)?"}
    E -- Ya --> NO
    E -- Tidak --> TO["to invoice"]
    D -- Tidak --> F{"Semua baris 'invoiced'?"}
    F -- Ya --> INV
    F -- Tidak --> G{"Semua 'invoiced'<br/>atau 'upselling'?"}
    G -- Ya --> UP["upselling<br/>(terkirim > dipesan)"]
    G -- Tidak --> NO
```

---

_Sumber: dokumentasi_sales_odoo.md §7_
