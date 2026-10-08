---
title: "Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming (CCC K437)"
type: source
tags: [source, arxiv, k437]
keywords: [2610.10184, k437]
related:
  - concepts/formulation-versus-implementation-gap.md
  - briefs/2026-10-08_ccc-k436-k440-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@concepts/formulation-versus-implementation-gap.md`
- `@briefs/2026-10-08_ccc-k436-k440-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming |
| **arXiv** | 2610.10184 (2026-10) |
| **Repo** | `DIR-LAB/pocket-agent` |
| **Retrieved** | 2026-10-08 |

## Narrative

**Verdict: ADOPT pattern.**

**Formulation is within reach; implementation is the barrier.** General-purpose LLMs orchestrated as agents, with **no task-specific training**, asked to turn natural-language scheduling problems into **constraint-programming** models. An MCP server supplies **context-aware retrieval of solver documentation** to cut hallucination during implementation. Six industry problems (flow-shop, job-shop, flexible job-shop, resource-constrained warehouse), three LLMs, scored on modelling accuracy, execution success, latency, and tokens. **The headline is the split:** the model can *formulate* the problem, and fails at *implementing* it. A multi-agent workflow raises the share of scripts that **run correctly as generated from 14.8% (direct LLM call) to 59.3%**, reaching **80.6% on the four less complex problems**, while tightly coupled intralogistics models remain open. **CCC reading:** this is the 'the plan was fine, the execution failed' shape that CCC keeps meeting, measured. It pairs with K431 (prompt-delivered SOPs where the *process* never ran) and K437's own finding that **an MCP server serving the right documentation is the mitigation** — retrieval grounded in the solver's actual reference, not model recall. Two transferable moves: **score formulation separately from runnability**, and **feed the tool's own docs through MCP rather than trusting the model to remember the API**. **Phase-0: `DIR-LAB/pocket-agent` MIT**, 5★, 5.2 MB, pushed 2026-02-20 — the agent framework used. No clone this wave. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "Formulation proves largely within reach of current LLMs, whereas implementation is the main barrier." [Source: arXiv 2610.10184 (retrieved 2026-10-08)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.10184-agentic-ai-assisted-modeling-for-production-sche.pdf` |
