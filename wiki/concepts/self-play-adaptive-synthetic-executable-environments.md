---
title: Self-play in adaptive synthetic executable environments (SPADE)
type: concept
tags: [concept, self-play, rl, synthetic-environments, k294]
keywords: [2608.19197, SPADE, hint-based regret, environment designer]
related:
  - sources/arxiv-spade-self-play-synthetic-environments-2608.19197.md
  - entities/tools/spade-rl.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/adversarial-curriculum-structured-reward-doc-fidelity.md
  - sources/brief-k290-k294-harness-wave-2026-08-20.md
  - briefs/2026-08-20_ccc-handoff-k290-k294-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- `@sources/arxiv-spade-self-play-synthetic-environments-2608.19197.md`
- `@entities/tools/spade-rl.md`

## Raw Concept

How can training environments co-evolve with the agent instead of exhausting a fixed pool?

## Narrative

**SPADE:** one LLM writes complete Gym-style executable envs (reset/step, rewards, verification) and learns as Reasoning Agent. **Hint-based regret** rewards envs at the capability frontier (solvable but challenging). Corpus grounding + env memory prevent symmetric self-play collapse.

**Cemini steal:** Eval/red-team packs can use executable micro-envs with verifiable rewards; closed self-improve loops need external eval contract (K162). MIT REFERENCE clone; trainer **`wont_wire`**.

| Verdict | **ADOPT** co-evolving executable env curriculum. **GO REFERENCE** MIT `.local/adopts/spade`. |
