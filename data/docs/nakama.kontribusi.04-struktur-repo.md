---
title: Nakama Aturan Kontribusi: Struktur repo
tags: nakama,kontribusi,dokumentasi
project: nakama
updated: 2026-10-30
---

| Path | Fungsi |
|---|---|
| `apps/server` | Hono HTTP API, agent service, tool playground, workers control |
| `apps/web` | React dashboard |
| `apps/cli` | Terminal chat client |
| `apps/platform/telegram` | Telegram channel worker |
| `apps/platform/whatsapp` | WhatsApp channel worker |
| `apps/platform/discord` | Discord channel worker |
| `apps/platform/automation` | Automation worker |
| `packages/core` | Soul, tools, skills, contracts |
| `packages/agent` | Chat loop, prompts, compaction |
| `packages/db` | SQLite schema and adapters |
| `packages/client` | HTTP + SSE client (`X-Org-Id`, auth) |
| `docs/website` | User-facing docs site (MDX) |

Workspaces: `apps/*`, `apps/platform/*`, `packages/*`.

_Sumber: ATURAN-KONTRIBUSI.md §4_
