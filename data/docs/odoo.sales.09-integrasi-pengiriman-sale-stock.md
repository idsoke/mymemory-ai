---
title: Odoo Sales: Integrasi Pengiriman (sale_stock)
tags: odoo,sales,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
sequenceDiagram
    autonumber
    participant SO as sale.order
    participant SOL as sale.order.line
    participant REF as stock.reference
    participant R as stock.rule
    participant PK as stock.picking

    SO->>SOL: action_confirm() → _action_launch_stock_rule()
    SOL->>REF: Buat stock.reference (jika belum ada)
    SOL->>SOL: _prepare_procurement_values()<br/>(warehouse, route, tanggal, partner pengiriman)
    SOL->>R: stock.rule.run(procurements)
    R->>R: _get_rule() berdasarkan route<br/>(MTS / MTO / Buy / Manufacture)
    R->>PK: _run_pull() → stock.move → picking<br/>(1, 2, atau 3 langkah sesuai warehouse)
    PK-->>SOL: Delivery divalidasi → qty_delivered
    SOL-->>SO: invoice_status diperbarui (policy delivery)
```

Jika qty di SO yang sudah dikonfirmasi diubah, `_action_launch_stock_rule(previous_product_uom_qty=...)` menjalankan procurement hanya untuk selisihnya.

---

_Sumber: dokumentasi_sales_odoo.md §9_
