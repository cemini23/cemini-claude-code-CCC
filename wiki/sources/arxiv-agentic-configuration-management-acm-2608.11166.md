---
title: "Agentic Configuration Management (ACM) reference model"
type: source
tags: [source, arxiv, acm, governance, configuration, k273]
keywords: [2608.11166, ACM, baselines, provenance, LangGraph, CrewAI]
related:
  - concepts/agentic-configuration-management-acm.md
  - entities/tools/agentic-configuration-management-acm.md
  - concepts/phase1-adopt-wire.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k270-k273-mcp-acm-wave-2026-08-12.md
  - briefs/2026-08-12_ccc-handoff-k270-k273-ingest.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- `@concepts/agentic-configuration-management-acm.md`
- `@entities/tools/agentic-configuration-management-acm.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems |
| **arXiv** | 2608.11166 |
| **Author** | Quessadda-Vial (PwC) |
| **Code** | Paper claims Python reference + adapters; no dedicated public ACM repo confirmed at Phase-0 (cites microsoft/agent-framework) |
| **Retrieved** | 2026-08-12 |

## Narrative

Framework-independent SCM for agentic systems: immutable configuration items, baselines, deterministic governance, lifecycle, dependency-aware impact, runtime provenance. Semantic projection adapters (LangGraph/CrewAI/OpenAI Agents SDK). Formal monotonic impact propagation.

| Verdict | **ADOPT** ACM governance vocabulary for Cemini harness configs. **NO-GO** product install until SPDX'd ACM artifact. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.11166-agentic-configuration-management-acm-a-reference.pdf`
