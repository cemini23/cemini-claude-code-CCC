---
title: "Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning (CCC K410)"
type: concept
tags: [concept, k410]
keywords: [2609.38147, k410]
related:
  - sources/arxiv-agentic-meta-reasoning-control-plane-2609.38147.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
  - concepts/lossless-visual-memory-harness.md
  - concepts/persistent-state-evidence-traceable-research.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- `@sources/arxiv-agentic-meta-reasoning-control-plane-2609.38147.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`

## Raw Concept

K410: ADOPT pattern — arXiv 2609.38147.

## Narrative

**Agentic meta-reasoning — control as its own agentic task.** Existing agents entangle control with object-level work: each control decision is a single step over an ever-growing history, so useful work is hard to compose and stops early as budgets grow. This harness **separates the controller from the workers**. Each control cycle runs four full agentic stages: **assess** (recompute compact state) → **propose** (enumerate candidate computations) → **evaluate** (choose under the remaining budget, or stop) → **dispatch** (spawn workers with selected context). **The controller carries a compact account of the run, not a replay of its history** — full worker outputs live in persistent memory as an action surface. Runs are recorded as an **artifact graph** (nodes = outputs, edges = context supply), which diagnoses a run by the work it produced. Controller calls are charged against the same budget as workers. Gains 3.6–4.2 points over a Direct Control Agent across 12 matched comparisons; ProgramBench 71.5% (GPT-5.5) vs 58.0% for Codex; keeps scaling where direct control plateaus, **though overhead hurts at small budgets**. **CCC-critical: it evaluates headless Claude Code (`claude -p`) with built-in tools off and a single MCP `container_bash` tool as the only channel.** Pairs `subagent-orchestration` / `token-economics-and-prompt-caching` (bounded controller context) / K387 KV working-set / K405 TokenCast / K318 budget routing. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.38147 locators." [Source: CCC K410 synthesis]
