---
title: Specification-driven scientific workflow management — Pegasus AI pipeline
type: concept
tags: [concept, specification-driven, scientific-workflow, pegasus, k118]
keywords: [2606.18425, intent-design-implementation, validation-plan]
related:
  - sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md
  - entities/tools/pegasus-ai-plugin-marketplace.md
  - entities/tools/openspec.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/agents-all-the-way-down-custom-methodology.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/agent-completion-verification-gates.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/mcp-adaptive-systems-context-survey.md
  - concepts/mcp-context-optimization.md
  - concepts/handoff-validity-agent-harness.md
  - sources/arxiv-agentic-eda-handoff-2606.19795.md
  - concepts/externalized-research-synthesis-validation.md
  - concepts/claim-drift-automated-research.md
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
  - entities/tools/xcientist.md
  - concepts/cross-model-verified-agent-translation.md
  - sources/arxiv-dual-agent-cross-model-protocol-translation-2606.20120.md
  - sources/arxiv-paperclaw-autonomous-research-2606.22610.md
  - entities/tools/paperclaw.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - sources/arxiv-bioinsight-multi-agent-biomedical-2606.20997.md
maturity: draft
created: 2026-06-18
updated: 2026-06-24
---

## Relations

- `@sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md` — RENCI/USC ISI paper
- `@entities/tools/pegasus-ai-plugin-marketplace.md` — pegasus-ai skills marketplace
- `@entities/tools/openspec.md` — CCC spec-before-code harness
- `@entities/patterns/full-prompt-goal-template.md` — pinned done criteria
- `@concepts/agents-all-the-way-down-custom-methodology.md` — P3 prototype → P4 harvest
- `@concepts/llm-as-code-agentic-programming.md` — program vs LLM orchestrator contrast
- `@concepts/agent-completion-verification-gates.md` — validation plan before execution

## Raw Concept

How do we generate complex workflows without opaque direct-to-code LLM synthesis?

## Narrative

**Intent → design → implementation** separation [2606.18425]:

| Stage | Artifact | CCC analogue |
|-------|----------|--------------|
| Intent | Prompt + dataset refs | `/goal` envelope |
| Design | Structured spec + validation plan | OpenSpec proposal |
| Implementation | Wrappers, DAG, containers | Code after spec approval |

**Spec contents:** workflow structure, dependencies, **validation plan** (experiments, metrics, expected figures), resolved design decisions, phased roadmap.

**Steal-for CCC ingest/harness:**

1. Never skip spec artifact — align with OpenSpec + ingest discussion ritual
2. Record design decisions in `wiki/log.md` when choosing orchestration patterns
3. AI debug agent pattern → `@concepts/failed-trajectory-harness-repair.md` closed-loop

**Domain:** Pegasus/HTCondor scientific pipelines — **not** Cemini prod. Plugin marketplace Apache-2.0 — CONDITIONAL-GO reference only.

**K122:** XCIENTIST **validation contracts** per experiment step extend spec-driven pattern — each step needs acceptance criteria + repair trace; pairs with `@concepts/claim-drift-automated-research.md` claim-boundary audit.

## Snippets

> "Unlike direct code synthesis, this specification is a human-readable artifact, allowing users to validate and refine the workflow design prior to execution."

> "Makes the generated workflow not only executable but also checkable and incrementally implementable."
