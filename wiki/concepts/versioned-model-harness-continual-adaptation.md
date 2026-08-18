---
title: Versioned model–harness continual adaptation (Macaron / K263)
type: concept
tags: [concept, continual-learning, harness, rsi, k263]
keywords: [2608.09819, Macaron, MindForge, Mixture-of-LoRA, HCP]
related:
  - sources/arxiv-macaron-v1-continual-learning-2608.09819.md
  - entities/tools/macaron-v1.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/continual-harness-online-self-improvement.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/black-box-rl-opaque-harness-optimization.md
  - sources/arxiv-clawgym-ii-black-box-rl-harness-2608.16798.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-11
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-macaron-v1-continual-learning-2608.09819.md`
- `@entities/tools/macaron-v1.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`

## Raw Concept

How do model and harness co-evolve under an external evaluation contract without silent RSI?

## Narrative

Macaron-V1: recursive improvement of **versioned model–harness pairs** under external contracts; Mixture-of-LoRA per-turn routing; MindForge lifecycle/provenance.

### Steal (ADOPT)

1. Treat model + harness as a **versioned pair** with parent/data/eval provenance.
2. External contract / eval gates successor construction (pairs K162 hierarchy — no closed self-scoring rewrite of pass criteria).
3. MoL-style specialist adapters as vocabulary only — **no** 744B weight pulls.

| Verdict | **ADOPT** vocabulary. Weights / null-SPDX SDK **NO-GO**. |
