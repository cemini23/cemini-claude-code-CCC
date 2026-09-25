---
title: "The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems (CCC K387)"
type: concept
tags: [concept, k387]
keywords: [2609.27746, k387]
related:
  - sources/arxiv-kv-cache-working-set-capacity-2609.27746.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-24_ccc-k385-k389-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-24
updated: 2026-09-25
---

## Relations

- `@sources/arxiv-kv-cache-working-set-capacity-2609.27746.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-24_ccc-k385-k389-sip-ready.md`

## Raw Concept

K387: ADOPT awareness — arXiv 2609.27746.

## Narrative

**Working-set view of KV cache** for LLM inference — online capacity planning treats cache occupancy as a dynamic working set, not a fixed prefix (pairs K228 cross-model KV awareness / K320 token economics / K364 tool-progress-aware serving). Serving and routing awareness only. Runtime **`wont_wire`**.

## Snippets

> "Prefix caching is critical for efficient large language model (LLM) serving, particularly for agentic workloads that repeatedly invoke the model with a growing conversation and tool-use history." [Source: https://arxiv.org/abs/2609.27746 (retrieved 2026-09-25)]
