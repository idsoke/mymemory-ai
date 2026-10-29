---
title: Nakama Aturan Kontribusi: Setup lokal
tags: nakama,kontribusi,dokumentasi
project: nakama
updated: 2026-10-30
---

```bash
git clone https://github.com/ahmadrosid/nakama.git
cd nakama
bun install

bun run dev:server   # API
bun run dev:web      # web dashboard (start server otomatis jika perlu) -> http://localhost:3003
bun run dev:cli      # terminal client
```

Docker (single container: API + web + workers) -> http://localhost:4310

```bash
docker pull ghcr.io/ahmadrosid/nakama:latest
docker run -d -p 4310:4310 -v nakama-data:/nakama/data --name nakama ghcr.io/ahmadrosid/nakama:latest

# atau build dari source
./scripts/docker-build-run.sh
./scripts/docker-destroy.sh   # fresh start (hapus container, volume, image)
```

_Sumber: ATURAN-KONTRIBUSI.md §3_
