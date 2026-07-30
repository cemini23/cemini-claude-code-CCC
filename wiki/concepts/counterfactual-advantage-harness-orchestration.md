---
title: Counterfactual / advantage-guided harness orchestration
type: concept
tags: [concept, harness, counterfactual, orchestration, k224]
keywords: [CHILL-Harness, CIEL, ARCO, advantage-margin, success-preserving]
related:
  - sources/arxiv-chill-harness-counterfactual-learning-2607.25825.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/measurement-gated-agent-harness-optimization.md
  - concepts/orchestration-reward-modeling-orch-rm.md
  - concepts/agentic-orchestration-options-abpm.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-chill-harness-counterfactual-learning-2607.25825.md`
- `@concepts/retrospective-harness-optimization-rho.md`
- `@concepts/measurement-gated-agent-harness-optimization.md`

## Raw Concept

Should harness workflow changes fire only when expected advantage clears a margin — without sacrificing task success?

## Narrative

Hand-crafted/global harness policies over-spend tokens and can reduce success on long horizons. **CHILL-Harness** estimates intervention-relative advantage from confidence-weighted execution evidence (CIEL) and realizes only authorized adaptations (ARCO) under success-preserving + advantage-margin constraints.

**Cemini steal:** Don't flip orchestration modes on vibes. Gate Keep→Change with an advantage margin; log rejection reasons. Aligns with FlashRT measurement gates (K200) and RHO (K169 caveats remain).

**Verdict:** **ADOPT** pattern. **NO-GO** `csdstar/chill-dev` (404).
