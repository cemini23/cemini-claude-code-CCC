---
title: "TPD — score the stage, do not imitate the trace (CCC k285 route)"
type: concept
tags: [concept, k285, cross-wiki]
keywords: [2610.10332, k285]
related:
  - sources/arxiv-task-progress-distillation-stage-scored-2610.10332.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-08_k285-ccc-route.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@sources/arxiv-task-progress-distillation-stage-scored-2610.10332.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-08_k285-ccc-route.md`

## Raw Concept

Routed from `@osint-wiki` via the k285 briefs. Canon stays on OSINT.

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

> "See source page for locators." [Source: CCC k285 synthesis]
