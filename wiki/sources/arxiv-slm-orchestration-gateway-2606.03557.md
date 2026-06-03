---
title: SLM agent orchestration gateway — arXiv 2606.03557
type: source
tags: [source, arxiv, agent-orchestration, slm, edge, k95]
keywords: [2606.03557, slm-router, intent-routing, service-registry, virtual-worlds]
related:
  - concepts/slm-agent-orchestration-gateway.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
maturity: draft
read_status: skimmed
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@concepts/slm-agent-orchestration-gateway.md` — CCC synthesis
- `@entities/tools/lazy-tool.md` — deferred tool discovery analogue
- `@entities/tools/conductor-mcp.md` — cross-backend routing analogue

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | From Prompt to Service: An SLM-Based Agent Orchestration Gateway for AI-Driven Virtual Worlds |
| **Author** | Louis Nisiotis, Aimilios Hadjiliasi (UCLan Cyprus) |
| **arXiv** | 2606.03557 |
| **Retrieved** | 2026-06-03 |
| **Read status** | skimmed |
| **Location** | `raw-sources/arxiv-2606.03557-from-prompt-to-service-an-slm-based-agent-orches.pdf` |

## Narrative

**SLM-based orchestration gateway** decouples a client from heterogeneous AI backends: edge SLM classifies prompt intent → service registry validates routing → backend invoked transparently. Evaluated in InterwovenXR virtual museum; sub-billion-parameter fine-tuned routers on mid-range edge hardware. Pattern maps to **lazy-tool / conductor intent routing** — thin router model + fat backend specialists without client changes.

## Snippets

> "Intent-driven service routing … enabling new AI capabilities … without modifying the client application."
> — [Source: arxiv-2606.03557-from-prompt-to-service-an-slm-based-agent-orches.pdf p.1]
