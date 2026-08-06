---
title: Canary tools for MCP tool-selection diagnosis (K250)
type: concept
tags: [concept, mcp, canary, tool-selection, diagnostic, k250]
keywords: [2608.04719, Canary Tools, CSR, semantic-decoy, capability-mirage, parameter-trap]
related:
  - sources/arxiv-canary-tools-mcp-tool-selection-2608.04719.md
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

- `@sources/arxiv-canary-tools-mcp-tool-selection-2608.04719.md` — K250 provenance
- `@concepts/hybrid-gui-mcp-tool-adoption-gap.md` — adoption gap peer (K245)
- `@concepts/operator-model-selection.md` — tier≠safety; CSR varies by model

## Raw Concept

How do we diagnose whether an agent selects MCP tools by reasoning vs surface cues?

## Narrative

K250 Canary Tools (arXiv **2608.04719**): inject **diagnostic probe tools** into the MCP set; measure Canary Selection Rate (CSR) and correlate with downstream failure.

### Six-type taxonomy

| Type | Trap |
|------|------|
| Semantic decoys | Misleading tool names/descriptions |
| Parameter traps | Schema-valid but wrong args |
| Capability mirages | Tools that cannot do claimed task |
| Prerequisite blindness | Missing dependency tools |
| Temporal decoys | Wrong timing / stale state |
| Granularity traps | Wrong abstraction level |

### Key findings

- CSR varies ~**36×** across models
- **Tier ≠ safety** — frontier models fail capability mirages; small models fail other types
- Softening give-away phrases leaves frontier CSR unchanged → measures **reasoning**, not phrase-spotting
- Susceptibility predicts failure (ρ=−0.34)

### Cemini steal (ADOPT)

1. Use taxonomy when auditing MCP tool menus and lazy-tool discovery
2. Do not equate model tier with tool-selection safety (`@concepts/operator-model-selection.md`)
3. Complements adoption-gap measurement (`@concepts/hybrid-gui-mcp-tool-adoption-gap.md`)

| Verdict | **ADOPT** taxonomy for diagnosis. **NO-GO** install (no public artifact). Entity `policy_wired`. |
