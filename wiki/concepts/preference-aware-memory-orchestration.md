---
title: "MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents (CCC K429)"
type: concept
tags: [concept, k429]
keywords: [2610.06830, k429]
related:
  - sources/arxiv-mempilot-preference-aware-memory-orchestration-2610.06830.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-06_ccc-k426-k430-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@sources/arxiv-mempilot-preference-aware-memory-orchestration-2610.06830.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-06_ccc-k426-k430-sip-ready.md`

## Raw Concept

K429: ADOPT pattern (no repo) — arXiv 2610.06830.

## Narrative

**MemPilot — memory curation as a runtime decision under an explicit cost budget.** Most agent memory is built **query-agnostically**, before the next question is known: that pays preprocessing cost for evidence never used, and **discards details that later turn out to matter**. Prior runtime-adaptive work exists but is rigid — hand-designed operations, fixed pipelines, or discrete budget tiers — and almost always optimises **token or dollar cost while ignoring latency**, which users actually feel. MemPilot keeps **two views** (a query-agnostic memory bank for cheap access, plus the **raw multimodal history**) and learns a **multi-step policy** that decides four things per step: **how much evidence to process, what curation instruction to give, which model to delegate to** (heterogeneous LLMs and VLMs have different quality/cost/latency profiles), **and whether visual evidence is needed**. Two RL details make it trainable under competing objectives: **objective-wise advantage decoupling** (estimate each objective's advantage separately, then aggregate) and **prefix-based marginal utility estimation** for fine-grained credit assignment across multi-step rollouts. Result: **preference sweeps trace broader performance–cost–latency frontiers** than trade-off-aware baselines. **CCC relevance:** the framing is the useful part — **memory is not a storage question, it is a budgeting question**, and latency belongs in the objective alongside cost. Pairs `@concepts/token-economics-and-prompt-caching.md` / K387 KV working-set / K425 cost-aware evolution / `@concepts/storage-budgeted-agent-memory-compression.md` / K419 lossless memory (the opposite posture, and the two bracket the design space). **No repo surfaced** (project website only). Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.06830 locators." [Source: CCC K429 synthesis]
