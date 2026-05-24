# Cursor — CCC (Cemini Claude Code meta-wiki)

## Home vs this folder

| Where you are | Project MCP (`exa`, `fetch`) | Global MCP |
|---------------|------------------------------|------------|
| **Cursor Home** (no folder) | Not loaded | `stash`, `brave-search`, `playwright`, `github` from `~/.cursor/mcp.json` |
| **This folder open** | `exa`, `fetch` (below) | Same globals |

**No lazy-tool here** — that is **OSINT WORKSPACE** only. Cross-wiki queries: open OSINT folder or read `wiki/` directly.

## Project MCP (this folder)

| Server | Role |
|--------|------|
| **exa** | Claude Code release notes, repo eval, URL verification — key in `~/.cemini/exa-api-key` or `EXA_API_KEY` |
| **fetch** | Quick public docs fetch when Exa unavailable |

Enable in **Settings → Tools & MCP** after first open.

## Rules (`.cursor/rules/`)

| File | Purpose |
|------|---------|
| `ccc-wiki-workflow.mdc` | Session start (`hot.md`, `CLAUDE.md`), ingest, lint, git |
| `ccc-wiki-pages.mdc` | Wiki frontmatter + bidirectional `related:` when editing `wiki/` |
| `ccc-visual-deliverables.mdc` | Canvas for large tables; built-in browser for docs |
| `ccc-rejected-cursor-tools.mdc` | K63 piracy cluster — never suggest |

Patterns adapted from [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) (CC0) — see `curated-rules/README.md`.

## Global rules

- `~/.cursor/rules/cemini-projects.mdc` — SSH hosts, sibling wiki paths, MCP map

## openevolve (harness experiments)

Phase-0 smoke test only — **does not modify this repo**:

```bash
./scripts/openevolve-phase0-smoke.sh
```

See `@wiki/entities/tools/openevolve.md`.

## Reload MCP

**Cmd+Shift+P** → **Reload Window**, or MCP panel → **Retry**, or quit Cursor (`Cmd+Q`) and reopen.
