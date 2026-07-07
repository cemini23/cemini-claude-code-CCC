---
title: Model-native vs tool-mediated fulfillment — a harness design axis
type: concept
tags: [concept, harness, action-protocol, mcp, model-native, tool-mediated, k141]
keywords: [model-native, tool-mediated, action protocol, lossy handoff, serving harness, shopx, 2606.31693]
related:
  - sources/arxiv-shopx-intent-to-item-fulfillment-2606.31693.md
  - concepts/code-as-agent-harness.md
  - concepts/mcp-context-optimization.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - entities/tools/lazy-tool.md
maturity: draft
created: 2026-07-07
updated: 2026-07-07
---

## Relations

- `@sources/arxiv-shopx-intent-to-item-fulfillment-2606.31693.md` — K141 provenance (ShopX)
- `@concepts/code-as-agent-harness.md` — where the action-protocol layer lives
- `@concepts/mcp-context-optimization.md` — tool-mediated side (MCP tool surface cost)

## Raw Concept

K141 arXiv **2606.31693** (ShopX) contrasts **model-native** execution (action space baked into the model) with **tool-mediated** orchestration (LLM routes intent through external search/rec/MCP tools). Domain is e-commerce; the design axis is general.

## Narrative

### The axis

| Approach | Mechanism | Cost |
|----------|-----------|------|
| **Tool-mediated** | LLM ↔ MCP/tool interfaces; each hop serializes intent through a narrow API | Lossy hand-offs; context saturation (`@concepts/mcp-context-optimization.md`) |
| **Model-native** | Action space + execution primitives inside the model via an action protocol | Fewer hand-offs; but requires training the action space in — no drop-in for closed models |

### CCC read [TENTATIVE]

CCC is almost entirely **tool-mediated** (Claude Code + MCP + skills) — correct for a general laptop harness where the action space is open-ended and models are closed-weight. ShopX's lesson is **not** "go model-native"; it is: **each tool hop is a lossy interface**, so minimize hops on hot paths. Practical CCC translations:

1. **Collapse hot-path tool chains** — prefer one capable tool over a chain of narrow ones where possible.
2. **Bounded projections over raw dumps** — same as substrate-constraints' docs CLI (`@concepts/substrate-constraints-coding-agent-oversight.md`): give the model a tight action surface, not a firehose.
3. **Action protocol clarity** — a well-specified model-facing action protocol beats ad-hoc tool sprawl (lazy-tool discovery is the tool-mediated mitigation).

| Verdict | **REFERENCE** — design-axis vocabulary; CCC stays tool-mediated, minimizes hops |

## Snippets

> "This model-centric design reduces lossy hand-offs between agent orchestration and item-space execution."
> — [Source: arxiv-2606.31693 abstract, retrieved 2026-07-07]
