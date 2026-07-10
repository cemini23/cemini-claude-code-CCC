---
title: Algorithmic impermeability — model-agnostic orchestration decoupled from inference
type: concept
tags: [concept, orchestration, model-agnostic, harness, handoff, k150]
keywords: [algorithmic impermeability, SIP, standardized intermediate payload, SDR, model swap, routing independence, 2607.06531, LCA]
related:
  - sources/arxiv-large-cancer-assistant-lca-2607.06531.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/code-as-agent-harness.md
  - concepts/subagent-orchestration.md
  - concepts/agentic-orchestration-options-abpm.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/etclovg-harness-layers.md
  - sources/brief-k150-algorithmic-impermeability-orchestration-2026-07-09.md
  - sources/arxiv-bioinsight-multi-agent-biomedical-2606.20997.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
maturity: draft
created: 2026-07-09
updated: 2026-07-10
---

## Relations

- `@sources/arxiv-large-cancer-assistant-lca-2607.06531.md` — K150 provenance (clinical PoC; harness steal)
- `@concepts/handoff-validity-agent-harness.md` — SIP as typed handoff contract
- `@concepts/multi-agent-evidence-artifact-layers.md` — evidence/synthesis/interface layers map to SIP boundary

## Raw Concept

K150 arXiv **2607.06531** (LCA, clinical oncology): **Algorithmic Impermeability** — orchestration/routing logic must remain **strictly independent** of underlying AI models so models can be swapped without re-wiring the pipeline.

## Narrative

### Three harness patterns [TENTATIVE]

| Pattern | Definition | CCC analogue |
|---------|------------|----------------|
| **Algorithmic impermeability** | Routing/orchestration logic cannot depend on model internals | Model swap without rewriting conductor routes, MCP tool lists, or subagent prompts |
| **SIP** (Standardized Intermediate Payload) | Typed boundary payload between orchestration and downstream volatile systems | OpenSpec AC artifacts, wiki ingest matrices, canvas data contracts — stable shape across model changes |
| **SDR** (Supplementary Data Requests) | On missing input, emit **targeted request** not silent failure | `/goal` missing-criteria prompts; HarnessFix "what context was absent?" |

### vs related concepts

- **Model-native** (`@concepts/model-native-vs-tool-mediated-fulfillment.md`) — action space inside model; LCA is the **opposite pole**: orchestration outside model.
- **Client-first-order** (`@concepts/client-as-first-order-harness-factor.md`) — client/harness dominates capability; impermeability says **routing must not entangle with model**.
- **Online-RL evolution** (`@concepts/agentic-online-rl-self-evolving-systems.md`) — control plane chooses weight vs harness update; impermeability keeps **harness routing invariant** across weight swaps.

### CCC steals

1. **Swap models without re-routing** — conductor queries, lazy-tool catalog, subagent templates stay stable when API model slug changes.
2. **SIP at handoff boundaries** — subagent returns typed brief (path + verdict table), not raw tool dumps; pairs with `@concepts/handoff-validity-agent-harness.md`.
3. **SDR not hallucinate** — when ingest lacks a field, emit explicit supplementary request (preingest LIKELY, missing LICENSE) instead of fabricating.
4. **PoC discipline** — validate routing invariant under model swap before claiming orchestration works (HexStrike client-naming complements this).

### Domain note

LCA's clinical oncology domain is **off-topic** for Cemini prod. This page owns **harness vocabulary only**.

| Verdict | **REFERENCE** — design patterns; NO-GO clinical framework install |

## Snippets

> "Empirically demonstrated algorithmic impermeability by maintaining an invariant routing projection during AI model swaps."
> — [Source: arxiv-2607.06531 abstract, retrieved 2026-07-09]
