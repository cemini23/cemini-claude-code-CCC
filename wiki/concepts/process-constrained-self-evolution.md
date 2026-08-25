---
title: "Process-constrained self-evolution — typed banks, frozen snapshots, process critics"
type: concept
tags: [concept, self-evolution, memory, evaluation, safety, clinical, k307]
keywords: [mediskill-evo, typed banks, frozen test-time snapshot, process critic, controller safety, 2608.23397]
related:
  - sources/arxiv-mediskill-evo-process-constrained-2608.23397.md
  - concepts/skill-misevolution.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-mediskill-evo-process-constrained-2608.23397.md`
- `@concepts/skill-misevolution.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Question answered: how can an agent improve its own process knowledge without fine-tuning and without misevolving? Source: arXiv 2608.23397 (CCC K307). Pairs K237 misevolution gates + K162 external-eval contract.

## Narrative

Single-bag experience memory (everything behind one retrieval interface) conflates knowledge types with different risk profiles. MediSkill-Evo's recipe:

1. **Typed banks** — Skills / Process Rules / Schemas / Measurement kept separate; each type gets its own scope and safeguards.
2. **Frozen test-time snapshot** — the evaluation suite is published *before* evolution runs; evolved candidates are scored against a snapshot they cannot influence.
3. **Process critic with veto** — a Process-Constrained Preference Harness binds evidence to source, rejects controller-invalid candidates outright, and ranks what survives through safety-prioritized critique.

Result shape (clinical, vs AgentClinic baseline): diagnosis accuracy 61.33→69.00, treatment-intent coverage 33.62→66.44, critical failures 31.00→16.33 — improvement **with** fewer critical failures, i.e., the constraint is where the safety comes from.

CCC mapping: this is the pattern any future `.cursor/skills` or harness self-improvement loop must follow — never evolve skills unattended, freeze evals first, and give a deterministic critic veto power over candidates.

## Snippets

> "A Process-Constrained Preference Harness binds evidence to its source, rejects controller-invalid candidates, and ranks actions through a safety-prioritized Clinical Process Critic." [Source: arXiv 2608.23397 abstract]
