---
title: Procedural memory in LLM agents — AFTER benchmark (arXiv 2606.23127)
type: source
tags: [source, arxiv, procedural-memory, skills, k124]
keywords: [2606.23127, after, skill-transfer, enterprise]
related:
  - concepts/procedural-memory-transfer-after.md
  - concepts/skill-vetting.md
  - entities/tools/claude-mem.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/agent-memory-stack-comparison.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@concepts/procedural-memory-transfer-after.md` — specialization vs generalization synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation |
| **Authors** | Belikova et al. |
| **arXiv** | 2606.23127v1 [cs.AI] |
| **Benchmark** | AFTER — 382 enterprise tasks, 6 roles, 22 procedural skills |
| **Location** | `raw-sources/arxiv-2606.23127-pdf-managing-procedural-memory-in-llm-agents-arx.pdf` |
| **Retrieved** | 2026-06-24 |
| **Read status** | read (AFTER design + transfer findings) |

## Narrative

Introduces **AFTER** benchmark for procedural skill transfer: local improvement, cross-task, cross-role, cross-model generalization splits.

**Findings [TENTATIVE — single paper]:**
- One refinement round: +3.7–6.7 aggregate points
- Skills from **diverse multi-model traces**: 73.1% cross-model test accuracy — beats single-model sources
- Narrow experience → over-specialization (train↑ test↓); diverse experience → reusable skills

**CCC relevance:** eval discipline for SKILL.md harvest and claude-mem procedural distill — prefer diverse task traces before promoting skills to `entities/skills/`. **REFERENCE** — no AFTER install until benchmark artifact located.

## Snippets

> "Procedural memory is a promising direction: a reusable layer of instructions, procedures, and strategies distilled from prior trajectories."
> — [Source: arxiv-2606.23127-pdf-managing-procedural-memory-in-llm-agents-arx.pdf, retrieved 2026-06-24]

> "Skills evolved from diverse multi-model execution traces achieve 73.1% cross-model test accuracy, outperforming all single-model trace sources."
> — [Source: arxiv-2606.23127-pdf-managing-procedural-memory-in-llm-agents-arx.pdf abstract, retrieved 2026-06-24]
