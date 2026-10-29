---
title: Odoo Gambaran Besar: Peta Modul & Dependensi
tags: odoo,overview,dokumentasi
project: odoo
updated: 2026-10-30
---

Panah menunjukkan arah dependensi (modul di ujung panah bergantung pada modul di pangkal panah). Modul penghubung seperti `sale_crm` dan `sale_stock` otomatis terpasang jika kedua modul yang dihubungkannya sudah ada.

```mermaid
flowchart TB
    subgraph CORE["Inti"]
        direction LR
        base["base / base_setup"]
        mail["mail"]
        product["product"]
        resource["resource"]
        utm["utm"]
    end

    account(["Accounting<br/>account"])
    sales_team["sales_team"]
    crm(["CRM<br/>crm"])
    sale(["Sales<br/>sale"])
    stock(["Inventory<br/>stock"])
    purchase(["Purchase<br/>purchase"])
    pos(["Point of Sale<br/>point_of_sale"])
    posr(["POS Restaurant<br/>pos_restaurant"])
    hr(["Employees<br/>hr"])
    hrwe["hr_work_entry"]
    att(["Attendances<br/>hr_attendance"])
    hol(["Time Off<br/>hr_holidays"])
    mrp(["Manufacturing<br/>mrp"])
    project(["Project<br/>project"])
    hrts(["Timesheet<br/>hr_timesheet"])
    web["website"]
    wsale(["eCommerce<br/>website_sale"])

    CORE --> account
    CORE --> sales_team
    CORE --> stock
    CORE --> hr
    sales_team --> crm
    sales_team --> sale
    account -->|"via account_payment"| sale
    account --> purchase
    account --> pos
    pos --> posr
    hr --> hrwe
    hrwe --> att
    hrwe --> hol
    stock --> mrp
    CORE --> project
    project --> hrts
    hr --> hrts
    CORE --> web
    web --> wsale
    sale --> wsale

    subgraph BRIDGE["Modul penghubung (auto-install)"]
        direction LR
        sale_crm["sale_crm"]
        sale_stock["sale_stock"]
        purchase_stock["purchase_stock"]
        pos_stock["pos_stock"]
        stock_account["stock_account"]
        pos_sale["pos_sale"]
        pos_hr["pos_hr"]
        hr_holidays_attendance["hr_holidays_attendance"]
        mrp_account["mrp_account"]
        sale_mrp["sale_mrp"]
        sale_project["sale_project"]
        sale_timesheet["sale_timesheet"]
        website_sale_stock["website_sale_stock"]
    end

    crm -.-> sale_crm
    sale -.-> sale_crm
    sale -.-> sale_stock
    stock -.-> sale_stock
    purchase -.-> purchase_stock
    stock -.-> purchase_stock
    pos -.-> pos_stock
    stock -.-> pos_stock
    stock -.-> stock_account
    account -.-> stock_account
    pos -.-> pos_sale
    sale -.-> pos_sale
    pos -.-> pos_hr
    hr -.-> pos_hr
    att -.-> hr_holidays_attendance
    hol -.-> hr_holidays_attendance
    mrp -.-> mrp_account
    stock_account -.-> mrp_account
    mrp -.-> sale_mrp
    sale_stock -.-> sale_mrp
    project -.-> sale_project
    sale -.-> sale_project
    sale_project -.-> sale_timesheet
    hrts -.-> sale_timesheet
    wsale -.-> website_sale_stock
    sale_stock -.-> website_sale_stock
```

Catatan versi 20.0: `sale`, `purchase`, dan `point_of_sale` **tidak bergantung langsung pada `stock`**. Integrasi stok selalu lewat modul penghubung (`sale_stock`, `purchase_stock`, `pos_stock`).

---

_Sumber: dokumentasi_overview_odoo.md §1_
