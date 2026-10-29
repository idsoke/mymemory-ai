---
title: Odoo Purchase: Vendor Bill & Bill Control
tags: odoo,purchase,dokumentasi
project: odoo
updated: 2026-10-30
---

Kebijakan penagihan diatur di produk (`purchase_method`):

- **On ordered quantities (`purchase`)**: bisa ditagih sejak PO dikonfirmasi. `qty_to_invoice = product_qty − qty_invoiced`.
- **On received quantities (`receive`)**: hanya bisa ditagih setelah barang diterima. `qty_to_invoice = qty_received − qty_invoiced`.

```mermaid
flowchart TB
    A{"Cara membuat bill"}
    A -- "Tombol Create Bill di PO" --> B["action_create_invoice()"]
    A -- "Upload / email PDF bill<br/>(OCR / e-Invoice)" --> C["Bill draft → bill.to.po.wizard<br/>atau action_bill_matching()"]
    A -- "Bill manual → pilih PO<br/>(Auto-complete)" --> D["Baris PO ditambahkan ke bill"]

    B --> E["_prepare_invoice()<br/>vendor, payment term, fiscal position,<br/>currency, partner_ref"]
    E --> F["Baris dengan qty_to_invoice ≠ 0<br/>→ _prepare_account_move_line()"]
    C --> F
    D --> F
    F --> G["account.move (in_invoice)<br/>atau in_refund jika negatif"]
    G --> H["qty_invoiced dihitung ulang"]
    H --> I{"invoice_status PO"}
    I -->|"ada qty_to_invoice ≠ 0"| I1["to invoice<br/>(Waiting Bills)"]
    I -->|"semua 0 & sudah ada bill"| I2["invoiced<br/>(Fully Billed)"]
    I -->|"lainnya / belum confirm"| I3["no<br/>(Nothing to Bill)"]
```

**Purchase Matching** (`purchase.bill.line.match`) menampilkan baris PO dan baris bill yang belum cocok per vendor, sehingga bill yang masuk bisa dicocokkan dengan PO yang benar.

---

_Sumber: dokumentasi_purchase_odoo.md §7_
