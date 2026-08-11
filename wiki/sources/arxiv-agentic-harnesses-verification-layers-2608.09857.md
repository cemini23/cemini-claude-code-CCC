---
title: "Agentic Harnesses — LLM verification layers for robot autonomy"
type: source
tags: [source, arxiv, verification, harness, robotics, k264]
keywords: [2608.09857, verification-layer, LLM-as-judge, accept-escalate-reject, PNNL]
related:
  - concepts/llm-verification-layer-accept-escalate-reject.md
  - entities/tools/verification-layers-robot.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - entities/tools/agent-trajectory-sentinel.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
---

## Relations

- `@concepts/llm-verification-layer-accept-escalate-reject.md`
- `@entities/tools/verification-layers-robot.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agentic Harnesses: LLM-Driven Verification Layers for Robot Autonomy |
| **arXiv** | 2608.09857 |
| **Authors** | Bhagra, Halapannavar, Bhattarai (PNNL) |
| **Code** | Claimed `github.com/rohanbhagra/verification_layers` — **404** at Phase-0 |
| **Retrieved** | 2026-08-11 |

## Narrative

LLM-as-judge ensemble between planning and MCP/execution: **accept / reject / escalate**. Chief judge meta-evaluates judge reasoning (never sees plan). ~85% precision; 97% adversarial containment (paper). Robotics runtime OOD.

| Verdict | **ADOPT** accept/reject/escalate verification middleware. **NO-GO** code (404). |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.09857-agentic-harnesses-llm-driven-verification-layers.pdf`
