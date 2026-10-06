---
title: "MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents (CCC K429)"
type: source
tags: [source, arxiv, k429]
keywords: [2610.06830, k429]
related:
  - concepts/preference-aware-memory-orchestration.md
  - briefs/2026-10-06_ccc-k426-k430-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@concepts/preference-aware-memory-orchestration.md`
- `@briefs/2026-10-06_ccc-k426-k430-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents |
| **arXiv** | 2610.06830 (2026-10) |
| **Retrieved** | 2026-10-06 |

## Narrative

**Verdict: ADOPT pattern (no repo).**

**MemPilot — memory curation as a runtime decision under an explicit cost budget.** Most agent memory is built **query-agnostically**, before the next question is known: that pays preprocessing cost for evidence never used, and **discards details that later turn out to matter**. Prior runtime-adaptive work exists but is rigid — hand-designed operations, fixed pipelines, or discrete budget tiers — and almost always optimises **token or dollar cost while ignoring latency**, which users actually feel. MemPilot keeps **two views** (a query-agnostic memory bank for cheap access, plus the **raw multimodal history**) and learns a **multi-step policy** that decides four things per step: **how much evidence to process, what curation instruction to give, which model to delegate to** (heterogeneous LLMs and VLMs have different quality/cost/latency profiles), **and whether visual evidence is needed**. Two RL details make it trainable under competing objectives: **objective-wise advantage decoupling** (estimate each objective's advantage separately, then aggregate) and **prefix-based marginal utility estimation** for fine-grained credit assignment across multi-step rollouts. Result: **preference sweeps trace broader performance–cost–latency frontiers** than trade-off-aware baselines. **CCC relevance:** the framing is the useful part — **memory is not a storage question, it is a budgeting question**, and latency belongs in the objective alongside cost. Pairs `@concepts/token-economics-and-prompt-caching.md` / K387 KV working-set / K425 cost-aware evolution / `@concepts/storage-budgeted-agent-memory-compression.md` / K419 lossless memory (the opposite posture, and the two bracket the design space). **No repo surfaced** (project website only). Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential." [Source: arXiv 2610.06830 (retrieved 2026-10-06)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.06830-mempilot-orchestrating-on-demand-multimodal-memo.pdf` |
