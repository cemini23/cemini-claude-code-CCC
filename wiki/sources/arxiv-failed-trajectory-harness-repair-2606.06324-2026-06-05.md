---
title: Failed trajectories to reliable LLM agents — harness flaw repair (arXiv 2606.06324)
type: source
tags: [source, arxiv, harness, agent-reliability, harnessfix, k100]
keywords: [2606.06324, harnessfix, htir, etclovg]
related:
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - concepts/code-as-agent-harness.md
  - sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md
  - sources/arxiv-maven-agentic-tool-calling-2605.30738.md
  - entities/tools/lazy-tool.md
maturity: draft
read_status: deep-read
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- `@concepts/failed-trajectory-harness-repair.md` — CCC synthesis
- `@concepts/etclovg-harness-layers.md` — ETCLOVG taxonomy extracted here

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws |
| **Authors** | Chen, Wang, Liu, Wang, Qing Wang (ISCAS) |
| **arXiv** | 2606.06324 |
| **PDF** | `raw-sources/arxiv-2606.06324-from-failed-trajectories-to-reliable-llm-agents.pdf` |
| **Retrieved** | 2026-06-05 |
| **Read status** | deep-read |

## Narrative

**HarnessFix** — four-agent loop: trace abstraction → diagnosis → scoped repair → validation. Core artifact: **HTIR** (Harness-aware Trace IR) with TraceSteps, temporal/provenance/control-flow links, and ETCLOVG layer facets. Repairs use layer-specific **operators** (Table II) with flaw-specific specs and regression-bounded acceptance (target flaw reduction + max new regressions).

Benchmarks: SWE-Bench Verified, Terminal-Bench 2.0 Verified, GAIA, AppWorld — reported +15.2%–50.0% over initial harnesses [TENTATIVE — not replicated locally].

## Snippets

> "We propose HarnessFix, a trace-guided framework for diagnosing agent failures and repairing agent harnesses."
> — [Source: arxiv-2606.06324 abstract, retrieved 2026-06-05]

> "TABLE I: Harness layers and their responsibilities." — Execution, Tool Interface, Context and Memory, Lifecycle and Orchestration, Observability, Verification and Evaluation, Governance and Security.
> — [Source: arxiv-2606.06324 §I, retrieved 2026-06-05]

> "TABLE II: Repair operators and associated flaws organized by harness layer."
> — [Source: arxiv-2606.06324 §III-C, retrieved 2026-06-05]

> "TargetImprovement: ΔD_target ≥ δ_min … RegressionBound: R_new ≤ r_max"
> — [Source: arxiv-2606.06324 §III-D2, retrieved 2026-06-05]

## Dead Ends

- **Full HarnessFix adoption on Cemini laptop** — research codebase not evaluated; steal vocabulary + manual flaw-record discipline instead.
