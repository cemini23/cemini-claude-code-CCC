---
title: "Terminal-state eval — the discovery–reliability gap (Thinkingbox)"
type: concept
tags: [concept, eval, mcp, sandbox, stateful, reliability, k296]
keywords: [2608.19741, Thinkingbox, pass@1, pass^20, terminal state, side effects, discovery-reliability]
related:
  - sources/arxiv-mcp-universe-rl-2608.22167.md
  - entities/tools/mcp-universe-rl.md
  - sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md
  - entities/tools/thinkingbox.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-21
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md`
- `@entities/tools/thinkingbox.md`
- `@sources/arxiv-mcp-universe-rl-2608.22167.md`
- `@entities/tools/mcp-universe-rl.md`

## Raw Concept

How do you evaluate an agent doing multi-turn, stateful, consequence-bearing work — where "plausible response" and "valid tool call" are not the same as "task completed"?

## Narrative

**Thinkingbox** (Microsoft): a sandbox that runs tool–agent–simulated-user interaction in **isolated MCP-compatible sessions**, records complete traces, and grades the **terminal backend state + side effects + dialogue** with task-specific executable checks (conjunctive: wrong / missing / extra persistent effects all fail). **507 policy-conditioned workflows** across retail, hospitality, auto insurance, neobank internal IT, consulting IT/HR support; 12 models × 20 trials.

**Discovery–reliability gap:** strongest model hits **65.36% pass@1** but only **25.25% pass^20** (all-20 attempts) — a success is *findable* far more often than it is *reliably repeatable* (≥1/20 on 91.12% of tasks). Many failed trials show **clean termination + valid state-changing actions**.

Failure taxonomy (avg share of failed trials): **Tool Usage 77.5%** (failures to *recover* from environment feedback — agent often proceeds as if a failed action succeeded), **Wrong State Update 12.1%** (right tool, wrong entity/date/status — looks operationally successful, terminal DB state violates the task), **Incomplete User Resolution 7.9%** (backend work done but user-facing resolution missing/contradictory), **No State-Changing Action 2.5%** (lookups done, required mutation never issued).

**Cemini steal:**

1. **One success ≠ reliability.** Report pass@1 *and* repeat-rate (pass^k / pass^20) for stateful harness evals — a single green run proves discoverability, not dependability.
2. **Tool-call / response validity is not a proxy for completion.** Valid calls with clean termination can still fail the terminal-state check; grade outcomes + collateral effects, not surface form (pairs K277 labels≠endpoints, K239 execution fidelity).
3. **Isolated sessions per attempt** — attempts must not share DB rows/cached tool state, or pass@k and training rewards become unreliable.
4. **Eval = stateful workflow harness**, not single-shot Q&A, when the work is consequential and multi-turn (pairs K275 VAKRA eval axes, K239 irreversible writes).

| Verdict | **ADOPT** — MIT **GO REFERENCE** clone `.local/adopts/thinkingbox`; runtime `wont_wire` (benchmark substrate, not a CCC MCP). |

## Snippets

> "The strongest achieves 65.36% pass@1, but only 25.25% pass^20. Moreover, many failed trials show clean termination and valid state-changing actions, showing that response or tool-call-level signals are not clear proxies for end-to-end task completion." [Source: arxiv 2608.19741 (retrieved 2026-08-21)]
