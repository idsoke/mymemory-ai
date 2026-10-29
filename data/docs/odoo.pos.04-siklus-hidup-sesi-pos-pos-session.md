---
title: Odoo Point of Sale: Siklus Hidup Sesi POS (pos.session)
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
stateDiagram-v2
    direction LR
    [*] --> opening_control : pos.config.open_ui()<br/>_check_before_creating_new_session()
    opening_control --> opened : set_opening_control(cashbox_value, notes)<br/>hitung kas awal, beri nomor sesi
    opened --> opened : Transaksi, cash in/out<br/>(try_cash_in_out)
    opened --> closing_control : Kasir klik "Close Register"<br/>hitung kas akhir
    closing_control --> closed : close_session_from_ui()<br/>_validate_session_accounting()
    closing_control --> opened : Batal tutup
    closed --> [*]

    note right of opened
        Mode Daily: cron membuat jurnal
        penjualan harian tanpa menutup sesi
    end note
```

Validasi sebelum membuat sesi baru (`_check_before_creating_new_session`): chart of accounts perusahaan, pricelist, mata uang, jurnal selisih kas (profit/loss), dan metode pembayaran.

---

_Sumber: dokumentasi_pos_odoo.md §4_
