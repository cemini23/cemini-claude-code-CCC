---
title: "Twin — playing an unknown game with a test-time digital twin"
type: source
tags: [source, arxiv, world-model, validate-before-act, arc-agi, k283]
keywords: [2608.14490, Twin, ARC-AGI-3, test-time-world-model, replay-validation, goal-inference, TWIN-ARC-AGI-3]
related:
  - concepts/test-time-world-model-validate-before-act.md
  - entities/tools/twin-arc-agi-3.md
  - concepts/active-abstraction-programmatic-world-models.md
  - entities/tools/tycho-arc-agi.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - "@game-dev-wiki/concepts/twin-test-time-world-model-stub.md"
maturity: draft
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@concepts/test-time-world-model-validate-before-act.md`
- `@entities/tools/twin-arc-agi-3.md`
- `@concepts/active-abstraction-programmatic-world-models.md` — K231 Tycho: build/use/bypass world models; Twin makes replay validation harness-mandatory
- `@entities/tools/tycho-arc-agi.md`
- `@game-dev-wiki/concepts/twin-test-time-world-model-stub.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Twin: Playing an Unknown Game with a Test-Time Digital Twin |
| **arXiv** | 2608.14490 |
| **Authors** | Alexy Skoutnev, Kirill Acharya, Gaston Longhitano, Madeleine Udell, Kevin Ellis, Iddo Drori (Stanford / Cornell / USC / Yeshiva) |
| **Code** | `github.com/Alexyskoutnev/TWIN-ARC-AGI-3` — **MIT** (verified LICENSE on disk) |
| **Retrieved** | 2026-08-17 |

## Narrative

Test-time world-model inference for unknown grid-world games (ARC-AGI-3, 64×64 × 16-color grids with hidden controls and win conditions). A frontier **coding agent writes an executable world model** — a Python "twin" with the fixed contract `step(grid, action) -> grid` and `goal_reached(grid) -> bool` — checked against every observed transition. Replay validation happens *inside the twin*: the harness **blocks any scored action until the twin reproduces every logged transition**. Each mismatch is a counterexample that drives repair (CEGIS / WorldCoder lineage).

The objective is **asymmetric**: dynamics can be verified against every interaction, but the goal (win condition) must be inferred from sparse reward — only a completed level provides a positive label. Twin treats the goal as a hypothesis to test before any reward, and discriminates rival goal predicates by the most efficient plan. The loop is `validate → explore → plan → execute-checked`: unscored compute is spent freely; only real actions are scored.

**Results.** Twin clears **179/183 levels (97.8%)** and **23/25 games**, scoring **93.3/100** on ARC-AGI-3 action-efficiency, beating OPINE-World (78.4), Prime Agent (78.3, same base model), EWM (63.8), and off-the-shelf Codex (61.1). Played directly, the base model scores **7.8%**. The harness earns the score: disabling the validate–explore–plan loop drops 93.3 → 61.1 and 23 → 13 cleared games. **92.9%** of scored actions execute a plan already tried in the twin. The first goal hypothesis is correct on **156/179 (87.2%)** cleared levels; search finds the rest. On the 13 games all systems clear, Twin uses 3,357 scored actions vs 5,367 (OPINE-World), 5,381 (EWM), 7,485 (human reference) — 0.61× the human count on average.

**Limitations.** Replay validation assumes deterministic, program-compressible dynamics and certifies only logged transitions (not unseen states); fixed search budgets mean a goal beyond the horizon goes unfound; truly latent state (a variable no frame ever shows) is out of scope.

| Verdict | **ADOPT** harness-enforced validate-before-act: no scored action until the twin replays every logged transition; goal hypothesis before reward. `Alexyskoutnev/TWIN-ARC-AGI-3` **MIT** → **GO REFERENCE**. ARC bench runtime **`wont_wire`**. Game-dev cross-wiki stub. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.14490-twin-playing-an-unknown-game-with-a-test-time-di.pdf`
