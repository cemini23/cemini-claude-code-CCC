---
title: "Agentified eval evidence-tree harness (K289)"
type: concept
tags: [concept, evaluation, agentified-benchmark, evidence-tree, world-model, harness, k289]
keywords: [2608.16859, HarnessEval-W, agentified eval, evidence tree, sub-agent routing, parent validation, world-model benchmark]
related:
  - sources/arxiv-harnesseval-w-visual-worlds-2608.16859.md
  - entities/tools/harnesseval-w.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/bounded-authority-auditable-trajectories.md
  - sources/arxiv-llm-agents-software-systems-security-slr-2608.28490.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-18
updated: 2026-08-31
---

## Relations

- `@sources/arxiv-harnesseval-w-visual-worlds-2608.16859.md`
- `@entities/tools/harnesseval-w.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — K162 verification hierarchy (no closed self-eval)
- `@concepts/measurement-integrity-mcp-security-eval.md` — K277 measurement integrity

## Raw Concept

A benchmark that returns only a scalar score is unauditable — the number can't be explained or verified. What if evaluation were itself a harness: decompose the case, spawn tool-equipped sub-agents, and aggregate validated evidence into a tree that justifies the score?

## Narrative

HarnessEval-W (arXiv 2608.16859) turns evaluation into a **transparent evidence tree** rather than a scalar-only rubric. Per case, it interprets context, routes to skills, decomposes into measurable subproblems, spawns specialized sub-agents with tailored context + diagnostic tools, and has a **parent agent validate the gathered evidence** before the final verdict. The pipeline can recurse.

### Steal (ADOPT)

1. **Eval = evidence tree, not a scalar.** The deliverable is what was tested, which tool supplied the visual grounding, and the logical chain justifying the score. A score without this chain has no persuasive power.
2. **Route case → skills → sub-agents with tools.** No fixed rubric fits all cases. Interpret each case's context, route to the skills that can legitimately evaluate it, and decompose into measurable subproblems delegated to specialized sub-agents (e.g., collision → bounding-box tracking + temporal-intersection + velocity estimation).
3. **Parent validates before verdict.** The parent agent checks evidence returned by all sub-agents before merging — a verification gate between evidence collection and scoring (pairs K162: no closed self-eval).
4. **Case construction is itself agentic + validated.** Cases are authored by sampling a scene taxonomy → grounding actions → validating each candidate before acceptance. Only groundable cases enter the benchmark (pairs K277 measurement integrity).
5. **Fine-grained diagnosis, not ranking alone.** The output explains *where and why* a model fails (e.g., a video generator adapted into a world model redistributes capability rather than uniformly improving).

### Why this pairs K162 and K277

K162's verification hierarchy bans closed self-eval loops; HarnessEval-W operationalizes the *effective* version — the parent validates sub-agent evidence before it becomes a score, and the reasoning chain is inspectable. K277's measurement integrity demands labels bind to executed behavior; HarnessEval-W's evidence tree does exactly that for world-model eval, binding each sub-score to a specific tool's visual grounding.

### Local adopt

- **No clone** — `mirros-lab/harnesseval-w` null SPDX (no LICENSE in pyproject). **Policy only.** The evidence-tree eval pattern is the transferable unit.

| Verdict | **ADOPT** agentified eval harness: decompose case → specialized sub-agents + tools → validated evidence tree (not scalar-only rubric). `policy_wired`; no runtime clone. |
