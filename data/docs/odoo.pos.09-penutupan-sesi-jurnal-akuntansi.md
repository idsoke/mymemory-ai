---
title: Odoo Point of Sale: Penutupan Sesi & Jurnal Akuntansi
tags: odoo,pos,dokumentasi
project: odoo
updated: 2026-10-30
---

Di Odoo 20.0, penutupan sesi membuat **dokumen penjualan ringkasan** (move tipe `out_invoice`, atau `out_refund` untuk retur) di **Closing Journal** dengan partner **Default Customer** dari konfigurasi POS. Order yang sudah di-invoice per customer tidak ikut dimasukkan.

```mermaid
flowchart TB
    A(["close_session_from_ui(payment_method_closing)"]) --> B{"Masih ada order draft?"}
    B -- Ya --> X["Ditolak:<br/>'draft_orders'"]
    B -- Tidak --> C["close_session_snoozes()<br/>lepaskan order preset masa depan"]
    C --> D["_validate_session_accounting()"]
    D --> D1["Pisahkan order:<br/>sudah invoice vs belum"]
    D1 --> D2["_check_invoiced_orders_are_posted()"]
    D1 --> D3["Abaikan order qty = 0"]
    D3 --> D4["Order penjualan → sales_move<br/>Order retur/negatif → refunds_move"]
    D4 --> D5["_create_session_account_move(orders)"]
    D5 --> L1["Baris produk:<br/>per (akun pendapatan + tarif pajak)"]
    D5 --> L2["Baris pajak:<br/>per (akun pajak + pajak)"]
    D5 --> L3["Baris pembayaran:<br/>per metode bayar (payment_term)"]
    L1 & L2 & L3 --> D6["Post move →<br/>account.payment per metode bayar<br/>& rekonsiliasi"]
    D6 --> E["_handle_bank_payment_method_difference()<br/>_handle_cash_statement_entries()<br/>(selisih kas → akun profit/loss)"]
    E --> F["state = closed, stop_at = now<br/>order → done"]
```

**Closing Mode** (`session_closing_mode`):

- **Daily**: cron `_cron_generate_invoice_period` (tiap 10 menit) menjalankan `_validate_session_accounting()` sekali sehari pada jam `session_closing_daily_hour` (default 04:00) untuk sesi yang belum ditutup.
- **At closing**: jurnal dibuat saat sesi ditutup.

---

_Sumber: dokumentasi_pos_odoo.md §9_
