---
title: Agentic Configuration Management (ACM) (K273)
type: concept
tags: [concept, governance, configuration, agentops, k273]
keywords: [2608.11166, ACM, baselines, provenance, impact-propagation]
related:
  - sources/arxiv-agentic-configuration-management-acm-2608.11166.md
  - entities/tools/agentic-configuration-management-acm.md
  - concepts/phase1-adopt-wire.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/model-harness-six-responsibilities.md
  - sources/brief-k270-k273-mcp-acm-wave-2026-08-12.md
  - briefs/2026-08-12_ccc-handoff-k270-k273-ingest.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- `@sources/arxiv-agentic-configuration-management-acm-2608.11166.md`
- `@entities/tools/agentic-configuration-management-acm.md`
- `@concepts/phase1-adopt-wire.md`

## Raw Concept

How do we govern heterogeneous agent configs (agents, tools, prompts, skills, workflows) as one coherent system?

## Narrative

ACM: immutable config items, baselines, deterministic governance, lifecycle, dependency-aware impact, runtime provenance — framework-independent projection layer over LangGraph/CrewAI/etc.

### Steal (ADOPT)

1. Treat Cursor/Claude harness configs as **configuration items** with baselines (settings, rules, skills, MCP allowlists).
2. Prefer deterministic validation + impact analysis before blast-radius harness edits.
3. Record provenance linking runtime behavior to config baseline (pairs Phase-1 wire inventory).
4. No ACM product install until a clear SPDX'd artifact exists.

| Verdict | **ADOPT** governance vocabulary. |
