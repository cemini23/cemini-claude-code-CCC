---
title: "Test-time world model — validate-before-act (K283)"
type: concept
tags: [concept, world-model, validate-before-act, arc-agi, harness, k283]
keywords: [2608.14490, Twin, replay-validation, harness-enforced-gate, goal-inference, asymmetric-objective]
related:
  - sources/arxiv-twin-test-time-digital-twin-2608.14490.md
  - entities/tools/twin-arc-agi-3.md
  - concepts/active-abstraction-programmatic-world-models.md
  - entities/tools/tycho-arc-agi.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - concepts/phase1-adopt-wire.md
  - "@game-dev-wiki/concepts/twin-test-time-world-model-stub.md"
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-twin-test-time-digital-twin-2608.14490.md`
- `@entities/tools/twin-arc-agi-3.md`
- `@concepts/active-abstraction-programmatic-world-models.md` — K231 Tycho (build/use/bypass)
- `@entities/tools/tycho-arc-agi.md`
- `@game-dev-wiki/concepts/twin-test-time-world-model-stub.md`

## Raw Concept

An agent playing an unknown game can either react to a black box or build an explicit model of it and reason inside it. What if the *harness* — not the agent's discretion — refuses to let any scored action through until the model reproduces every observed transition?

## Narrative

Twin (arXiv 2608.14490) makes world-model validation a **harness-enforced gate**. A coding agent writes an executable "twin" (`step` + `goal_reached`), which must replay every logged transition before any scored action is submitted. The objective is **asymmetric**: fit to observed dynamics is a hard precondition for action (certified by replay), while goal reachability is pursued through search and hypothesis — not imposed jointly during synthesis.

### Steal (ADOPT)

1. **Validate-before-act as a harness gate, not an agent preference.** Concurrent systems *request* validation in prompts; Twin's harness **blocks** the executor until the twin replays the full log. The mechanical gate is what stops unvalidated actions from compounding across long games — Twin alone clears bp35/lf52/sk48 (9/10/8 levels). Harness enforcement beats prompt instruction.
2. **Each committed action is planned progress, a counterexample, or a deliberate probe.** Execute-checked submits one move at a time and halts at the first mismatch; the mismatch is appended to the log and invalidates the twin until repair. No wasted scored action.
3. **Counterexample-driven repair (CEGIS).** Validate shows the twin is wrong, Explore shows *where*, Repair fixes the code — and the repaired twin must replay the *full* log, so a local fix can't break an earlier mechanic.
4. **Goal before reward.** Don't wait for the first win to infer the goal. Propose a tentative goal predicate (it must evaluate false on every logged frame, and any previously-reached non-goal is permanently excluded), plan the cheapest test, and let a level boundary confirm it. Twin's first goal hypothesis is correct on 87.2% of cleared levels.
5. **Asymmetric objective discipline.** `∀(s,a,s′) ∈ D: T̂(s,a)=s′` (fit must hold for *every* logged transition) vs `∃` route (reachability needs only *one* imagined path). Split them: consistency is the gate; optimism lives in planning/goal discovery.

### Why this pairs K231 (Tycho)

Tycho (K231) established build/use/bypass of programmatic world models under costly interaction — and noted auto-repair that improves transition-match can still hurt action efficiency. Twin is the harness-mandatory replay gate layered on that recipe: **don't auto-build world models every verify-fail unless advantage-gated, but when building, require full-log replay validation before any scored action.** The K231 caveat (improve transition-match ≠ improve action efficiency) is exactly what Twin's harness-enforced gate + goal-before-reward ordering addresses.

### Local adopt

- `Alexyskoutnev/TWIN-ARC-AGI-3` — MIT (~7.1MB) → `.local/adopts/TWIN-ARC-AGI-3` **GO REFERENCE**. ARC bench runtime **`wont_wire`**.

| Verdict | **ADOPT** harness-enforced validate-before-act + goal-before-reward. REFERENCE clone; ARC runtime `wont_wire`. Game-dev cross-wiki stub. |
