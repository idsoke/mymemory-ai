---
title: Odoo Sales: Cron & Hak Akses
tags: odoo,sales,dokumentasi
project: odoo
updated: 2026-10-30
---

**Cron** (`sale/data/ir_cron.xml`, keduanya **nonaktif** secara default):

| Nama | Method | Fungsi |
|---|---|---|
| automatic invoicing: send ready invoice | `payment.transaction._cron_send_invoice()` | Kirim invoice otomatis setelah pembayaran online |
| Sales: Send pending emails | `sale.order._cron_send_pending_emails()` | Kirim email konfirmasi yang ditunda (`sale.async_emails`) |

**Hak akses** (grup dari `sales_team`):

```mermaid
flowchart BT
    U["base.group_user"]
    S1["sales_team.group_sale_salesman<br/>User: Own Documents Only"]
    S2["sales_team.group_sale_salesman_all_leads<br/>User: All Documents"]
    S3["sales_team.group_sale_manager<br/>Administrator"]
    U --> S1 --> S2 --> S3

    F1["sale.group_auto_done_setting<br/>Lock Confirmed Sales"]
    F2["sale.group_discount_per_so_line<br/>Discount on lines"]
    F3["sale.group_warning_sale<br/>Warning produk/customer"]
    F4["sale.group_proforma_sales<br/>Pro Forma Invoices"]
    F1 -. fitur .- S1
    F2 -. fitur .- S1
    F3 -. fitur .- S1
    F4 -. fitur .- S1
```

---

_Sumber: dokumentasi_sales_odoo.md §10_
