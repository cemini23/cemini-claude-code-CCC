---
title: Exa MCP server
type: entity
tags: [mcp-server, exa, search, web-research, paid-api]
keywords: [exa, exa.ai, exa-mcp-server, web_search_exa, deep_researcher, embeddings search, neural search]
related:
  - entities/tools/exa-mcp.md
  - concepts/cross-wiki-routing.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/lazy-tool.md
maturity: core
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/exa-mcp.md` — Claude-Code-side wiring and per-tool guidance
- `@concepts/cross-wiki-routing.md` — Exa's `deep_researcher` is one fan-out alternative to conductor

## Raw Concept

Exa.ai (exa.com) — paid neural-search API. Exposed to Claude Code via the official `exa-mcp-server` package. This page covers the *server* (what it is, how it's wired, what the keys are); the *Claude Code-side surface* (which tool to call when) lives at `@entities/tools/exa-mcp.md`.

## Narrative

Exa is a neural / embedding-based web search engine optimized for LLM consumption. Where Google / Brave return keyword-matched results meant for human eyes, Exa returns semantically-matched results with extracted, deduplicated, LLM-clean content blocks. For Cemini's wiki workflows (ingest, OOD-query, Phase-0 audit) this maps better than keyword search.

**Installation** (canonical Cemini wiring):

```json
{
  "mcpServers": {
    "exa": {
      "command": "npx",
      "args": ["-y", "exa-mcp-server"],
      "env": {
        "EXA_API_KEY": "${EXA_API_KEY}"
      }
    }
  }
}
```

The key lives in `.env` (gitignored). The `${EXA_API_KEY}` expansion is handled by the MCP host. Cemini's `.env.example` template documents the variable; the actual key never enters git.

**Tool surface** — eight tools per the current server build (see `@entities/tools/exa-mcp.md` for the routing table). Cemini's adoption pattern:

- Routine: `web_search_exa`, `crawling_exa`, `get_code_context_exa`. These cover ~95% of session use.
- Occasional: `web_search_advanced_exa` (when date/domain filters matter), `company_research_exa` (ticker watchlist gap-fill), `people_search_exa` (founder/exec lookup).
- Rare: `deep_researcher_start` / `_check`. Reserved for genuinely multi-source synthesis — typical job costs ~$0.30-$1.50 and takes 1-5 minutes async.

**Cost discipline**:

- Default `numResults: 3-5` for routine queries. Higher values rarely improve signal-to-noise.
- `deep_researcher_*` only when ≥3 distinct sources are required and the question can't be answered by 3 routine searches.
- Cemini reviews monthly Exa usage in the Exa dashboard; a session that burns >$1 of Exa without a deep-research justification gets investigated.

**Phase-0 verdict**: GO. Adopted across all five sibling wikis. The OSINT CLAUDE.md "External research — Exa MCP" section is the cross-wiki canon for Exa cost discipline; this page references that section rather than duplicating.

## Dead Ends

- **Using Exa for navigational lookups** — "what is exa.ai?" → Google is faster and free. Exa earns its slot on semantic / domain-specific search.
- **Treating Exa as a knowledge base** — it's a search engine. Ingest results into wiki source pages; don't rely on re-querying the same URL each session.
