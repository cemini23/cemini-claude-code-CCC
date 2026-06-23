---
title: Autonomous coding agents for enterprise data intelligence (DIA)
type: concept
tags: [concept, autonomous-coding-agent, enterprise-data, text-to-sql, k123]
keywords: [2606.19319, dia, aca, artifact-grounded, shared-memory]
related:
  - sources/arxiv-data-intelligence-agents-dia-2606.19319.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/code-as-agent-harness.md
  - concepts/agent-completion-verification-gates.md
  - concepts/claim-drift-automated-research.md
  - concepts/externalized-research-synthesis-validation.md
  - concepts/handoff-validity-agent-harness.md
maturity: draft
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- `@sources/arxiv-data-intelligence-agents-dia-2606.19319.md` — C3 AI DIA paper (2606.19319)
- `@concepts/llm-as-code-agentic-programming.md` — program-owned control flow peer
- `@concepts/claim-drift-automated-research.md` — artifact validation prevents drift

## Raw Concept

How should enterprise data workflows treat **autonomous coding agents** as the central abstraction instead of text-emitting LLM chains?

## Narrative

**ACA-first data intelligence** [TENTATIVE — 2606.19319]: three stages (interpret → schema → query) share one sandboxed coder + **shared memory** for experience reuse. Each stage surfaces **inspectable artifacts** for domain expert review — replaces lossy handoffs between owners, engineers, analysts.

### CCC steal-for

| DIA pattern | Cemini mapping |
|-------------|----------------|
| Generate-execute-validate-repair | Ingest pipeline + `wiki_lint.py` + Phase-0 scripts |
| Shared memory across agents | `wiki/`, claude-mem, conductor |
| Expert review gates | discuss-before-write, OpenSpec approval |
| Single ACA, NL instruction adaptation | Skills + rules vs per-benchmark fine-tuning |

**Verdict:** **REFERENCE** — C3 AI production system; steal artifact-grounded ACA pattern for harness eval prompts. **NO-GO** install DIA stack on cemini prod.

## Snippets

> "The first system, to our knowledge, to treat the ACA rather than the LLM as the central abstraction for data intelligence."
> — [Source: arxiv-2606.19319-data-intelligence-agents-interpreting-modeling-a.pdf, retrieved 2026-06-23]
