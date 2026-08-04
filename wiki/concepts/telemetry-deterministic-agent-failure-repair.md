---
title: Telemetry + deterministic verify + rollback agent failure repair (K242)
type: concept
tags: [concept, telemetry, monitoring, verification, repair, k242]
keywords: [2608.02464, Agent Trajectory Sentinel, ESN, CUSUM, rollback, deterministic verify]
related:
  - sources/arxiv-agent-trajectory-sentinel-2608.02464.md
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

- `@sources/arxiv-agent-trajectory-sentinel-2608.02464.md` — K242 provenance
- `@entities/tools/agent-trajectory-sentinel.md` — MIT REFERENCE clone
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix mutates harness; Sentinel repairs trajectories in-session
- `@concepts/self-healing-agent-sessions.md` — retry budget vs telemetry-triggered rollback
- `@concepts/agent-completion-verification-gates.md` — deterministic verify as completion gate

## Raw Concept

Cheap runtime telemetry for anomaly detection plus deterministic recomputation from tool results — with rollback+re-run as preferred repair.

## Narrative

K242 **Agent Trajectory Sentinel** (arXiv **2608.02464**, Sunny Dubey): two-layer stack.

### Layer 1 — telemetry monitor

- One-class ESN + CUSUM; ~200µs/step
- AUROC 0.872; detection rate 0.71 at 5% false-alarm
- **Healthy-null does not transfer cold** (0.527) — recalibrate per deployment

### Layer 2 — deterministic verification

- Recompute totals from tool results + coverage check
- 0 FP on 63 failures / 0 of 1825 healthy trajectories

### Repair posture

| Strategy | Repair rate |
|----------|-------------|
| Rollback + re-run | 45% |
| Resample only | 16% |
| Success overall | 52% → 73% |

### vs related patterns

| Pattern | Sentinel difference |
|---------|---------------------|
| `@concepts/failed-trajectory-harness-repair.md` | HarnessFix edits harness artifacts; Sentinel repairs within session |
| `@concepts/self-healing-agent-sessions.md` | Self-healing = retry budget; Sentinel adds telemetry + deterministic verify |

| Verdict | **ADOPT** cheap telemetry + deterministic verify + rollback repair. **GO** MIT REFERENCE. `policy_wired`. |

## Snippets

> Healthy-null does not transfer cold — must recalibrate.
> — [Source: arxiv-2608.02464, retrieved 2026-08-04]

## Dead Ends

- **Default runtime MCP wire** — policy pattern only; not prod MCP allowlist default
- **Skipping recalibration** — cold-transfer AUROC ~0.527
