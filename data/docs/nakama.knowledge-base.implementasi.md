---
title: Nakama Knowledge Base: implementasi saat ini (dicek 2026-11-07)
tags: nakama,knowledge-base,rag,search
project: nakama
updated: 2026-11-07
---

- KB per profile (`{soul}/data/knowledge-base`) + KB org bersama (shared/published), API di `apps/server/src/http/routes/profiles.ts` (`/v1/profiles/{id}/knowledge-base`, `/v1/orgs/{orgId}/knowledge-base`).
- Store/ekstraksi: `packages/core/src/knowledge-base/{store,extract,catalog,paths}.ts`. Format: txt, md, csv, pdf, docx. Dedup by content hash.
- Tool agent `knowledge_base_search` di `packages/core/src/tools/knowledge-base-search.ts`: ripgrep + SQLite FTS5 BM25 (`tokenize='porter unicode61'`, stemmer Inggris). TIDAK ada embedding/vektor/reranker.
- Semantic memory opsional via plugin `packages/plugins/supermemory` (layanan Supermemory eksternal; actions exposeAsTool).
- Ekstensi: plugin (`nakama.plugin.json`: actions→tool, ui, workers, skills, migrations) atau MCP server per profile.
