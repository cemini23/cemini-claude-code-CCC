---
title: "Scale-CDA — cooperative driving assistant via OpenDBC + MCP bridge"
type: source
tags: [source, arxiv, automotive, mcp, edge-llm, k249]
keywords: [2608.04235, Scale-CDA, OpenDBC, Openpilot, V2X, meta-action, edge-MLLM]
related:
  - concepts/edge-mcp-meta-action-executor-pattern.md
  - entities/tools/scale-cda.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- `@concepts/edge-mcp-meta-action-executor-pattern.md`
- `@entities/tools/scale-cda.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Scale-CDA |
| **arXiv** | 2608.04235 |
| **Repo** | None (Scale-CDA); cites commaai/opendbc, openpilot, openWakeWord only |
| **Domain** | Automotive cooperative driving — OOD for CCC |
| **Retrieved** | 2026-08-06 |

## Narrative

Open HW/SW CDA retrofit via OpenDBC + Openpilot; &lt;$1k parts; MQTT V2X; edge MLLM via **MCP bridge** → JSON advisories + **meta-action executors** into Openpilot planner hooks without altering safety-certified core. End-to-end &lt;60ms; on-board privacy.

| Verdict | **ADOPT** edge-MCP + meta-action executor pattern (GenAI proposes; verified executors enact; don't mutate safety core). **NO-GO** install / automotive stack. Entity `wont_wire`. |
