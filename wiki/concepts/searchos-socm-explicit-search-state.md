---
title: SearchOS SOCM — explicit shared search state for multi-agent seeking
type: concept
tags: [concept, multi-agent, search, context, harness, k180]
keywords: [2607.15257, SOCM, Evidence Graph, Coverage Map, Failure Memory, middleware harness]
related:
  - sources/arxiv-searchos-v1-open-domain-agent-collaboration-2607.15257.md
  - entities/tools/searchos.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/verifiable-search-agent-environment.md
  - concepts/mcp-context-optimization.md
  - sources/brief-k180-searchos-socm-2026-07-17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- `@sources/arxiv-searchos-v1-open-domain-agent-collaboration-2607.15257.md` — K180 provenance
- `@entities/tools/searchos.md` — MIT local adopt
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — skill hierarchy peer

## Raw Concept

How do multi-agent search systems avoid repetitive loops when context grows?

## Narrative

### Steal

1. Externalize progress: **Frontier / Evidence Graph / Coverage Map / Failure Memory** — not only chat history.
2. Middleware harness records grounded observations and trips on stalls/budget.
3. Schedule work against **coverage gaps**, not round-robin chat.
4. Hierarchical strategy/access skills (pair K164) to avoid rediscovering dead ends.

### Cemini mapping

| Surface | Use |
|---------|-----|
| Deep-research / wiki sweeps | Coverage map of open questions + failure memory of dead URLs |
| TipDrop research bots | Don't re-query failed vendor endpoints without backoff memory |
| Poker/metagame research | Evidence graph for opponent notes (pair K154 bounds) |

### Verdict

**ADOPT** SOCM checklist. **GO** local clone of MIT `SearchOS` for reference (`.local/adopts/SearchOS`). Prod deploy of full stack optional / WATCH until exercised.

## Snippets

> "Search Tool Middleware Harness that intercepts model and tool interactions to record grounded evidence" — Abstract
