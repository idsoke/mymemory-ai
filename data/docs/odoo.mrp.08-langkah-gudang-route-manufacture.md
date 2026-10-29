---
title: Odoo Manufacturing: Langkah Gudang & Route Manufacture
tags: odoo,mrp,dokumentasi
project: odoo
updated: 2026-10-30
---

Field `manufacture_steps` di `stock.warehouse`:

```mermaid
flowchart LR
    subgraph S1["mrp_one_step (1 langkah)"]
        direction LR
        A1["Stock"] -->|"komponen"| P1["Produksi"] -->|"produk jadi"| A2["Stock"]
    end
    subgraph S2["pbm (2 langkah)"]
        direction LR
        B1["Stock"] -->|"Pick Components"| B2["Pre-Production<br/>(pbm_loc_id)"] --> P2["Produksi"] --> B3["Stock"]
    end
    subgraph S3["pbm_sam (3 langkah)"]
        direction LR
        C1["Stock"] -->|"Pick Components"| C2["Pre-Production"] --> P3["Produksi"] --> C3["Post-Production<br/>(sam_loc_id)"] -->|"Store Finished Product"| C4["Stock"]
    end
```

```mermaid
flowchart TD
    OP["Reorder rule (orderpoint)<br/>atau SO dengan route MTO"] --> R{"Route produk"}
    R -- "Manufacture" --> MR["stock.rule action = manufacture<br/>_run_manufacture()"]
    MR --> MO["mrp.production (draft/confirmed)<br/>origin = dokumen sumber"]
    R -- "Buy" --> PO["RFQ (purchase_stock)"]
    MO -->|"komponen kurang & punya route"| SUB["procurement komponen<br/>→ MO anak / RFQ"]
    MO --> REF["stock.reference<br/>(menghubungkan dokumen terkait)"]
```

Lead time: `produce_delay` (lama produksi) dan `days_to_prepare_mo` (waktu persiapan) di BoM dipakai untuk menghitung tanggal mulai MO.

---

_Sumber: dokumentasi_mrp_odoo.md §8_
