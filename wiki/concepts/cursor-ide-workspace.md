---
title: Cursor IDE workspace — primary laptop harness (May 2026)
type: concept
tags: [concept, cursor, mcp, workspace, osint, rules, canvas, browser]
keywords: [open folder, lazy-tool, project mcp, global mcp, osint workspace, cemini-projects, visual deliverables, github mcp]
related:
  - concepts/deep-research-evaluation-prompt.md
  - concepts/cross-wiki-routing.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-code.md
  - entities/mcp-servers/stash.md
  - entities/mcp-servers/exa.md
  - entities/tools/awesome-cursorrules.md
  - entities/tools/cursor-community-plugins.md
  - entities/tools/openevolve.md
maturity: validated
created: 2026-05-21
updated: 2026-05-21
---

## Relations

- `@concepts/deep-research-evaluation-prompt.md` — v4 surface 7 references this harness
- `@concepts/claude-desktop-vs-claude-code.md` — Claude Code remains secondary harness
- `@entities/tools/lazy-tool.md` — required OSINT project MCP router
- `@entities/tools/claude-code.md` — hooks, `/plugin`, claude-mem
- `@entities/mcp-servers/stash.md` — global episodic memory
- `@entities/mcp-servers/exa.md` — external research
- `@osint-wiki/.cursor/README.md` — operational MCP README (live config)
- `@entities/tools/awesome-cursorrules.md` — CC0 rules catalog; cherry-pick into `.cursor/rules/` (K63)
- `@entities/tools/cursor-community-plugins.md` — discovery index only (no LICENSE file)
- `@entities/tools/openevolve.md` — harness optimization experiments (Docker-isolated)

## Raw Concept

Question: **How does Cemini use Cursor on the MacBook for wiki curation and research, and how does that differ from Claude Code?**

## Narrative

As of May 2026, **Cursor** is the primary IDE for OSINT wiki authoring, bulk eval spot-checks, and most laptop-side agent work. **Claude Code** remains in use for claude-mem, plugin marketplace, hooks, and some prod deploy sessions. Both are documented under **CCC wiki** (surface 7 of the multi-wiki eval prompt) — not a separate seventh domain wiki.

### Open Folder discipline

| Project root | Purpose |
|--------------|---------|
| `~/Desktop/OSINT WORKSPACE` | Wiki, conductor, kb-server, prod-mcp proxy, ingest scripts |
| `~/Desktop/projects/CeminiSuite` | App repo (separate `.cursor/mcp.json`) |
| `~/Desktop/projects/Cemini claude code CCC` | Harness meta-wiki + `prompts/` |

**lazy-tool** only loads when a project folder is open — Cursor Home without a folder shows stash/github only.

### MCP map (OSINT project)

**Project** (`.cursor/mcp.json`): `lazy-tool` (**must stay On**), `prod-mcp`, `exa`, `fetch`.

**Global** (`~/.cursor/mcp.json`): `github`, `stash` (`:8088`), `brave-search`, `playwright` (fallback).

Tunnels: LaunchAgents `com.cemini.stash-tunnel`, `com.cemini.prod-mcp-tunnel`. Verify: `curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8088/sse` and `http://127.0.0.1:18002/mcp`.

### Rules and deliverables

**OSINT WORKSPACE**

- `.cursor/rules/osint-mcp-defaults.mdc` — lazy-tool routing
- `.cursor/rules/osint-visual-deliverables.mdc` — prefer built-in `browser_*` over Playwright; canvas for heavy tables

**CCC meta-wiki** (`~/Desktop/projects/Cemini claude code CCC`)

- `.cursor/mcp.json` — project **exa** (`scripts/mcp_exa.sh`) + **fetch**; no lazy-tool
- `.cursor/rules/ccc-wiki-workflow.mdc`, `ccc-wiki-pages.mdc`, `ccc-visual-deliverables.mdc`, `ccc-rejected-cursor-tools.mdc`
- `.cursor/README.md` — MCP reload + global vs project scope

**Global**

- `~/.cursor/rules/cemini-projects.mdc` — SSH hosts (`cemini-prod`, `cemini-librarian`), sibling wiki paths

**Deployment boundary:** OSINT workspace stages `briefs/` and edits wiki git; it does **not** modify `/opt/cemini` application code.

### vs Claude Code

| Capability | Cursor | Claude Code |
|------------|--------|-------------|
| Wiki authoring | Primary | Occasional |
| claude-mem | — | Yes |
| `/plugin` marketplace | — | Yes |
| Hooks SessionStart/Stop | — | Yes |
| Canvas / built-in browser | Yes | — |
| Global github MCP | Yes (`setup_cursor_github_mcp.sh`) | Separate config |

## Snippets

```bash
# GitHub MCP setup (OSINT)
cd "<osint-wiki-workspace>"   # private clone; path varies per maintainer
./scripts/setup_cursor_github_mcp.sh
```

[CONFIRMED] Project MCP layout documented in `@osint-wiki/.cursor/README.md` (2026-05-21).
