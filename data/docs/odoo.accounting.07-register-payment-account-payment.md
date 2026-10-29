---
title: Odoo Accounting / Invoicing: Register Payment & account.payment
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    [*] --> draft : Payment dibuat manual
    draft --> paid : action_post()
    [*] --> paid : Dari wizard Register Payment
    paid --> reconciled : Cocok dengan bank statement<br/>(action_validate)
    paid --> rejected : action_reject()<br/>(mis. cek ditolak)
    draft --> canceled : action_cancel()
    paid --> canceled : action_cancel()
    canceled --> draft : action_draft()
```

Pilihan di wizard **Register Payment**: bayar penuh atau sebagian, *Keep open* atau *Mark as fully paid* (selisih dicatat sebagai write-off), *Group payments* untuk banyak invoice dari partner yang sama, serta pembayaran dengan mata uang berbeda (selisih kurs dicatat lewat exchange difference entry).

---

_Sumber: dokumentasi_accounting_odoo.md §7_
