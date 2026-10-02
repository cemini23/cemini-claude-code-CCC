---
title: "YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents (CCC K416)"
type: source
tags: [source, arxiv, k416]
keywords: [2610.01097, k416]
related:
  - concepts/persistent-state-evidence-traceable-research.md
  - briefs/2026-10-02_ccc-k416-k420-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-02
---

## Relations

- `@concepts/persistent-state-evidence-traceable-research.md`
- `@briefs/2026-10-02_ccc-k416-k420-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents |
| **arXiv** | 2610.01097 (2026-10) |
| **Repo** | `PrayPrey/Your-Research-Agent` |
| **Retrieved** | 2026-10-02 |

## Narrative

**Verdict: ADOPT pattern; NO-GO clone (no license).**

**YouRA — research state as a durable object, not a byproduct of chat.** The paper's diagnosis: end-to-end research agents produce fluent papers whose claims diverge from the experiments actually run. It names three causes, and all three reduce to one absence — **the trajectory is never held as explicit, persistent, verifiable structure**: (1) context and evidence fragmentation, where state buried in conversation is vulnerable to truncation and hallucination; (2) **no structured failure memory**, so failures never become constraints on later work; (3) unreliable workflow control, because the same dialogue both does the work and decides when to stop, retry, or redesign. Three components answer it: a **Verification State Architecture (VSA)** holding hypotheses, gates, and evidence pointers; an **Independent Controller** that reads that state to drive lifecycle, recovery, and review while **separating control from execution**; and **Stateful Reflection** that logs failures as structured lessons and routes recovery through **bounded repair → redesign → reset**. Ablating any component lowers the score, and the two *core-state* removals (VSA, Controller) drop it below both baselines on two of three backbones. failure profiles differ by component: no-VSA produces numbers that disagree across sections and claims contradicting execution logs; no-Controller produces crashed runs reported as completed findings. **CCC relevance is direct** — this is K410's control/worker split plus K414's verified ledger plus K413's execution contract, applied to research rather than proofs, with the strongest claim being that **externalization is load-bearing, not stylistic**. Pairs K406 Assay (claim–evidence binding) / K409 meta-skills / `@concepts/specification-driven-scientific-workflow-management.md`. **Phase-0: `PrayPrey/Your-Research-Agent` NOASSERTION**, 1★, **~508 MB** — no license and a large tree → **no clone**. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "the research trajectory is not maintained as explicit, persistent, verifiable structure across the pipeline." [Source: arXiv 2610.01097 (retrieved 2026-10-02)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.01097-youra-a-persistent-state-architecture-for-eviden.pdf` |
