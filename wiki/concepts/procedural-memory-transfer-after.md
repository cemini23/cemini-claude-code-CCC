---
title: Procedural memory transfer — AFTER benchmark findings
type: concept
tags: [concept, procedural-memory, skills, enterprise, k124]
keywords: [2606.23127, after, specialization, generalization]
related:
  - sources/arxiv-procedural-memory-after-2606.23127.md
  - concepts/skill-vetting.md
  - entities/tools/claude-mem.md
  - concepts/continual-harness-online-self-improvement.md
  - entities/skills/tech-debt-audit.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/dual-representation-agent-memory.md
  - entities/patterns/full-prompt-goal-template.md
  - sources/brief-k124-harness-policy-hands-on-2026-06-24.md
  - concepts/modular-instruction-memory-learnable-selection.md
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
  - sources/arxiv-memharness-reconstructed-memory-2607.28272.md
  - sources/arxiv-artanno-bidirectional-hai-annotation-2608.05026.md
  - concepts/bidirectional-hai-skill-evolution.md
  - entities/tools/artanno.md
maturity: draft
created: 2026-06-24
updated: 2026-08-06
---

## Relations

- `@sources/arxiv-procedural-memory-after-2606.23127.md` — AFTER benchmark paper
- `@concepts/skill-vetting.md` — Phase-0 before promoting distilled procedures to skills

## Raw Concept

When does procedural memory produce reusable skills vs source-context overfitting?

## Narrative

**AFTER** (2606.23127) evaluates procedural memory on **specialization** (in-context gain) vs **generalization** (held-out task, cross-role, cross-model transfer).

| Finding | Implication for CCC |
|---------|---------------------|
| +3.7–6.7 pts after one refinement round | Worth one wiki_lint + backlink pass after skill harvest |
| Diverse multi-model traces → 73.1% cross-model | Don't distill skills from a single model/session only |
| Narrow experience → train↑ test↓ | Per-repo skills need cross-wiki validation before `entities/skills/` promotion |

**Cemini rule [TENTATIVE]:** promote workflow to SKILL.md only after ≥2 independent sessions or wikis demonstrate reuse.

### K252 BiHAA — Interaction-Driven Evolution (2026-08-06)

K252 ArtAnno extends AFTER with bidirectional augmentation: AI assists humans; humans distill trajectories into skills/KB. Promotion still requires step 12 gate via `@concepts/skill-vetting.md`. See `@concepts/bidirectional-hai-skill-evolution.md`.

## Snippets

> "Skills extracted from narrow experience may work in their source setting yet fail when the context changes."
> — [Source: arxiv-2606.23127, retrieved 2026-06-24]
