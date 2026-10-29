---
title: Nakama Ringkasan: Cara menjalankan
tags: nakama,ringkasan,dokumentasi
project: nakama
updated: 2026-10-30
---

**Lokal (Bun):**
```bash
bun install
bun run dev:web      # buka http://localhost:3003
```

**Docker:**
```bash
docker pull ghcr.io/ahmadrosid/nakama:latest
printf 'NAKAMA_SECRETS_KEY=%s\n' "$(openssl rand -base64 32)" > nakama-secrets.env
docker run -d -p 4310:4310 -v nakama-data:/nakama/data \
  --env-file nakama-secrets.env --name nakama ghcr.io/ahmadrosid/nakama:latest
# buka http://localhost:4310
```

Saat pertama kali dibuka, ikuti **setup wizard**: buat akun admin, organisasi, provider AI, dan profile.

_Sumber: 01-ringkasan.md §4_
