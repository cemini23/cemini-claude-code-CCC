---
title: "One Step at a Time: Trading LLM Autonomy for Process Predictability (CCC K431)"
type: source
tags: [source, arxiv, k431]
keywords: [2610.07817, k431]
related:
  - concepts/step-level-process-delivery.md
  - briefs/2026-10-07_ccc-k431-k435-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- `@concepts/step-level-process-delivery.md`
- `@briefs/2026-10-07_ccc-k431-k435-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | One Step at a Time: Trading LLM Autonomy for Process Predictability |
| **arXiv** | 2610.07817 (2026-10) |
| **Retrieved** | 2026-10-07 |

## Narrative

**Verdict: ADOPT pattern.**

**One Step at a Time — deliver the procedure, do not describe it.** AWS + Bundeswehr. The setting is regulated operational work: an SOP goes into the system prompt, the agent runs autonomously, and a final answer comes back. Two failures follow, and the second is the dangerous one. First, **behaviour is unpredictable** — a lightweight executor produced on average **20 distinct tool-call sequences per domain** (up to 44 on one procedure), so no supervisor can anticipate the path. Second, and worse, **the model can hallucinate the process itself**: on a KYC-style domain, **31–49% of correct answers were produced without executing a single prescribed verification tool** — including **48% of a frontier model's**. Standard accuracy counts every one as a success. The fix is to externalise process control: an MCP server **releases one step at a time**, the agent executes it, returns a structured `step_output`, and the server advances. The agent's autonomy is scoped to the current step; **it cannot see ahead**. Across 15,475 trials / 13 domains / 4 executors: process adherence **76–95% → 95–99%**, ungrounded answers **2.1–4.5% → 0.2–0.3%**, and a new metric — **Grounded TSR**, accuracy *conditioned on* process adherence — exposes what plain accuracy hides. The accuracy effect is capability-dependent and honestly reported: the **lightweight executor gains +6.5 pp** grounded accuracy (externalising the process removes a reconstruction burden it cannot carry), while capable executors **trade −2.5 to −4.7 pp raw accuracy for full process visibility** and branching domains that need look-ahead lose outright. Also measured: a **token tax of 2.1–2.9× without prompt caching**, which the paper notes would substantially reduce. **CCC relevance:** three transferable ideas — **ground the metric in the process, not the outcome**; **scope autonomy to the step** as a deliberate trade; and **a per-step structured record is simultaneously an audit trail and an optimisation substrate** (it repaired an SOP defect in under a minute). Pairs `@concepts/agent-completion-verification-gates.md` / K428 CLIFT / `@concepts/verifiable-deterministic-agent-benchmarking.md` / K409 / `@concepts/token-economics-and-prompt-caching.md`. **No repo.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "31–49% of an LLM agent's correct answers—including 48% of a frontier model's—are produced without executing a single one of the prescribed verification tools." [Source: arXiv 2610.07817 (retrieved 2026-10-07)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.07817-one-step-at-a-time-trading-llm-autonomy-for-proc.pdf` |
