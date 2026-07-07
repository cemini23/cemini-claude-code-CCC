---
title: AReaL / AREAL2.0 — online RL bridge for LLM agent applications
type: entity
tags: [entity, tool, rl-infra, online-rl, self-evolving, ant-group, reference, k139]
keywords: [areal, areal2.0, rl bridge, online rl, apache-2.0, ant group, 2607.01120]
related:
  - concepts/agentic-online-rl-self-evolving-systems.md
  - sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - sources/brief-k139-agentic-online-rl-self-evolving-2026-07-07.md
maturity: draft
created: 2026-07-07
updated: 2026-07-07
phase_0_verdict: "REFERENCE/WATCH 2026-07-07 — Apache-2.0, 5.5k★, pushed 2026-07-07; enterprise online-RL infra; NO-GO laptop dependency"
---

## Relations

- `@concepts/agentic-online-rl-self-evolving-systems.md` — three-pillar architecture this tool instantiates
- `@sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md` — position paper + AREAL2.0

## Raw Concept

Phase-0 target from K139 ingest (arXiv 2607.01120). `github.com/areal-project/AReaL` — "The RL Bridge for LLM-based Agent Applications."

## Narrative

### Phase-0 (2026-07-07)

| Check | Result |
|-------|--------|
| License | **Apache-2.0** (`gh api` SPDX) |
| Maturity | **5.5k★**; pushed 2026-07-07 (active) |
| Class | Enterprise **online RL** training/serving infra |
| Failure mode | Requires RL training stack + GPU fleet — not a laptop harness tool |

### CCC posture

| Verdict | **REFERENCE / WATCH** |
|---------|------------------------|
| Install | **NO-GO** on laptop — CCC runs no LoRA/RL locally |
| Steal-from | ATDP (step-granular trajectory logging), evolution-control-plane triggering discipline |
| Prod | Server-side agent-evolution reference if Cemini ever runs weight-side loops on `cemini-prod` |

Distinct from harness-only self-improvement (`@concepts/continual-harness-online-self-improvement.md`) — AReaL is the **weight-update** infrastructure the CCC stance deliberately defers.

## Snippets

> "The RL Bridge for LLM-based Agent Applications. Made Simple & Flexible."
> — [Source: github.com/areal-project/AReaL description, retrieved 2026-07-07]
