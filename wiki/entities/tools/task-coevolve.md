---
title: "Task-CoEvolve — adaptive validation-task selection for harness optimization (U Tokyo)"
type: entity
tags: [entity, tool, harness, optimization, eval, k298]
keywords: [2608.20169, Task-CoEvolve, policy_wired, NO-GO clone, variance-weighted]
related:
  - sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md
  - concepts/adaptive-validation-task-selection-harness-optimization.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md`
- `@concepts/adaptive-validation-task-selection-harness-optimization.md`

## Raw Concept

Phase-0 entity for CCC K298 — Task-CoEvolve variance-weighted val-task sampling; GitHub repo has **no LICENSE** → NO-GO clone.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| Task-CoEvolve code | `Agent4Science-UTokyo/Task-CoEvolve` | **NO-GO clone** (null SPDX / no LICENSE file) |

**Phase-0:** `scripts/adopt_k298_phase0.sh` — no clone.

ADOPT policy: sample informative val tasks (−80% evals, matches full-set) when iterating the CCC harness; do not auto-evolve `.cursor/skills` or rewrite `## Verify`/pass criteria. **Dual-ID: CCC K298** (fills the Task-CoEvolve item in `briefs/2026-08-21_k244-harness-skill-wayfinder.md`); K244 stays UrbanAgent.

## Phase-1

`policy_wired` → `.cursor/rules/cemini-phase1-policy-wires.mdc` (§K298). Pairs K281 / K292 / K162.
