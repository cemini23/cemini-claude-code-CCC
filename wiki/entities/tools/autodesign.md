---
title: "AutoDesign — meta-harness optimizer for long-horizon agentic design (Meituan / MBZUAI)"
type: entity
tags: [entity, tool, meta-harness, poster, mit, k281]
keywords: [k281, AutoDesign, DesignHarness, PosterBench, meta-harness-optimizer, MIT, meituan, mbzuai]
related:
  - sources/arxiv-metacaster-meta-harness-tsf-2608.23473.md
  - entities/tools/metacaster.md
  - sources/arxiv-autodesign-meta-harness-2608.13560.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/brief-k162-rsi-verification-hierarchy-2026-07-14.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
  - sources/brief-k237-meta-harness-vero-misevolution-2026-08-14.md
  - concepts/agent-as-intermediary-engineer.md
maturity: draft
wire_status: wont_wire
created: 2026-08-14
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-autodesign-meta-harness-2608.13560.md`
- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@sources/arxiv-metacaster-meta-harness-tsf-2608.23473.md`
- `@entities/tools/metacaster.md`

## Raw Concept

Phase-0 entity for CCC K281 — AutoDesign.

## Narrative

Repo `github.com/Yaxin9Luo/AutoDesign` — LICENSE file **MIT** on disk (gh API NOASSERTION — verify the file before clone; per SIP it is MIT). GitHub size ~43MB → clone to `.local/adopts/AutoDesign` as **GO REFERENCE** if SPDX-clean and <500MB. Steal: meta-harness loop (optimizer edits the harness from rollout feedback) **with HITL / external eval contract** — no closed self-rewrite of pass criteria (pairs K162). Poster / Image-gen runtime **`wont_wire`**.

**Phase-0:** `scripts/adopt_k281_phase0.sh`
