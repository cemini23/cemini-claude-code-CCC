---
title: "Screenshots or Tools? — hybrid GUI–MCP adoption gap"
type: source
tags: [source, arxiv, gui, mcp, osworld, k245]
keywords: [2608.03327, OSWorld-MCP, tool-adoption-gap, screenshot, reasoning-model]
related:
  - concepts/hybrid-gui-mcp-tool-adoption-gap.md
  - entities/tools/hybrid-gui-mcp-osworld.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/operator-model-selection.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- `@concepts/hybrid-gui-mcp-tool-adoption-gap.md`
- `@entities/tools/hybrid-gui-mcp-osworld.md`
- `@concepts/model-native-vs-tool-mediated-fulfillment.md`
- `@concepts/mcp-context-optimization.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Screenshots or Tools? Hybrid GUI–MCP |
| **arXiv** | 2608.03327 |
| **Benchmark** | OSWorld-MCP — 309 tasks, 5 runs |
| **Repo** | None found (Phase-0) |
| **Retrieved** | 2026-08-05 |

## Narrative

Identical GUI–MCP harness on OSWorld-MCP (309 tasks, 5 runs). Same MCP tools:

- **Reasoning model:** +4.0pp (both >2 SE)
- **Non-reasoning model:** −5.9pp (both >2 SE)

Non-reasoning models ignore, misname, or false-terminate around tools. Reasoning model still calls a tool on only 55/309 tasks (23.9% of tool-reachable) — **adoption gap**. On VLC 16/17 tool-reachable tasks, never calls one.

**Cause:** cheaper screenshot route exists; model never trained to take the tool path.

Dense tool-bonus RL: spreadsheet adoption 0.03→0.33, carries to greedy; **held-out accuracy does not follow**. Behavior steerable; competence not. Bottleneck is tool-call semantics.

**Context optimization:** successful tool call often makes next screenshot redundant. Drop it + halve image history ≈ −1/3 input tokens, small accuracy cost. Retrain under same observation rule → **37.8% vs 33.0% uncompressed at 53% input cost**; rich–lean gap → 0 on pre-registered degraded subset.

| Verdict | **ADOPT** (1) do not assume MCP helps — sign depends on reasoning vs instruction model (2) measure adoption gap not just tool presence (3) drop redundant post-tool screenshots only when train/infer observation rule matches. **NO-GO** install. Entity `policy_wired`. |
