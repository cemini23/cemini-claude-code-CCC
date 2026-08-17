---
title: K282–K284 harness wave — CCC brief stub
type: source
tags: [source, brief, k282, k283, k284]
keywords: [agentrewind, twin-arc-agi-3, differential-fault-injection, 2026-08-17]
related:
  - sources/arxiv-agentrewind-recoverable-execution-2608.14380.md
  - sources/arxiv-twin-test-time-digital-twin-2608.14490.md
  - sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - concepts/test-time-world-model-validate-before-act.md
  - concepts/differential-fault-injection-llm-modernization.md
  - entities/tools/agentrewind.md
  - entities/tools/mettlebench.md
  - entities/tools/twin-arc-agi-3.md
  - entities/patterns/differential-fault-injection-validation.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - briefs/2026-08-17_ccc-k282-k284-sip-ready.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-agentrewind-recoverable-execution-2608.14380.md`
- `@sources/arxiv-twin-test-time-digital-twin-2608.14490.md`
- `@sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md`
- `@briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md`

## Raw Concept

Brief stub for the K282–K284 ingest (2026-08-17). Three-paper harness wave: K282 AgentRewind (recoverable execution checkpoints), K283 Twin (test-time world model, validate-before-act), K284 differential fault injection (off-nominal LLM-modernization validation).

## Narrative

Three-paper batch: K282 AgentRewind → **ADOPT** aligned context+env checkpoints + resume recovery (MIT `replay-agent-recorder` + Apache-2.0 `MettleBench` GO REFERENCE); K283 Twin → **ADOPT** harness-enforced validate-before-act + goal-before-reward (MIT `TWIN-ARC-AGI-3` GO REFERENCE; ARC runtime `wont_wire`); K284 differential fault injection → **ADOPT** off-nominal paired validation (no public SPDX → policy only). K283 pairs K231 Tycho; K284 pairs K235 mutation-consistency + K162 verification hierarchy.

## Sources

- arXiv 2608.14380 / 2608.14490 / 2608.14527
- `briefs/2026-08-17_k282-k284-harness-wave-prod.md`
