---
title: Nakama Setup Lokal: Cara menjalankan project
tags: nakama,setup,dokumentasi
project: nakama
updated: 2026-10-30
---

```bash
export PATH="$HOME/.bun/bin:$PATH"   # jika belum source ~/.bashrc

bun run dev:web      # dashboard web, http://localhost:3003 (auto-start server)
bun run dev:server   # API saja
bun run dev:cli      # terminal client
```

_Sumber: SETUP-LOKAL.md §3_
