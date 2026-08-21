---
title: "Adaptive validation-task selection for harness optimization (Task-CoEvolve)"
type: concept
tags: [concept, harness, optimization, eval, sampling, k298]
keywords: [2608.20169, Task-CoEvolve, variance-weighted, Terminal-Bench, full-set estimation]
related:
  - sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md
  - entities/tools/task-coevolve.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - sources/arxiv-k244-harness-skill-selection-cluster.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md`
- `@entities/tools/task-coevolve.md`

## Raw Concept

When iterating a harness optimizer loop, must every candidate be re-scored on the full validation pack every iteration?

## Narrative

**Task-CoEvolve** (U Tokyo): harness optimization rewrites the harness code around a **fixed** LLM (harness alone drives up to 6× benchmark difference). Naive loops evaluate the full fixed val set every iteration — expensive (long-horizon terminal tasks occupy sandboxes for tens of minutes) and static (solved-always / failed-always tasks stop discriminating). Task-CoEvolve instead:

1. **Variance-weighted sampling** — tasks where candidate harnesses *disagree* (Bernoulli variance of historical success rate ≈ balanced success/failure) are most informative; the sampling distribution shifts with the harness toward the **capability frontier**.
2. **Full-set score estimation** — use task inclusion probabilities to estimate full-set scores from the sampled subset, keeping candidate comparisons consistent across iterations despite different subsets.

Results: online text classification approaches full-set search at **7% budget**, **beats full-set at 20%** (less overfitting to the full pack); **Terminal-Bench 2.1 matches full-set search with 20% of evaluations** (67–80% lower search cost).

**Cemini steal (pairs K281 AutoDesign meta-harness loop / K292 HCL / K162 external eval contract):**

1. **Do not re-score the full val pack every harness loop.** Sample informative/disagreeing tasks; estimate full-set from partial evals (inclusion-probability weighting).
2. **Budget can beat full-set** — a 20% informative subset can beat full-set search (less overfitting); keep pass criteria fixed regardless.
3. **Do not auto-evolve `.cursor/skills`** (misevolution gate — skills worsen with practice); **do not rewrite `## Verify` / pass criteria** mid-run. This optimizes *which tasks you evaluate on*, never *what counts as success*.
4. `Agent4Science-UTokyo/Task-CoEvolve` **no LICENSE** → **NO-GO clone** (null SPDX).

| Verdict | **ADOPT** — `policy_wired`. Fills the Task-CoEvolve item in the k244 steal brief (`briefs/2026-08-21_k244-harness-skill-wayfinder.md`); **dual-ID: CCC K298**, not K244 (K244 = UrbanAgent). |

## Snippets

> "On Terminal-Bench 2.1, Task-CoEvolve matches the performance of full-set search using only 20% of the evaluations, while reducing the overall search cost by 67–80%." [Source: arxiv 2608.20169 (retrieved 2026-08-21)]
