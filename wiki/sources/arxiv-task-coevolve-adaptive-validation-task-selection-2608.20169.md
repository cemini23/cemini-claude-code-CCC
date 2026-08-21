---
title: "Task-CoEvolve — adaptive validation task selection for harness optimization"
type: source
tags: [source, arxiv, harness, optimization, eval, k298]
keywords: [2608.20169, Task-CoEvolve, variance-weighted sampling, Terminal-Bench, harness optimization]
related:
  - concepts/adaptive-validation-task-selection-harness-optimization.md
  - entities/tools/task-coevolve.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - sources/arxiv-k244-harness-skill-selection-cluster.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@concepts/adaptive-validation-task-selection-harness-optimization.md`
- `@entities/tools/task-coevolve.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection |
| **arXiv** | 2608.20169 |
| **Authors** | Miyai, Aizawa, Yamasaki (The University of Tokyo) |
| **Code** | `github.com/Agent4Science-UTokyo/Task-CoEvolve` — **no LICENSE** → **NO-GO clone** |
| **Retrieved** | 2026-08-21 |

## Narrative

Harness optimization (meta-level agent iteratively rewrites the harness around a **fixed** LLM — up to 6× performance difference on the same benchmark) normally evaluates the full fixed validation set every iteration: expensive (long-horizon terminal tasks occupy sandboxes for tens of minutes) and static (tasks stop discriminating as the harness evolves). **Task-CoEvolve** co-evolves the validation task set: (i) **variance-weighted sampling** — tasks where candidate harnesses disagree (Bernoulli variance of historical success rate) are more informative; the sampling distribution tracks the capability frontier as the harness evolves; (ii) **full-set score estimation** from partial evaluations via inclusion probabilities, keeping iterations comparable.

Results: on online text classification, approaches full-set search at a **7% budget** and **outperforms full-set at 20%**; on **Terminal-Bench 2.1** matches full-set search with **20% of evaluations**, cutting search cost **67–80%**.

| Verdict | **ADOPT** pattern: when iterating the CCC harness, sample informative val tasks instead of re-scoring the full pack every loop; estimate full-set from partial evals. `Agent4Science-UTokyo/Task-CoEvolve` **no LICENSE** → **NO-GO clone**. **Do not** auto-evolve `.cursor/skills` (misevolution) or rewrite `## Verify` / pass criteria. Pairs K281 / K292 / K162. |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.20169-task-coevolve-efficient-harness-optimization-via.pdf` |
