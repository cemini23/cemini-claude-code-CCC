---
title: Passive awareness — async multi-agent coordination
type: concept
tags: [concept, multi-agent, async, coding-agent, k232]
keywords: [AgentRadio, threads, wait-for-mentions, SWE-Atlas]
related:
  - sources/arxiv-agentradio-passive-awareness-multi-agent-2607.28430.md
  - entities/tools/agentradio.md
  - concepts/subagent-orchestration.md
  - concepts/event-sourced-poly-agent-handoff.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/handoff-validity-agent-harness.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- `@sources/arxiv-agentradio-passive-awareness-multi-agent-2607.28430.md`
- `@entities/tools/agentradio.md`
- `@concepts/subagent-orchestration.md`
- `@concepts/channel-fracture-cross-agent-memory-delivery.md`

## Raw Concept

How can parallel coding agents share mid-execution findings without stopping work for phase-boundary handoffs?

## Narrative

Phase-synced multi-agent systems make communication and work exclusive. **AgentRadio** adds harness primitives: threads, messages, **wait-for-mentions** as background — passive awareness. Empiric: 4 agents → 62.1% vs 32.3% single on SWE-Atlas QnA.

**Cemini steal:** Cursor Task/subagents + conductor-style fleets need a **non-blocking inbox**, not only staged handoffs. Pair with channel-fracture audits so "sent" ≠ "received."

**Verdict:** **ADOPT** async awareness pattern. **GO** Apache `.local/adopts/AgentRadio`.
