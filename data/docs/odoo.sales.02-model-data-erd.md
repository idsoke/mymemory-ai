---
title: Odoo Sales: Model Data (ERD)
tags: odoo,sales,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
erDiagram
    SALE_ORDER {
        char name "S00001"
        selection state "draft | sent | sale | cancel"
        boolean locked
        selection invoice_status "upselling | invoiced | to invoice | no"
        boolean invoicing_closed
        datetime date_order
        date validity_date
        boolean require_signature
        float prepayment_percent
        monetary prepayment_amount
        monetary amount_untaxed
        monetary amount_tax
        monetary amount_total
        monetary amount_to_invoice
    }
    SALE_ORDER_LINE {
        char name
        float product_uom_qty "Qty dipesan"
        float qty_delivered
        float qty_invoiced
        float qty_to_invoice
        selection qty_delivered_method "manual | analytic | stock_move | timesheet"
        selection invoice_policy "order | delivery"
        selection invoice_status
        float price_unit
        float discount
        boolean is_downpayment
        selection display_type "section | note"
    }
    PRODUCT_PRODUCT {
        char name
        selection type "consu | service | combo"
        selection invoice_policy
    }
    RES_PARTNER {
        char name
    }
    PRODUCT_PRICELIST {
        char name
    }
    ACCOUNT_PAYMENT_TERM {
        char name
    }
    ACCOUNT_FISCAL_POSITION {
        char name
    }
    ACCOUNT_MOVE {
        char name
        selection move_type "out_invoice | out_refund"
    }
    ACCOUNT_MOVE_LINE {
        float quantity
    }
    PAYMENT_TRANSACTION {
        char reference
        selection state
    }
    CRM_TEAM {
        char name
    }
    RES_USERS {
        char name
    }
    CRM_LEAD {
        char name
    }
    SALE_ORDER_TEMPLATE {
        char name
    }
    ACCOUNT_TAX {
        char name
    }

    SALE_ORDER ||--|{ SALE_ORDER_LINE : order_line
    SALE_ORDER }o--|| RES_PARTNER : "partner_id / partner_invoice_id / partner_shipping_id"
    SALE_ORDER }o--o| PRODUCT_PRICELIST : pricelist_id
    SALE_ORDER }o--o| ACCOUNT_PAYMENT_TERM : payment_term_id
    SALE_ORDER }o--o| ACCOUNT_FISCAL_POSITION : fiscal_position_id
    SALE_ORDER }o--o| CRM_TEAM : team_id
    SALE_ORDER }o--o| RES_USERS : "user_id (Salesperson)"
    SALE_ORDER }o--o{ ACCOUNT_MOVE : invoice_ids
    SALE_ORDER }o--o{ PAYMENT_TRANSACTION : transaction_ids
    SALE_ORDER }o--o| CRM_LEAD : "opportunity_id (sale_crm)"
    SALE_ORDER }o--o| SALE_ORDER_TEMPLATE : "sale_order_template_id (sale_management)"
    SALE_ORDER_LINE }o--|| PRODUCT_PRODUCT : product_id
    SALE_ORDER_LINE }o--o{ ACCOUNT_TAX : tax_ids
    SALE_ORDER_LINE }o--o{ ACCOUNT_MOVE_LINE : invoice_lines
    ACCOUNT_MOVE ||--|{ ACCOUNT_MOVE_LINE : line_ids
```

**Model wizard (TransientModel):**

| Model | File | Fungsi |
|---|---|---|
| `sale.advance.payment.inv` | `sale/wizard/sale_make_invoice_advance.py` | Create Invoice: reguler, down payment persentase, atau nominal tetap |
| `sale.order.discount` | `sale/wizard/sale_order_discount.py` | Diskon global / per baris |
| `sale.mass.cancel.orders` | `sale/wizard/mass_cancel_orders.py` | Batalkan banyak order |
| `crm.quotation.partner` | `sale_crm/wizard/crm_opportunity_to_quotation.py` | Pilih/buat customer sebelum quotation dari opportunity |

---

_Sumber: dokumentasi_sales_odoo.md §2_
