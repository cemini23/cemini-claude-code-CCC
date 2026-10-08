---
title: "CoTrace — a harness-tuned agent does not travel (CCC k285 route)"
type: concept
tags: [concept, k285, cross-wiki]
keywords: [2610.10426, k285]
related:
  - sources/arxiv-cotrace-harness-fingerprint-routing-2610.10426.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-08_k285-ccc-route.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@sources/arxiv-cotrace-harness-fingerprint-routing-2610.10426.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-08_k285-ccc-route.md`

## Raw Concept

Routed from `@osint-wiki` via the k285 briefs. Canon stays on OSINT.

## Narrative

**The training value of a trajectory depends on which harness produced it.** Pooling search
trajectories across harnesses **disconnects policy training from the deployed runtime** — the model
learns from traces recorded under a scaffold it will never run in. CoTrace routes trajectories by a
**harness fingerprint** and alternates harness and policy promotion. Qwen3.5-9B on Tmax: **78 → 88
(SFT) → 90 (RL)**, at **30–50 trajectories per iteration** against 149–308 for pooled training — so
the fingerprint both improves the result and cuts the data by ~4×.

**The caveat is the finding, and the brief states it plainly: on Terminal-Bench 2.1 and SWE-bench
Lite the gains largely vanish under a foreign runtime. A harness-tuned agent does not travel.**

**CCC reading.** This is a first-class harness claim and it cuts against a comfortable assumption —
that an improvement learned inside one scaffold transfers to another. CCC documents a *federation* of
harnesses (Claude Code, Cursor, Codex, Grok, and the `/route` lane). If tuning is harness-local, then
**an improvement measured in one lane is not evidence for another**, and every cross-lane claim needs
the runtime held fixed or the transfer measured. It pairs directly with K431 (**Grounded TSR** —
score the process, not the outcome) and K438 (**non-agentic benchmarks correlating as low as
−0.394**): three independent results this month saying *the measuring instrument is part of the
result*. Pairs `@concepts/harness-as-eval-artifact.md` /
`@concepts/agentic-meta-reasoning-control-plane.md` / `@concepts/code-as-agent-harness.md`.

**Boundary:** FILE only. No install, no clone.

## Snippets

> "See source page for locators." [Source: CCC k285 synthesis]
