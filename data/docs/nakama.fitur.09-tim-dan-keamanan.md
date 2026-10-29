---
title: Nakama Fitur Tersedia: Tim dan keamanan
tags: nakama,fitur,dokumentasi
project: nakama
updated: 2026-10-30
---

| Fitur | Penjelasan | Doc |
|---|---|---|
| Multi-tenancy | Banyak org di satu server; data terisolasi per org. | `multi-tenancy` |
| Teams (org induk & team) | Org induk membuat team (satu level) dan publish knowledge, skills, agent template, tools, dan models ke semua team. Chat, file, memori, kredensial, automation, dan usage team tetap privat. Menu **System → Organization**. | `multi-tenancy` |
| Undangan & role | Undang member; role admin / member / viewer. Viewer tidak bisa menjalankan agent. | `multi-tenancy` |
| Org switcher | User pindah org aktif dari dashboard. | — |
| Pairing channel | Akun Telegram/WhatsApp/Discord/Slack dihubungkan ke user Nakama dengan pairing code, supaya orang asing tidak bisa chat dengan bot. | `telegram`, `slack` |
| Profile pack | Export/import satu agent ke org atau instalasi lain, tanpa secret dan plugin. | `profiles` |
| Review kode skill | Kode skill buatan member tidak aktif sebelum direview admin. | `changelog` |
| Secret managers | Ambil `NAKAMA_SECRETS_KEY` dari Vault, AWS, atau GCP Secret Manager. Key provider bisa dari env atau file (`*_FILE`). Key yang disimpan di Settings dienkripsi dengan master key. | `secret-managers` |
| Outbound connections | Daftar fitur yang menghubungi layanan luar dan data apa yang keluar. | `outbound-connections` |
| Threat model | Analisis STRIDE (`THREAT_MODEL.md`). | — |

_Sumber: 02-fitur-tersedia.md §9_
