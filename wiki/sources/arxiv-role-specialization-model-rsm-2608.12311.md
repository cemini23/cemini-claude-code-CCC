---
title: "Role Specialization Model (RSM) — coordinating LLM-based tools in agentic SE"
type: source
tags: [source, arxiv, agentic-se, multi-tool, role-coordination, k276]
keywords: [2608.12311, RSM, role-specialization, HITL, prompt-hardening, SE-3.0, ISO-25010]
related:
  - concepts/role-specialization-model-multi-tool-coordination.md
  - entities/patterns/role-specialization-model.md
  - concepts/code-as-agent-harness.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- `@concepts/role-specialization-model-multi-tool-coordination.md`
- `@entities/patterns/role-specialization-model.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Role Specialization Model (RSM): Coordinating LLM-Based Tools in Agentic Software Development — An Exploratory Case Study |
| **arXiv** | 2608.12311 |
| **Authors** | Carlos Alberto Fernández-y-Fernández, Jorge R. Aguilar Cisneros (UTM / UPAEP, México) |
| **Code** | None — exploratory case study, no product install required |
| **Retrieved** | 2026-08-13 |

## Narrative

Case study coordinating **three LLM tools by role** in one agentic-SE workflow: **Antigravity** (agentic IDE, Gemini backend — architect/designer), **Gemini CLI** (data generation, docs, file pipelines), **Qwen Code** (code-specialized, local via Ollama — privacy-preserving coder). Project: Python desktop "Climate Data Visualizer" (Tkinter + Pandas + Matplotlib).

**RSM = separation-of-concerns applied to assistive tools**: each tool gets a differentiated responsibility domain; overlap minimized. RQ1–RQ3 cover coordination feasibility, deviations from the planned role split, and ISO/IEC 25010 quality.

**Observed deviations (RQ2):** three factors — **absent scope boundaries**, **tool capability overlap**, **cognitive cost of context-switching**. Responsibility for managing drift falls to the human orchestrator.

**Prompt-hardening (steal):** explicit **negative constraints** ("DO NOT run commands / Do NOT use tools / write plain text") fixed a recurrence of agents invoking unavailable internal tools — consistent with constraint-density degradation. Over-detailed rule files reduce success + increase cost → **failure-backed instructions only** (add a rule only after a demonstrated recurrent error). CoT can degrade simple instruction-following precision (CoT paradox).

**Conclusions:** role specialization is valid but needs explicit scope boundaries; human verification of agent-generated outputs remains indispensable; a fourth LLM-as-judge role is a promising extension.

| Verdict | **ADOPT** explicit role coordination + HITL verify + prompt-hardening. Case study — no mandatory product install; pattern only. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.12311-the-role-specialization-model-rsm-coordinating-l.pdf`
