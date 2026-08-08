---
title: "CASCADE — LangGraph MCP gene-perturbation server"
type: entity
tags: [entity, tool, mcp, langgraph, bioinformatics, k259]
keywords: [2608.05359, jab57/CASCADE, MIT, wont_wire, OOD]
related:
  - sources/arxiv-cascade-agentic-regulatory-network-2608.05359.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/brief-k259-cascade-mcp-claim-validation-2026-08-08.md
  - briefs/2026-08-08_ccc-handoff-k259-cascade-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-08
updated: 2026-08-08
---

## Relations

- `@sources/arxiv-cascade-agentic-regulatory-network-2608.05359.md`
- `@concepts/mcp-claim-validation-and-parameter-grounding.md`

## Raw Concept

Phase-0 entity for K259 CASCADE MCP server (cancer regulatory networks).

## Narrative

| Artifact | Repo | Size | Verdict |
|----------|------|------|---------|
| CASCADE | `jab57/CASCADE` MIT | ~352MB shallow (no DepMap/model) | **GO** REFERENCE `.local/adopts/CASCADE` |

Cancer genomics **OOD** — do not add to prod/Cursor MCP allowlist. Optional DepMap CSV ~413MB and model ~120MB **not** downloaded (stay under 500MB adopt budget).

**Phase-0:** `scripts/adopt_k259_phase0.sh`

## Phase-1

`wont_wire` runtime. Steal patterns → `@concepts/mcp-claim-validation-and-parameter-grounding.md` (`policy_wired`).
