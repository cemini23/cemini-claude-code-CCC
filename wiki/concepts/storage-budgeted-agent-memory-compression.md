---
title: Storage-budgeted agent memory compression — MemRefine pattern
type: concept
tags: [concept, agent-memory, compression, memrefine, k117]
keywords: [2606.13177, memrefine, delete-merge-preserve, llm-judge]
related:
  - sources/arxiv-memrefine-storage-budgeted-memory-2606.13177.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - concepts/tool-response-context-pruning-summarization.md
  - entities/tools/claude-mem.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/three-cache-architecture.md
  - concepts/prompt-cache-aligned-context-management.md
  - sources/brief-k117-memory-seagym-finacumen-prod-2026-06-17.md
maturity: draft
created: 2026-06-17
updated: 2026-06-30
---

## Relations

- `@sources/arxiv-memrefine-storage-budgeted-memory-2606.13177.md` — KAIST MemRefine paper
- `@concepts/multi-factor-agentic-memory-value-model.md` — multi-factor forget at consolidation
- `@concepts/tool-response-context-pruning-summarization.md` — inference-time context pruning (orthogonal)
- `@entities/tools/claude-mem.md` — adopted memory layer to compact
- `@concepts/agent-memory-stack-comparison.md` — Mem0/A-MEM peers cited in paper
- `@concepts/three-cache-architecture.md` — wiki vs claude-mem budget tiers

## Raw Concept

How do we shrink an agent memory store to a hard budget without destroying retrieval quality?

## Narrative

**Storage-budgeted memory management** [TENTATIVE — 2606.13177]: distinct from session summarization (pre-store) and retrieved-context compression (inference-time). Target = **already-built** memory store.

**MemRefine loop:**

| Step | Actor | Action |
|------|-------|--------|
| 1 | Similarity | Propose candidate pairs |
| 2 | LLM judge | delete / merge / preserve on **factual** overlap |
| 3 | Repeat | Until storage ≤ budget |

**CCC steal-for:**

- claude-mem compaction passes: similarity for candidates, LLM judge for merge vs drop (not pure recency chop)
- `hot.md` rotation under char budget with factual dedup
- Pair with blind-forgetting eval from `@concepts/multi-factor-agentic-memory-value-model.md`

**Verdict:** REFERENCE — no verified paper repo; adopt policy in memory maintenance rules.

## Snippets

> "Two textually similar entries may carry redundant facts … complementary facts … or distinct facts that both warrant preservation."

> "A general module inserted after memory construction and before retrieval."
