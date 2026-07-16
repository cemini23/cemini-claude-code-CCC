---
title: "Do Agent Optimizers Compound? Continual-Learning Eval on Terminal-Bench 2.0"
type: source
tags: [source, arxiv, harness-optimization, continual-learning, gepa, meta-harness, relai-vcl, k171]
keywords: [2607.14004, compounding, regression control, Terminal-Bench, RELAI]
related:
  - concepts/agent-optimizer-compounding-and-regression-control.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/failure-mode-harness-adaptation-mapping.md
  - concepts/retrospective-harness-optimization-rho.md
  - entities/tools/relai-continual-learning-terminal-bench.md
  - sources/brief-k171-agent-optimizer-compounding-2026-07-16.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
---

## Relations

- `@concepts/agent-optimizer-compounding-and-regression-control.md` — synthesized steal
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — K169 sibling eval rigor (static vs continual)
- `@concepts/continual-harness-online-self-improvement.md` — continual harness cluster
- `@entities/tools/relai-continual-learning-terminal-bench.md` — Phase-0 repo (NO-GO license)
- `@sources/brief-k171-agent-optimizer-compounding-2026-07-16.md` — prod brief stub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0 |
| **Author** | Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi (RELAI.ai) |
| **Type** | arXiv technical report, cs.AI |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.14004-do-agent-optimizers-compound-a-continual-learnin.pdf` | **Retrieved** | 2026-07-16 |
| **arXiv** | 2607.14004v1 |
| **Pages** | 16 |
| **Read status** | read |
| **Code** | `github.com/relai-ai/Continual-Learning-Terminal-Bench` |

## Narrative

### Thesis

Published harness-optimizer gains are usually **one-shot** on a fixed bench. Production agents are re-optimized as new failures/tasks arrive. The **compounding question**: after one optimization round, can the same method be applied again on an expanded task stream **without eroding** prior gains?

### Protocol

Two-phase continual-learning eval on hard Terminal-Bench 2.0 tasks. Methods compared under **identical optimization budgets**: GEPA, Meta Harness, RELAI-VCL (Verifiable Continual Learning). Metrics: Phase-1 pass, transfer to unseen Phase-2 tasks, re-opt after folding new tasks, lifelong average.

### Results (Table 1)

| Agent | Phase 1 | Transfer | Re-opt | Lifelong avg |
|-------|---------|---------|--------|--------------|
| Baseline | 62.5% | 56.8% | 56.8% | 58.7% |
| GEPA | 70.8% | 54.5% (**< baseline**) | 72.7% | 66.0% |
| Meta Harness | 66.6% | 68.2% | 59.1% (fails to improve) | 64.6% |
| **RELAI-VCL** | **79.2%** | **72.7%** | **77.3%** | **76.4%** |

Key claim: gains **compound only when regression control is inside the optimization loop** (inductive bias against non-generalizing shortcuts). GEPA looks good statically then **overfits**; Meta Harness transfers but stalls on second budget; only VCL does both transfer + continue improving.

### CCC reading (with K169)

K169 showed harness evolution often fails matched-budget / held-out tests in the **static** setting. This paper adds the **continual** axis: even methods that win Phase-1 can destroy transfer. For Cemini: any GEPA-style / Meta-Harness-style / auto-harness loop must include **explicit regression gates** before promoting edits (pair K162 execution verification + K169 held-out).

**Magnitude claims on RELAI-VCL remain vendor-adjacent** — treat as `[TENTATIVE]` until independent replication; the **negative results on GEPA transfer** and the **regression-in-the-loop** design lesson are the durable steals.

## Snippets

> "optimization gains compounded only when regression control was built into the optimization loop" — Abstract

> "GEPA's optimized agent transfers below the unoptimized baseline" — Abstract

> — [Source: arxiv-2607.14004, retrieved 2026-07-16]
