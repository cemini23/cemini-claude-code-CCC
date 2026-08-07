---
title: Trajectory error-lifecycle attribution (TrajDebug) (K256)
type: concept
tags: [concept, trajectory, debugging, causal-attribution, k256]
keywords: [2608.06346, TrajDebug, error-trigger, critical-failure]
related:
  - sources/arxiv-trajdebug-error-lifecycle-2608.06346.md
  - entities/tools/trajdebug.md
  - concepts/telemetry-deterministic-agent-failure-repair.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/verification-gated-persist-pivot-runtime.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-trajdebug-error-lifecycle-2608.06346.md`
- `@entities/tools/trajdebug.md`
- `@concepts/telemetry-deterministic-agent-failure-repair.md`

## Raw Concept

How do we find the earliest decisive error in a long failed agent trajectory — not just the last wrong action?

## Narrative

K256 TrajDebug (arXiv **2608.06346**): three auditable stages — trigger detection (verbatim evidence for commitment + violated reference) → error-state classification → causal attribution to failure-responsible origin among terminal-relevant candidates.

### Cemini steal (ADOPT)

1. On failed long-horizon sessions: ask for earliest wrong commitment with quote evidence, not only terminal symptom (pairs K242 Sentinel / K253 persist-pivot).
2. Prefer deterministic evidence-grounded attribution before LLM-as-judge for “what went wrong.”
3. Keep TrajDebug clone as REFERENCE until detector `.py` lands — do not runtime-wire empty stubs.

| Verdict | **ADOPT** method. Skeleton MIT REFERENCE only. Entity `wont_wire`. |
