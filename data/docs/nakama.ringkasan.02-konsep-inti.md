---
title: Nakama Ringkasan: Konsep inti
tags: nakama,ringkasan,dokumentasi
project: nakama
updated: 2026-10-30
---

| Konsep | Arti |
|---|---|
| **Organization (org)** | Tenant. Batas isolasi data. Profile, sesi, automation, tools, MCP, skills, dan usage terpisah per org. |
| **Profile / Agent** | Satu agent. Punya model AI, tools, skills, channel, dan **soul**. |
| **Soul** | File identitas agent: `SOUL.md`, `STYLE.md`, `INSTRUCTIONS.md`, `MEMORY.md`. Disimpan di `~/.nakama/orgs/{orgId}/profiles/{profileId}/`. |
| **Org Memory** | Fakta bersama milik org, diatur admin, masuk ke prompt semua agent. |
| **Tools** | Kemampuan agent: baca file, bash, web search, email, dll. |
| **Skills** | Instruksi siap pakai yang bisa dipakai ulang oleh agent. |
| **Channel** | Tempat chat: web, CLI, desktop, Telegram, WhatsApp, Discord, Slack. |
| **Automation** | Prompt yang jalan otomatis sesuai jadwal (cron). |
| **Role** | Peran user di org: admin, member, viewer. |

_Sumber: 01-ringkasan.md §2_
