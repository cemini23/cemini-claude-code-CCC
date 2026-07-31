---
title: PaperClaw — autonomous research lifecycle harness
type: entity
tags: [entity, tool, research-harness, paperclaw, k124]
keywords: [2606.22610, sequenxai, domain-idea-paper, hypothesis-map]
related:
  - sources/arxiv-paperclaw-autonomous-research-2606.22610.md
  - concepts/externalized-research-synthesis-validation.md
  - entities/tools/xcientist.md
  - entities/tools/deep-scientist.md
  - entities/tools/autoresearch-claw.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/code-as-agent-harness.md
  - sources/brief-k124-harness-memory-research-cluster-2026-06-24.md
  - entities/tools/clarus.md
  - sources/arxiv-clarus-scientific-collaboration-infrastructure-2606.30246.md
  - concepts/web-scale-scientific-collaboration-infrastructure.md
maturity: draft
wire_status: wont_wire
wire_target: "REFERENCE shelf"
created: 2026-06-24
updated: 2026-07-31
---

## Relations

- `@sources/arxiv-paperclaw-autonomous-research-2606.22610.md` — paper provenance
- `@entities/tools/xcientist.md` — parallel research harness (claim drift focus)
- `@entities/tools/deep-scientist.md` — hypothesis-loop peer

## Raw Concept

Official implementation of arXiv **2606.22610** — Domain → Idea → Hypothesis → Paper autonomous research with HITL refinement.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/SequenxAI/PaperClaw |
| **License** | MIT [CONFIRMED — gh api 2026-06-24] |
| **Stars** | ~7 (early) |
| **Project** | https://sequenxai.github.io/PaperClaw |
| **Maintainer** | SequenxAI / University of Tokyo |

**Pipeline:** domain curation (live indexes) → idea spec + main-result contract → stoppable hypothesis map (propose/test/reflect) → full-lifecycle memory → venue-compliant paper. Web + desktop + CLI; in-cycle research assistant at every stage.

**Phase-0 (K124):** clone + MIT license — **PASS**.

**Adoption verdict:** **CONDITIONAL-GO** laptop eval — steal hypothesis-map stoppability, lifecycle memory, citation validation for CCC wiki research workflows. **NO-GO** prod (overlaps XCIENTIST; academic paper domain).

**Compare:** `@entities/tools/xcientist.md` (validation contracts + claim drift), `@entities/tools/deep-scientist.md` (lighter hypothesis loop). **Clarus contrast (K135):** `@entities/tools/clarus.md` — open collaboration network vs closed pipeline.

## Snippets

> "Domain → Idea → Paper, autonomously."
> — [Source: arxiv-2606.22610 tagline, retrieved 2026-06-24]
