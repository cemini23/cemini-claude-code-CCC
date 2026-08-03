---
title: "CyberNeuro — privacy-preserving neuroimaging workbench"
type: entity
tags: [entity, tool, mcp, multi-agent, neuroimaging, k234]
keywords: [CyberNeuro, WandaMind, wanda-cyberbench, NeuroClaw baseline]
related:
  - sources/arxiv-cyberneuro-privacy-agentic-neuroimaging-2607.28841.md
  - concepts/local-first-mcp-multi-agent-workbench.md
  - sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md
  - briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc — local-first MCP + skill-DAG + HITL pattern (policy only)"
created: 2026-08-03
updated: 2026-08-03
---

## Relations

- `@sources/arxiv-cyberneuro-privacy-agentic-neuroimaging-2607.28841.md`
- `@concepts/local-first-mcp-multi-agent-workbench.md`

## Raw Concept

Phase-0 entity for K234 CyberNeuro — local-first MCP multi-agent neuroimaging workbench (no public code).

## Narrative

| Artifact | Availability | Verdict |
|----------|--------------|---------|
| wanda-cyberbench.com | HTTP 401 (gated) | **NO-GO** install |
| Wanda core `MEKOMIKU/cc-haha` | 404 | **NO-GO** |
| NeuroClaw `CUHK-AIM-Group/NeuroClaw` | MIT ~60MB | **REFERENCE** baseline only — **not cloned** |

Neuroimaging domain is OOD for Cemini ops. Adopt **patterns only** (local-first MCP, skill-DAG, HITL panel).

**Phase-0:** `scripts/adopt_k234_phase0.sh`

## Phase-1

`wont_wire` runtime — policy pattern note in `cemini-phase1-policy-wires.mdc` (parent update).
