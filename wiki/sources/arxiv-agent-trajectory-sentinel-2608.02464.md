---
title: "Agent Trajectory Sentinel — telemetry + deterministic verify + rollback repair"
type: source
tags: [source, arxiv, telemetry, monitoring, repair, k242]
keywords: [2608.02464, Sunny Dubey, ESN, CUSUM, deterministic verification]
related:
  - concepts/telemetry-deterministic-agent-failure-repair.md
  - entities/tools/agent-trajectory-sentinel.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/self-healing-agent-sessions.md
  - concepts/agent-completion-verification-gates.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- `@concepts/telemetry-deterministic-agent-failure-repair.md`
- `@entities/tools/agent-trajectory-sentinel.md`
- `@concepts/failed-trajectory-harness-repair.md`
- `@concepts/self-healing-agent-sessions.md`
- `@concepts/agent-completion-verification-gates.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agent Trajectory Sentinel |
| **Author** | Sunny Dubey |
| **arXiv** | 2608.02464 |
| **Repo** | `sunnydubey1111/agent-trajectory-sentinel` |
| **License** | MIT (~108MB disk / 32MB GH) |
| **Local clone** | `.local/adopts/agent-trajectory-sentinel` |
| **Retrieved** | 2026-08-04 |

## Narrative

Two-layer failure detection and repair:

1. **Telemetry monitor** — one-class ESN+CUSUM; ~200µs/step; AUROC 0.872; detects 0.71 at 5% FA. Healthy-null does **not** transfer cold (0.527) — must recalibrate per deployment.
2. **Deterministic verification** — recompute totals from tool results + coverage check; 0 FP on 63 failures / 0 of 1825 healthy.

Repair: rollback+re-run 45% vs 16% resample-only; success 52%→73%.

| Verdict | **ADOPT** cheap telemetry + deterministic verify + rollback repair. **GO** MIT REFERENCE. `policy_wired` (not default runtime MCP). |
