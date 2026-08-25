---
title: "RLM + Continual Harness — REPL substrates and cross-trajectory harness state"
type: concept
tags: [concept, rlm, harness, repl, memory, subagents, k309]
keywords: [prime agent, recursive language model, ipython repl, continual harness, agents view, 2608.23552]
related:
  - sources/arxiv-prime-agent-rlm-harness-2608.23552.md
  - entities/tools/prime-agent.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - concepts/skill-misevolution.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-prime-agent-rlm-harness-2608.23552.md`
- `@entities/tools/prime-agent.md`
- `@concepts/harness-continual-learning-guarded-evolution.md` (K292)
- `@concepts/skill-misevolution.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Question answered: what does a harness look like when it treats context as programmable data and persists across trajectories? Source: arXiv 2608.23552 (CCC K309). Pairs K229 pi-rlm (brief-level), K292 HCL, K162.

## Narrative

Two coupled ideas:

1. **RLM substrate** — a persistent IPython REPL in which the model processes its own context programmatically (search, chunk, transform) and spends test-time compute in code instead of tokens. Context stops being an append-only transcript.
2. **Continual Harness** — histories, memories, skills, prompts, and subagent specifications persist **across trajectories**, with recursive subagents coordinating agent-to-agent and an Agents View for human inspection of daemon-backed sessions.

The measurement claim matters most for this wiki's eval discipline: by standardizing execution/recovery/verification/resource accounting, the membrane keeps **harness failures from being scored as model failures** (ARC-AGI-3 RHAE Best@1 30% → 95.5% is a harness delta, not a weights delta).

Cost of persistence: cross-trajectory state is exactly where K292 **harness-level forgetting** and K237 **misevolution** live. Any adoption of Continual-Harness-style self-writes requires retention checks on held-out packs and **HITL before any skill/prompt write**. Runtime stays `wont_wire` on CCC — Cursor / `/route` / claude-ds are not being replaced.

## Snippets

> "A persistent IPython REPL follows the Recursive Language Model abstraction for programmatic context processing and test-time compute, while Continual Harness preserves histories, memories, skills, prompts, and subagent specifications across trajectories." [Source: arXiv 2608.23552 abstract]
