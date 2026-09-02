---
title: "Meta-harness continual improvement — wrap, don't rebuild (CCC K335)"
type: concept
tags: [concept, meta-harness, continual-improvement, swe, multiday, eval-gate, policy, k335]
keywords: [2609.01481, Harness-of-Harness, HoH, meta-harness, continual improvement, independent evaluation, versioned history, progressive exposure]
related:
  - sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md
  - entities/tools/harness-of-harness.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/stratified-harness-evolution.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - concepts/harness-as-eval-artifact.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- `@sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md`
- `@entities/tools/harness-of-harness.md`
- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/harness-continual-learning-guarded-evolution.md`
- `@concepts/harness-as-eval-artifact.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

The question: how do you improve a coding-agent harness over multi-day SWE trajectories without replacing the whole stack? Answer from HoH (K335) [Source: wiki/sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md]: add a **meta-harness** above existing harnesses — iterative plan–code–test with independent eval, versioned history, and scoped increments.

## Narrative

**Meta-harness pattern.** HoH does not train weights or rewrite Cursor/`/route`. It wraps an existing coding-agent harness and runs an outer optimization loop over orchestration choices: tool exposure, verification steps, increment scoping, and loop configuration. The inner harness still executes tasks; the outer loop learns what harness configuration retains gain on **held-out** SWE eval.

**Protocol (ADOPT):**

1. **Wrap, don't rebuild** — preserve production scaffolds; meta-layer sits on top (pairs `@concepts/harness-as-eval-artifact.md` K334: evaluate the harness artifact).
2. **Small verifiable increments** — each meta iteration must produce a testable delta; balance bug-fix/repair work with capability expansion.
3. **Independent eval gate** — separate implementation-time self-tests from held-out scoring; do not treat green local tests as retained improvement (pairs `@concepts/meta-harness-optimization-hitl-eval-contract.md` K281/K162 external eval contract).
4. **Versioned project history** — checkpoint harness configs and trajectories for rollback when continued search erases gains (pairs `@concepts/vague-goal-self-evolution.md` K332 checkpoint discipline).
5. **Progressive tool/skill exposure** — expand affordances gradually; avoid turn-zero catalog dumps (pairs K311 SCOUT lazy discovery).

**Evidence:** +52.25% avg relative gain (max 82.86%) after three meta iterations across three harness–model pairs — on independent evaluation, not self-report.

**CCC policy lines (wire `policy_wired`):**

- Multi-day SWE needs **meta-loop discipline** — outer verify before trusting inner loop changes.
- **`Flesymeb/HarnessOfHarness` MIT** → GO REFERENCE `.local/adopts/HarnessOfHarness`; runtime **`wont_wire`** — do not replace Cursor/`/route`/claude-ds.
- **Never auto-evolve `.cursor/skills`** (pairs K237 misevolution, K313 stratified evolution HITL).
- Retention checks on held-out packs before adopting learned harness state (pairs `@concepts/harness-continual-learning-guarded-evolution.md` K292).

| Confidence | `[CONFIRMED]` — results from the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "Wrap existing harnesses; do not rebuild orchestration from scratch." [Source: wiki/sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md — K335 policy line]

> "Separate implementation-time testing from independent evaluation." [Source: wiki/sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md — K335 policy line]
