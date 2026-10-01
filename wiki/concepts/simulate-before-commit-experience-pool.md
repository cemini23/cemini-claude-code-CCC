---
title: "PrecogUI: Pre-cognitive Simulation for Proactive GUI Agents (CCC K283)"
type: concept
tags: [concept, k283]
keywords: [2609.36923, k283]
related:
  - sources/arxiv-precogui-pre-cognitive-simulation-2609.36923.md
  - "@seo-wiki/sources/arxiv-kang-2026-precogui-proactive-gui-agents-2609.36923-2026-09-30.md"
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-01_ccc-k411-k415-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@sources/arxiv-precogui-pre-cognitive-simulation-2609.36923.md`
- `@seo-wiki/sources/arxiv-kang-2026-precogui-proactive-gui-agents-2609.36923-2026-09-30.md` — cross-wiki primary (SEO K283)
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-01_ccc-k411-k415-sip-ready.md`

## Raw Concept

K283: REFERENCE (cross-wiki steal; no code) — arXiv 2609.36923.

## Narrative

**PrecogUI — simulate before you commit.** Routed inbound from `@seo-wiki/` (SEO K283). A pre-cognitive GUI-agent architecture with three parts. A **Proactive Experience Pool (PEP)** caches recurring anomaly and success patterns as `state-action-result` tuples in dual memory. A **Proactive Simulation Executor (PSE)** learns to forecast the next symbolic UI layout given a candidate action, so it can **rank candidate actions by predicted reliability** and avoid anomalies before they happen. A **Pre-cognitive Execution Controller (PEC)** fuses priors and predictions, prioritizes foreseen anomalies, and closes the loop with error correction. Results: 79.2% SR low-interference / 52.7% high; 89.4% element-type accuracy. **CCC relevance is the discipline, not the domain:** rank candidate actions by predicted reliability and keep a pool of past failures so the same one is not repeated. That maps onto pre-flight checks, verify-before-publish gates, and failure memory — the same shape as `@concepts/test-time-world-model-validate-before-act.md` and K406 Assay's evidence gate. Pairs the failure-memory line and `@concepts/agent-completion-verification-gates.md`. **No code published** ('will be publicly available') → nothing to clone, no Phase-0. **Further implementation: none** (per the routing brief). Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.36923 locators." [Source: CCC K283 synthesis]
