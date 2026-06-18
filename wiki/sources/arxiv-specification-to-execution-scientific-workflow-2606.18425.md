---
title: Specification to execution — AI-assisted Pegasus scientific workflows (arXiv 2606.18425)
type: source
tags: [source, arxiv, pegasus, scientific-workflow, mcp, k118]
keywords: [2606.18425, pegasus-ai, specification-driven, htcondor, federated-learning]
related:
  - concepts/specification-driven-scientific-workflow-management.md
  - entities/tools/pegasus-ai-plugin-marketplace.md
  - entities/tools/openspec.md
  - concepts/mcp-adaptive-systems-context-survey.md
  - concepts/agent-completion-verification-gates.md
  - concepts/claude-plugins-catalog-patterns.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/skill-vetting.md
  - concepts/mcp-context-optimization.md
maturity: draft
read_status: read
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- `@concepts/specification-driven-scientific-workflow-management.md` — CCC synthesis
- `@entities/tools/pegasus-ai-plugin-marketplace.md` — pegasus-ai Claude plugin
- `@entities/tools/openspec.md` — spec-before-code parallel (CCC harness)
- `@concepts/mcp-adaptive-systems-context-survey.md` — MCP orchestration context

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | From Specification to Execution: AI Assisted Scientific Workflow Management |
| **Authors** | Thareja et al. (RENCI UNC); Safri, Mayani, Deelman (USC ISI) |
| **arXiv** | 2606.18425v1 [cs.SE] |
| **Location** | `raw-sources/arxiv-2606.18425-from-specification-to-execution-ai-assisted-scie.pdf` |
| **Retrieved** | 2026-06-18 |
| **Read status** | read (pipeline, pegasus-ai skills, FL eval, MCP architecture) |

## Narrative

**Problem:** Scientific WMS (Pegasus, Nextflow, Galaxy) excel at **execution** but assume workflows are pre-defined; design/debug remain manual. Direct LLM code synthesis lacks transparency and WMS integration.

**Approach — three stages:**

1. **Prompt + dataset description** — capture intent without WMS expertise
2. **Structured specification** — human-readable design: dependencies, validation plan (metrics/figures), design decisions, implementation roadmap
3. **Code generation** — workflow defs, wrappers, configs, containers after spec approval

**pegasus-ai plugin** (`github.com/pegasus-isi/claude-plugin-marketplace`) — eight skills: scaffold, wrapper, dockerfile, debug, review, convert, help, kiso.

**Runtime:** Pegasus WMS + HTCondor on FABRIC testbed (9 GPUs, 4 sites). **AI debugging agent** — log analysis, failure patterns, closed-loop resubmit. **MCP gateway** — remote submission/monitoring (architecture described; quant eval deferred).

**Eval:** Federated learning medical imaging (TCIA + NIH ChestX-ray). Thousands of jobs; non-expert users reached expert-level sub-workflow patterns. Compared **Claude Code**, **Codex**, **Opencode/Kimi** for development cost.

**CCC relevance:** specification-before-implementation steal for OpenSpec/`/goal`; MCP gateway pattern for conductor; **REFERENCE** for Pegasus install (not Cemini prod stack).

## Snippets

> "The specification also records a validation plan … design decisions … and an implementation roadmap with phases and status."

> "Separating workflow intent, design, and implementation through a structured specification phase."
