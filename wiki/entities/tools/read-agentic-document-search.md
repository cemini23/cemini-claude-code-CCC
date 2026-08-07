---
title: "READ — embedding-free agentic document search"
type: entity
tags: [entity, tool, rag, mcp, k255]
keywords: [2608.06305, twospoon/READ, MIT, wont_wire]
related:
  - sources/arxiv-beyond-topk-read-agentic-retrieval-2608.06305.md
  - concepts/interpretable-agentic-document-ops.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-beyond-topk-read-agentic-retrieval-2608.06305.md`
- `@concepts/interpretable-agentic-document-ops.md`

## Raw Concept

Phase-0 entity for K255 READ MCP document tools.

## Narrative

| Artifact | Repo | Size | Verdict |
|----------|------|------|---------|
| READ | `twospoon/READ` MIT | ~8.4MB | **GO** REFERENCE `.local/adopts/READ` |

Runtime MCP **wont_wire** by default (study first; BM25 may suffice).

**Phase-0:** `scripts/adopt_k255_phase0.sh`

## Phase-1

`policy_wired` interface pattern; clone REFERENCE only.
