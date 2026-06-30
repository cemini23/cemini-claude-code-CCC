---
title: ESAA-Conversational
type: entity
tags: [entity, tool, memory, handoff, powershell, k125]
keywords: [2606.23752, esaa, event-sourced, poly-agent]
related:
  - sources/arxiv-esaa-conversational-event-sourced-2606.23752.md
  - concepts/event-sourced-poly-agent-handoff.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/handoff-validity-agent-harness.md
  - entities/tools/claude-mem.md
  - sources/brief-k125-esaa-windows-handoff-2026-06-25.md
maturity: draft
created: 2026-06-25
updated: 2026-06-30
---

## Relations

- `@sources/arxiv-esaa-conversational-event-sourced-2606.23752.md`
- `@concepts/event-sourced-poly-agent-handoff.md`

## Raw Concept

ESAA-Conversational v1.1.0 — PowerShell CLI package for event-sourced conversational memory, handoff envelopes, and curation across poly-agent setups. Prompted by K125 ingest (2606.23752).

## Narrative

| Field | Value |
|-------|-------|
| **Platform** | Windows PowerShell (primary) |
| **License** | Not verified — no public GitHub at Phase-0 |
| **Verdict** | **CONDITIONAL-GO** — laptop Windows smoke only; macOS NO-GO until port |
| **Overlap** | claude-mem (passive observation), channel-fracture mitigations (receiver pull) |

**Phase-0:** `scripts/adopt_k125_phase0.sh` — no clone; paper + package reference only.

**Steal-from:** event log + handoff envelope schema for Task subagent returns and CPR curation rubric.

## Dead Ends

- Public GitHub repo not found at ingest — do not assume install path until author publishes.

## Snippets

> v1.1.0 PowerShell CLI for event-sourced memory, handoff, and curation.
> — [Source: arxiv-2606.23752-esaa-conversational-an-event-sourced-memory-laye.pdf, retrieved 2026-06-25]
