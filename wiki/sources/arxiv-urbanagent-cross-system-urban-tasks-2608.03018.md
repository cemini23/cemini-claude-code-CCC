---
title: "UrbanAgent — cross-system urban tasks with unified tool registry"
type: source
tags: [source, arxiv, urban, mcp, tool-augmented, k244]
keywords: [2608.03018, UrbanAgent, Urban-Eval, clarify-before-act, execution-quality]
related:
  - concepts/clarify-before-act-evidence-aligned-close.md
  - entities/tools/urbanagent.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- `@concepts/clarify-before-act-evidence-aligned-close.md`
- `@entities/tools/urbanagent.md`
- `@concepts/confidence-aware-tool-orchestration.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | UrbanAgent |
| **arXiv** | 2608.03018 |
| **Repo** | None found (Phase-0) |
| **Domain** | Urban cross-system tasks — OOD for CCC |
| **Retrieved** | 2026-08-05 |

## Narrative

Tool-augmented agent for cross-system urban tasks: code execution + API + MCP in one registry.

**Adaptive closed loop:**

1. Clarify missing information before acting
2. Ground tool use in live observations
3. Align final response with observed evidence + task constraints

**Urban-Eval benchmark** axes: task success + execution quality (required tool coverage, dependency validity, evidence traceability).

**Results:** 71% task success, +10pp vs strongest baseline; holds across GPT-5-mini, Gemini-2.5-flash, DeepSeek-V4-flash, Qwen3-235B-A22B.

| Verdict | **ADOPT** clarify-before-act + evidence-aligned close + execution-quality eval axes. **NO-GO** install. Entity `wont_wire`. |
