---
title: SimpleAgenticScenario — TUM ABPM light-sensing reference repo
type: entity
tags: [entity, tool, reference, abpm, k136]
keywords: [simple-agentic-scenario, johanneslbck, mcp, light-sensing, oo1-oo4]
related:
  - sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md
  - concepts/agentic-orchestration-options-abpm.md
  - concepts/orchestration-option-quantitative-metrics.md
  - sources/brief-k136-agentic-orchestration-options-abpm-2026-07-01.md
maturity: draft
created: 2026-07-01
updated: 2026-07-01
---

## Relations

- `@sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md` — paper cites this repo for OO1–OO4 implementations
- `@concepts/agentic-orchestration-options-abpm.md` — orchestration option taxonomy

## Raw Concept

Reference implementation for arXiv 2606.31518 light-sensing cyber-physical scenario — REST sensors/lamp + MCP-connected LLM agents + cpee.org process orchestration variants.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/JohannesLbck/SimpleAgenticScenario |
| **License** | **None** (no LICENSE file) [CONFIRMED gh api 2026-07-01] |
| **Stars** | 0 |
| **Last push** | 2026-06-05 |
| **Verdict** | **REFERENCE** — study OO1–OO4 wiring patterns; **NO-GO** prod install or fork without license |

Implements predictive light sensing with lux rules (Tab. 2), MCP tool bridge to REST endpoints, and cpee.org models for OO3/OO4/OO5/OO6. Tested LLMs include Ministral, Gemma, Qwen variants.

**CCC steal:** MCP-over-REST layering pattern and metric scripts — do not deploy IoT stack on cemini-prod.

## Dead Ends

- **2026-07-01 Phase-0:** `gh api` reports `license: null` — cannot Adopt per `@osint-wiki/LESSONS.md` no-LICENSE pattern.
