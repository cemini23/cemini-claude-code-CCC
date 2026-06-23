---
title: Dual-agent cross-model verified protocol translation (arXiv 2606.20120)
type: source
tags: [source, arxiv, cross-model, verification, lab-automation, k123]
keywords: [2606.20120, parser-agent, validator-agent, microplate, elisa]
related:
  - concepts/cross-model-verified-agent-translation.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/specification-driven-scientific-workflow-management.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- `@concepts/cross-model-verified-agent-translation.md` — harness generalization
- `@concepts/gatekeeper-layered-agent-evaluation.md` — layered verification peer

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform |
| **Authors** | Choi et al. (KIMM, South Korea) |
| **arXiv** | 2606.20120v1 |
| **Location** | `raw-sources/arxiv-2606.20120-2606-20120v1-dual-agent-framework-for-cross-mode.pdf` |
| **Retrieved** | 2026-06-23 |
| **Read status** | read (dual-agent loop, 7×3 model sweep) |

## Narrative

**Problem:** Natural-language lab protocols vs device control commands — semantic gap for microplate automation (well mapping, replicates, parallel dispensing).

**Architecture:**
1. **Parser Agent** — NL protocol → structured representation
2. **Rule-based mapping engine** — deterministic device commands from platform constraints
3. **Validation Agent (heterogeneous LLM)** — completeness, parameter accuracy, execution order; self-correction loop on failure

**Eval:** 7 Parser × 3 Validator model sweep on ELISA protocols; demonstrated Bradford assay on robotic platform.

**CCC steal:** cross-model verification (parser ≠ validator) + deterministic mapping layer between NL and execution — parallels OpenSpec spec + lint gate. **REFERENCE** only (lab robotics domain).

## Snippets

> "A heterogeneous LLM Validation Agent verifies completeness, parameter accuracy, and execution order, and triggers a self-correction loop with structured feedback when errors are detected."
> — [Source: arxiv-2606.20120-2606-20120v1-dual-agent-framework-for-cross-mode.pdf, retrieved 2026-06-23]
