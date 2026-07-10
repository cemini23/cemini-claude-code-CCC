---
title: Orchestration option quantitative metrics — M, ABC, F1, traceability log
type: concept
tags: [concept, orchestration, metrics, abpm, k136]
keywords: [2606.31518, cyclomatic, abc-complexity, f1, traceability]
related:
  - sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md
  - concepts/agentic-orchestration-options-abpm.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/agent-completion-verification-gates.md
  - sources/brief-k136-agentic-orchestration-options-abpm-2026-07-01.md
  - entities/tools/simple-agentic-scenario.md
  - concepts/multilingual-long-horizon-agent-eval.md
  - sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md
maturity: draft
created: 2026-07-01
updated: 2026-07-10
---

## Relations

- `@concepts/agentic-orchestration-options-abpm.md` — OO1–OO4 framework
- `@sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md` — paper eval tables

## Raw Concept

How to compare agent orchestration designs quantitatively when choosing OO1 vs OO3 for a harness workflow?

## Narrative

arXiv **2606.31518** Sect. 4 proposes metrics for comparing orchestration realizations on the **same** scenario (light sensing OO1–OO6):

### Task specificity

| Metric | Definition | Interpretation |
|--------|------------|----------------|
| **Cyclomatic M** | \(M = E - N + 2P\) on surrounding process | Higher when more logic in process frame vs agent |
| **ABC** | \(\|ABC\| = \sqrt{A^2 + B^2 + C^2}\) — assignments, branches (activities/subprocesses), conditionals | Weighted variant can down-rank agent subprocesses |

OO1/OO2 → minimal M (single agent component). OO3/OO4 → higher M as rules move to process engine.

**CCC use:** compare scatter-gather + OpenSpec graphs vs single-session ingest — **comparative only**, not absolute quality score.

### Correctness

Precision **P**, recall **R**, **F1** over rule set **R** — TP/FP/FN on required lamp actions. OO4 reached F1≈0.97 vs OO1≈0.40 in paper table; deterministic OO5/OO6 = ground truth.

### Reactivity

**FNR** and average **R_s** (time to consequence). Paper: FNR uninformative; R_s confounded by model load — prefer harness timers over LLM latency assumptions.

### Traceability

Compare orchestrator log **L_o** vs ground-truth executed events **L_t** — same TP/FP/FN framing. Agent self-logs (OO1/OO2) underperform engine logs (OO3/OO4).

**CCC steal:** treat `wiki/log.md` + git commits + CI artifacts as **L_t**; never trust chat transcript alone as audit log.

## Snippets

> "Both M and ABC provide only a comparative measure between flows/orchestrations of the same process/workflow, and do not have any semantic meaning when considering a single orchestration in isolation."
> — [Source: arxiv-2606.31518-design-and-implementation-of-agentic-orchestrati.pdf Sect. 4, retrieved 2026-07-01]
