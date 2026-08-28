---
title: "ProgRouter — online progress-guided orchestration (CCC K318)"
type: source
tags: [source, arxiv, orchestration, routing, cost, multi-agent, k318]
keywords: [2608.25992, ProgRouter, progress scorer, step-wise routing, cascade, quality-cost, budget]
related:
  - concepts/progress-guided-step-routing.md
  - entities/skills/route.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@concepts/progress-guided-step-routing.md`
- `@entities/skills/route.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | PROGROUTER: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs |
| **arXiv** | 2608.25992 (2026-08-26) |
| **Authors** | Songyuan Li (Aston), Ahmed M. Abdelmoniem (QMUL), Shiqiang Wang (Exeter) |
| **Code** | No public SPDX hit → policy |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: ADOPT — step-wise LLM pick from progress + remaining difficulty + cost, not one-shot cascade.**

Existing cascade routing makes **one-shot, query-level** decisions and cannot adapt to multi-step workflows, where the right LLM per step depends on evolving task progress, remaining difficulty, and cost-efficiency requirements.

PROGROUTER components:

- **Multi-view task progress scorer** — combines coarse workflow outcome regimes with fine-grained signals: subtask completion, progress trends, workflow state quality.
- **Dual-path task progress predictor** + **adaptive meta-gating** — estimate the progress gain for each candidate routed LLM.
- **Online step-wise routing** — balances progress gain, task time budgets, and long-term operating cost efficiency.

Evaluated on HumanEval Plus, MBPP, MATH-500, ASQA (agentic codegen, math, RAG long-form QA): reduces operating cost vs key baselines while maintaining task-solving performance.

Pairs `/route` quality-cost (`@entities/skills/route.md`). No public SPDX → `policy_wired`, no clone.

| Confidence | `[TENTATIVE]` — paper results as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "Cascade routing methods make one-shot, query-level decisions and cannot adapt to the dynamic, state-dependent nature of multi-step workflows." [Source: arXiv 2608.25992 abstract]

> "PROGROUTER … adaptively selects LLM agents across workflow steps to preserve task-solving quality while adhering to time and cost budgets." [Source: arXiv 2608.25992 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.25992-progrouter-online-progress-guided-orchestration.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
