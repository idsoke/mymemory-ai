# mymemory-ai

Local knowledge-graph memory for AI assistants, exposed as an MCP server.

- `data/docs/<id>.md` — one note per node (source of truth, versioned)
- `data/relations.jsonl` — edges between notes
- `index.db` — SQLite FTS5 search index, rebuilt at startup (not committed)

## Tools

`search`, `get_doc`, `list_docs`, `save_doc`, `append_doc`, `delete_doc`, `link`, `unlink`, `neighbors`

## Setup

```bash
uv venv .venv && uv pip install --python .venv/bin/python mcp
claude mcp add mymemory --scope user -- /home/idris/mymemory-ai/.venv/bin/python /home/idris/mymemory-ai/server.py
```

## Sync

`sync.sh` commits and pushes `data/`; cron runs it every 30 minutes:

```
*/30 * * * * /home/idris/mymemory-ai/sync.sh >> /home/idris/mymemory-ai/sync.log 2>&1
```
