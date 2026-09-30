---
title: "Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning (CCC K410)"
type: source
tags: [source, arxiv, k410]
keywords: [2609.38147, k410]
related:
  - concepts/agentic-meta-reasoning-control-plane.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
  - concepts/headless-claude-code-controlled-eval-lane.md
maturity: draft
read_status: deep-read
created: 2026-09-30
updated: 2026-09-30

---

## Relations

- `@concepts/agentic-meta-reasoning-control-plane.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`
- `@concepts/headless-claude-code-controlled-eval-lane.md` — headless Claude Code controlled eval lane (K407/K410)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning |
| **arXiv** | 2609.38147 (2026-09) |
| **Retrieved** | 2026-09-30 |

## Narrative

**Verdict: ADOPT pattern.**

**Agentic meta-reasoning — control as its own agentic task.** Existing agents entangle control with object-level work: each control decision is a single step over an ever-growing history, so useful work is hard to compose and stops early as budgets grow. This harness **separates the controller from the workers**. Each control cycle runs four full agentic stages: **assess** (recompute compact state) → **propose** (enumerate candidate computations) → **evaluate** (choose under the remaining budget, or stop) → **dispatch** (spawn workers with selected context). **The controller carries a compact account of the run, not a replay of its history** — full worker outputs live in persistent memory as an action surface. Runs are recorded as an **artifact graph** (nodes = outputs, edges = context supply), which diagnoses a run by the work it produced. Controller calls are charged against the same budget as workers. Gains 3.6–4.2 points over a Direct Control Agent across 12 matched comparisons; ProgramBench 71.5% (GPT-5.5) vs 58.0% for Codex; keeps scaling where direct control plateaus, **though overhead hurts at small budgets**. **CCC-critical: it evaluates headless Claude Code (`claude -p`) with built-in tools off and a single MCP `container_bash` tool as the only channel.** Pairs `subagent-orchestration` / `token-economics-and-prompt-caching` (bounded controller context) / K387 KV working-set / K405 TokenCast / K318 budget routing. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Between decisions the controller carries only a compact account of the run rather than replaying its full history." [Source: arXiv 2609.38147 (retrieved 2026-09-30)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.38147-thinking-before-thinking-scaling-agentic-inferen.pdf` |
