---
title: Odoo Purchase: Cron, Pengaturan & Hak Akses
tags: odoo,purchase,dokumentasi
project: odoo
updated: 2026-10-30
---

**Cron:** `Purchase reminder` (`purchase/data/ir_cron_data.xml`) mengirim email pengingat ke vendor sebelum tanggal penerimaan, jika `receipt_reminder_email` aktif (grup `purchase.group_send_reminder`).

**Pengaturan perusahaan:**

| Field | Pilihan |
|---|---|
| `po_double_validation` | `one_step` (1 tingkat) / `two_step` (2 tingkat di atas nominal tertentu) |
| `po_double_validation_amount` | Batas nominal yang butuh persetujuan manager |
| `po_lock` | `edit` (PO bisa diubah) / `lock` (PO terkunci setelah konfirmasi) |

**Hak akses:**

```mermaid
flowchart BT
    U["base.group_user"]
    PU["purchase.group_purchase_user<br/>User"]
    PM["purchase.group_purchase_manager<br/>Administrator<br/>(bisa approve PO)"]
    U --> PU --> PM

    F1["purchase.group_warning_purchase<br/>Warning produk/vendor"]
    F2["purchase.group_send_reminder<br/>Receipt reminder"]
    F1 & F2 -. fitur .- PU
```

---

_Sumber: dokumentasi_purchase_odoo.md §10_
