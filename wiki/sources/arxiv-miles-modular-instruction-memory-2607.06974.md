---
title: MILES — Modular Instruction Memory with Learnable Selection (2607.06974)
type: source
tags: [source, arxiv, memory, reasoning, test-time, k153]
keywords: [2607.06974, miles, modular instruction memory, learnable selection, self-improving reasoning, unsw]
related:
  - concepts/modular-instruction-memory-learnable-selection.md
  - concepts/metamemory-scaffold-proficiency-training.md
  - concepts/dual-representation-agent-memory.md
  - concepts/continual-harness-online-self-improvement.md
  - sources/brief-k153-miles-modular-instruction-memory-2026-07-13.md
maturity: draft
read_status: read
created: 2026-07-13
updated: 2026-07-13
phase_0_verdict: "REFERENCE 2026-07-13 — no public code repo at Phase-0; steal coarse-to-fine memory selection optimized for final-answer correctness"
---

## Relations

- `@concepts/modular-instruction-memory-learnable-selection.md` — CCC synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning |
| **Authors** | Ruilin Tong, Dong Gong — UNSW Sydney |
| **arXiv** | 2607.06974v1 [cs.CL] |
| **Code** | **None** at Phase-0 — Project Page: MILES (no GitHub in paper) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.06974-2607-06974v1-miles-modular-instruction-memory-wi.pdf` |
| **Retrieved** | 2026-07-13 |

## Narrative

MILES improves **sequential** LLM reasoning at **test time** via **modular instruction memory** — not whole-solution templates (poor generalization) nor heuristic step selection (not optimized for final correctness).

**Memory unit:** asymmetric pair of **sub-goal embedding** + **sub-instruction**, each with a **learnable selection head**.

**Coarse-to-fine retrieval:**
1. **Coarse** — expand memory; collect supervision from confident samples to train selection heads
2. **Fine** — rerank coarse candidates with learned heads for uncertain samples

Claims superior accuracy-efficiency tradeoff vs prior memory methods; transferability across problem streams.

| Verdict | **REFERENCE** — harness steal: correctness-optimized memory composition under incremental test-time expansion |

## Snippets

> "MILES maintains modular memory units consisting of asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head."
> — [Source: arxiv-2607.06974 abstract, retrieved 2026-07-13]
