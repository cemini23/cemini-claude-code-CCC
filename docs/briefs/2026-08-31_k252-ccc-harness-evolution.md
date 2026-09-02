---
title: K252 CCC harness evolution — EvoUndo, Logos, skill routing, Prove2Me
type: brief
tags: [brief, ccc, k252, harness]
target: claude.ai
created: 2026-08-31
updated: 2026-08-31
---

## Target

CCC meta-wiki / harness policy awareness. **No runtime install.**

## Summary

Verdict: **policy vocabulary only — 0 Integrate GO.** K252 adds four harness papers: recoverability-constrained self-evolution (EvoUndo), cross-process composable harness (Logos), personalized skill routing with counterfactual eval, and mission-based Lean formalization (Prove2Me). Pairs existing federation wires K282 (AgentRewind), K237 (skill misevolution), K313/K314 (StarHarness/Recuris), K280 (Vero), BPS skill-set-budget. **HITL before any `.cursor/skills` mutation.**

## Body

1. **EvoUndo** — treat recoverability as an explicit invariant for harness self-mutation; naive repair fails most capability-positive mutations; pairs K282 rewind checkpoints.
2. **Logos** — ROS-like cross-process bus + append-only transcript; cold switching without repeated external effects after kill/resume; pairs distributed harness thinking, not a Cursor replacement.
3. **Personalized skill routing** — per-user skill selection beyond task-only matching; counterfactual eval; pairs BPS/skill-set-budget, not independent top-k packing.
4. **Prove2Me** — collaborative Lean formalization missions; agent-first with bounded human audit; K280 Vero vocabulary only — **wont_wire** Lean toolchain on laptop harness.
5. Phase-0: no verified public SPDX clones. Do **not** conflate arXiv Logos with `maior/logosai-framework`.

## Sources

- @concepts/k252-harness-evolution-wave.md
- @sources/arxiv-2608.28363-evoundo-recoverability-2026-08-31.md
- @sources/arxiv-2608.28553-logos-cross-process-bus-2026-08-31.md
- @sources/arxiv-2608.28241-personalized-skill-routing-2026-08-31.md
- @sources/arxiv-2608.28433-prove2me-formalization-2026-08-31.md
