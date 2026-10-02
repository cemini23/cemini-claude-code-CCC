---
title: "LLM-Driven Multi-Agent Control for Skill-Based Smart Manufacturing (CCC K417)"
type: source
tags: [source, arxiv, k417]
keywords: [2610.01364, k417]
related:
  - concepts/state-injection-over-history-reconstruction.md
  - briefs/2026-10-02_ccc-k416-k420-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-02
---

## Relations

- `@concepts/state-injection-over-history-reconstruction.md`
- `@briefs/2026-10-02_ccc-k416-k420-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LLM-Driven Multi-Agent Control for Skill-Based Smart Manufacturing |
| **arXiv** | 2610.01364 (2026-10) |
| **Retrieved** | 2026-10-02 |

## Narrative

**Verdict: REFERENCE (cross-domain; 3 primitives transfer).**

**Siemens — inject the state, do not make the agent reconstruct it.** A six-module simulated factory where **each module gets its own LLM agent and its own MCP tool server** wrapping that module's OPC UA skills; agents coordinate over **MQTT**. Three architectures are compared head-to-head across nine production challenges: **orchestrator** (central agent, global view), **peer-to-peer** (direct agent-to-agent), and **monolithic** (one agent, all modules). Monolithic and P2P tie at **93% mean solve rate**; the orchestrator scores 87% but **uniquely solves the silent conveyor-belt fault in all 10 runs** by rerouting around the blocked segment from its global view. The headline CCC finding is the **state-injection ablation**: prepending the current factory state as a structured context block raises solve rate **88% → 93%**, and without it the agent cannot distinguish a real hardware fault from state it inferred wrongly. Injection also lets the harness trim conversation history aggressively, because the state block is authoritative rather than reconstructed. Two more transferable mechanisms: **dynamic tool constraint** (a manager publishes only the *physically valid* tools before each call, so the model cannot attempt a rejected operation) and the finding that **92–98% of tokens are input** — the cost sits in state + history injection, not output. Fault diagnosis was **emergent**, with no explicit failure-handling logic written for it. Cross-domain (industrial), so REFERENCE — but the three primitives are pure harness design. Pairs K402 MCP error surfaces / K318 step routing / `@concepts/context-engineering.md` / K415 instance-adaptive harness. **No repo surfaced.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "This relieves LLMs from having to reconstruct the state themselves from the conversation history, with the added benefit of enabling aggressive token-conserving context-history trimming." [Source: arXiv 2610.01364 (retrieved 2026-10-02)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.01364-llm-driven-multi-agent-control-for-skill-based-s.pdf` |
