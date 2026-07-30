---
title: Standing policy / SOP instruction-following benchmarks
type: concept
tags: [concept, benchmark, policy, long-context, k222]
keywords: [HANDBOOK.md, SOP, strict grading, standing instructions]
related:
  - sources/arxiv-handbook-md-long-context-agentic-policy-2607.25398.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - concepts/businesscasebench-rubric-from-expert-solutions.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-handbook-md-long-context-agentic-policy-2607.25398.md`
- `@concepts/verifiable-deterministic-agent-benchmarking.md`
- `@concepts/substrate-constraints-coding-agent-oversight.md`

## Raw Concept

Do long standing policy documents (skills, CLAUDE.md, handbooks) actually constrain agent tool use over an extended horizon?

## Narrative

Task-completion benches miss the enterprise pattern: rules live in a document the request never mentions. **HANDBOOK.md**: 65 tasks, SOPs 20–124 pages, 824 deterministic criteria; best strict pass **36.2%**.

Failure modes to test for in Cemini harnesses:
1. Plausible in-env request overrides standing policy
2. Required check performed then ignored
3. Rule detail loss over long horizons
4. Reported compliance without achieving it

**Verdict:** **ADOPT** as eval posture for skills/CLAUDE.md/policy files. **NO-GO** install until released SPDX bench.

## Snippets

> Under strict grading … best … passes 36.2% of trials. [Source: arXiv 2607.25398]
