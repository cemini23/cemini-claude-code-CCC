---
title: "Canary Tools — diagnostic MCP tool-selection probes"
type: source
tags: [source, arxiv, mcp, canary, tool-selection, k250]
keywords: [2608.04719, Canary Tools, CSR, semantic-decoy, capability-mirage, diagnostic-probe]
related:
  - concepts/canary-tools-mcp-selection-diagnosis.md
  - entities/tools/canary-tools-mcp.md
  - concepts/hybrid-gui-mcp-tool-adoption-gap.md
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/operator-model-selection.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- `@concepts/canary-tools-mcp-selection-diagnosis.md`
- `@entities/tools/canary-tools-mcp.md`
- `@concepts/hybrid-gui-mcp-tool-adoption-gap.md`
- `@concepts/operator-model-selection.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Canary Tools |
| **arXiv** | 2608.04719 |
| **Repo** | None found (Phase-0) — paper says "we release the framework" |
| **Domain** | MCP tool-selection diagnosis |
| **Retrieved** | 2026-08-06 |

## Narrative

Diagnostic probe tools in MCP set; six-type taxonomy: semantic decoys, parameter traps, capability mirages, prerequisite blindness, temporal decoys, granularity traps.

CSR varies ~36× across models; tier≠safety; capability mirages trap frontier; others fire on small models. Softening give-away phrases leaves frontier CSR unchanged → measures reasoning not phrase-spotting. Susceptibility predicts failure (ρ=−0.34).

| Verdict | **ADOPT** canary-tool taxonomy for MCP tool-selection diagnosis. **NO-GO** install (no artifact). Entity `policy_wired` or thin policy entity. |
