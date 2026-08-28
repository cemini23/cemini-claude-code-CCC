---
title: "Progress-guided step routing — route per step, not per query (CCC K318)"
type: concept
tags: [concept, routing, orchestration, cost, quality-cost, k318]
keywords: [ProgRouter, progress scorer, step-wise routing, cascade, meta-gating, budget, 2608.25992]
related:
  - sources/arxiv-progrouter-progress-orchestration-2608.25992.md
  - entities/skills/route.md
  - concepts/skill-set-selection-under-budget.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-progrouter-progress-orchestration-2608.25992.md`
- `@entities/skills/route.md`
- `@concepts/skill-set-selection-under-budget.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

The question: cascade routing picks one LLM per query at the start; multi-step workflows need a different model mid-task as progress and difficulty evolve. How do we route per step under cost budgets? Answer from ProgRouter [Source: wiki/sources/arxiv-progrouter-progress-orchestration-2608.25992.md]: online progress-guided routing.

## Narrative

One-shot cascade routing is wrong for multi-step workflows: the right LLM at each step depends on **evolving task progress, remaining task difficulty, and cost-efficiency requirements** — none of which exist at query time.

The ProgRouter pattern (ADOPT):

1. **Multi-view task progress scorer** — coarse workflow outcome regimes + fine-grained signals (subtask completion, progress trends, workflow state quality).
2. **Dual-path progress predictor + adaptive meta-gating** — estimate the progress gain of each candidate routed LLM.
3. **Online step-wise routing** — balance progress gain, task time budgets, and long-term operating cost efficiency.

CCC application: `/route` (via `@entities/skills/route.md`) makes **one decision per turn anyway**; the steal is to score the step against *progress + remaining difficulty + cost* instead of a static query-complexity heuristic. This also extends `@concepts/skill-set-selection-under-budget.md` (pick skills under budget, per step) and K311 SCOUT (retrieve per step, not at turn 0).

| Confidence | `[CONFIRMED]` — paper results across HumanEval Plus/MBPP/MATH-500/ASQA; pattern adoption, not reproduced in CCC |
|------------|------------|

## Snippets

> "Cascade routing methods make one-shot, query-level decisions and cannot adapt to the dynamic, state-dependent nature of multi-step workflows." [Source: arXiv 2608.25992 abstract]
