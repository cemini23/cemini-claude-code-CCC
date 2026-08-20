---
title: "Harness Continual Learning — continual adaptation beyond model parameters"
type: source
tags: [source, arxiv, continual-learning, harness, meta-harness, k292]
keywords: [2608.19013, HCL, harness-level forgetting, guarded evolution, frozen model]
related:
  - concepts/harness-continual-learning-guarded-evolution.md
  - entities/tools/harness-continual-learning-hcl.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/versioned-model-harness-continual-adaptation.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k290-k294-harness-wave-2026-08-20.md
  - briefs/2026-08-20_ccc-handoff-k290-k294-ingest.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- `@concepts/harness-continual-learning-guarded-evolution.md`
- `@entities/tools/harness-continual-learning-hcl.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Harness Continual Learning: Continual Adaptation Beyond Model Parameters |
| **arXiv** | 2608.19013 |
| **Authors** | Borui Kang et al. (U Wollongong / Nanjing U) |
| **Code** | none public |
| **Retrieved** | 2026-08-20 |

## Narrative

**Harness Continual Learning (HCL):** learning object shifts from model parameters to **harness state** (Task Interface, Experience Memory, Capability Map, Adaptive Router) around a frozen foundation model. Introduces **harness-level forgetting** — coupled harness updates can break earlier reliable behavior without changing weights.

**Guarded harness evolution:** Continual Optimizer proposes candidates from post-execution feedback; Continual Evaluator commits only after current improvement + historical retention + validity checks. >10% relative gains across textual, multimodal, and open-world settings.

| Verdict | **ADOPT** guarded harness evolution + explicit retention budget + harness-level forgetting metric. Pairs K281 AutoDesign, K162 external eval contract, K263 versioned harness pairs. **Policy only**. |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.19013-harness-continual-learning-continual-adaptation.pdf` |
