---
title: "CordisBench — component lifecycles in dynamic agent harnesses (CCC K336)"
type: source
tags: [source, arxiv, harness-lifecycle, component-teardown, eval-axis, plugin, policy, k336]
keywords: [2609.01600, CordisBench, component lifecycle, teardown order, scale degradation, deterministic semantics, dependency graph, 1200 questions]
related:
  - concepts/harness-component-lifecycle-reasoning.md
  - concepts/cross-process-plugin-agent-harness.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- `@concepts/harness-component-lifecycle-reasoning.md`
- `@concepts/cross-process-plugin-agent-harness.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CordisBench: Evaluating Component Lifecycle Reasoning in Dynamic Agent Harnesses |
| **arXiv** | 2609.01600 (cs.AI, 2026-09-02) |
| **Authors** | CordisBench authors (see paper) |
| **Venue** | arXiv preprint |
| **Code** | Paper cites GitHub + Hugging Face — **no public SPDX repo found at Phase-0** → **WATCH** until SPDX; no clone this wave |
| **Retrieved** | 2026-09-02 |

## Narrative

**Verdict: ADOPT eval axis — teardown order and dependency propagation in dynamic harnesses; prefer execution verify over LLM lifecycle reasoning at scale.**

CordisBench evaluates whether agents reason correctly about **component lifecycles** in dynamic harnesses — install, configure, interact, and **tear down** plugins/modules whose dependencies affect final system state. The benchmark comprises **1,200 questions** across lifecycle scenarios; **528 are executable** against a deterministic reference semantics (Cordis execution engine).

**Findings (the steals):**

- **Teardown order changes final state** — removing components in different orders yields different end states when dependencies exist; models must reason about **ordering**, not only presence/absence.
- **Scale degradation** — models handle small systems (≈2 components) but accuracy drops as interactions scale (up to ≈32 components).
- **Deterministic reference semantics match execution on all 528 executable questions** — when a formal lifecycle spec exists, **compute or execute-verify** instead of trusting LLM anticipation of teardown effects.
- **LLM lifecycle reasoning does not scale** — parametric "common sense" about plugins fails where dependency graphs grow; formal semantics + execution beat model prediction.

CCC policy lines: treat dynamic harness changes as **dependency + teardown-order** problems; prefer deterministic execution verify when spec available (pairs K327 Logos: append-only transcript, no repeated effect at tool-call boundaries). Paper cites public artifacts but **no SPDX found** → WATCH; eval runtime `wont_wire`; concept `policy_wired`.

| Confidence | `[CONFIRMED]` — benchmark design and scale results from the paper; SPDX status `[NEEDS VERIFICATION 2026-09-02]` |
|------------|------------|

## Snippets

> "Teardown order changes final state when component dependencies exist — lifecycle reasoning is an ordering problem, not a presence problem." [Source: arXiv 2609.01600 — core finding]

> "Models degrade as interaction scale grows from small systems to dozens of components." [Source: arXiv 2609.01600 — scale degradation]

> "Deterministic reference semantics match Cordis execution on all 528 executable questions — prefer execution verify over LLM lifecycle anticipation when formal spec exists." [Source: arXiv 2609.01600 — eval methodology]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.01600-cordisbench-can-language-models-reason-about-com.pdf` |
|--------------|------------------------------------------------------------------------|
