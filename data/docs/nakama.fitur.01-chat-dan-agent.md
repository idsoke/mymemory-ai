---
title: Nakama Fitur Tersedia: Chat dan agent
tags: nakama,fitur,dokumentasi
project: nakama
updated: 2026-10-30
---

| Fitur | Penjelasan | Doc |
|---|---|---|
| Chat web | Dashboard seperti ChatGPT. Pilih agent dari rail kiri, lalu chat. | `overview` |
| Edit pesan & regenerate | Ubah pesan yang sudah dikirim, lalu buat ulang balasan. | `changelog` |
| Token & biaya per balasan | Lihat pemakaian token, konteks, dan biaya di setiap balasan. | `changelog` |
| Profiles | Satu agent = satu profile, dengan model, tools, skills, dan soul sendiri. | `profiles` |
| Soul files | `SOUL.md`, `STYLE.md`, `INSTRUCTIONS.md`, `MEMORY.md` membentuk perilaku agent. | `profiles`, `agent-prompt` |
| Memori agent | Agent menulis ke `MEMORY.md`; memori lama diarsipkan ke `memory-archive/`. | `builtin-tools` |
| Org Memory | Fakta bersama org, diatur admin, masuk ke prompt semua agent. | `org-memory` |
| Agent groups | Beberapa agent dalam satu chat, dengan satu brief, saling serah tugas. | `agent-groups` |
| Chat agents (ACP) | Chat sebuah profile dijalankan oleh Claude atau Codex lewat Agent Client Protocol. | `chat-agents`, `acp-agents` |
| Sub agent | Agent mendelegasikan tugas ke agent lain dari profile yang sama. | `builtin-tools` |
| Pindah profile antar org | Profile bisa dipindah ke organisasi lain. | `changelog` |

_Sumber: 02-fitur-tersedia.md §1_
