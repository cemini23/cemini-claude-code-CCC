---
title: Embedded agent modular edge architecture
type: concept
tags: [concept, edge-agents, governance, k95]
keywords: [2606.02862, embedded-agents, governance-layer, on-device, cloud-augmented]
related:
  - sources/arxiv-embedded-agent-modular-edge-2606.02862.md
  - concepts/agent-sandbox-unikraft.md
  - concepts/tier1-tier2-agent-model.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@sources/arxiv-embedded-agent-modular-edge-2606.02862.md` — primary paper
- `@entities/patterns/tier1-tier2-agent-model.md` — policy enforcement analogue

## Raw Concept

K95 arXiv **2606.02862** — tiered embedded agents (MCU on-device vs edge SLM vs cloud) with a **governance layer** for observability, policy, and fleet safety. Out of scope for laptop Claude Code; governance pattern is steal-from.

## Narrative

| Paper tier | CCC analogue |
|------------|--------------|
| On-device agent | Tier-1 read-only subagents, sandboxed hooks |
| Cloud-augmented | Opus/Sonnet backend + local router (Cursor rules) |
| Governance layer | `skill-vetting`, defenseclaw admission, Tier-2 gates |

| Verdict | **REFERENCE** — no embedded deployment; extract governance-layer checklist for hook/MCP policy docs |

## Snippets

> "Governance Layer … observability, policy enforcement, and safety across distributed fleets."
> — [Source: arxiv-2606.02862-toward-a-modular-architecture-for-embedded-agent.pdf p.1]
