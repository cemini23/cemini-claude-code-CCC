---
title: "Harness-of-Harness — multi-day autonomous SWE with continual improvement (CCC K335)"
type: source
tags: [source, arxiv, meta-harness, continual-improvement, swe, multiday, policy, k335]
keywords: [2609.01481, Harness-of-Harness, HoH, meta-harness, continual improvement, plan-code-test, independent evaluation, Flesymeb]
related:
  - concepts/meta-harness-continual-improvement.md
  - entities/tools/harness-of-harness.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/stratified-harness-evolution.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- `@concepts/meta-harness-continual-improvement.md`
- `@entities/tools/harness-of-harness.md`
- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/harness-continual-learning-guarded-evolution.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Harness-of-Harness: Multi-Day Autonomous Software Engineering with Continual Harness Improvement |
| **arXiv** | 2609.01481 (cs.SE, 2026-09-02) |
| **Authors** | Flesymeb / HarnessOfHarness authors (see paper) |
| **Venue** | arXiv preprint |
| **Code** | `Flesymeb/HarnessOfHarness` **MIT** ~312MB → **GO REFERENCE** `.local/adopts/HarnessOfHarness` |
| **Retrieved** | 2026-09-02 |

## Narrative

**Verdict: ADOPT pattern — meta-harness on top of existing coding-agent harnesses; wrap, do not rebuild.**

Harness-of-Harness (HoH) is a **meta-harness** that wraps existing coding-agent stacks (Claude Code, OpenHands, etc.) and runs **multi-day** plan–code–test loops with **continual harness improvement** — not weight training. The outer loop optimizes orchestration, tooling exposure, and verification discipline while the inner harness executes SWE tasks.

**Design principles (the steals):**

- **Wrap existing harnesses** — do not replace production scaffolds from scratch; HoH sits above them.
- **Small verifiable increments** — scope each iteration to testable deltas; balance repair with capability growth.
- **Separate implementation-time testing from independent evaluation** — the agent's self-tests during coding are not the final score; an independent eval gate measures retained gain.
- **Versioned project history** — retain trajectory for rollback and checkpoint selection across multi-day runs.
- **Progressive tool/skill exposure** — expand affordances gradually rather than dumping full catalogs at turn zero (pairs K311 lazy tool discovery).

**Results:** +52.25% average relative gain (max 82.86%) after three meta-harness iterations across three harness–model pairs — measured on held-out SWE evaluation, not self-report during implementation.

CCC policy lines: meta-loop discipline for long-horizon SWE; independent eval gate; versioned history (pairs K281 AutoDesign, K292 HCL retention, K313 stratified evolution). **Do not replace Cursor / `/route`.** MIT REFERENCE clone only; runtime `wont_wire`. **Never auto-evolve `.cursor/skills`.**

| Confidence | `[CONFIRMED]` — results and design from the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "HoH wraps existing coding-agent harnesses rather than rebuilding orchestration from scratch — a meta-harness for multi-day continual improvement." [Source: arXiv 2609.01481 — design thesis]

> "+52.25% average relative gain after three iterations across three harness–model pairs on independent evaluation." [Source: arXiv 2609.01481 — results summary]

> "Implementation-time testing is separated from independent evaluation — self-tests during coding do not substitute for held-out scoring." [Source: arXiv 2609.01481 — eval discipline]

| **Location** | Pending archive to `cemini-egress-fi:/opt/cemini-bulk/research/ccc/` |
|--------------|------------------------------------------------------------------------|
