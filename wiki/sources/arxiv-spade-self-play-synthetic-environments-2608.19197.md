---
title: "SPADE — self-play in adaptive synthetic executable environments"
type: source
tags: [source, arxiv, self-play, rl, synthetic-environments, k294]
keywords: [2608.19197, SPADE, environment designer, hint-based regret, Gym interface]
related:
  - concepts/self-play-adaptive-synthetic-executable-environments.md
  - entities/tools/spade-rl.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/adversarial-curriculum-structured-reward-doc-fidelity.md
  - sources/brief-k290-k294-harness-wave-2026-08-20.md
  - briefs/2026-08-20_ccc-handoff-k290-k294-ingest.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- `@concepts/self-play-adaptive-synthetic-executable-environments.md`
- `@entities/tools/spade-rl.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SPADE: Self-Play in Adaptive Synthetic Executable Environments |
| **arXiv** | 2608.19197 |
| **Code** | `github.com/spade-rl/spade` — **MIT** LICENSE on disk (~1.4MB) |
| **Retrieved** | 2026-08-20 |

## Narrative

Single LLM plays **Environment Designer** (writes Gym-style executable Python envs with reset/step) and **Reasoning Agent**. Designer trained via **hint-based regret** — reward gap with/without privileged hints targets frontier-difficulty envs. Corpus grounding + environment memory critical. +5.3 avg on held-out benchmarks; +13.9 ACEBench-Agent tool-use.

| Verdict | **ADOPT** co-evolving executable env designer + hint-based regret curriculum. **GO REFERENCE** MIT clone. Trainer runtime **`wont_wire`**. Pairs K162 closed-loop guardrails. |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.19197-spade-self-play-in-adaptive-synthetic-executable.pdf` |
