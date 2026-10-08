---
title: "CoTrace — a harness-tuned agent does not travel (CCC k285 route)"
type: source
tags: [source, k285, cross-wiki]
keywords: [2610.10426, k285]
related:
  - concepts/harness-fingerprint-trajectory-routing.md
  - briefs/2026-10-08_k285-ccc-route.md
  - "@osint-wiki/sources/arxiv-2610.10426-cotrace-2026-10-08.md"
maturity: draft
read_status: skimming
cross-wiki-source: "@osint-wiki/sources/arxiv-2610.10426-cotrace-2026-10-08.md"
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@concepts/harness-fingerprint-trajectory-routing.md`
- `@briefs/2026-10-08_k285-ccc-route.md`
- `@osint-wiki/sources/arxiv-2610.10426-cotrace-2026-10-08.md` — cross-wiki canon

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CoTrace — a harness-tuned agent does not travel |
| **arXiv** | 2610.10426 (2026-10) |
| **Canon** | `@osint-wiki/sources/arxiv-2610.10426-cotrace-2026-10-08.md` |
| **Routed by** | `briefs/2026-10-08_k285-ccc-harness-coevolution.md` / `..._resilience.md` |

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

> "on Terminal-Bench 2.1 and SWE-bench Lite the gains largely vanish under a foreign runtime" [Source: `@osint-wiki/sources/arxiv-2610.10426-cotrace-2026-10-08.md` via k285 (retrieved 2026-10-08)]
