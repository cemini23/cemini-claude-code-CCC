---
title: "Query-aware role fusion — don't spawn N agents for multi-perspective work (CCC K322)"
type: concept
tags: [concept, multi-agent, steering-vector, roles, cost, watch, k322]
keywords: [MoRe, mixture of roles, steering vector, query-aware router, GRPO, token cost, 2608.27338]
related:
  - sources/arxiv-more-mixture-of-roles-2608.27338.md
  - concepts/context-engineering.md
  - concepts/subagent-orchestration.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-more-mixture-of-roles-2608.27338.md`
- `@concepts/context-engineering.md`
- `@concepts/subagent-orchestration.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

The question: multi-perspective problem solving usually means spawning multiple agents with different roles — at 20× the token cost. Is there a cheaper single-model alternative? Answer from MoRe [Source: wiki/sources/arxiv-more-mixture-of-roles-2608.27338.md]: yes — fuse role steering vectors per query in one pass.

## Narrative

**WATCH — not adopted.** MoRe trains a diversified **codebook of steering vectors**, each encoding a latent role, and a **query-aware router** fuses the relevant subset into a single composed steering vector applied to a **frozen backbone** in one single-turn inference. Trained with a three-stage SFT curriculum + GRPO post-training (GRPO **`wont_wire`** in CCC).

Results: +2.2% over single-agent baselines on reasoning + personality benchmarks; **on par with MAS at 20× lower token cost**.

CCC steal: **do not auto-spawn N agents as the default multi-perspective move.** MAS's multi-turn role fusion inflates context length and inference cost (`@concepts/context-engineering.md`); a composed-role single pass is the cost-efficient alternative. Where Cemini does spawn subagents (`@concepts/subagent-orchestration.md`), each spawn must earn its context budget — same discipline as K311/K164.

| Confidence | `[TENTATIVE]` — single paper; GRPO mechanics not reproducible in CCC |
|------------|------------|

## Snippets

> "MoRe … adaptively composes multiple specializations into a single steering vector for single-turn inference." [Source: arXiv 2608.27338 abstract]
