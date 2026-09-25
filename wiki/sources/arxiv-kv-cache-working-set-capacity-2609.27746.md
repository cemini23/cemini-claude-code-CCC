---
title: "The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems (CCC K387)"
type: source
tags: [source, arxiv, k387]
keywords: [2609.27746, k387]
related:
  - concepts/kv-cache-working-set-serving.md
  - briefs/2026-09-24_ccc-k385-k389-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-09-24
updated: 2026-09-25
---

## Relations

- `@concepts/kv-cache-working-set-serving.md`
- `@briefs/2026-09-24_ccc-k385-k389-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems |
| **arXiv** | 2609.27746 (2026-09) |
| **Retrieved** | 2026-09-24 |

## Narrative

**Verdict: ADOPT awareness.**

**Working-set view of KV cache** for LLM inference — online capacity planning treats cache occupancy as a dynamic working set, not a fixed prefix (pairs K228 cross-model KV awareness / K320 token economics / K364 tool-progress-aware serving). Serving and routing awareness only. Runtime **`wont_wire`**.

## Snippets

> "Prefix caching is critical for efficient large language model (LLM) serving, particularly for agentic workloads that repeatedly invoke the model with a growing conversation and tool-use history. By reusing the key-value (KV) states of previously processed prefixes, prefix caching avoids redundant prefill computation. Its effectiveness, however, depends on retaining a sufficiently large set of KV cache states." [Source: https://arxiv.org/abs/2609.27746 (retrieved 2026-09-25)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.27746-the-kv-cache-working-set-online-capacity-plannin.pdf` |
