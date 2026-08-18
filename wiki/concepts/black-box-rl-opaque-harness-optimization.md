---
title: "Black-box RL on opaque harnesses (K287)"
type: concept
tags: [concept, agent-harness, reinforcement-learning, black-box-rl, serving-proxy, prefix-tree, k287]
keywords: [2608.16798, ClawGym II, serving proxy, prefix tree, PPO, GRPO, mix-harness, black-box RL]
related:
  - sources/arxiv-clawgym-ii-black-box-rl-harness-2608.16798.md
  - entities/tools/clawgym-ii.md
  - concepts/scaffold-over-tool-interface.md
  - concepts/versioned-model-harness-continual-adaptation.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-clawgym-ii-black-box-rl-harness-2608.16798.md`
- `@entities/tools/clawgym-ii.md`
- `@concepts/scaffold-over-tool-interface.md` — K262 scaffold > interface
- `@concepts/versioned-model-harness-continual-adaptation.md` — K263 versioned model-harness pairs
- `@concepts/meta-harness-optimization-hitl-eval-contract.md` — K281 AutoDesign: meta-optimization over the harness; ClawGym II optimizes the *model* through the harness

## Raw Concept

Modern harnesses are too complex to expose their internal control flow for RL — but the model still needs training to exploit them. What if the harness were treated as an opaque rollout engine, and policy optimization operated on a serving proxy's captured calls instead?

## Narrative

ClawGym II (arXiv 2608.16798) is a unified **black-box RL** framework: decouple policy optimization from opaque harness execution, place a **serving proxy** at the model boundary to capture calls, rebuild **prefix trees** from fragmented/ forked traces, and optimize PPO/GRPO over the tree structure. Training–inference consistency is preserved via black-box token-in-token-out + importance-sampling rollout correction. **Mix-harness training** jointly optimizes one model from heterogeneous harnesses (OpenClaw + Claude Code).

### Steal (ADOPT)

1. **Treat the harness as an opaque rollout engine.** Don't instrument its internals; intercept at the model boundary with a serving proxy. The harness keeps its native execution logic and operates independently.
2. **Sandbox per rollout.** Each task environment + harness lives in a temporary sandbox provisioned on demand and destroyed on completion — isolates state, enables concurrency, and prevents cross-rollout leakage.
3. **Rebuild prefix trees from captured calls.** Black-box traces are fragmented, forked, and redundant; organize captured model calls into a prefix tree to recover reliable multi-turn trajectories, then adapt PPO (critic-based) and GRPO (critic-free) to optimize over the recovered tree.
4. **Preserve training–inference consistency.** The bias between the inference engine and the training engine is real; black-box token-in-token-out + token-level importance-sampling rollout correction mitigate it — otherwise training destabilizes.
5. **Mix-harness joint training.** Each task–harness pair is a training instance; rollouts from structurally different harnesses jointly optimize one model, which matches or surpasses single-harness training. No harness-specific rewrites.

### Why this pairs K281 (AutoDesign) and K262/K263

K281 AutoDesign optimizes the *harness* from rollout feedback (model fixed); ClawGym II optimizes the *model* through a fixed opaque harness — the two are complementary optimization axes. K262 (scaffold > interface) says the harness abstraction matters more than the surface; ClawGym II operationalizes that by optimizing *through* the abstraction. K263 (versioned model-harness pairs) is the bookkeeping discipline that black-box RL makes necessary — a model optimized through one harness version must be pinned to it.

### Local adopt

- **No clone** — no public ClawGym II SPDX repo. **Policy only.** The serving-proxy + prefix-tree pattern is the transferable unit.

| Verdict | **ADOPT** intercept model calls at serving proxy; rebuild prefix trees; PPO/GRPO on trees; mix-harness joint training; sandbox per rollout. `policy_wired`; no runtime clone. |
