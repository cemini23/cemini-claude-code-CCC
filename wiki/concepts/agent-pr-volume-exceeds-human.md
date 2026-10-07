---
title: "Agent-authored PRs exceed human-authored PRs — the review-capacity gap (CCC k284)"
type: concept
tags: [concept, ecosystem, code-review, k284, audit]
keywords: [agent PRs, code review, LGTM, review capacity, deterministic gates, audit change set]
related:
  - concepts/agent-completion-verification-gates.md
  - concepts/repo-level-verified-code-proof-eval.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- `@concepts/agent-completion-verification-gates.md`
- `@concepts/repo-level-verified-code-proof-eval.md`

## Raw Concept

Filed from `@briefs/2026-10-07_k284-ccc-design-registries.md` (CCC k284 daily brief, 2026-10-07). Not paper-derived — the brief is the
source, and the brief's own boundary applies.

## Narrative

**A measured change in the shape of software work**, reported in the k284 brief from The Pragmatic
Engineer's LDX3 keynote (GitHub / Linear / Factory data):

- **Agent-authored pull requests exceeded human-authored ones on GitHub in August 2026** — a **9×
  rise in 8 months**.
- **"Code reviews are dead"** — review has degraded into a **theatre of LGTM stamps**, and quality
  and reliability are **falling**.
- Migrations collapse from **years to weeks**.
- Old practices are returning: **tests, tracer bullets, planning**.
- **AI cost is a top concern** — open models plus smart routing cut Uber's per-token cost 50%+.

**Why CCC cares: this is the empirical case for the wiki's own doctrine.** If agent-authored change
arrives faster than human review capacity can absorb it, then **review cannot be the gate**. The
consequence is the position CCC already holds in several places — **audit the change set with
deterministic gates, not by reviewing harder**. See
`@concepts/agent-completion-verification-gates.md` and the mechanical-gate work in K406 Assay and
K424's graded ladder.

**The pairing worth noting:** the same brief that reports review degrading also reports the
*mechanical* answers improving — K431's step-level process delivery (adherence 76–95% → 95–99%),
K434's honest measurement that we do **not** yet know history-based compaction timing beats a token
budget, and K428's certified verifier bank. **Deterministic, checkable signals are the direction;
"review more carefully" is not.**

**Confidence `[TENTATIVE]`:** these are **conference-keynote figures cited in a brief**, not a paper
with a released methodology. The direction is consistent with other sources CCC holds; the specific
numbers (9×, 50%+) are single-source and unreproduced here. Treat as a trend signal, not a measured
rate.

## Snippets

> "Agent-authored PRs exceeded human-authored ones on GitHub in August 2026 (9× in 8 months)." [Source:
> `@briefs/2026-10-07_k284-ccc-design-registries.md`, citing The Pragmatic Engineer LDX3 keynote]

> "**Code reviews are dead** — a theater of LGTM stamps. **Quality and reliability falling.**"
> [Source: same]
