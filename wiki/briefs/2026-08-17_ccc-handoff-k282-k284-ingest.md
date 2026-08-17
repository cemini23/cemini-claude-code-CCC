---
title: CCC handoff — K282–K284 harness wave
type: brief
tags: [brief, handoff, k282, k283, k284]
related:
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-k282-k284-sip-ready.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - concepts/test-time-world-model-validate-before-act.md
  - concepts/differential-fault-injection-llm-modernization.md
  - entities/tools/agentrewind.md
  - entities/tools/mettlebench.md
  - entities/tools/twin-arc-agi-3.md
  - entities/patterns/differential-fault-injection-validation.md
  - sources/arxiv-agentrewind-recoverable-execution-2608.14380.md
  - sources/arxiv-twin-test-time-digital-twin-2608.14490.md
  - sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md
  - concepts/phase1-adopt-wire.md
created: 2026-08-17
updated: 2026-08-17
---

## Summary

Three-paper batch (K282–K284): K282 AgentRewind → **ADOPT** aligned context+env checkpoints + resume-from-checkpoint recovery (pairs K239 execution fidelity, K242 rollback); K283 Twin → **ADOPT** harness-enforced validate-before-act + goal-before-reward (pairs K231 Tycho); K284 differential fault injection → **ADOPT** off-nominal paired validation for LLM code transforms (pairs K235, K162).

## Local

- `.local/adopts/replay-agent-recorder` (MIT ~3.7MB) — GO REFERENCE
- `.local/adopts/MettleBench` (Apache-2.0 ~31MB) — GO REFERENCE
- `.local/adopts/TWIN-ARC-AGI-3` (MIT ~7.1MB) — GO REFERENCE
- Re-cloned (prior shelf empty): `.local/adopts/MARC-v1` (MIT), `.local/adopts/vero` (Apache-2.0), `.local/adopts/AutoDesign` (MIT)
- K284: **no public SPDX ftinj clone** → policy only (no GAMESS runtime on CCC laptop)

## Routing

- Prod + hands-on (`briefs/2026-08-17_k282-k284-*` + `docs/briefs/2026-08-17_k282-k284-*`)
- **Atto** (light): K283 validate-before-act for extract solvers
- Cybersec: K284 differential fault injection (off-nominal LLM-code validation stub)
- Game-dev: K283 Twin / ARC-AGI-3 (test-time world model stub)
