---
title: "AgentRadio — passive awareness for long-horizon multi-agent collaboration"
type: source
tags: [source, arxiv, multi-agent, coding-agent, async, k232]
keywords: [2607.28430, AgentRadio, SWE-Atlas, threads, wait-for-mentions]
related:
  - concepts/passive-awareness-async-multi-agent-coordination.md
  - concepts/subagent-orchestration.md
  - concepts/event-sourced-poly-agent-handoff.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - entities/tools/agentradio.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- `@concepts/passive-awareness-async-multi-agent-coordination.md`
- `@entities/tools/agentradio.md`
- `@concepts/subagent-orchestration.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration |
| **Author** | Ren, Zang, Wang, Forder, Deb, Carroll, Guo (Coral AI Labs et al.) |
| **arXiv** | 2607.28430 |
| **Pages** | 9 |
| **Retrieved** | 2026-07-31 |
| **Code** | `Coral-Protocol/AgentRadio` Apache-2.0 (~13MB) — **GO** REFERENCE |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.28430-agentradio-passive-awareness-for-long-horizon-mu.pdf` |

## Narrative

Staged handoffs make communication and work mutually exclusive — mid-execution discoveries wait for the next boundary. AgentRadio: **threads / messages / wait-for-mentions** (background), so agents stay passively aware. 4× Claude Code + AgentRadio: **62.1%** SWE-Atlas QnA vs **32.3%** single Opus 4.6 (+29.8pp); beats single Opus 4.8 (57.2%). Gains grow with difficulty. **ADOPT** async awareness layer; **GO** Apache clone.
