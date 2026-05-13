---
title: exa-mcp — Exa search MCP server
type: entity
tags: [tool, mcp-server, exa, search, web-research, claude-code]
keywords: [exa, exa mcp, web_search_exa, crawling_exa, deep_researcher, get_code_context_exa, company_research_exa]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/exa.md
maturity: core
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/mcp-servers/exa.md` — the Exa server tool inventory + cost discipline

## Raw Concept

Exa is Cemini's canonical external-research path across all sibling wikis. This page covers the **Claude Code-side surface**: how the MCP server is wired, which tools are called from which workflow, and what the cost discipline looks like. The server-side detail lives at `@entities/mcp-servers/exa.md`.

## Narrative

The Exa MCP server exposes ~8 tools to Claude Code:

| Tool | Role |
|------|------|
| `mcp__exa__web_search_exa` | Quick targeted lookup — fact-check, find a primary source URL |
| `mcp__exa__web_search_advanced_exa` | Date-bounded, domain-scoped, or category-filtered |
| `mcp__exa__crawling_exa` | Pull clean LLM-friendly content from a known URL — turns `[Source: https://...]` into verifiable text for `## Snippets` |
| `mcp__exa__get_code_context_exa` | GitHub repo context — README, structure, key files. Primary tool for Phase-0 audits |
| `mcp__exa__company_research_exa` | Entity-expansion for tickers / orgs |
| `mcp__exa__people_search_exa` | Founder / exec / researcher discovery |
| `mcp__exa__deep_researcher_start` / `_check` | Async multi-step research jobs |

**Workflow integration** (mirrors the rule documented in every sibling wiki's CLAUDE.md):
- **Ingest**: when a source cites a URL, prefer `crawling_exa` to pull it into `## Snippets` rather than transcribing manually
- **Query (OOD)**: before declaring a wiki gap, run `web_search_exa`. If results converge, ingest the top 1-2 hits as new source pages
- **GitHub-repo eval**: `get_code_context_exa` is the Phase-0 audit's primary tool

**Cost discipline**: Exa is a paid API. Default `numResults: 3-5` for routine queries; `deep_researcher_*` reserved for genuine multi-source synthesis. Per OSINT's tracking, deep-researcher runs cost ~$0.30-$1.50 per job; routine searches are sub-cent.

**Wiring**: the server is installed via `npx -y exa-mcp-server` against an `EXA_API_KEY` env var. Configuration lives in `~/Library/Application Support/Claude/claude_desktop_config.json` (Desktop app) or `.mcp.json` (per-project). Keys never enter the wiki — they're `.env`-gitignored.

The `exa:search` skill (from `exa@claude-plugins-official`) fans out across parallel subagents for genuinely complex research questions — this is Cemini's bridge into the subagent-orchestration concept (`@concepts/subagent-orchestration.md`).

## Dead Ends

- **Running `deep_researcher_*` for routine fact-checks** — overkill and expensive. The 3-5 result `web_search_exa` is the right default.
- **Bypassing `crawling_exa` and pasting raw URLs** — burns context budget on noisy HTML; the crawler returns LLM-clean markdown.
