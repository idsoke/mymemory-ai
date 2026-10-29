---
title: Odoo Accounting / Invoicing: Model Data (ERD)
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
erDiagram
    ACCOUNT_MOVE {
        char name "INV/2026/00001"
        selection move_type "entry | out_invoice | out_refund | in_invoice | in_refund | out_receipt | in_receipt"
        selection state "draft | posted | cancel"
        selection payment_state "not_paid | in_payment | paid | partial | reversed | blocked"
        date date "Tanggal akuntansi"
        date invoice_date
        date invoice_date_due
        monetary amount_untaxed
        monetary amount_tax
        monetary amount_total
        monetary amount_residual
        selection auto_post "no | at_date | monthly | quarterly | yearly"
        char inalterable_hash
    }
    ACCOUNT_MOVE_LINE {
        char name
        monetary debit
        monetary credit
        monetary balance
        monetary amount_currency
        monetary amount_residual
        boolean reconciled
        selection display_type "product | tax | payment_term | rounding | line_section | line_note ..."
        float quantity
        float price_unit
    }
    ACCOUNT_ACCOUNT {
        char code
        char name
        selection account_type "asset_receivable | liability_payable | income | expense | ..."
        boolean reconcile
    }
    ACCOUNT_JOURNAL {
        char name
        char code
        selection type "sale | purchase | cash | bank | credit | general"
    }
    ACCOUNT_TAX {
        char name
        selection type_tax_use "sale | purchase | none | adjustment"
        selection amount_type "percent | fixed | division | group"
        float amount
    }
    ACCOUNT_PAYMENT {
        char name
        selection payment_type "inbound | outbound"
        selection partner_type "customer | supplier"
        selection state "draft | paid | reconciled | canceled | rejected"
        monetary amount
        date date
    }
    ACCOUNT_PARTIAL_RECONCILE {
        monetary amount
    }
    ACCOUNT_FULL_RECONCILE {
        char name
    }
    ACCOUNT_BANK_STATEMENT_LINE {
        date date
        char payment_ref
        monetary amount
        boolean is_reconciled
    }
    ACCOUNT_PAYMENT_TERM {
        char name
    }
    ACCOUNT_FISCAL_POSITION {
        char name
    }
    RES_PARTNER {
        char name
    }
    RES_CURRENCY {
        char name
    }
    ACCOUNT_ANALYTIC_ACCOUNT {
        char name
    }

    ACCOUNT_MOVE ||--|{ ACCOUNT_MOVE_LINE : line_ids
    ACCOUNT_MOVE }o--|| ACCOUNT_JOURNAL : journal_id
    ACCOUNT_MOVE }o--o| RES_PARTNER : partner_id
    ACCOUNT_MOVE }o--|| RES_CURRENCY : currency_id
    ACCOUNT_MOVE }o--o| ACCOUNT_PAYMENT_TERM : invoice_payment_term_id
    ACCOUNT_MOVE }o--o| ACCOUNT_FISCAL_POSITION : fiscal_position_id
    ACCOUNT_MOVE |o--o| ACCOUNT_MOVE : "reversed_entry_id (credit note)"
    ACCOUNT_MOVE_LINE }o--|| ACCOUNT_ACCOUNT : account_id
    ACCOUNT_MOVE_LINE }o--o{ ACCOUNT_TAX : tax_ids
    ACCOUNT_MOVE_LINE }o--o| ACCOUNT_TAX : "tax_line_id (baris pajak)"
    ACCOUNT_MOVE_LINE }o--o| ACCOUNT_ANALYTIC_ACCOUNT : analytic_distribution
    ACCOUNT_MOVE_LINE ||--o{ ACCOUNT_PARTIAL_RECONCILE : "matched_debit_ids / matched_credit_ids"
    ACCOUNT_MOVE_LINE }o--o| ACCOUNT_FULL_RECONCILE : full_reconcile_id
    ACCOUNT_PARTIAL_RECONCILE }o--o| ACCOUNT_FULL_RECONCILE : full_reconcile_id
    ACCOUNT_PAYMENT ||--o| ACCOUNT_MOVE : "move_id (jurnal pembayaran)"
    ACCOUNT_PAYMENT }o--|| ACCOUNT_JOURNAL : journal_id
    ACCOUNT_PAYMENT }o--o| RES_PARTNER : partner_id
    ACCOUNT_BANK_STATEMENT_LINE ||--|| ACCOUNT_MOVE : "move_id (_inherits)"
    ACCOUNT_JOURNAL }o--o| ACCOUNT_ACCOUNT : default_account_id
```

**Model wizard (TransientModel) utama:**

| Model | File | Fungsi |
|---|---|---|
| `account.payment.register` | `wizard/account_payment_register.py` | Register Payment dari invoice/bill |
| `account.move.reversal` | `wizard/account_move_reversal.py` | Credit note / reverse entry |
| `account.move.send.wizard` | `wizard/account_move_send_wizard.py` | Kirim & cetak invoice (email, PDF, e-Invoice) |
| `account.secure.entries.wizard` | `wizard/account_secure_entries_wizard.py` | Hash/kunci entri (inalterability) |
| `account.automatic.entry.wizard` | `wizard/account_automatic_entry_wizard.py` | Ubah periode / akun secara otomatis |
| `validate.account.move` | `wizard/account_validate_account_move.py` | Posting massal |

---

_Sumber: dokumentasi_accounting_odoo.md §2_
