---
title: Gatekeeper layered agent evaluation — rubric + consistency metrics
type: concept
tags: [concept, evaluation, gatekeeper, harness, k121]
keywords: [2606.18422, design-entropy, eval-harness-trust]
related:
  - sources/arxiv-gatekeepers-layered-eval-quantum-vqe-2606.18422.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - concepts/claim-drift-automated-research.md
  - concepts/externalized-research-synthesis-validation.md
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
  - concepts/cross-model-verified-agent-translation.md
  - sources/arxiv-dual-agent-cross-model-protocol-translation-2606.20120.md
  - concepts/recoverable-tool-reliability-hazards.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/arxiv-toolbench-x-tool-environment-unreliability-2606.25819.md
  - sources/brief-k121-tokenpilot-safeclaw-gatekeepers-prod-2026-06-21.md
  - concepts/agentic-orchestration-options-abpm.md
  - sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md
  - concepts/orchestration-option-quantitative-metrics.md
maturity: draft
created: 2026-06-21
updated: 2026-07-01
---

## Relations

- `@sources/arxiv-gatekeepers-layered-eval-quantum-vqe-2606.18422.md` — UBC quantum VQE paper
- `@concepts/agent-completion-verification-gates.md` — runtime completion proof
- `@concepts/agent-rubrics-self-correction.md` — rubric-driven review
- `@concepts/failed-trajectory-harness-repair.md` — harness bugs in eval traces
- `@concepts/seagym-self-evolving-harness-evaluation.md` — harness eval environments

## Raw Concept

How do we evaluate agent outputs when failures are structured and the harness itself can hallucinate?

## Narrative

**Layered evaluation** [TENTATIVE — 2606.18422] (quantum VQE domain, domain-agnostic steal):

| Layer | Function | CCC analogue |
|-------|----------|--------------|
| Gatekeeper rubric | Screen before expensive steps | OpenSpec AC, premortem, skill-vetting |
| Fidelity check | Compare to reference implementation | `wiki_lint.py`, test suites |
| Design entropy | Run-to-run consistency | Repeated eval variance (super-audit) |

**Harness-in-the-loop:** eval platform silent fallback templates attributed failures to models — applies to CCC ingest evals and subagent return verification.

**K122 claim-boundary audit:** XCIENTIST report-writing audits source fidelity before claims ship — complementary layer to gatekeeper screening; see `@concepts/claim-drift-automated-research.md`.

**K136 regulated flows:** Blood-donation case study — deterministic parallel services enforce hard stops (consent abort); gatekeeper + process frame (**OO4**) before LLM Q&A subtasks. See `@concepts/agentic-orchestration-options-abpm.md`.

**Verdict:** **REFERENCE** — adopt gatekeeper + consistency layers in eval briefs; no quantum stack install.

## Snippets

> "Two apparent model failures originated in the harness through silent fallback-template substitution."

> — [Source: arxiv-2606.18422-gatekeepers-and-hallucinations-a-layered-evaluat.pdf]
