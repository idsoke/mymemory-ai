---
title: Odoo Accounting / Invoicing: Status Pembayaran (payment_state)
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    [*] --> not_paid : Invoice diposting
    not_paid --> partial : Sebagian dibayar
    partial --> in_payment : Lunas, pembayaran<br/>belum cocok dengan bank
    not_paid --> in_payment : Lunas, pembayaran<br/>belum cocok dengan bank
    in_payment --> paid : Pembayaran direkonsiliasi<br/>dengan bank statement
    partial --> paid
    not_paid --> paid
    not_paid --> reversed : Dibatalkan penuh<br/>dengan credit note
    paid --> partial : Unreconcile sebagian
    not_paid --> blocked : Diblokir (sengketa)
    blocked --> not_paid
```

`in_payment` hanya terlihat jika modul `accountant` terpasang (`_get_invoice_in_payment_state()`). Di Invoicing saja, invoice yang lunas langsung menjadi `paid`.

---

_Sumber: dokumentasi_accounting_odoo.md §5_
