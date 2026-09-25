---
title: "Agent-Editing World Model: Rethinking World Modeling for LLM Agents (CCC K389)"
type: source
tags: [source, arxiv, k389]
keywords: [2609.28416, k389]
related:
  - concepts/agent-editing-world-model.md
  - briefs/2026-09-24_ccc-k385-k389-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-09-24
updated: 2026-09-25
---

## Relations

- `@concepts/agent-editing-world-model.md`
- `@briefs/2026-09-24_ccc-k385-k389-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agent-Editing World Model: Rethinking World Modeling for LLM Agents |
| **arXiv** | 2609.28416 (2026-09) |
| **Retrieved** | 2026-09-24 |

## Narrative

**Verdict: ADOPT pattern.**

LLM agents **maintain and edit explicit world models** for planning — harness pattern distinct from implicit context-only state (pairs K283 Twin validate-before-act / K296 terminal-state eval / K334 harness-as-eval-artifact). **No clone** unless SPDX verified at Phase-0. Runtime **`wont_wire`**.

## Snippets

> "Recent advances in large language models (LLMs) have enabled agents to tackle long-horizon tasks across diverse environments. To further improve agent performance, existing language world models typically predict environment observations, yet reconstructing high-entropy, execution-dependent tool responses offers limited value when real feedback is available. Meanwhile, agents suffer from task-state contamination, where unsupported assumptions and outdated plans persist in history and distort subsequent decisions." [Source: https://arxiv.org/abs/2609.28416 (retrieved 2026-09-25)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.28416-agent-editing-world-model-rethinking-world-model.pdf` |
