---
title: "MARC v1 — deterministic multi-agent clinical coordination (K279)"
type: concept
tags: [concept, multi-agent, clinical, decomposer, failure-attribution, k279]
keywords: [2608.13476, MARC, decomposer-from-NL, stage-wise-failure-attribution, role-specialized, YAML-config, LangChain]
related:
  - sources/arxiv-marc-v1-clinical-multi-agent-2608.13476.md
  - entities/tools/marc-v1.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@sources/arxiv-marc-v1-clinical-multi-agent-2608.13476.md`
- `@entities/tools/marc-v1.md`
- `@concepts/role-specialization-model-multi-tool-coordination.md`

## Raw Concept

Replace monolithic LLM prompting with **deterministic multi-agent orchestration** where role-specialized agents (extraction, reasoning, answer generation, evaluation) pass explicit context and leave traceable intermediate outputs — and where a **Decomposer** generates the whole pipeline from plain language.

## Narrative

MARC coordinates role-specialized agents with **explicit context passing + traceable intermediate outputs**, enabling **stage-wise failure attribution** (a failed stage is locatable — you know *which* agent's output was bad). The **Decomposer** generates task-specific agent prompts from a plain-language description, eliminating manual prompt engineering. YAML-config-driven: change agent model/prompt/knowledge sources without code. Model-agnostic, CPU-compatible, aimed at clinical domain experts without programming expertise.

### Steal (ADOPT / GO REFERENCE)

1. **Decomposer-from-NL** — generate the agent pipeline (roles, prompts, RAG config) from a plain-language task description. Promising for cross-wiki / research harnesses where task shapes vary.
2. **Stage-wise failure attribution** — traceable intermediate outputs per stage; attribute failures to the specific agent+stage, not the pipeline as a whole. Directly useful for multi-agent harness debugging (pairs K162 verification discipline, K276 role coordination).
3. **Role-specialized agent pipeline** — extraction / reasoning / answer / evaluation separation with explicit handoffs (Level-2 autonomy pattern).
4. **Declarative YAML configuration** — swap model, prompt, or knowledge source per agent with no code change.

### Local adopt

`Penn-RAIL/MARC-v1` **MIT** ~30MB → cloned to `.local/adopts/MARC-v1` as **GO REFERENCE**. **Clinical `wont_wire`** — no clinical runtime; keep as a structural reference for harness pipelines.

| Verdict | **GO REFERENCE** (MIT clone) + steal decomposer / stage-wise attribution / role separation. Clinical `wont_wire`. |
