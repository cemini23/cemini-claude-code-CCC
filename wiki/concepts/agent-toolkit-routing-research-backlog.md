---
title: "Agent-toolkit routing research backlog"
type: concept
tags: [concept, routing, backlog, retrieval, recall, k244]
keywords: [BrowseComp-Plus_CM, ClimbMix, evidence recall, routing backlog, agentic search]
related:
  - sources/arxiv-k244-harness-skill-selection-cluster.md
  - concepts/skill-set-selection-under-budget.md
  - concepts/wayfinder-fog-of-war-planning.md
  - concepts/adaptive-validation-task-selection-harness-optimization.md
  - sources/newsletter-rss-latent-space-2026-08-20-wayfinder.md
  - sources/substack-rss-addy-osmani-2026-08-21-software-factory.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-k244-harness-skill-selection-cluster.md`

## Raw Concept

Where do steal-from findings that are *not* ready to wire get parked so they don't die in chat or get force-wired?

## Narrative

**Routing backlog** — the parking lot for propose-only / OOD / not-yet-verified findings from the k244 cluster and related waves. Rule: **brief-over-stub when in doubt; never force a wire; do not clone without SPDX.**

Open items:

1. **BrowseComp-Plus_CM retrieval bottleneck** — agentic search evals that *freeze a query-built 100K corpus* overstate recall: ClimbMix projection drops evidence recall **84.3% → 21.4%** with −5 pts accuracy. File on the routing backlog as an eval-design caveat, **not** a clone.
2. **BPS skill-set router** (`/phase1` proposal) — see `@concepts/skill-set-selection-under-budget.md`.
3. **EnvHarness wrap** (keep verifier, EnvRigger synthesizes plug-ins) — see `@sources/arxiv-k244-harness-skill-selection-cluster.md`.
4. **Wayfinder skill** — see `@concepts/wayfinder-fog-of-war-planning.md`.
5. **Task-CoEvolve** val-task sampling — **wired as CCC K298** (`@concepts/adaptive-validation-task-selection-harness-optimization.md`), not backlog.

| Verdict | **Backlog** — tracked here; nothing in this page is runtime-wired. |
