---
title: Hybrid GUI–MCP tool adoption gap (K245)
type: concept
tags: [concept, gui, mcp, adoption-gap, osworld, k245]
keywords: [2608.03327, OSWorld-MCP, screenshot, reasoning-model, tool-call-semantics]
related:
  - sources/arxiv-screenshots-or-tools-gui-mcp-2608.03327.md
  - entities/tools/hybrid-gui-mcp-osworld.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/operator-model-selection.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
  - sources/arxiv-canary-tools-mcp-tool-selection-2608.04719.md
  - concepts/canary-tools-mcp-selection-diagnosis.md
  - entities/tools/canary-tools-mcp.md
maturity: draft
created: 2026-08-05
updated: 2026-08-06
---

## Relations

- `@sources/arxiv-screenshots-or-tools-gui-mcp-2608.03327.md` — K245 provenance
- `@concepts/model-native-vs-tool-mediated-fulfillment.md` — screenshot vs tool path axis
- `@concepts/mcp-context-optimization.md` — post-tool screenshot drop
- `@concepts/operator-model-selection.md` — reasoning vs non-reasoning sign flip

## Raw Concept

When both screenshots and MCP tools are available in a GUI agent harness, do models actually use the tools — and does availability help?

## Narrative

K245 (arXiv **2608.03327**): identical GUI–MCP harness on OSWorld-MCP (309 tasks, 5 runs).

### MCP availability is not uniformly beneficial

| Model class | Δ vs screenshot-only |
|-------------|---------------------|
| Reasoning | +4.0pp (>2 SE) |
| Non-reasoning | −5.9pp (>2 SE) |

Non-reasoning models ignore, misname, or false-terminate around tools. **Do not assume MCP helps** — sign depends on model class.

### Adoption gap (presence ≠ use)

Reasoning model calls a tool on only **55/309** tool-reachable tasks (23.9%). VLC: 16/17 tool-reachable, **zero** tool calls. Cause: cheaper screenshot route exists; models not trained on tool path.

Dense tool-bonus RL raises spreadsheet adoption 0.03→0.33 (greedy carries) but **held-out accuracy does not follow** — behavior steerable, competence not; bottleneck is **tool-call semantics**.

### Observation-rule-matched context trim

Successful tool call often makes next screenshot redundant. Drop redundant post-tool screenshots + halve image history ≈ −1/3 input tokens, small accuracy cost. With matched train/infer observation rule: **37.8% vs 33.0%** uncompressed at **53%** input cost; rich–lean gap → 0 on pre-registered degraded subset.

### Cemini policy (ADOPT)

1. Measure **adoption gap**, not just tool presence in harness
2. Match model tier to expected MCP benefit (see `@concepts/operator-model-selection.md`)
3. Drop redundant post-tool screenshots **only** when train and inference observation rules align

| Verdict | **ADOPT** policy. **NO-GO** install. Entity `policy_wired`. |

### K250 — canary-tool diagnosis (2026-08-06)

K250 Canary Tools adds **diagnostic probe tools** and six-type taxonomy (semantic decoys, parameter traps, capability mirages, etc.) to measure CSR — complements adoption-gap measurement. Tier≠safety for tool selection. See `@concepts/canary-tools-mcp-selection-diagnosis.md`.
