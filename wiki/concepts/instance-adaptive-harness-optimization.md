---
title: "Turbo Harness: Instance-Adaptive Harness Optimization (CCC K415)"
type: concept
tags: [concept, k415]
keywords: [2609.40330, k415]
related:
  - sources/arxiv-turbo-harness-instance-adaptive-2609.40330.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-01_ccc-k411-k415-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@sources/arxiv-turbo-harness-instance-adaptive-2609.40330.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-01_ccc-k411-k415-sip-ready.md`

## Raw Concept

K415: CONDITIONAL-GO (MIT) — arXiv 2609.40330.

## Narrative

**Turbo Harness — one global harness is not enough.** Harness optimization usually produces a single harness applied uniformly to every instance. This work recycles the artifacts a completed outer-loop search already produced, summarizes them into a **playbook** of both successful *and* unsuccessful editing strategies, and trains a small **harness editor** (Qwen3.5-9B) to patch the global harness **per instance**. The editor runs **once per instance**, so overhead is small, and the tailored harness often needs fewer execution steps from the much larger execution model. Gains are large: SWE-smith-MR 50.7% → 64.0% with Claude Haiku 4.5, 70.7% → 88.0% with Gemini 3.7 Flash; top pass rate on Terminal-Bench 2.1. **The case studies carry the CCC lesson, and it is a sharp one:** the same harness knob has **opposite optima on different tasks**, and the editor's edits reach **executable loop code, not prompt wording** — it fires a verification gate at step 6 instead of 8, relaxes an aggressive submit gate to buy a real fix-and-verify budget, and teaches an edit detector to also recognize append redirection. Critically: **forcing tool use globally is a documented playbook anti-pattern that regresses the whole suite by 6.7%**, while being exactly right for one task. Pairs K404 harness learning / K409 meta-skills / K410 meta-reasoning / K169 harness-evolution baseline critique — note this is an *instance-adaptive* answer to that critique. **Phase-0: `Tyrion58/turbo-harness` MIT**, 3★, 0 forks, pushed 2026-09-30 — brand new. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.40330 locators." [Source: CCC K415 synthesis]
