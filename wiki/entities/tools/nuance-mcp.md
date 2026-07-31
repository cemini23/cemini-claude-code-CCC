---
title: nuance-mcp — schema-bound instrument MCP skills (MIT)
type: entity
tags: [tool, mcp, schema, skills, mit, k198]
keywords: [NUANCE-IT/nuance-mcp, schema-bound, live-job, microscopy]
related:
  - sources/arxiv-schema-bound-mcp-instrument-skills-2607.17012.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
maturity: draft
created: 2026-07-21
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-ccc-harness.mdc"
---

## Relations

- `@sources/arxiv-schema-bound-mcp-instrument-skills-2607.17012.md` — paper
- `@concepts/schema-bound-mcp-tool-surface.md` — pattern
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — validation peer

## Raw Concept

`github.com/NUANCE-IT/nuance-mcp` — MIT reference for schema-bound MCP + skills. Local: `.local/adopts/nuance-mcp` (~1.2MB).

## Narrative

### Phase-0

| Check | Result |
|-------|--------|
| License | **MIT** [CONFIRMED] |
| Size | ~1.2MB depth-1 — OK |
| Domain | Scientific instruments / simulator — pattern steal, not prod wiring |
| Failure mode | Instrument control blast radius — never point at LIVE TipDrop/trading without separate adopt |

### Verdict

**GO** local REFERENCE clone. **ADOPT** schema-bound + MCP-prompt skills pattern. Do not wire into Cemini prod MCP allowlist without operator ticket.
