---
title: Nakama Aturan Kontribusi: Testing
tags: nakama,kontribusi,dokumentasi
project: nakama
updated: 2026-10-30
---

```bash
bun test
```

- Assert **behavior** (output, status code, side effect) — jangan assert
  teks prompt, string deskripsi, atau copy error yang persis.
- Jangan pakai `.only` atau `.skip` di kode yang di-commit.

### LLM cassette tests (MSW)

Test provider live merekam satu HTTP call asli, commit cassette-nya, lalu
replay offline setelahnya.

- Helper: `apps/server/src/testing/llm-msw-cassette.ts` (`withMswCassette`)
- Cassette disimpan di: `apps/server/src/testing/cassettes/`
- Nama file test live: `*.llm.test.ts`
- Default: replay jika cassette ada (`LLM_VCR_MODE` unset -> `auto` lokal,
  `replay` di CI)
- Re-record (butuh API key provider):
  ```bash
  bun test path/to/foo.llm.test.ts
  LLM_VCR_MODE=record bun test path/to/foo.llm.test.ts
  ```

_Sumber: ATURAN-KONTRIBUSI.md §7_
