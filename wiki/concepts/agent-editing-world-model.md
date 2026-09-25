---
title: "Agent-Editing World Model: Rethinking World Modeling for LLM Agents (CCC K389)"
type: concept
tags: [concept, k389]
keywords: [2609.28416, k389]
related:
  - sources/arxiv-agent-editing-world-model-2609.28416.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-24_ccc-k385-k389-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-24
updated: 2026-09-25
---

## Relations

- `@sources/arxiv-agent-editing-world-model-2609.28416.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-24_ccc-k385-k389-sip-ready.md`

## Raw Concept

K389: ADOPT pattern — arXiv 2609.28416.

## Narrative

LLM agents **maintain and edit explicit world models** for planning — harness pattern distinct from implicit context-only state (pairs K283 Twin validate-before-act / K296 terminal-state eval / K334 harness-as-eval-artifact). **No clone** unless SPDX verified at Phase-0. Runtime **`wont_wire`**.

## Snippets

> "Recent advances in large language models (LLMs) have enabled agents to tackle long-horizon tasks across diverse environments. Existing language world models typically predict environment observations, yet reconstructing high-entropy, execution-dependent tool responses offers limited value when real feedback is available." [Source: https://arxiv.org/abs/2609.28416 (retrieved 2026-09-25)]
