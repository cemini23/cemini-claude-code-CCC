---
title: Prompt-cache-aligned context management — TokenPilot pattern
type: concept
tags: [concept, prompt-cache, context-management, tokenpilot, k121]
keywords: [2606.17016, cache-continuity, lifecycle-eviction, ingestion-compaction]
related:
  - sources/arxiv-tokenpilot-cache-efficient-context-2606.17016.md
  - entities/tools/lightmem2.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/three-cache-architecture.md
  - concepts/mcp-context-optimization.md
  - concepts/tool-response-context-pruning-summarization.md
  - entities/tools/lazy-tool.md
  - concepts/storage-budgeted-agent-memory-compression.md
  - sources/brief-k121-tokenpilot-safeclaw-gatekeepers-prod-2026-06-21.md
maturity: draft
created: 2026-06-21
updated: 2026-06-30
---

## Relations

- `@sources/arxiv-tokenpilot-cache-efficient-context-2606.17016.md` — TokenPilot paper
- `@entities/tools/lightmem2.md` — MIT reference implementation
- `@concepts/token-economics-and-prompt-caching.md` — 5-minute TTL discipline
- `@concepts/three-cache-architecture.md` — prefix stability rules
- `@concepts/mcp-context-optimization.md` — four-layer MCP cost stack
- `@concepts/tool-response-context-pruning-summarization.md` — content reduction without cache bust
- `@entities/tools/lazy-tool.md` — stable tool surface for cache hits
- `@concepts/storage-budgeted-agent-memory-compression.md` — memory budget peer

## Raw Concept

How do we shrink agent context without destroying prompt-cache continuity?

## Narrative

**Core trade-off** [TENTATIVE — 2606.17016]: text sparsity vs **prompt cache continuity**. Truncation/compaction that mutates input boundaries causes KV cache misses even when tokens drop.

### TokenPilot mechanisms

| Mechanism | Scope | CCC mapping |
|-----------|-------|-------------|
| Ingestion-Aware Compaction | Global prefix stabilization | Filter noise at MCP ingest; lazy-tool stable catalog |
| Lifecycle-Aware Eviction | Local segment utility | Evict stale turns when task completes; keep prefix stable |

**Claimed savings:** ~61% cost on PinchBench/Claw-Eval with competitive accuracy.

### Harness rules

1. Never compact across **stable prefix boundaries** (CLAUDE.md, rules, tool catalog header).
2. Evict **completed task spans** on conservative batch schedule — align with `@concepts/handoff-validity-agent-harness.md` completion evidence.
3. Measure cache hits via billing dashboards (`@entities/tools/ai-token-monitor.md`) when adopting LightMem2.

**Install:** LightMem2 **CONDITIONAL-GO** — evaluate vs claude-mem + manual pruning before prod.

## Snippets

> "Managing context growth is an essential prerequisite for sustainable real-world deployment."

> — [Source: arxiv-2606.17016-tokenpilot-cache-efficient-context-management-fo.pdf]
