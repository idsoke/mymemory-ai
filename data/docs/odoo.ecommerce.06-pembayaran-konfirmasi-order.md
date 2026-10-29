---
title: Odoo Website & eCommerce: Pembayaran & Konfirmasi Order
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
sequenceDiagram
    autonumber
    participant V as Pelanggan
    participant PAY as /shop/payment
    participant TX as payment.transaction
    participant PROV as Payment provider
    participant SO as sale.order
    participant INV as account.move

    V->>PAY: pilih metode bayar
    PAY->>TX: buat transaksi (/shop/payment/transaction/ID order)
    TX->>PROV: redirect / inline form
    PROV-->>TX: notifikasi status (webhook / return)
    TX->>TX: _post_process()
    alt state authorized atau done
        TX->>SO: _check_amount_and_confirm_order()<br/>jika jumlah ≥ syarat konfirmasi
        SO->>SO: action_confirm() → state = sale<br/>(+ email konfirmasi)
    end
    opt done & company.sale_automatic_invoice
        TX->>INV: _invoice_sale_orders(): invoice otomatis & dibayar
    end
```

Konfirmasi hanya terjadi bila **tepat satu** quotation terkait transaksi dan `_is_confirmation_amount_reached()` terpenuhi (mendukung prepayment sebagian, lihat dokumentasi Sales).

---

_Sumber: dokumentasi_website_sale_odoo.md §6_
