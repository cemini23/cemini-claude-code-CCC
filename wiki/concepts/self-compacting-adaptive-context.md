---
title: Self-compacting adaptive context management
type: concept
tags: [concept, context-compaction, context-rot, k124]
keywords: [2606.23525, selfcompact, rubric-gated, meta-cognitive]
related:
  - sources/arxiv-self-compacting-agents-2606.23525.md
  - entities/patterns/cpr-context-compression.md
  - concepts/long-thread-context-decay.md
  - concepts/tool-response-context-pruning-summarization.md
  - entities/tools/claude-code.md
  - concepts/token-economics-and-prompt-caching.md
  - entities/patterns/full-prompt-goal-template.md
  - sources/brief-k124-harness-policy-hands-on-2026-06-24.md
maturity: draft
created: 2026-06-24
updated: 2026-06-25
---

## Relations

- `@sources/arxiv-self-compacting-agents-2606.23525.md` — SELFCOMPACT paper
- `@entities/patterns/cpr-context-compression.md` — CCC compress/preserve/resume pattern

## Raw Concept

When should an agent compact its own context — and who decides the trigger?

## Narrative

**SELFCOMPACT** (2606.23525) pairs:
1. **Compaction tool** — model invokes to summarize accumulated trace
2. **Lightweight rubric** — when to fire (sub-task resolved, converging) vs suppress (mid-derivation, stuck)

Contrasts three regimes:

| Regime | Trigger | Risk |
|--------|---------|------|
| None | Never | Context rot anchors bad reasoning |
| Fixed interval | Token threshold | Mid-derivation wipe; fact loss |
| User `/compact` | Human | Meta-cognitive burden on operator |
| **Rubric-gated self-compact** | Model + rubric | Requires both elements |

**CCC mapping:**
- Claude Code native compaction ≈ fixed-interval [NEEDS VERIFICATION 2026-06-24]
- `hot.md` rewrite ≈ manual rubric-gated compact at session boundaries
- Task subagent spawn ≈ fork-with-clean-context instead of compact

**Steal-from:** UserPromptSubmit hook with rubric snippet ("compact only after sub-task checkpoint recorded in hot.md").

## Snippets

> "Although unprompted models cannot reliably tell when their own context is rotting, a lightweight rubric closes this gap."
> — [Source: arxiv-2606.23525, retrieved 2026-06-24]
