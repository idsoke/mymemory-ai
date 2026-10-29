---
title: Odoo Purchase: Model Data (ERD)
tags: odoo,purchase,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
erDiagram
    PURCHASE_ORDER {
        char name "P00001"
        selection state "draft | sent | to approve | purchase | cancel"
        boolean locked
        boolean acknowledged
        selection priority "0 Normal | 1 Urgent"
        datetime date_order "Order Deadline"
        datetime date_approve
        datetime date_planned "Expected Arrival"
        selection invoice_status "no | to invoice | invoiced"
        selection receipt_status "pending | partial | full"
        char partner_ref "Referensi vendor"
        char origin
        monetary amount_untaxed
        monetary amount_total
    }
    PURCHASE_ORDER_LINE {
        char name
        float product_qty
        float qty_received
        selection qty_received_method "manual | stock_moves"
        float qty_invoiced
        float qty_to_invoice
        float price_unit
        float discount
        datetime date_planned
        selection display_type "line_section | line_subsection | line_note"
    }
    PRODUCT_PRODUCT {
        char name
        selection purchase_method "purchase | receive"
    }
    PRODUCT_SUPPLIERINFO {
        float min_qty
        float price
        int delay "Lead time (hari)"
        date date_start
        date date_end
    }
    RES_PARTNER {
        char name "Vendor"
    }
    ACCOUNT_MOVE {
        char name
        selection move_type "in_invoice | in_refund"
    }
    ACCOUNT_MOVE_LINE {
        float quantity
    }
    STOCK_PICKING {
        char name "WH/IN/00001"
    }
    STOCK_MOVE {
        float product_uom_qty
    }
    STOCK_PICKING_TYPE {
        char name "Receipts"
    }
    ACCOUNT_TAX {
        char name
    }
    ACCOUNT_PAYMENT_TERM {
        char name
    }
    ACCOUNT_INCOTERMS {
        char code
    }
    RES_USERS {
        char name "Buyer"
    }

    PURCHASE_ORDER ||--|{ PURCHASE_ORDER_LINE : order_line
    PURCHASE_ORDER }o--|| RES_PARTNER : partner_id
    PURCHASE_ORDER }o--o| RES_PARTNER : "dest_address_id (dropship)"
    PURCHASE_ORDER }o--o| RES_USERS : "user_id (Buyer)"
    PURCHASE_ORDER }o--o| ACCOUNT_PAYMENT_TERM : payment_term_id
    PURCHASE_ORDER }o--o| ACCOUNT_INCOTERMS : incoterm_id
    PURCHASE_ORDER }o--o{ ACCOUNT_MOVE : invoice_ids
    PURCHASE_ORDER }o--o{ STOCK_PICKING : "picking_ids (purchase_stock)"
    PURCHASE_ORDER }o--o| STOCK_PICKING_TYPE : "picking_type_id (Deliver To)"
    PURCHASE_ORDER_LINE }o--|| PRODUCT_PRODUCT : product_id
    PURCHASE_ORDER_LINE }o--o{ ACCOUNT_TAX : tax_ids
    PURCHASE_ORDER_LINE ||--o{ ACCOUNT_MOVE_LINE : invoice_lines
    PURCHASE_ORDER_LINE ||--o{ STOCK_MOVE : "move_ids (purchase_stock)"
    PURCHASE_ORDER_LINE }o--o| PRODUCT_SUPPLIERINFO : selected_seller_id
    PRODUCT_SUPPLIERINFO }o--|| RES_PARTNER : partner_id
    PRODUCT_SUPPLIERINFO }o--|| PRODUCT_PRODUCT : "product_tmpl_id / product_id"
    STOCK_PICKING ||--o{ STOCK_MOVE : move_ids
    ACCOUNT_MOVE ||--|{ ACCOUNT_MOVE_LINE : line_ids
```

**Model pendukung & wizard:**

| Model | File | Fungsi |
|---|---|---|
| `purchase.bill.line.match` | `purchase/models/purchase_bill_line_match.py` | View pencocokan baris PO ↔ baris vendor bill |
| `bill.to.po.wizard` | `purchase/wizard/bill_to_po_wizard.py` | Buat/tautkan PO dari vendor bill |
| `account.accrued.orders.wizard` | `purchase/wizard/accrued_orders.py` | Jurnal accrual untuk barang diterima tapi belum ditagih |

---

_Sumber: dokumentasi_purchase_odoo.md §2_
