---
title: "TPD — score the stage, do not imitate the trace (CCC k285 route)"
type: source
tags: [source, k285, cross-wiki]
keywords: [2610.10332, k285]
related:
  - concepts/stage-scored-distillation.md
  - briefs/2026-10-08_k285-ccc-route.md
  - "@osint-wiki/sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md"
maturity: draft
read_status: skimming
cross-wiki-source: "@osint-wiki/sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md"
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@concepts/stage-scored-distillation.md`
- `@briefs/2026-10-08_k285-ccc-route.md`
- `@osint-wiki/sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md` — cross-wiki canon

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TPD — score the stage, do not imitate the trace |
| **arXiv** | 2610.10332 (2026-10) |
| **Canon** | `@osint-wiki/sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md` |
| **Routed by** | `briefs/2026-10-08_k285-ccc-harness-coevolution.md` / `..._resilience.md` |

## Narrative

**Label each action with a task *stage*, then score stage–action pairs instead of
generating long traces.** The distinction matters: imitating a trace teaches a model to reproduce
*someone's* sequence; scoring stage–action pairs teaches it which action is right *at this stage*,
which generalises across orderings. ALFWorld, Qwen3-1.7B: **at 200 demos, 67.7% against 48.0%
(+19.7 pp)**. A **shuffled-stage control drops success 55.2% → 37.6%** — so the stage label is doing
real work, not decoration. A deterministic harness executes the chosen action.

**CCC reading.** This is the same move as K428 (CLIFT: certify a reusable question bank rather than
imitate a trajectory) and K431 (Grounded TSR: score the process, not the outcome), arriving from a
third direction: **decompose the task into named stages and score at stage granularity.** Two
reusable pieces — **the shuffled control** (prove the label carries information by destroying it) and
**the deterministic executor** (the model chooses, the harness acts). Pairs
`@concepts/verifiable-deterministic-agent-benchmarking.md` /
`@concepts/progressive-skill-discovery-access-control.md` / K431 / K428.

**Boundary:** FILE only. No install, no clone.

## Snippets

> "A shuffled-stage control drops success 55.2% → 37.6%." [Source: `@osint-wiki/sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md` via k285 (retrieved 2026-10-08)]
