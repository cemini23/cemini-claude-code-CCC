---
title: "DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents (CCC K413)"
type: source
tags: [source, arxiv, k413]
keywords: [2609.40306, k413]
related:
  - concepts/execution-contract-failure-attribution.md
  - briefs/2026-10-01_ccc-k411-k415-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@concepts/execution-contract-failure-attribution.md`
- `@briefs/2026-10-01_ccc-k411-k415-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents |
| **arXiv** | 2609.40306 (2026-09) |
| **Retrieved** | 2026-10-01 |

## Narrative

**Verdict: REFERENCE (cross-domain; 3 primitives transfer).**

**DynaHarness — a command contract that records its own evidence.** A slow brain (Qwen3-VL-4B) proposes a capability and symbolic arguments; a **fast brain** grounds and monitors at 2 Hz, **refuses unresolved actions, substitutes capabilities, and requests replans**, while a 20 Hz controller executes. The invention is the **physical execution contract**: every robot-facing command is bounded by budget and lease, and every grounding, refusal, substitution, and completion is **recorded**. That record then does double duty — **offline failure attribution** localizes a fault to one of N ordered layers, and **paired regression checks** gate whether the resulting capability revision is admitted. The loop closes only when a revision passes regression; a later full-round confirmation **rejected** a candidate that had won on the targeted cells. On LIBERO-Pro: 75.2% on 800 fresh states vs 17.5% for the frozen policy. **Cross-domain** (robotics), so REFERENCE — but three primitives transfer directly: a **bounded execution contract**, **attribution from recorded evidence rather than from episode outcome**, and **paired-regression admission** for any self-modification. That last one is the CCC lesson: the candidate that won on its target lost on the full round, and was correctly kept out. Pairs K406 Assay (mechanical gate) / K403 Tracekit (evidence ledger) / `test-time-world-model-validate-before-act` / K404 harness learning. **No code repo** — project page only. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Failure attribution localizes faults in these records and directs targeted revisions of reusable capabilities or execution mechanisms. Paired regression checks govern admission or rejection, closing the self-evolution loop." [Source: arXiv 2609.40306 (retrieved 2026-10-01)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.40306-dynaharness-a-dynamic-physical-harness-for-self.pdf` |
