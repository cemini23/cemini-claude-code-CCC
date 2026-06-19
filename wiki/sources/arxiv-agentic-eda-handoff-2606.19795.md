---
title: Agentic EDA — handoff perspective survey (arXiv 2606.19795)
type: source
tags: [source, arxiv, handoff, eda, eacp, k119]
keywords: [2606.19795, handoff-validity, eacp, stage-bound, flow-bound]
related:
  - concepts/handoff-validity-agent-harness.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/agent-completion-verification-gates.md
  - concepts/subagent-orchestration.md
maturity: draft
read_status: read
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- `@concepts/handoff-validity-agent-harness.md` — harness generalization
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — silent handoff failure peer
- `@concepts/specification-driven-scientific-workflow-management.md` — workflow handoff contracts

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agentic Electronic Design Automation: A Handoff Perspective |
| **Authors** | Liu et al. (CUHK); Fengyu Yan (Primarius) |
| **arXiv** | 2606.19795v1 [cs.SE] |
| **Location** | `raw-sources/arxiv-2606.19795-agentic-electronic-design-automation-a-handoff-p.pdf` |
| **Retrieved** | 2026-06-19 |
| **Read status** | read (taxonomy, 82 systems, EACP five layers) |

## Narrative

**Organizing principle:** **handoff validity** — transferred object satisfies consumer acceptance conditions with sufficient context, evidence, and provenance.

**Three boundary classes** (82 systems surveyed):

| Class | Scope | Example coordination |
|-------|-------|----------------------|
| Stage-Bound | Single EDA stage | Generate–repair vs checker |
| Flow-Bound | Tools, sessions, pipeline | Orchestrate–transform; recover–resume |
| Organization-Bound | Knowledge/authority | Retrieve–answer with source grounding |

**EACP** (five-layer EDA Agent Communication Protocol — research agenda):

1. Agent Discovery — capability manifest + EDA compatibility scope
2. Agent Message — envelope with intent, correlation, evidence refs
3. Tool Invocation — typed EDA tool calls across vendor APIs
4. Workflow Orchestration — graph with checkpoints, recovery, termination
5. Security & IP — authorization, disclosure, audit across trust domains

**CCC relevance:** handoff vocabulary for subagent returns, ingest artifacts, conductor queries — **REFERENCE** (not EDA prod).

## Snippets

> "A handoff is valid when the transferred object satisfies the consumer's acceptance conditions and carries sufficient context, evidence, and provenance for downstream use."
