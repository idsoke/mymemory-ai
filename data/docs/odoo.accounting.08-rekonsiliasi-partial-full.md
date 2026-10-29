---
title: Odoo Accounting / Invoicing: Rekonsiliasi (Partial & Full)
tags: odoo,accounting,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
flowchart TB
    A["Dua baris jurnal di akun yang bisa direkonsiliasi<br/>(receivable / payable / outstanding)<br/>debit invoice ↔ kredit payment"] --> B["account.move.line.reconcile()"]
    B --> C["_create_reconciliation_partials()<br/>account.partial.reconcile<br/>(debit_move_id, credit_move_id, amount)"]
    C --> D["amount_residual tiap baris berkurang"]
    D --> E{"Mata uang berbeda / kurs berubah?"}
    E -- Ya --> F["_create_exchange_difference_move()<br/>jurnal selisih kurs"]
    E -- Tidak --> G
    F --> G{"Semua residual = 0?"}
    G -- Ya --> H["account.full.reconcile<br/>(nomor matching)<br/>reconciled = True"]
    G -- Tidak --> I["Tetap partial"]
    H --> J["payment_state invoice dihitung ulang"]
    I --> J

    K["remove_move_reconcile()<br/>(Unreconcile)"] -.-> C
```

**Reconciliation model** (`account.reconcile.model`) membantu rekonsiliasi bank, dengan dua jenis (`rule_type`): `reco_model` (model write-off/counterpart yang diterapkan manual) dan `matching_rule` (cocokkan otomatis dengan invoice/payment).

---

_Sumber: dokumentasi_accounting_odoo.md §8_
