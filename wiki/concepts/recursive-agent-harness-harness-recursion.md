---
title: Recursive Agent Harness — harness recursion for long context
type: concept
tags: [concept, harness-recursion, subagents, long-context, k115]
keywords: [2606.13643, rah, oolong, task-tool, code-orchestration]
related:
  - sources/arxiv-recursive-agent-harnesses-2606.13643.md
  - concepts/subagent-orchestration.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/code-as-agent-harness.md
  - entities/patterns/scatter-gather.md
  - concepts/claude-harness-dynamic-workflows-k88.md
  - sources/brief-k115-context-memory-recursion-prod-2026-06-15.md
maturity: draft
created: 2026-06-15
updated: 2026-06-30
---

## Relations

- `@sources/arxiv-recursive-agent-harnesses-2606.13643.md` — PwC Oolong eval
- `@concepts/subagent-orchestration.md` — Task tool parent
- `@concepts/dynamic-workflow-orchestrator-off-model.md` — code orchestrator off-model
- `@concepts/code-as-agent-harness.md` — harness vs model recursion
- `@entities/patterns/scatter-gather.md` — parallel fan-out
- `@concepts/claude-harness-dynamic-workflows-k88.md` — Anthropic dynamic workflows lineage

## Raw Concept

When long-context work needs per-entry LLM reasoning, should recursion spawn model calls or full harnesses?

## Narrative

**Harness recursion (RAH)** [TENTATIVE — 2606.13643]: parent agent writes **executable code** that spawns **full subagent harnesses** (tools + filesystem + LLM) per entry — complement to **model recursion** (RLMs: nested model calls without tools).

| Approach | Tools per entry | Oolong-Synthetic (GPT-5) |
|----------|-----------------|--------------------------|
| Coding agent (regex in one window) | Single window | 71.75% |
| RLM | No tools | 64.38% |
| **RAH** | Full harness per entry | **81.36%** |

**CCC mapping:** Claude Code **Task** tool + scatter-gather + K107 off-model orchestrator = production RAH. Parent writes script or dispatches parallel Tasks; each subagent has isolated context and tools.

**Depth limit:** configurable recursion depth on subagents — mirror in conductor fan-out budgets.

**Repo note:** `darkness22s/recursive-agent-harness` — tests pass, **no license**, unrelated product scope → **NO-GO install**.

**Verdict:** **REFERENCE** — vocabulary + eval evidence; use existing Task tool, don't adopt npm package.

## Snippets

> "The recursive unit is a full agent harness with filesystem tools, code execution, and planning rather than a model call with no tools."

> "Code execution plus subagent spawning — same instinct as Anthropic dynamic workflows in production."
