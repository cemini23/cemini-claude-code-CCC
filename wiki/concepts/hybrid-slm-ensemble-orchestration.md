---
title: Hybrid SLM ensemble orchestration — evidence + debate
type: concept
tags: [concept, slm, orchestration, ensemble, debate, k207]
keywords: [2607.20216, hybrid pipeline, adversarial debate, open-weight]
related:
  - sources/arxiv-slm-ensemble-malware-orchestration-2607.20216.md
  - concepts/slm-agent-orchestration-gateway.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - concepts/failure-mode-harness-adaptation-mapping.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k206-k209-mcp-slm-rag-ethics-2026-07-23.md
maturity: draft
created: 2026-07-23
updated: 2026-07-23
---

## Relations

- `@sources/arxiv-slm-ensemble-malware-orchestration-2607.20216.md`
- `@concepts/slm-agent-orchestration-gateway.md`
- `@entities/patterns/glasswing-deliberate-disagreement.md`
- `@concepts/failure-mode-harness-adaptation-mapping.md` — SLM harness peer (K169)

## Raw Concept

K207: orchestrated small open-weight models (evidence pipeline + adversarial debate + optional specialist) can approach/beat ungrounded frontier single-LLM on structured analysis — still need human verification.

## Narrative

### Steal (ADOPT)

1. TipDrop/David cheap lane: prefer **evidence-grounded multi-stage** + optional peer critique over one big closed model for repetitive structured Q&A.
2. Pair general SLM with domain specialist when available (hierarchical consultation).
3. Accuracy ~35% on hard malware bench → **never autonomous** money/LIVE decisions (K162/K205).
4. `slms_mal` repo **404** — pattern only.

| Verdict | **ADOPT** hybrid orchestration checklist; **NO-GO** install |
