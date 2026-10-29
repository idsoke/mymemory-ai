---
title: Nakama Aturan Kontribusi: Code style & pengecekan sebelum push
tags: nakama,kontribusi,dokumentasi
project: nakama
updated: 2026-10-30
---

Lint & format pakai Biome via Ultracite (config: `biome.jsonc`).

```bash
bun run check   # ultracite check
bun run fix     # ultracite fix
bun run knip    # cari file/dependency/export yang tidak terpakai
```

- Husky menjalankan `bun x ultracite fix` otomatis di staged files saat
  commit (pre-commit hook) dan re-stage hasilnya.
- CI gagal kalau ada temuan dari `bun run knip`.

Prinsip kode (Ultracite):
- Type-safe & eksplisit, hindari `any`, pakai `unknown` bila tipe belum jelas.
- Modern JS/TS: arrow function, `for...of`, optional chaining, `const` by
  default.
- Async/await, bukan promise chain; selalu `await` promise di fungsi async.
- React: function component, hooks di top level, jangan definisikan
  komponen di dalam komponen lain, pakai semantic HTML/ARIA.
- Jangan tinggalkan `console.log`/`debugger`/`alert` di kode produksi.
- Keamanan: `rel="noopener"` untuk `target="_blank"`, hindari
  `dangerouslySetInnerHTML`, jangan pakai `eval()`.
- React/UI: jangan tambahkan subtitle/helper text/copy deskriptif di bawah
  heading/label/card secara default — cukup satu heading/label yang jelas,
  kecuali user eksplisit minta atau memang perlu mencegah kesalahpahaman.

_Sumber: ATURAN-KONTRIBUSI.md §6_
