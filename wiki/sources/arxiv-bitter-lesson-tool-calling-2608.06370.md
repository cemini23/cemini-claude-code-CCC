---
title: "The Bitter Lesson of Tool Calling — PTC vs JSON"
type: source
tags: [source, arxiv, tool-calling, programmatic, bfcl, k258]
keywords: [2608.06370, PTC, BFCL, CodeAct, programmatic-tool-calling, PwC]
related:
  - concepts/programmatic-vs-json-tool-calling.md
  - entities/tools/programmatic-tool-calling-ptc.md
  - concepts/code-as-agent-harness.md
  - concepts/maven-agentic-tool-calling-generalization.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@concepts/programmatic-vs-json-tool-calling.md`
- `@entities/tools/programmatic-tool-calling-ptc.md`
- `@concepts/code-as-agent-harness.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Bitter Lesson of Tool Calling |
| **arXiv** | 2608.06370 |
| **Authors** | Ishan Patel, Sahil Sen, Elias Lumer, Vamse Kumar Subbiah (PwC CTIO) |
| **Repo** | None found at Phase-0 |
| **Retrieved** | 2026-08-07 |

## Narrative

Programmatic tool calling (typed Python stubs + single-turn `execute_python`) vs native JSON tool calling on BFCL v4 (309-entry subset, 14 models). PTC matches or exceeds JSON in **11/14** models; GPT-5.6 family +10.6pp; 13/14 under parallel fan-out; stable under context rot where JSON drops ~2.3pp avg. Performance tracks model capability across generations.

| Verdict | **ADOPT** PTC for code-capable models (pairs `@concepts/code-as-agent-harness.md`). **NO-GO** install (no public eval harness). Entity `policy_wired`. |

**Location (2026-08-07):** local `raw-sources/<file>` — egress-fi SCP timed out (banner exchange); re-archive when jump is up → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`.
