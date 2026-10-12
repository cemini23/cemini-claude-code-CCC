---
title: "NOMOS — compile the policy, verify it statically, gate the call (K288)"
type: concept
tags: [concept, k288, mcp, security]
keywords: [2610.11030, nomos, tool-call-gate, deterministic]
related:
  - concepts/streaming-trajectory-monitor-pre-execution-gate.md
  - concepts/llms-are-not-world-models.md
  - concepts/implicit-trust-mcp-input-channels.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-12_k286-k288-ccc-route.md
  - briefs/2026-10-12_ccc-k445-k448-sip-ready.md
  - concepts/typed-judgement-desk-pattern.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-12
updated: 2026-10-12
---

## Relations

- `@concepts/streaming-trajectory-monitor-pre-execution-gate.md`
- `@concepts/llms-are-not-world-models.md`
- `@concepts/implicit-trust-mcp-input-channels.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-12_k286-k288-ccc-route.md`

## Raw Concept

Routed inbound via `@osint-wiki` K286 / K288 (CCC-home desks), delivered in `briefs/`. Canon stays
on OSINT.

## Narrative

**Compile the policy once, verify it statically, enforce it in code — a deterministic, LLM-free tool-call gate.** NOMOS answers K285's 'guardrails are not the answer': a compiler turns a **written agent policy** into a **runtime gate with no LLM** in four passes — PARSE → EXTRACT (the *only* LLM pass; N=5 majority vote) → **RESOLVE** (deterministic static checks: self-blocking reachability, argument–signature consistency, domain satisfiability, state contradictions, write-scope correctness) → MATERIALIZE. The runtime gate evaluates each proposed tool call against **facts taken only from real tool results and user turns** and returns allow/block in **microseconds with zero LLM**. **Results:** violations among state-changing calls **66.3% → 2.6%** (airline) and **30.8% → 6.9%** (retail); **AgentDojo banking ASR 0.0%** (288 pairs) vs **46.5%** undefended; pass^5/pass^1 **0.51 → 0.67**. A prompt-level reimplementation costs **+74% wall-clock and 347 LLM calls** vs **3 µs and zero**. **The caution that matters:** RESOLVE **repairs 37% and rejects 13%** of extracted rules — **generated policy is wrong about a third of the time**, so **policy extraction must be statically verified, never trusted**: *an LLM-written policy is an input to a checker, not a control*. **CCC reading:** this is the mechanism-level twin of K444's **L3 pre-execution gate** — the same shape (block an irreversible call whose prerequisites are missing), but NOMOS is the *compiler* that turns prose policy into that gate and the *static verifier* that makes it trustworthy. Pairs `streaming-trajectory-monitor-pre-execution-gate` (K444) / `llms-are-not-world-models` (K285) / `implicit-trust-mcp-input-channels`. Cross-wiki: cybersec-primary. **Implementation proprietary, not released** (DOI `10.5281/zenodo.22123419`). Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "An LLM-written policy is an input to a checker, not a control." [Source: OSINT K286/K288 briefs (retrieved 2026-10-12)]
