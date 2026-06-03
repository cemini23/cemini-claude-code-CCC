---
title: Adaptive Auto-Harness — arXiv 2606.01770
type: source
tags: [source, arxiv, agent-harness, self-improvement, k95]
keywords: [2606.01770, adaptive-auto-harness, open-ended-streams, harness-tree, a-evo-lab]
related:
  - concepts/adaptive-auto-harness-open-ended-streams.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/continual-harness-online-self-improvement.md
  - entities/tools/adaptive-auto-harness.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: skimmed
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@concepts/adaptive-auto-harness-open-ended-streams.md` — CCC synthesis
- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — overfitting / non-monotonic gains
- `@entities/tools/adaptive-auto-harness.md` — upstream repo

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams |
| **Author** | Zewen Liu et al. (Emory, Amazon, Penn State, UIUC, Northeastern) |
| **arXiv** | 2606.01770 |
| **Retrieved** | 2026-06-03 |
| **Read status** | skimmed |
| **Location** | `raw-sources/arxiv-2606.01770-adaptive-auto-harness-sustained-self-improvement.pdf` |
| **Code** | [A-EVO-Lab/AdaptiveHarness](https://github.com/A-EVO-Lab/AdaptiveHarness) |

## Narrative

Extends auto-harness systems (A-Evolve, GEPA, Meta-Harness) from **fixed offline benchmarks** to **open-ended task streams** where histories grow, task types vary, and distributions shift. Decomposes oracle gap into evolution loss + adaptation loss; uses a stateful multi-agent evolver, harness tree with solve-time routing, and human-steering hooks. Evaluated on prediction-market, security-competition, and event-forecasting streams. Documents that unbounded evolution can overfit early stream evidence (skills/prompt bloat, fading pass-rate lift).

## Snippets

> "A single repeatedly and densely updated harness [is] brittle, causing performance degradation as accuracy peaks early and then declines."
> — [Source: arxiv-2606.01770-adaptive-auto-harness-sustained-self-improvement.pdf p.1]

> "The framework decomposes the gap to an oracle harness into evolution loss and adaptation loss."
> — [Source: arxiv-2606.01770-adaptive-auto-harness-sustained-self-improvement.pdf p.1]
