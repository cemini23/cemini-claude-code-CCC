---
title: "Graph Engineering / System Intelligence — the layer after harness and loop engineering"
type: concept
tags: [concept, orchestration, graphs, system-intelligence, survey, k301]
keywords: [graph engineering, system intelligence, work organization, agent team, runtime state, 2608.21156]
related:
  - sources/arxiv-graph-engineering-llm-agents-2608.21156.md
  - concepts/subagent-orchestration.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-graph-engineering-llm-agents-2608.21156.md`
- `@concepts/subagent-orchestration.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Question answered: what comes after Prompt → Context → Harness → Loop Engineering when tasks exceed any single agent's organizational capacity? Source: arXiv 2608.21156 (CCC K301).

## Narrative

**Graph Engineering** = deliberately designing the **explicit, evolving graph** over which agent work flows — nodes are tasks/agents/state stores, edges are dependencies/communication/verification handoffs — instead of letting structure emerge implicitly from prompts. **System Intelligence** is the capability that results.

Three sub-areas with uneven maturity (survey §9.7): Work Organization and Agent Team Engineering (common), explicit Runtime State Management (emerging: checkpoints, shared boards, event streams, evidence stores), uncertainty-aware graph analysis (rare).

CCC mapping: `/goal` plans, conductor fan-outs, Task-tool Tier-1/Tier-2 splits, and `hot.md` session state are all informal instances. Adopted as **policy vocabulary** for describing and reviewing multi-session orchestration — name the graph explicitly when a workflow spans >1 session or >2 agents. Companion catalog `DEEP-JLU/Awesome-Graph-Engineering` (MIT) is a digest pointer only; **no clone** (catalog-churn rule).

## Snippets

> "Achieving System Intelligence … requires explicit structures for organizing work, coordinating heterogeneous agents, and maintaining evolving execution states." [Source: arXiv 2608.21156 abstract]
