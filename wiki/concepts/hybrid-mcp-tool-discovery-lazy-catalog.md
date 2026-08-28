---
title: "Hybrid MCP tool discovery — lazy catalog via meta-tools (CCC K311)"
type: concept
tags: [concept, mcp, context-engineering, retrieval, tool-discovery, k311]
keywords: [tool_search, execute_tool, BM25, dense retrieval, RRF, token budget, tools/list, lazy loading]
related:
  - sources/arxiv-scout-hybrid-mcp-tool-discovery-2608.23992.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/skill-set-selection-under-budget.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
  - entities/skills/scout-tool-search.md
maturity: draft
created: 2026-08-26
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-scout-hybrid-mcp-tool-discovery-2608.23992.md`
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md`
- `@concepts/skill-set-selection-under-budget.md`

## Raw Concept

The question: how do agents use a 2,000-tool MCP catalog without loading it into context? Answer from PayPal's SCOUT [Source: wiki/sources/arxiv-scout-hybrid-mcp-tool-discovery-2608.23992.md]: expose two meta-tools and retrieve schemas per step.

## Narrative

Full `tools/list` injection is O(N) context forever; prompt caching amortizes cost but the model still attends to every schema on every query. SCOUT's lazy pattern:

1. **Two meta-tools** — `tool_search` (hybrid retrieval) + `execute_tool` (routed invocation). Discovery decoupled from execution.
2. **Hybrid retrieval** — BM25 sparse + dense vectors fused with Reciprocal Rank Fusion (k=60), ×3 candidate expansion per branch, top-k=5 default.
3. **Protocol in descriptions** — "Never guess a tool_name. Always get it from tool_search first." No fine-tuning, no client changes; works in Claude Code, Cursor, ChatGPT, Copilot, Codex CLI.
4. **Ops discipline** — authorization filtered inside the vector DB, insert-before-delete zero-downtime refresh, graceful degradation to BM25-only then full injection.

Production number: 140.2k tokens → 1.3k (**99% cut**) with full capability preserved.

CCC policy (ADOPT): never load the full tool catalog at turn 0; retrieve per step, then execute. Same principle as K164 lazy skill stacks (`@concepts/hierarchical-skill-stack-lazy-orchestration.md`) and BPS set-not-top-k (`@concepts/skill-set-selection-under-budget.md`) applied to MCP tool surfaces. Leftover implementation (propose-only): SCOUT-style meta-tools on `/route` — HITL later.

| Confidence | `[CONFIRMED]` — production deployment at PayPal across six MCP clients |
|------------|------------|

## Snippets

> "SCOUT reduces MCP tool-token consumption from 140.2k tokens (70.1% of context) to 1.3k tokens (0.8%), a 99% reduction" [Source: arXiv 2608.23992 abstract]
