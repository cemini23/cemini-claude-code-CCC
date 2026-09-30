---
title: "Headless Claude Code as a controlled evaluation lane (CCC K407/K410)"
type: concept
tags: [concept, evaluation, claude-code, harness, k407, k410]
keywords: [claude -p, headless, built-in tools disabled, MCP-only lane, eval lane, reader swap, budget injection]
related:
  - sources/arxiv-auditable-long-term-memory-deterministic-chain-2609.38021.md
  - sources/arxiv-agentic-meta-reasoning-control-plane-2609.38147.md
  - concepts/harness-as-eval-artifact.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- `@sources/arxiv-auditable-long-term-memory-deterministic-chain-2609.38021.md`
- `@sources/arxiv-agentic-meta-reasoning-control-plane-2609.38147.md`
- `@concepts/harness-as-eval-artifact.md`
- `@concepts/verifiable-deterministic-agent-benchmarking.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`

## Raw Concept

K407 and K410 both run headless Claude Code with the built-in tools disabled as a controlled comparison lane (K410 via a single MCP tool, with budget injection).

## Narrative

**Two independent September-2026 papers use headless Claude Code as a controlled
evaluation lane.** This is the point of this page: a research practice, observed twice, that CCC
should know about when designing its own evals or interpreting others'.

**The pattern (4 parts `[CONFIRMED]` — 2 independent sources):**

1. **Run Claude Code headless** — `claude -p` / non-interactive CLI, not the IDE or interactive session.
2. **Disable the built-in tools.** K407 calls this the "CLI lane": "the Claude Code command line,
   with the built-in tools disabled." K410 disables native tools so that every action flows through
   one channel.
3. **Expose exactly one capability.** K410 allows a **single MCP tool** (`container_bash`) so both
   the coding agent and the research harness see identical truncation, memory limits, and recovery
   behavior. File edits then happen through heredocs and shell commands — exactly as for the other
   arms.
4. **Inject an explicit model-call budget.** K410 prefixes a budget line to the next tool result
   each time another tenth of the allowance is consumed, and at 90% forces submission.

**Why it matters for CCC.** A headless, tools-disabled Claude Code is a **fixed, comparable
substrate**. It makes the harness the only variable. That is the same discipline CCC applies when it
treats a harness as an eval artifact (`@concepts/harness-as-eval-artifact.md`) and when it insists
that external eval contracts never be rewritten by the thing under test.

**Caveat from K407 — the lane is not the whole answer.** The lane fixes the reader, but the *judge*
still moved: the official GPT-4o judge flipped 3 verdicts when re-scoring byte-identical answers.
Fixing the execution lane does not fix the scoring lane. Pair this page with
`@concepts/verifiable-deterministic-agent-benchmarking.md`.

**Status:** policy/awareness only. No hook, tool, or runtime wire derives from this page.

## Snippets

> "Claude Code runs with its built-in tools off and only the MCP tool allowed; Codex runs with --sandbox read-only, so its own shell cannot write anything scored, with the MCP tool approved per-call." [Source: arXiv 2609.38147 implementation details (retrieved 2026-09-30)]
