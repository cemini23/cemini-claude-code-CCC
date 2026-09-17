---
title: "Ask the Tool, Don't Guess: Tool Calls Hold Their Progress (CCC K364)"
type: source
tags: [source, arxiv, k364]
keywords: [2609.18849, k364]
related:
  - concepts/tool-call-progress-aware-serving.md
  - briefs/2026-09-17_ccc-k363-k367-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-17
updated: 2026-09-17
---

## Relations

- `@concepts/tool-call-progress-aware-serving.md`
- `@briefs/2026-09-17_ccc-k363-k367-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Ask the Tool, Don't Guess: Tool Calls Hold Their Progress |
| **arXiv** | 2609.18849 (2026-09) |
| **Retrieved** | 2026-09-17 |

## Narrative

**Verdict: ADOPT policy.**

Agentic requests spend wall-clock time in tools while KV cache holds GPU memory. Serving systems evict/retain cache by **pre-call duration guesses** (name, history, declared duration) — but no pre-call estimate can know true tool duration or rank tools reliably. **Serving should read progress from the tool call itself**, not guess. Pairs K320 usage vs context / token economics / K327 resume boundaries. Awareness only; runtime **`wont_wire`**.

## Snippets

> "Ask the Tool, Don't Guess: Tool Calls Hold Their Progress — CCC K364 synthesis." [Source: arXiv 2609.18849 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.18849-ask-the-tool-don-t-guess-agent-tool-calls-hold-t.pdf` |
