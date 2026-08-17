---
title: "AgentRewind — runtime recovery framework (Zhongguancun Academy / UCAS / Tsinghua)"
type: entity
tags: [entity, tool, agent-harness, checkpointing, recovery, mit, k282]
keywords: [k282, AgentRewind, replay-agent-recorder, MIT, aligned-checkpoints, rewind-memory]
related:
  - sources/arxiv-agentrewind-recoverable-execution-2608.14380.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - entities/tools/mettlebench.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-agentrewind-recoverable-execution-2608.14380.md`
- `@concepts/recoverable-agent-execution-checkpoints.md`
- `@entities/tools/mettlebench.md`

## Raw Concept

Phase-0 entity for CCC K282 — AgentRewind (runtime recovery layer).

## Narrative

Repo `github.com/Futuresis/replay-agent-recorder` — LICENSE **MIT** (verified on disk; `Copyright (c) 2026 Replay contributors`). ~3.7MB → cloned to `.local/adopts/replay-agent-recorder` as **GO REFERENCE**.

Steal: a runtime recovery layer between agent and environment that records aligned `(context, environment)` checkpoints, restores the selected checkpoint on rewind, and injects rewind memory. Framework-level; **`wont_wire`** into the CCC harness (no integration yet) — treat as REFERENCE pattern for recoverable execution.

**Phase-0:** `scripts/adopt_k282_phase0.sh`
