---
title: Adaptive Auto-Harness — open-ended task streams
type: concept
tags: [concept, agent-harness, self-improvement, k95]
keywords: [2606.01770, adaptive-auto-harness, harness-tree, stream-overfitting, a-evolve]
related:
  - sources/arxiv-adaptive-auto-harness-2606.01770.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/federated-daily-research-digest.md
  - entities/tools/adaptive-auto-harness.md
  - entities/tools/openevolve.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@sources/arxiv-adaptive-auto-harness-2606.01770.md` — primary paper
- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — non-monotonic harness benefit
- `@concepts/continual-harness-online-self-improvement.md` — prior continual-harness line

## Raw Concept

K95 arXiv **2606.01770** — auto-harness for **chronological open-ended streams** (prediction markets, security comps, forecasting), not static SWE-bench-style sets. Uses harness tree + solve-time routing + human-steering when history lacks signal.

## Narrative

### Design rules for CCC [TENTATIVE]

1. **Do not unboundedly grow skills/prompts** on daily digest streams — pairs with `@concepts/harness-updating-vs-benefit-nonmonotonic.md`.
2. **Route by task type** — harness tree ≈ per-wiki lazy-tool catalogs + conductor routing.
3. **Human-steering hooks** — operator gates on Tier-2 harness changes (`skill-vetting`, premortem skill).
4. **Score stream benefit**, not single-batch lift — daily digest + wiki log as longitudinal eval.

| Verdict | **REFERENCE** for sustained harness ops — do not deploy AdaptiveHarness on prod without Phase-0; steal routing + anti-overfit discipline |

## Snippets

> "Longer frequent evolution can overfit earlier stream evidence."
> — [Source: arxiv-2606.01770-adaptive-auto-harness-sustained-self-improvement.pdf p.1]
