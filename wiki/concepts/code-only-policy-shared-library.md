---
title: "Embodied Turing Machines: Stateful Code for Robot Recursive Self-Impro (CCC K443)"
type: concept
tags: [concept, k443]
keywords: [2610.12369, k443]
related:
  - sources/arxiv-code-only-as-policy-embodied-turing-2610.12369.md
  - concepts/agent-optimizer-compounding-and-regression-control.md
  - concepts/recursive-agent-harness-harness-recursion.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-09_ccc-k441-k444-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-09
updated: 2026-10-09
---

## Relations

- `@sources/arxiv-code-only-as-policy-embodied-turing-2610.12369.md`
- `@concepts/agent-optimizer-compounding-and-regression-control.md`
- `@concepts/recursive-agent-harness-harness-recursion.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-09_ccc-k441-k444-sip-ready.md`

## Raw Concept

K443: REFERENCE (cross-domain; pattern transfers) — arXiv 2610.12369.

## Narrative

**When the state is explicit and the code is robust, no model needs to run at test time.** Robotics (RoboDojo, 42 bimanual tasks) — but the harness shape is the transferable part. **Code-Only-as-Policy (COAP):** the embodied world is modelled as an **Embodied Turing Machine** whose *tape* is the robot+environment state and whose *rules* are code; code measures and tracks the state, makes every decision from it, and **one program runs every episode**. A **shared code library** is developed offline by coding agents (Opus 5.5 Max), and **83% of the code a new task runs is reused from the library**. Three claimed advantages over VLAs and agent harnesses — **Explicit State** (inspectable, persistent, measured), **Execution** (controllable, recoverable by backtracking, ~0.3 ms/step on CPU, 0.8–2.4% of a VLA's compute), **Extensibility** (reuse / inherit / extend; capabilities accumulate without regressing old tasks). **Two mechanisms worth stealing:** (1) an **offline RSI loop over git worktrees** — each agent works in its own worktree, inspects the recorded state of failed runs, proposes a diff, and the diffs form a *search frontier of runnable branches* evaluated in parallel under identical conditions; acceptance is a **non-regression gate** `J(θ+Δ) ≥ J(θ) + ε` with ε above rerun noise. (2) a **default-off parameter compatibility guarantee** (Eq. 3): an extension must leave the execution trace of every task that does *not* pass the new argument byte-identical, so earlier tasks keep their behaviour *by construction* and only the adopting task changes. Result: 70.24% vs 31.38% SOTA. **CCC reading:** K436/K437's 'explicit beats implicit' argument taken to its end, and it converges with CCC's own harness-evolution lane — the **non-regression gate** is `agent-optimizer-compounding-and-regression-control`, and the **git-worktree parallel branch search** is the concrete mechanism behind CCC's 'keep the change iff it wins' rule (pairs K411's mutation-keep loop and K415's harness editor). It also cites **Anthropic's 'Code execution with MCP'** and **Cloudflare's 'Code Mode'** — code as the agent's action interface. Cross-domain REFERENCE. **No public repo.** Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "See source page for arXiv 2610.12369 locators." [Source: CCC K443 synthesis]
