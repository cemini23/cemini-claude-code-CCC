---
title: "K244 harness skill-selection cluster — BPS, EnvHarness, Task-CoEvolve"
type: source
tags: [source, arxiv, cluster, skills, harness, k244, k298]
keywords: [2608.19993, 2608.19880, Task-CoEvolve, BPS, EnvRigger, skill selection]
related:
  - concepts/skill-set-selection-under-budget.md
  - concepts/adaptive-validation-task-selection-harness-optimization.md
  - sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md
  - concepts/skill-misevolution.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - entities/skills/skill-set-budget.md
  - entities/skills/env-harness-wrap.md
  - entities/skills/wayfinder.md
maturity: draft
read_status: skimmed
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@concepts/skill-set-selection-under-budget.md`
- `@concepts/adaptive-validation-task-selection-harness-optimization.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | K244 harness skill-selection cluster — steal-from (another wiki's K244) |
| **Papers** | arXiv 2608.19993 (BPS set-level skill select) · arXiv 2608.19880 (EnvHarness/EnvRigger) · `github.com/Agent4Science-UTokyo/Task-CoEvolve` |
| **Retrieved** | 2026-08-20/21 |

## Narrative

**Cluster source page (propose-only steals).** Fills the missing-source citations of `briefs/2026-08-21_k244-harness-skill-wayfinder.md`:

1. **BPS set-level skill select, not top-k.** Monotone submodular benefit − token penalty; bicriteria (1−1/e, 1). 0.73 vs 0.20–0.52 routers; 28% fewer tokens. Complements vs distractors.
2. **EnvHarness wrap, don't rebuild.** Keep the verifier; EnvRigger synthesizes plug-ins from trajectories. Up to +9.0 held-out, 9.8% fewer steps.
3. **Task-CoEvolve variance-weighted val tasks.** 80% fewer evals; 20% budget can beat full-set (less overfitting). **Dual-ID: this repo is CCC K298** (see `sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md`); the K244 number here is the *steal-from brief's* board, not a CCC K.

Retrieval bottleneck note (BrowseComp-Plus_CM): agentic search evals that freeze a query-built 100K corpus overstate recall — ClimbMix projection 84.3%→21.4% evidence recall, −5 pts accuracy. Filed on routing backlog (see `@concepts/agent-toolkit-routing-research-backlog.md`), not a clone.

| Verdict | **ADOPT decision-rule + wrap policy** — skills `skill-set-budget`, `env-harness-wrap`, `wayfinder` HITL-wired 2026-08-21. No BPS solver clone; EnvRigger WATCH. |
