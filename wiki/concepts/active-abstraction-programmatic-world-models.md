---
title: Active abstraction with programmatic world models
type: concept
tags: [concept, world-model, coding-agent, abstraction, k231]
keywords: [Tycho, ARC-AGI-3, RHAE, build-use-bypass]
related:
  - sources/arxiv-tycho-active-abstraction-world-models-2607.28287.md
  - entities/tools/tycho-arc-agi.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - concepts/cost-aware-tool-acquisition-stopping.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
  - "@game-dev-wiki/concepts/tycho-arc-agi-active-abstraction-stub.md"
maturity: draft
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- `@game-dev-wiki/concepts/tycho-arc-agi-active-abstraction-stub.md` — game-dev stub

- `@sources/arxiv-tycho-active-abstraction-world-models-2607.28287.md`
- `@entities/tools/tycho-arc-agi.md`
- `@concepts/llm-as-code-agentic-programming.md`
- `@concepts/cost-aware-tool-acquisition-stopping.md`

## Raw Concept

When should a coding agent construct, repair, consult, or bypass an executable world model under costly interaction?

## Narrative

**Active abstraction (Tycho):** generate a testable programmatic model from interaction and decide when acquiring/using it is worth the cost. Surprising result: better transition-match after auto-repair can **hurt** action efficiency vs letting the actor request model work — sim fidelity ≠ objective identification ≠ next-action value.

**Cemini steal:** Don't auto-build harnesses/simulators on every verify fail. Gate model construction like CAM-DF tool acquisition — actor-requested or advantage-gated. LLM-as-code owns the Moore/simulation loop; LLM fills reasoning nodes.

**Verdict:** **ADOPT** build/use/bypass policy. **GO** Apache `.local/adopts/Tycho`.
