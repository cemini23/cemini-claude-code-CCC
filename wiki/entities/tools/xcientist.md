---
title: XCIENTIST — research harness for AI scientists
type: entity
tags: [entity, tool, research-harness, ai-scientist, k122]
keywords: [2606.18874, OpenDFM, xcientist, paper-graph, validation-contract]
related:
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
  - concepts/claim-drift-automated-research.md
  - concepts/externalized-research-synthesis-validation.md
  - entities/tools/deep-scientist.md
  - entities/tools/autoresearch-claw.md
  - entities/tools/openspec.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/agent-completion-verification-gates.md
  - concepts/code-as-agent-harness.md
  - entities/tools/paperclaw.md
  - sources/arxiv-paperclaw-autonomous-research-2606.22610.md
maturity: draft
created: 2026-06-22
updated: 2026-06-24
---

## Relations

- `@sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md` — paper provenance
- `@concepts/claim-drift-automated-research.md` — claim drift taxonomy
- `@concepts/externalized-research-synthesis-validation.md` — architecture synthesis
- `@entities/tools/openspec.md` — CCC spec-before-code parallel (lighter weight)

## Raw Concept

Official implementation of arXiv **2606.18874** — externalizes literature synthesis and experiment validation for automated research.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/OpenDFM/Xcientist |
| **License** | MIT [CONFIRMED — gh api 2026-06-22] |
| **Stars** | ~20 (early) |
| **Project page** | https://kotohanon.github.io/Xcientist/ |
| **Maintainer** | X-LANCE Lab, SJTU |

**Stack:** Paper graph infrastructure + research harness (literature review, MCTS ideation, contract-governed experiment agent, report audit) + web UI.

**Phase-0 (K122):** clone + license verify — **2 pass**.

**Adoption verdict:** **REFERENCE** — steal claim-drift taxonomy, validation contracts, trajectory eval for CCC wiki ingest and OpenSpec workflows. **NO-GO** prod install on cemini-librarian/prod (domain-specific ML research stack; overlaps conceptually with wiki ingest but different runtime).

**Compare:** `@entities/tools/deep-scientist.md`, `@entities/tools/autoresearch-claw.md` — hypothesis loops without full process-accountability layer.

## Snippets

> "Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness"
> — [Source: github.com/OpenDFM/Xcientist README, retrieved 2026-06-22]
