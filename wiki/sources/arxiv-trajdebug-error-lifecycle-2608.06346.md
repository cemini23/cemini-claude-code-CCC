---
title: "TRAJDEBUG — tracing error lifecycle in long-horizon trajectories"
type: source
tags: [source, arxiv, trajectory, debugging, k256]
keywords: [2608.06346, TrajDebug, THU-KEG, critical-failure, causal-attribution]
related:
  - concepts/trajectory-error-lifecycle-attribution.md
  - entities/tools/trajdebug.md
  - concepts/telemetry-deterministic-agent-failure-repair.md
  - concepts/failed-trajectory-harness-repair.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@concepts/trajectory-error-lifecycle-attribution.md`
- `@entities/tools/trajdebug.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories |
| **arXiv** | 2608.06346 |
| **Repo** | `THU-KEG/TrajDebug` — MIT LICENSE present; **0 `.py` files** (README: code under internal review) |
| **Retrieved** | 2026-08-07 |

## Narrative

Evidence-grounded pipeline: (1) error trigger detection with verbatim commitment + violated reference; (2) error-state classification; (3) causal attribution to earliest decisive failure. Multi-granularity trajectory views + local viewer.

| Verdict | **ADOPT** error-lifecycle attribution method. **GO** thin MIT REFERENCE shelf (paper+LICENSE+stubs, ~4.2MB). **wont_wire** until detector code ships. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/<basename>` (archived 2026-08-07; local `raw-sources/` copy retained).
