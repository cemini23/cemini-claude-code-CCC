---
title: "Autoresearch loop — LLM proposal × objective × mutation pattern for Claude Code"
type: entity
tags: [pattern, claude-code, autoresearch, neuro-symbolic, multi-agent, conductor-evolution, cross-wiki-stub]
keywords: [autoresearch-loop, proposal-objective-mutation, sharpe-as-loss, gemini-sec-2-6, atlas-gic, conductor-priors, darwinian-prompt-evolution]
related:
  - entities/patterns/ralph-loop.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/subagent-orchestration.md
  - entities/tools/claude-obsidian.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
cross-wiki-source: "@osint-wiki/concepts/autoresearch-loop-pattern.md"
---

## Relations

- @entities/patterns/ralph-loop.md — Ralph is the simpler sibling: file-based memory + iteration without the objective-function leg. Autoresearch adds the explicit success metric and mutation step.
- @entities/patterns/full-prompt-goal-template.md — `/goal` is a single-shot version of the proposal stage; autoresearch wraps it in the objective + mutation loop.
- @concepts/subagent-orchestration.md — autoresearch loops are natural Tier-2 subagent workloads (bounded blast radius, parallelisable).
- @entities/tools/claude-obsidian.md — claude-obsidian's `/autoresearch` is a concrete-tool implementation (rejected for Cemini's stack, but the pattern is reusable).
- @osint-wiki/concepts/autoresearch-loop-pattern.md — cross-wiki primary; the load-bearing definition, five documented instantiations, and the conductor-evolution-target framing live there.

## Raw Concept

CCC-side stub cross-routed from the OSINT primary. Autoresearch is a three-leg architectural pattern (proposal → objective → mutation) that emerged from the 2026-05-04 ingest batch comparing Gemini's `gemini-sci-research` §2.6 (math research), atlas-gic (algorithmic trading with rolling Sharpe), and claude-obsidian (multi-round documents). The OSINT primary documents five independent instantiations; this stub records the Claude-Code-side relevance.

## Narrative

### The pattern

```
┌──────────────┐    ┌────────────────────┐    ┌──────────────────┐
│   LLM        │ →  │   Objective        │ →  │  Mutation /      │
│   proposal   │    │   function         │    │  rollback        │
└──────────────┘    └────────────────────┘    └──────────────────┘
       ↑                                                │
       └────────────────── feedback ───────────────────┘
```

- **Proposal** — the LLM suggests a candidate (hypothesis / config / prompt / skill).
- **Objective** — a deterministic or semi-deterministic scoring function evaluates it (numerical traceback, rolling Sharpe, MLLM-judged critique, RL gradient).
- **Mutation** — based on the score, the loop either accepts the proposal (commit), rolls it back (revert), or mutates it (gradient step / prompt-rewrite / skill-replacement).

### Five documented instantiations (per OSINT primary)

1. Gemini paper §2.6 — math expression proposal → numerical traceback → context injection
2. atlas-gic — strategy proposal → rolling Sharpe → git commit/revert
3. claude-obsidian `/autoresearch` — multi-round document elaboration
4. xskill — Skills + Experiences dual-stream accumulation via MLLM-judged critique
5. Deep GraphRAG (DW-GRPO) — weight-level mutation via RL gradient

### CCC-side relevance

- **Cemini's conductor (`@entities/tools/conductor-mcp.md`) is the natural target** for autoresearch evolution. Current state: human-tuned `--build-priors`. Future state: autoresearch-driven prior mutation based on routing-decision objective scoring. The OSINT primary calls this out explicitly.
- **`/goal` + Ralph are the lightweight Cemini-side variants.** `/goal` ships the proposal; Ralph's file-based memory carries state between iterations; the operator (currently) plays the objective function. The autoresearch loop is what you get when you automate the objective + mutation legs.
- **Worth knowing the pattern's shape** even when not running it — recognising autoresearch in someone else's tool (Gemini's research stack, atlas-gic, claude-obsidian) tells you what its load-bearing components are and what would break.

## Snippets

> An autoresearch loop has three components: proposal (LLM-generated candidate), objective (deterministic scoring), and mutation (accept / reject / evolve based on score).
[Source: @osint-wiki/concepts/autoresearch-loop-pattern.md]
