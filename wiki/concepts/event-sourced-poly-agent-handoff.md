---
title: Event-sourced poly-agent handoff
type: concept
tags: [concept, event-sourcing, handoff, memory, k125]
keywords: [2606.23752, esaa, event-log, curation, poly-agent]
related:
  - sources/arxiv-esaa-conversational-event-sourced-2606.23752.md
  - sources/brief-k125-memory-orchestration-cluster-2026-06-25.md
  - entities/tools/esaa-conversational.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/handoff-validity-agent-harness.md
  - entities/patterns/cpr-context-compression.md
  - entities/tools/claude-mem.md
  - concepts/subagent-orchestration.md
  - concepts/agent-memory-stack-comparison.md
  - sources/brief-k125-memory-orchestration-cluster-2026-06-25.md
  - sources/brief-k125-esaa-windows-handoff-2026-06-25.md
  - concepts/passive-awareness-async-multi-agent-coordination.md
  - sources/arxiv-agentradio-passive-awareness-multi-agent-2607.28430.md
maturity: draft
created: 2026-06-25
updated: 2026-07-31
---

## Relations

- `@sources/arxiv-esaa-conversational-event-sourced-2606.23752.md` — ESAA-Conversational paper
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — push-vs-pull contrast
- `@concepts/handoff-validity-agent-harness.md` — receiver validation

## Raw Concept

Question: how should heterogeneous agents hand off conversational state without silent memory loss or uncurated context bloat?

## Narrative

**Event-sourced poly-agent handoff** [TENTATIVE — ESAA 2606.23752]: append-only **event log** of turns, tool results, and handoff intents; receivers **replay + project** curated views instead of accepting blind pushes. Handoff envelopes carry provenance for validation before merge.

**Steal-from for Cemini harness:**

1. **Receiver-validated handoff** — Task subagent returns structured envelope; parent verifies read-back before continuing (extends channel-fracture inverse verification).
2. **Curation before compact** — CPR compress leg selects events to retain vs archive (pairs with SelfCompact rubric).
3. **Event log analogue** — `wiki/log.md` + claude-mem observation stream as append-only provenance (not full ESAA stack).

**Tool path:** ESAA-Conversational PowerShell CLI — **CONDITIONAL-GO** Windows laptop smoke only.

## Snippets

> Continuity, handoff, and curation across heterogeneous poly-agent systems via event-sourced memory.
> — [Source: arxiv-2606.23752-esaa-conversational-an-event-sourced-memory-laye.pdf, retrieved 2026-06-25]
