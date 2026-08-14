---
title: "MARC-v1 — multi-agent clinical reasoning framework (Penn RAIL)"
type: entity
tags: [entity, tool, multi-agent, clinical, mit, k279, reference]
keywords: [k279, MARC, Penn-RAIL, decomposer, stage-wise-failure-attribution, MIT, LangChain, clinical]
related:
  - sources/arxiv-marc-v1-clinical-multi-agent-2608.13476.md
  - concepts/marc-clinical-multi-agent-coordination.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@sources/arxiv-marc-v1-clinical-multi-agent-2608.13476.md`
- `@concepts/marc-clinical-multi-agent-coordination.md`
- `@concepts/role-specialization-model-multi-tool-coordination.md`

## Raw Concept

Phase-0 entity for CCC K279 — MARC-v1 framework.

## Narrative

Repo `github.com/Penn-RAIL/MARC-v1` — **MIT** LICENSE file on disk, ~30MB → cloned to `.local/adopts/MARC-v1` as **GO REFERENCE**. Steal: **decomposer-from-NL** (generate agent pipeline from plain-language task description), **stage-wise failure attribution** (traceable intermediate outputs), **role-specialized agent pipeline** (extraction / reasoning / answer / evaluation with explicit handoffs). Declarative YAML configuration (swap model/prompt/RAG per agent, no code change). **Clinical `wont_wire`** — no clinical runtime wiring; structural reference for harness pipelines.

**Phase-0:** `scripts/adopt_k279_phase0.sh`
