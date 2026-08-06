---
title: "Scale-CDA — cooperative driving MCP retrofit"
type: entity
tags: [entity, tool, automotive, mcp, edge-llm, k249]
keywords: [2608.04235, Scale-CDA, wont_wire, OpenDBC, Openpilot]
related:
  - sources/arxiv-scale-cda-cooperative-driving-mcp-2608.04235.md
  - concepts/edge-mcp-meta-action-executor-pattern.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- `@sources/arxiv-scale-cda-cooperative-driving-mcp-2608.04235.md`
- `@concepts/edge-mcp-meta-action-executor-pattern.md`

## Raw Concept

Phase-0 entity for K249 Scale-CDA — automotive cooperative driving; no Scale-CDA public repo; automotive OOD.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| Scale-CDA paper | None (cites opendbc, openpilot, openWakeWord) | **NO-GO** install |

**Phase-0:** `scripts/adopt_k249_phase0.sh`

Steal edge-MCP + meta-action executor pattern only — GenAI proposes; verified executors enact; safety core unchanged.

## Phase-1

`wont_wire` — pattern in `@concepts/edge-mcp-meta-action-executor-pattern.md`.
