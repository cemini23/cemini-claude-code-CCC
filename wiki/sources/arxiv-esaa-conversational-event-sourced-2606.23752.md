---
title: ESAA-Conversational — event-sourced poly-agent handoff (arXiv 2606.23752)
type: source
tags: [source, arxiv, event-sourcing, handoff, memory, k125]
keywords: [2606.23752, esaa, powershell, poly-agent, curation]
related:
  - concepts/event-sourced-poly-agent-handoff.md
  - entities/tools/esaa-conversational.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/handoff-validity-agent-harness.md
  - entities/patterns/cpr-context-compression.md
  - entities/tools/claude-mem.md
  - concepts/subagent-orchestration.md
  - concepts/agent-memory-stack-comparison.md
  - sources/brief-k125-memory-orchestration-cluster-2026-06-25.md
  - sources/brief-k125-esaa-windows-handoff-2026-06-25.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-30
---

## Relations

- `@concepts/event-sourced-poly-agent-handoff.md` — synthesis
- `@entities/tools/esaa-conversational.md` — PowerShell CLI entity
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — inverse verification contrast

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous Poly-Agent Systems |
| **Authors** | ESAA project (extends arXiv 2606.08156 core) |
| **arXiv** | 2606.23752 (v1.1.0 package) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2606.23752-esaa-conversational-an-event-sourced-memory-laye.pdf` |
| **Retrieved** | 2026-06-25 |
| **Read status** | read (event log, handoff envelopes, curation CLI) |

## Narrative

**ESAA-Conversational v1.1.0** ships a **PowerShell-first** CLI where conversational turns, tool outcomes, and handoff intents append to an immutable event log. Poly-agent continuity = replay + curated projections (not silent cross-agent push). Handoff packets carry provenance so receiver agents validate before merge.

**CCC steal-from:** event-sourced handoff beats cron-delegated memory push (cf. channel fracture); maps to `hot.md` checkpoints, claude-mem observation streams, Task subagent return envelopes. **CONDITIONAL-GO** laptop — Windows/PowerShell only; no macOS prod path without port.

## Snippets

> Event-sourced memory layer for continuity, handoff, and curation across heterogeneous poly-agent systems.
> — [Source: arxiv-2606.23752-esaa-conversational-an-event-sourced-memory-laye.pdf abstract, retrieved 2026-06-25]
