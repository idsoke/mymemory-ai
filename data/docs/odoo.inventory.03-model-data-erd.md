---
title: Odoo Inventory: Model Data (ERD)
tags: odoo,inventory,dokumentasi
project: odoo
updated: 2026-10-30
---

```mermaid
erDiagram
    STOCK_WAREHOUSE {
        char name
        char code "WH"
        selection reception_steps "one_step | two_steps | three_steps"
        selection delivery_steps "ship_only | pick_ship | pick_pack_ship"
    }
    STOCK_LOCATION {
        char complete_name
        selection usage "supplier | view | internal | customer | inventory | production | transit"
    }
    STOCK_PICKING_TYPE {
        char name
        selection code "incoming | outgoing | internal"
        char sequence_code
    }
    STOCK_PICKING {
        char name "WH/IN/00001"
        selection state "draft | waiting | confirmed | assigned | done | cancel"
        selection move_type "direct | one"
        datetime scheduled_date
        datetime date_done
        char origin
    }
    STOCK_MOVE {
        char reference
        selection state "draft | waiting | confirmed | partially_available | assigned | done | cancel"
        float product_uom_qty "Demand"
        float quantity "Qty dikerjakan"
        selection procure_method "make_to_stock | make_to_order"
        boolean is_scrap
    }
    STOCK_MOVE_LINE {
        float quantity
        boolean picked
    }
    STOCK_QUANT {
        float quantity
        float reserved_quantity
        float inventory_quantity "Hasil hitung fisik"
    }
    STOCK_LOT {
        char name "Lot / Serial"
        datetime expiration_date "product_expiry"
    }
    STOCK_PACKAGE {
        char name
    }
    STOCK_ROUTE {
        char name
    }
    STOCK_RULE {
        char name
        selection action "pull | push | pull_push | buy | manufacture"
        selection procure_method "make_to_stock | make_to_order | mts_else_mto"
    }
    STOCK_WAREHOUSE_ORDERPOINT {
        float product_min_qty
        float product_max_qty
        selection trigger "auto | manual"
    }
    STOCK_REFERENCE {
        char name "Mis. S00012"
    }
    PRODUCT_PRODUCT {
        char name
        selection tracking "none | lot | serial"
        boolean is_storable
    }
    RES_PARTNER {
        char name
    }

    STOCK_WAREHOUSE ||--o{ STOCK_LOCATION : "lot_stock_id, view_location_id, ..."
    STOCK_WAREHOUSE ||--o{ STOCK_PICKING_TYPE : "in_type_id, out_type_id, ..."
    STOCK_WAREHOUSE }o--o{ STOCK_ROUTE : route_ids
    STOCK_LOCATION ||--o{ STOCK_LOCATION : location_id
    STOCK_PICKING }o--|| STOCK_PICKING_TYPE : picking_type_id
    STOCK_PICKING }o--|| STOCK_LOCATION : "location_id / location_dest_id"
    STOCK_PICKING }o--o| RES_PARTNER : partner_id
    STOCK_PICKING ||--o{ STOCK_MOVE : move_ids
    STOCK_PICKING |o--o{ STOCK_PICKING : backorder_id
    STOCK_MOVE ||--o{ STOCK_MOVE_LINE : move_line_ids
    STOCK_MOVE }o--|| PRODUCT_PRODUCT : product_id
    STOCK_MOVE }o--o| STOCK_RULE : rule_id
    STOCK_MOVE }o--o{ STOCK_MOVE : "move_orig_ids / move_dest_ids"
    STOCK_MOVE }o--o{ STOCK_REFERENCE : reference_ids
    STOCK_MOVE_LINE }o--o| STOCK_LOT : lot_id
    STOCK_MOVE_LINE }o--o| STOCK_PACKAGE : "package_id / result_package_id"
    STOCK_QUANT }o--|| PRODUCT_PRODUCT : product_id
    STOCK_QUANT }o--|| STOCK_LOCATION : location_id
    STOCK_QUANT }o--o| STOCK_LOT : lot_id
    STOCK_QUANT }o--o| STOCK_PACKAGE : package_id
    STOCK_ROUTE ||--o{ STOCK_RULE : rule_ids
    STOCK_RULE }o--|| STOCK_LOCATION : "location_src_id / location_dest_id"
    STOCK_RULE }o--o| STOCK_PICKING_TYPE : picking_type_id
    STOCK_WAREHOUSE_ORDERPOINT }o--|| PRODUCT_PRODUCT : product_id
    STOCK_WAREHOUSE_ORDERPOINT }o--|| STOCK_LOCATION : location_id
```

**Model pendukung:** `stock.putaway.rule` (aturan penempatan barang masuk), `product.removal` (strategi pengambilan: FIFO, LIFO, Closest Location, Least Packages, dan FEFO dari `product_expiry`), `stock.storage.category`, `stock.package.type`, `stock.picking.batch` (batch/wave).

---

_Sumber: dokumentasi_inventory_odoo.md §3_
