---
title: "Agent Trajectory Sentinel — telemetry + deterministic verify"
type: entity
tags: [entity, tool, telemetry, monitoring, repair, k242]
keywords: [2608.02464, sunnydubey1111, ESN, CUSUM, MIT]
related:
  - sources/arxiv-agent-trajectory-sentinel-2608.02464.md
  - concepts/telemetry-deterministic-agent-failure-repair.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/self-healing-agent-sessions.md
  - concepts/agent-completion-verification-gates.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- `@sources/arxiv-agent-trajectory-sentinel-2608.02464.md`
- `@concepts/telemetry-deterministic-agent-failure-repair.md`

## Raw Concept

Phase-0 entity for K242 Agent Trajectory Sentinel — MIT telemetry + deterministic verification + rollback repair.

## Narrative

| Artifact | License | Size | Verdict |
|----------|---------|------|---------|
| `sunnydubey1111/agent-trajectory-sentinel` | MIT | ~108MB disk / 32MB GH | **GO** REFERENCE |

Local: `.local/adopts/agent-trajectory-sentinel`

**Phase-0:** `scripts/adopt_k242_phase0.sh`

## Phase-1

Telemetry + deterministic verify + rollback repair → `policy_wired` in `cemini-phase1-policy-wires.mdc` (parent update). Not default runtime MCP.
