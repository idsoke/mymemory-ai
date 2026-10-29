---
title: Odoo Website & eCommerce: Abandoned Cart & Email Otomatis
tags: odoo,ecommerce,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart LR
    C["Cart draft dengan partner<br/>(bukan public user)"] --> T{"Tidak berubah selama<br/>cart_abandoned_delay jam?"}
    T -- "Ya" --> AB["is_abandoned_cart = True"]
    AB --> CR{"send_abandoned_cart_followup<br/>& belum dikirim?"}
    CR -- "Ya" --> EM["Cron kirim email<br/>cart_recovery_mail_template_id"]
    EM --> FL["cart_recovery_email_sent = True"]
```

**Cron** (`website_sale/data/ir_cron_data.xml`):

| Nama | Fungsi |
|---|---|
| eCommerce: send email to customers about their abandoned cart | Email pemulihan cart |
| eCommerce: send order rating request emails | Minta rating setelah order (`send_order_rating_emails`) |
| eCommerce: Update suggested products | Perbarui rekomendasi produk |
| Product: send email regarding products availability | Notifikasi produk tersedia kembali |

---

_Sumber: dokumentasi_website_sale_odoo.md §9_
