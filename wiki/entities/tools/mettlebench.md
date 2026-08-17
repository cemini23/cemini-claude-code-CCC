---
title: "MettleBench — long-horizon engineering assignment benchmark"
type: entity
tags: [entity, tool, benchmark, agent-harness, apache-2.0, k282]
keywords: [k282, MettleBench, checklist-progress, ordered-criteria, Apache-2.0, long-horizon]
related:
  - sources/arxiv-agentrewind-recoverable-execution-2608.14380.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - entities/tools/agentrewind.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-agentrewind-recoverable-execution-2608.14380.md`
- `@concepts/recoverable-agent-execution-checkpoints.md`
- `@entities/tools/agentrewind.md`

## Raw Concept

Phase-0 entity for CCC K282 — MettleBench (the AgentRewind benchmark).

## Narrative

Repo `github.com/Kelvin-Coffee/MettleBench` — LICENSE **Apache-2.0** (verified on disk). ~31MB → cloned to `.local/adopts/MettleBench` as **GO REFERENCE**.

82 tasks / 640 ordered, interdependent acceptance criteria derived from five engineering benchmarks (Terminal-Bench 2.0, ProgramBench, SWE-bench, ProjectEval, GitTaskBench). Each task is a single assignment with a hidden ordered checklist; the backend returns only the first unsatisfied criterion. Two metrics: binary task success + checklist prefix progress `ρ = ℓ/n`. REFERENCE for long-horizon eval with partial-progress scoring; runtime **`wont_wire`** (benchmark corpus, not a CCC tool).

**Phase-0:** `scripts/adopt_k282_phase0.sh`
