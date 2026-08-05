---
title: Clarify-before-act and evidence-aligned close (K244)
type: concept
tags: [concept, orchestration, verification, urban, k244]
keywords: [2608.03018, UrbanAgent, clarify, evidence-aligned, execution-quality]
related:
  - sources/arxiv-urbanagent-cross-system-urban-tasks-2608.03018.md
  - entities/tools/urbanagent.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- `@sources/arxiv-urbanagent-cross-system-urban-tasks-2608.03018.md` — K244 provenance
- `@concepts/confidence-aware-tool-orchestration.md` — tiered evidence peer

## Raw Concept

What closed-loop discipline should tool-augmented agents follow before and after tool use?

## Narrative

K244 UrbanAgent (arXiv **2608.03018**): tool-augmented agent unifying code exec + API + MCP in one registry for cross-system urban tasks. Urban domain is OOD; the **adaptive closed loop** generalizes:

1. **Clarify before act** — resolve missing information before tool calls
2. **Ground in live observations** — tool use tied to current state, not parametric guess
3. **Evidence-aligned close** — final response must match observed evidence + task constraints

**Eval axes (Urban-Eval):** task success + execution quality — required tool coverage, dependency validity, evidence traceability. 71% task success (+10pp vs baseline); stable across GPT-5-mini, Gemini-2.5-flash, DeepSeek-V4-flash, Qwen3-235B-A22B.

### Cemini steal (ADOPT)

- Ask/clarify sub-step before irreversible or expensive tool chains
- Close with explicit evidence trace — what was observed vs assumed
- Score harness runs on execution quality, not completion text alone

| Verdict | **ADOPT** pattern. **NO-GO** UrbanAgent install (`wont_wire`). |
