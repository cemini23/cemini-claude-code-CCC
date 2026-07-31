---
title: Modular instruction memory with learnable selection (MILES pattern)
type: concept
tags: [concept, memory, reasoning, harness, test-time, k153]
keywords: [miles, 2607.06974, sub-goal, sub-instruction, coarse-to-fine, learnable selection, sequential reasoning]
related:
  - sources/arxiv-miles-modular-instruction-memory-2607.06974.md
  - concepts/metamemory-scaffold-proficiency-training.md
  - concepts/dual-representation-agent-memory.md
  - concepts/procedural-memory-transfer-after.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/agent-completion-verification-gates.md
  - sources/brief-k153-miles-modular-instruction-memory-2026-07-13.md
  - briefs/2026-07-13_ccc-handoff-memory-search-trustx-ingest.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
  - sources/arxiv-memharness-reconstructed-memory-2607.28272.md
maturity: draft
created: 2026-07-13
updated: 2026-07-31
---

## Relations

- `@sources/arxiv-miles-modular-instruction-memory-2607.06974.md` — K153 provenance

## Raw Concept

K153 arXiv **2607.06974** — MILES treats **sequential problem streams** as a memory-composition problem: select reusable **sub-instructions** optimized for **final-answer correctness**, not template reuse alone.

## Narrative

### vs CCC memory patterns

| Pattern | MILES | CCC analogue |
|---------|-------|--------------|
| Whole-solution cache | Rejected (poor novelty generalization) | Avoid caching full session transcripts as "skills" |
| Step-level heuristic pick | Rejected | Prefer rubric/gatekeeper over ad-hoc retrieval |
| **Modular sub-goal + sub-instruction** | Core unit | Wiki concept pages + skill snippets as modular units |
| **Learnable selection** | Trained on confident samples | super-audit / gatekeeper rerank before reuse |
| **Coarse-to-fine** | Expand then rerank | preingest LIKELY → deep read; `/goal` AC before promote |

### Harness steal [TENTATIVE]

1. Store **modular** memory (sub-goal + procedure snippet), not monolithic chat logs
2. Optimize selection for **task completion correctness** (pytest, wiki_lint), not similarity alone
3. **Coarse-to-fine:** cheap recall → learned/rubric rerank on uncertain cases
4. Incremental expansion under test-time constraints — pairs with `@concepts/hot.md` session cache discipline

| Verdict | **REFERENCE** — no install; adopt selection + modularity vocabulary in memory/skill promotion |

## Snippets

> "Learning selection policies requires … test-time settings where memory expands incrementally and only limited supervision is available."
> — [Source: arxiv-2607.06974 §1 paraphrase, retrieved 2026-07-13]
