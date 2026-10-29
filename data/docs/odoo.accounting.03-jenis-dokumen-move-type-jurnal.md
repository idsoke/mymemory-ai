---
title: Odoo Accounting / Invoicing: Jenis Dokumen (move_type) & Jurnal
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

Semua dokumen akuntansi adalah `account.move`. Jenisnya ditentukan oleh `move_type`, dan setiap dokumen dicatat di sebuah jurnal.

```mermaid
flowchart LR
    subgraph SALE["Jurnal Sales (type = sale)"]
        OI["out_invoice<br/>Customer Invoice"]
        OR["out_refund<br/>Customer Credit Note"]
        ORC["out_receipt<br/>Sales Receipt"]
    end
    subgraph PUR["Jurnal Purchase (type = purchase)"]
        II["in_invoice<br/>Vendor Bill"]
        IR["in_refund<br/>Vendor Credit Note"]
        IRC["in_receipt<br/>Purchase Receipt"]
    end
    subgraph BANK["Jurnal Bank / Cash / Credit Card"]
        PAY["Jurnal pembayaran<br/>(account.payment)"]
        BSL["Bank statement line"]
    end
    subgraph MISC["Jurnal Miscellaneous (type = general)"]
        EN["entry<br/>Journal Entry manual,<br/>penyesuaian, valuasi stok, dll."]
    end

    OI -- "Piutang (asset_receivable)" --> PAY
    II -- "Utang (liability_payable)" --> PAY
    PAY --> BSL
```

**Tipe akun (`account_type`)** dikelompokkan menjadi: Aset (`asset_receivable`, `asset_cash`, `asset_current`, `asset_non_current`, `asset_prepayments`, `asset_fixed`), Liabilitas (`liability_payable`, `liability_credit_card`, `liability_current`, `liability_non_current`), Ekuitas (`equity`, `equity_unaffected`), Pendapatan (`income`, `income_other`), Beban (`expense`, `expense_other`, `expense_depreciation`, `expense_direct_cost`), dan `off_balance`.

---

_Sumber: dokumentasi_accounting_odoo.md §3_
