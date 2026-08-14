---
title: "MARC v1 — open-source multi-agent framework for clinical AI reasoning and coordination"
type: source
tags: [source, arxiv, multi-agent, clinical, decomposer, failure-attribution, k279]
keywords: [2608.13476, MARC, Penn-RAIL, decomposer, stage-wise-failure-attribution, role-specialized, LangChain, YAML-config]
related:
  - concepts/marc-clinical-multi-agent-coordination.md
  - entities/tools/marc-v1.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@concepts/marc-clinical-multi-agent-coordination.md`
- `@entities/tools/marc-v1.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination |
| **arXiv** | 2608.13476 |
| **Authors** | Saisha Shetty, Satvik Tripathi, Austin Lin, et al. (Penn RAIL / UC Davis / Drexel) |
| **Code** | `github.com/Penn-RAIL/MARC-v1` — **MIT** LICENSE file (local clone) |
| **Retrieved** | 2026-08-14 |

## Narrative

Open-source framework replacing monolithic LLM prompting with **deterministic multi-agent orchestration** for clinical reasoning. Coordinates **role-specialized agents** for extraction, reasoning, answer generation, and evaluation, with **explicit context passing and traceable intermediate outputs**, enabling **stage-wise failure attribution**. Adds a **Decomposer** module that generates task-specific agent prompts from a plain-language description, eliminating manual prompt engineering. Entirely configurable via YAML (agent sequences, model assignments, RAG augmentation) — **no code modification**; model-agnostic; API-based or local CPU-compatible deployments.

Demonstrated on three tasks: biomedical QA, radiology report generation, task-adaptive pipeline construction. Sequential modular pipeline with explicit handoffs (Level 2 autonomy pattern).

| Verdict | **GO REFERENCE** (`Penn-RAIL/MARC-v1` MIT ~30MB → cloned to `.local/adopts/MARC-v1`). **Steal:** decomposer-from-NL, stage-wise failure attribution, role-specialized agent pipeline. **Clinical `wont_wire`** — no clinical runtime wiring. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.13476-marc-v1-an-open-source-multi-agent-framework-for.pdf`
