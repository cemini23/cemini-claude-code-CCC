---
title: MemRefine — LLM-guided storage-budgeted agent memory (arXiv 2606.13177)
type: source
tags: [source, arxiv, memrefine, agent-memory, compression, k117]
keywords: [2606.13177, memrefine, storage-budget, llm-judge, locomo]
related:
  - concepts/storage-budgeted-agent-memory-compression.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - entities/tools/claude-mem.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/tool-response-context-pruning-summarization.md
maturity: draft
read_status: read
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- `@concepts/storage-budgeted-agent-memory-compression.md` — CCC synthesis
- `@concepts/multi-factor-agentic-memory-value-model.md` — forgetting/value peer
- `@entities/tools/claude-mem.md` — compaction target
- `@concepts/agent-memory-stack-comparison.md` — memory stack context

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MemRefine: LLM-Guided Compression for Long-Term Agent Memory |
| **Authors** | Kim et al. (Korea Univ., KAIST, DeepAuto.ai) |
| **arXiv** | 2606.13177v1 [cs.CL] |
| **Location** | `raw-sources/arxiv-2606.13177-2606-13177v1-memrefine-llm-guided-compression-fo.pdf` |
| **Retrieved** | 2026-06-17 |
| **Read status** | read (task definition, LLM judge loop, benchmarks) |

## Narrative

Introduces **storage-budgeted memory management** — keep an already-constructed agent memory store within a fixed budget while preserving retrieval-useful information.

**MemRefine** = post-construction compression module (after memory build, before retrieval):

1. **Similarity** proposes candidate pairs (graph or non-graph stores)
2. **LLM judge** decides per pair: **delete**, **merge**, or **preserve** based on **factual content** (not surface wording)
3. Iterate until budget met

Evaluated on **A-MEM** graph memory and **Mem0** pipeline across LoCoMo-style benchmarks. Meets target budgets; preserves downstream performance under moderate compression; beats rule-based similarity/graph-pruning baselines under tight budgets.

**Repo:** no verified public implementation for this paper (2026-06-17). `zz2cc/MemRefine` on GitHub is a **different** project (3DrawAgent CKE) — do not conflate.

## Snippets

> "Similarity to propose candidate pairs but defers delete, merge, and preserve decisions to an LLM judge based on factual content."

> "Post-construction memory compression … without modifying the host memory pipeline."
