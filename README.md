# odoo-mymemory-ai

A small, local **knowledge-graph memory for AI coding assistants**, exposed as an
[MCP](https://modelcontextprotocol.io) server. Notes are plain Markdown files in git,
relations between notes form a graph, and SQLite FTS5 provides full-text search.
Any MCP client (Claude Code, Claude Desktop, …) can search it before exploring a
codebase and save what it learned afterwards, so knowledge survives across sessions.

This repository is the author's working instance, used for Odoo 20.0 module
documentation (notes are in Indonesian). The code itself is project-agnostic.

## Why

- **Persistent:** assistants forget everything between sessions; this does not.
- **Cheap retrieval:** `search` returns short snippets instead of re-reading large codebases.
- **Plain text in git:** human-readable, diffable, portable, no vendor lock-in.
  The notes stay useful even without the server.
- **Local and private:** nothing leaves your machine except your own git remote.
- **Graph navigation:** `neighbors` walks typed relations
  (`odoo.sales --membuat_invoice_di--> odoo.accounting`) to find related notes.

Trade-offs worth knowing: search is keyword-based (no embeddings yet), notes can go
stale when the code changes, and relations are maintained by hand or by the importer.

## How it works

```
data/docs/<id>.md      one note per node: small "key: value" header + markdown body
data/relations.jsonl   one {"src", "rel", "dst"} edge per line, sorted
index.db               SQLite FTS5 index; rebuilt at startup, refreshed before each search
                       (disposable, not committed)
```

A note looks like this:

```markdown
---
title: Odoo Sales: Siklus Hidup Sales Order
tags: odoo,sales,dokumentasi
project: odoo
updated: 2026-10-30
---

Body in markdown (Mermaid diagrams welcome).
```

Ids are stable, dotted names such as `odoo.sales` or `odoo.sales.03-siklus-hidup-sales-order`
(letters, digits, `.`, `_`, `-`; max 128 characters).

## Tools

| Tool | Purpose |
|---|---|
| `search(query, limit, project)` | Full-text search; all terms first, then any term |
| `get_doc(id)` | Full note plus its direct relations |
| `list_docs(project, tag)` | List notes, optionally filtered |
| `save_doc(id, title, body, tags, project)` | Create or replace a note |
| `append_doc(id, text)` | Append to an existing note |
| `delete_doc(id)` | Delete a note and every relation touching it |
| `link(src, rel, dst)` / `unlink(...)` | Add / remove a directed relation |
| `neighbors(id, depth)` | Relations around a note, up to 3 hops |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/) (or plain `pip`).

```bash
git clone https://github.com/idsoke/odoo-mymemory-ai.git ~/mymemory-ai
cd ~/mymemory-ai
uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt
```

Register it with Claude Code (use absolute paths):

```bash
claude mcp add mymemory --scope user -- ~/mymemory-ai/.venv/bin/python ~/mymemory-ai/server.py
```

Restart the client so the tools load. Other MCP clients: run
`.venv/bin/python server.py` over stdio.

**Starting fresh:** to use it for your own project, delete the notes in `data/docs/`
(keep `.gitkeep`), empty `data/relations.jsonl`, and either delete `docs_import.json`
or point it at your own docs (see below).

## Importing an existing documentation folder (optional)

If you already keep documentation as Markdown files elsewhere, you can make that
folder the single source of truth and import it automatically. `import_docs.py`:

- splits each source file into one summary note (`<id>`) plus one note per
  `## N. Heading` section (`<id>.NN-<slug>`);
- rewrites only notes whose content changed (so periodic runs do not create empty commits);
- deletes notes for sections removed from the source; when a section was only renamed
  (same number), hand-made relations move to the new note;
- keeps the structural relations in sync (`index --berisi-->`, `odoo.workspace --punya_modul-->`,
  `<id> --punya_bagian--> <section>`).

Configure it in `docs_import.json`:

```json
{
  "source_dir": "/mnt/d/dokumentasi/odoo",
  "pattern": "dokumentasi_*_odoo.md",
  "docs": {
    "dokumentasi_sales_odoo.md": {"id": "odoo.sales", "label": "Sales", "tag": "sales"},
    "dokumentasi_overview_odoo.md": {"id": "odoo.overview", "label": "Overview", "tag": "overview",
                                     "module": false, "title": "Custom summary title"}
  }
}
```

A matching file that is not listed gets an automatic `odoo.<name>` id. If
`docs_import.json` or `source_dir` is missing, the import is skipped.

```bash
.venv/bin/python import_docs.py --dry-run   # show what would change
.venv/bin/python import_docs.py
```

Imported notes are overwritten by the next import, so edit the source files, not the notes.

## Sync

`sync.sh` runs the import, optionally mirrors `data/` to a readable folder
(`MYMEMORY_MIRROR`, default `/mnt/d/dokumentasi/odoo/mymemory`; set it empty to
disable; one-way, edits there are overwritten), then commits and pushes `data/`.
Run it from cron, e.g. every 30 minutes:

```
*/30 * * * * $HOME/mymemory-ai/sync.sh >> $HOME/mymemory-ai/sync.log 2>&1
```

Notes for WSL: cron runs only while WSL is running, and pushing from cron needs
non-interactive git credentials (an HTTPS credential helper such as
`gh auth git-credential`, or an SSH key without passphrase / with an agent).

## Replicating the Odoo documentation workflow

The notes under `data/docs/odoo.*` were generated from Mermaid diagram docs
(Markdown plus an HTML viewer that exports each diagram to PNG/JPG/SVG), written by an AI
assistant and checked against the Odoo 20.0 source. To do the same for another
codebase, a prompt like this works well:

> Create diagram documentation for this repository: one `dokumentasi_<module>_<project>.md`
> per module with Mermaid diagrams (flowchart, stateDiagram, erDiagram, sequenceDiagram)
> and numbered `## N. Heading` sections, an HTML companion that can export each diagram
> to PNG/JPG, and an overview document with a module map and an index table. Verify every
> field, method and class name against the code before writing it.

The HTML companion is produced by `tools/build_html.py`:

```bash
python3 tools/build_html.py dokumentasi_sales_odoo.md dokumentasi_sales_odoo.html "Sales docs"
```

Then point `docs_import.json` at the output folder.

## License

[MIT](LICENSE).
