---
title: "Graph Engineering in the Era of LLM Agents — from individual intelligence to system intelligence"
type: source
tags: [source, arxiv, survey, graph-engineering, system-intelligence, orchestration, k301]
keywords: [2608.21156, graph engineering, system intelligence, prompt/context/harness/loop engineering, awesome list]
related:
  - concepts/graph-engineering-system-intelligence.md
  - concepts/subagent-orchestration.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@concepts/graph-engineering-system-intelligence.md`
- `@concepts/subagent-orchestration.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence |
| **arXiv** | 2608.21156 |
| **Authors** | Yuyuan Feng, Zhishang Xiang, Chaobin Yang, Qinggang Zhang, Yi Chang et al. (large consortium) |
| **Companion** | `DEEP-JLU/Awesome-Graph-Engineering` — **MIT** (gh API SPDX verified 2026-08-25) — **catalog, NO clone** (LESSONS 2026-05-13 catalog-churn pattern) |
| **Retrieved** | 2026-08-25 |

## Narrative

Survey positioning **Graph Engineering** as the next paradigm after the four this wiki already operates: Prompt Engineering → Context Engineering → Harness Engineering → Loop Engineering → **Graph Engineering**. The claim: individual-intelligence augmentation cannot fix architectural mismatch when tasks require heterogeneous expertise, interdependent subtasks, parallel execution, independent verification, and persistent state — intelligence must be organized at the system level over **explicit, evolving graphs** of tasks, agents, communication, and execution state (**System Intelligence**).

Cross-domain maturity finding: Work Organization and Agent Team Engineering are already common; explicit Runtime State Management (checkpoints, shared task boards, event streams, evidence stores) is emerging; uncertainty-aware graphs are rare.

CCC mapping: this vocabulary names what `/goal` + conductor + Task-fan-out already do informally. Adopt as **policy vocabulary** for describing multi-session orchestration; no runtime wire.

| Verdict | **ADOPT** vocabulary — Graph Engineering / System Intelligence as the layer after harness/loop engineering. Awesome-list **digest pointer only, no clone**. |
|---------|---------|

## Snippets

> "We refer to this capability as System Intelligence: the ability of an agent system to organize and coordinate multiple intelligent components into a coherent, adaptive whole that pursues a shared objective." [Source: arXiv 2608.21156 abstract]

> "Work Organization and Agent Team Engineering are already common … Explicit Runtime State Management is also becoming more visible through checkpoints … shared task boards, event streams, experimental evidence" [Source: arXiv 2608.21156 §9.7]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.21156-graph-engineering-in-the-era-of-llm-agents-from.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
