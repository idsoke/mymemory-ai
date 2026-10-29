---
title: Nakama Setup Lokal: Langkah yang sudah dilakukan
tags: nakama,setup,dokumentasi
project: nakama
updated: 2026-10-30
---

### 1. Cek fork & auth GitHub

Repo lokal `idsoke/nakama` sudah merupakan fork resmi dari `ahmadrosid/nakama`
(dicek via `gh repo view idsoke/nakama --json isFork,parent,owner`), dan `gh`
sudah ter-autentikasi sebagai akun `idsoke`. Tidak perlu fork ulang.

### 2. Install Bun

Bun belum terpasang di environment ini. Diinstall dengan installer resmi:

```bash
curl -fsSL https://bun.sh/install | bash
```

Hasil: Bun terpasang di `~/.bun/bin/bun` (versi 1.4.0). Installer otomatis
menambahkan `~/.bun/bin` ke `PATH` lewat `~/.bashrc`. Untuk shell baru cukup
buka terminal baru, atau jalankan:

```bash
source ~/.bashrc
```

### 3. Tambah remote `upstream`

Supaya fork bisa disinkronkan dengan repo asli:

```bash
git remote add upstream https://github.com/ahmadrosid/nakama.git
git fetch upstream
```

Remote sekarang:

```
origin      https://github.com/idsoke/nakama       (fetch/push)
upstream    https://github.com/ahmadrosid/nakama.git (fetch/push)
```

### 4. Install dependencies

```bash
bun install
```

Ini otomatis juga menjalankan `bun install --cwd docs/website` (workspace
docs terpisah) dan setup Husky (`husky` postinstall hook untuk pre-commit
lint otomatis).

Hasil:
- Root + `apps/*` + `packages/*`: 1058 packages
- `docs/website`: 294 packages

### 5. Cek sinkronisasi `main`

```bash
git rev-list --count HEAD..upstream/main   # -> 0 (tidak ketinggalan)
git rev-list --count upstream/main..HEAD   # -> 0 (tidak ada commit ekstra)
```

Branch `main` di fork identik dengan `upstream/main`.

_Sumber: SETUP-LOKAL.md §2_
