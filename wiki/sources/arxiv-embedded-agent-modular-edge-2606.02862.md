---
title: Modular embedded agent architecture — arXiv 2606.02862
type: source
tags: [source, arxiv, edge-agents, embedded, k95]
keywords: [2606.02862, embedded-agents, edge-ai, slm, governance-layer]
related:
  - concepts/embedded-agent-modular-edge-architecture.md
  - concepts/agent-sandbox-unikraft.md
maturity: draft
read_status: skimmed
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@concepts/embedded-agent-modular-edge-architecture.md` — CCC synthesis
- `@concepts/agent-sandbox-unikraft.md` — isolation tier reference

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Toward a Modular Architecture for Embedded Agent Systems at the Edge |
| **Author** | Marcus Rüb (Foresthub.Ai), Michael Gerhards (Deloitte) |
| **arXiv** | 2606.02862 |
| **Retrieved** | 2026-06-03 |
| **Read status** | skimmed |
| **Location** | `raw-sources/arxiv-2606.02862-toward-a-modular-architecture-for-embedded-agent.pdf` |

## Narrative

Reference architecture for **embedded agent systems** under MCU memory/energy constraints. Tiered design: on-device agents (TinyML, rule logic) vs cloud-augmented agents (SLM reasoning); cross-cutting **governance layer** for observability, policy, and fleet safety. Architectural trade-offs (latency, energy, reliability) — not Claude Code deployment, but governance-layer pattern is steal-from for Tier-2 agent policy hooks.

## Snippets

> "Integration of a cross-cutting Governance Layer, ensuring observability, policy enforcement, and safety across distributed fleets of autonomous devices."
> — [Source: arxiv-2606.02862-toward-a-modular-architecture-for-embedded-agent.pdf p.1]
