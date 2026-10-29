---
title: Odoo Point of Sale: Model Data (ERD)
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
erDiagram
    POS_CONFIG {
        char name "Nama Point of Sale"
        boolean cash_control
        boolean use_pricelist
        boolean use_presets
        boolean cash_rounding
        boolean module_pos_restaurant
        selection iface_tax_included "subtotal | total"
        selection session_closing_mode "daily | closing"
        float session_closing_daily_hour
    }
    POS_SESSION {
        char name
        selection state "opening_control | opened | closing_control | closed"
        datetime start_at
        datetime stop_at
        monetary opening_balance
        monetary closing_balance
        monetary closing_difference
    }
    POS_ORDER {
        char name
        char pos_reference
        char uuid
        selection state "draft | paid | done | cancel"
        datetime date_order
        monetary amount_total
        monetary amount_tax
        monetary amount_paid
        monetary amount_return
        boolean to_invoice
    }
    POS_ORDER_LINE {
        char full_product_name
        float qty
        float price_unit
        float discount
        monetary price_subtotal
        monetary price_subtotal_incl
    }
    POS_PAYMENT {
        monetary amount
        datetime payment_date
        char transaction_id
        boolean is_change
    }
    POS_PAYMENT_METHOD {
        char name
        selection type "cash | bank | pay_later"
        selection payment_method_type "none | terminal | external_qr"
        boolean active
    }
    POS_CATEGORY {
        char name
        int sequence
    }
    POS_PRESET {
        char name "Dine in / Takeaway / Delivery"
    }
    POS_PREP_ORDER {
        int id
    }
    POS_PREP_LINE {
        float quantity
    }
    PRODUCT_PRODUCT {
        char name
        boolean available_in_pos
    }
    RES_PARTNER {
        char name
    }
    ACCOUNT_MOVE {
        char name
        selection move_type
    }
    ACCOUNT_JOURNAL {
        char name
        selection type
    }
    PRODUCT_PRICELIST {
        char name
    }
    ACCOUNT_FISCAL_POSITION {
        char name
    }

    POS_CONFIG ||--o{ POS_SESSION : session_ids
    POS_CONFIG }o--o{ POS_PAYMENT_METHOD : payment_method_ids
    POS_CONFIG }o--o{ POS_CATEGORY : iface_available_categ_ids
    POS_CONFIG }o--o{ PRODUCT_PRICELIST : available_pricelist_ids
    POS_CONFIG }o--o{ POS_PRESET : available_preset_ids
    POS_CONFIG }o--|| ACCOUNT_JOURNAL : "journal_id / closing_journal_id"
    POS_CONFIG }o--|| RES_PARTNER : default_partner_id
    POS_SESSION ||--o{ POS_ORDER : order_ids
    POS_SESSION ||--o{ ACCOUNT_MOVE : "sale_move_ids / refund_move_ids"
    POS_ORDER ||--|{ POS_ORDER_LINE : lines
    POS_ORDER ||--o{ POS_PAYMENT : payment_ids
    POS_ORDER }o--o| RES_PARTNER : partner_id
    POS_ORDER }o--o| ACCOUNT_MOVE : "account_move (invoice)"
    POS_ORDER }o--o| PRODUCT_PRICELIST : pricelist_id
    POS_ORDER }o--o| ACCOUNT_FISCAL_POSITION : fiscal_position_id
    POS_ORDER }o--o| POS_PRESET : preset_id
    POS_ORDER ||--o{ POS_PREP_ORDER : prep_order_ids
    POS_PREP_ORDER ||--o{ POS_PREP_LINE : prep_line_ids
    POS_ORDER_LINE }o--|| PRODUCT_PRODUCT : product_id
    POS_ORDER_LINE |o--o{ POS_ORDER_LINE : "refunded_orderline_id / combo_parent_id"
    POS_PAYMENT }o--|| POS_PAYMENT_METHOD : payment_method_id
    POS_PAYMENT_METHOD }o--o| ACCOUNT_JOURNAL : journal_id
```

**Model pendukung lain:** `pos.bill` (pecahan uang untuk hitung kas), `pos.note` (catatan cepat), `pos.printer` (printer dapur/struk), `pos.snooze` (produk sementara tidak tersedia), `pos.bus.mixin`, `pos.load.mixin`.

**Model wizard (TransientModel):**

| Model | File | Fungsi |
|---|---|---|
| `pos.make.payment` | `wizard/pos_payment.py` | Input pembayaran order dari backend |
| `pos.make.invoice` | `wizard/pos_make_invoice.py` | Membuat invoice untuk order |
| `pos.details.wizard` | `wizard/pos_details.py` | Laporan Sales Details |
| `pos.daily.sales.reports.wizard` | `wizard/pos_daily_sales_reports.py` | Laporan penjualan harian per sesi |
| `pos.price.inclusion.wizard` | `wizard/pos_price_inclusion_wizard.py` | Pilih harga termasuk/tidak termasuk pajak saat POS pertama dibuka |
| `pos.confirmation.wizard` | `wizard/pos_confirmation_wizard.py` | Dialog konfirmasi umum |

---

_Sumber: dokumentasi_pos_odoo.md §3_
