---
title: "A Chat Assistant for Software Exploration in a 3D Software Visualization (CCC K436)"
type: source
tags: [source, arxiv, k436]
keywords: [2610.09901, k436]
related:
  - concepts/read-versus-write-guardrails.md
  - briefs/2026-10-08_ccc-k436-k440-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@concepts/read-versus-write-guardrails.md`
- `@briefs/2026-10-08_ccc-k436-k440-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A Chat Assistant for Software Exploration in a 3D Software Visualization |
| **arXiv** | 2610.09901 (2026-10) |
| **Repo** | `explorviz/explorviz-frontend` |
| **Retrieved** | 2026-10-08 |

## Narrative

**Verdict: ADOPT pattern (repo stale).**

**The split is read versus write, and the write side is where it fails.** A chat assistant in a 3D software-visualization tool (ExplorViz, city metaphor), built on **CopilotKit** rather than MCP — an explicit architecture note: the visualization state lives in the React frontend, so a separate MCP server 'is not a good fit', and the assistant forwards prompts to a Node service that holds the API keys. Eleven-participant study. **Read actions were rated well:** generated summaries and explanations 'largely correct', highlighting entities and creating colour themes rated high usability. **Write actions were not:** 'open-ended chat-assisted software restructuring in the visualization showed mixed results', ratings for expectation alignment in editing 'notably lower', and the authors' own conclusion is that restructuring workflows 'require stronger guardrails' and better previews and undo. **CCC reading:** this is the same asymmetry CCC holds as a rule — reads are cheap to get wrong, writes are not — and here it is measured in a user study rather than asserted. The safety design that follows: bind agent actions to **well-defined existing entities** so they are confirmable and reversible (which this paper did, and which is why highlighting worked), and **do not expose open-ended structural mutation** as a first-class agent action. Also measured: **input tokens ran ~84× output**, so the cost sits in context, not generation (pairs K429/K425/`token-economics`). **Phase-0: `explorviz/explorviz-frontend` Apache-2.0 but last pushed 2022-03-20 — four years stale**, so the public tree is not the paper's build → no clone. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "open-ended chat-assisted software restructuring in the visualization showed mixed results. This suggests a need for stronger guardrails" [Source: arXiv 2610.09901 (retrieved 2026-10-08)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.09901-a-chat-assistant-for-software-exploration-in-a-3.pdf` |
