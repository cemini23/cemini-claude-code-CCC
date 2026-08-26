---
title: "SCOUT — hybrid semantic tool discovery for enterprise MCP gateway (CCC K311)"
type: source
tags: [source, arxiv, mcp, tool-discovery, context-engineering, hybrid-retrieval, k311]
keywords: [2608.23992, SCOUT, PayPal, MCP gateway, BM25, RRF, tool_search, execute_tool, token reduction]
related:
  - concepts/hybrid-mcp-tool-discovery-lazy-catalog.md
  - briefs/2026-08-26_ccc-k310-k314-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@concepts/hybrid-mcp-tool-discovery-lazy-catalog.md`
- `@briefs/2026-08-26_ccc-k310-k314-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation (SCOUT) |
| **arXiv** | 2608.23992 |
| **Authors** | Olympia Saha, Amy Wang, Srinivasan Manoharan (PayPal, Inc.) |
| **Code** | No public repo — internal PayPal deployment → policy only |
| **Retrieved** | 2026-08-26 |

## Narrative

Production pattern from PayPal's AI Proxy: an enterprise MCP gateway aggregating 200+ servers / 2,000+ tools saturated 140.2k tokens (70.1% of a 200k context) before the first user message. SCOUT reframes tool exposure as a context-selection problem: `tools/list` returns only two synthetic meta-tools, `tool_search` and `execute_tool`. `tool_search` runs agentic RAG — BM25 sparse + dense vector search fused with Reciprocal Rank Fusion (k=60), candidate expansion ×3 per branch, default top-k=5 clamped [1,20] — then `execute_tool` routes to the backend server. Result: 140.2k → ~1.3k tokens (**99% cut**), validated across six MCP clients (Claude Code, Claude Desktop, ChatGPT, Copilot, Cursor, Codex CLI) with zero client-side changes.

Design details CCC steals: authorization filtering at the retrieval layer; insert-before-delete upserts for zero-downtime catalog refresh; graceful degradation (BM25-only on embedding failure, full injection only as last resort); description text carries the protocol ("Never guess a tool_name. Always get it from tool_search first."). Prompt caching does not solve this — cost drops but the model still attends to the whole catalog.

Pairs K164 (`@concepts/hierarchical-skill-stack-lazy-orchestration.md`) lazy orchestration and BPS (`@concepts/skill-set-selection-under-budget.md`) set-not-top-k: never load the full tool catalog at turn 0.

| Verdict | **ADOPT** lazy hybrid retrieval (`tool_search` + `execute_tool`) instead of full schema dumps. No public SPDX → no clone. `wire_status: policy_wired`. Atto steal brief written. |
|---------|---------|

## Snippets

> "SCOUT surfaces two synthetic MCP meta-tools, tool_search and execute_tool … reduces MCP tool-token consumption from 140.2k tokens (70.1% of context) to 1.3k tokens (0.8%), a 99% reduction." [Source: arXiv 2608.23992 abstract]

> "A hard guardrail is included: 'Never guess a tool_name. Always get it from tool_search first.'" [Source: arXiv 2608.23992 §5.1]

> "Prompt caching partially alleviates the cost of reprocessing static tool schemas, but it does not reduce context window consumption or improve selection accuracy." [Source: arXiv 2608.23992 §1]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.23992-hybrid-semantic-tool-discovery-for-enterprise-mc.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
