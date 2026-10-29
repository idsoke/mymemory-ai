---
title: Nakama Ringkasan: Arsitektur singkat
tags: nakama,ringkasan,dokumentasi
project: nakama
updated: 2026-10-30
---

```
Klien (web, CLI, desktop, Telegram, WhatsApp, Discord, Slack)
        │  HTTP / SSE + header X-Org-Id
        ▼
apps/server (Hono)
  auth → org middleware → routes
  AgentService → @nakama/agent (chat loop, tools, provider AI, MCP)
        │
        ▼
State: SQLite (@nakama/db), folder soul, config.ini, file lampiran
Worker: automation, telegram, whatsapp, discord, slack, plugin
```

Struktur monorepo:

| Folder | Isi |
|---|---|
| `apps/server` | API server (Hono) |
| `apps/web` | Dashboard React |
| `apps/cli` | Aplikasi terminal |
| `apps/desktop` | Aplikasi desktop |
| `apps/platform/*` | Worker channel (telegram, whatsapp, discord, slack, automation) |
| `packages/core` | Soul, tools, skills, kontrak API |
| `packages/agent` | Chat loop, prompt, kompaksi konteks |
| `packages/db` | Database |
| `packages/client` | API client |

Ukuran: ±474.000 baris TypeScript, ±2.046 file (tanpa `node_modules`).

_Sumber: 01-ringkasan.md §3_
