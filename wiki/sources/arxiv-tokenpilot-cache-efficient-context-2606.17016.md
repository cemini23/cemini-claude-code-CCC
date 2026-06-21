---
title: TokenPilot — cache-efficient context management (arXiv 2606.17016)
type: source
tags: [source, arxiv, tokenpilot, prompt-cache, context-management, k121]
keywords: [2606.17016, lightmem2, ingestion-aware-compaction, lifecycle-eviction]
related:
  - concepts/prompt-cache-aligned-context-management.md
  - entities/tools/lightmem2.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/mcp-context-optimization.md
  - concepts/three-cache-architecture.md
  - concepts/tool-response-context-pruning-summarization.md
maturity: draft
read_status: read
created: 2026-06-21
updated: 2026-06-21
---

## Relations

- `@concepts/prompt-cache-aligned-context-management.md` — CCC synthesis
- `@entities/tools/lightmem2.md` — integrated implementation
- `@concepts/token-economics-and-prompt-caching.md` — 5-minute TTL economics

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TokenPilot: Cache-Efficient Context Management for LLM Agents |
| **Authors** | Xu et al. (Zhejiang University + HomologyAI) |
| **arXiv** | 2606.17016 |
| **Integration** | `github.com/zjunlp/LightMem2` |
| **Location** | `raw-sources/arxiv-2606.17016-tokenpilot-cache-efficient-context-management-fo.pdf` |
| **Retrieved** | 2026-06-21 |
| **Read status** | read |

## Narrative

**Problem:** Long-horizon agent sessions accumulate context; naive truncation/compaction **mutates prompt prefixes** → KV cache misses → cost spikes.

**TokenPilot — dual granularity:**

| Layer | Mechanism | Goal |
|-------|-----------|------|
| Global | **Ingestion-Aware Compaction** | Stabilize prompt prefixes at ingestion gate |
| Local | **Lifecycle-Aware Eviction** | Batch-turn offload when task relevance expires |

**Results [TENTATIVE]:** PinchBench + Claw-Eval — ~61% cost reduction isolated/continuous modes while maintaining competitive task performance vs prior memory systems.

**CCC steal:** align compaction with prompt-cache continuity — pair with `@concepts/tool-response-context-pruning-summarization.md` and `@entities/tools/lazy-tool.md`.

## Snippets

> "Unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation."

> "TokenPilot has been integrated into LightMem2."
