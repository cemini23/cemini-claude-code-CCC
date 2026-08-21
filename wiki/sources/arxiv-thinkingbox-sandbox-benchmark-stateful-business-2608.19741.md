---
title: "Thinkingbox — sandbox + benchmark for agents in stateful business workflows"
type: source
tags: [source, arxiv, mcp, sandbox, benchmark, stateful, reliability, k296]
keywords: [2608.19741, Thinkingbox, pass@1, pass^20, terminal state, side effects, microsoft]
related:
  - concepts/terminal-state-eval-discovery-reliability-gap.md
  - entities/tools/thinkingbox.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@concepts/terminal-state-eval-discovery-reliability-gap.md`
- `@entities/tools/thinkingbox.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows |
| **arXiv** | 2608.19741 |
| **Authors** | Li, Ko, Keramati et al. (Microsoft) |
| **Code** | `github.com/microsoft/thinkingbox` — **MIT** LICENSE on disk |
| **Retrieved** | 2026-08-21 |

## Narrative

Sandbox orchestrating multi-turn **tool–agent–simulated-user** interaction over **isolated MCP-compatible sessions**, with complete execution traces and outcome evaluation over **terminal backend state** (side-effect-centered judging: executable checks on final state + side effects + dialogue, conjunctive verdict). **Thinkingbox-Bench: 507 policy-conditioned workflows** across retail/e-commerce, travel & hospitality, auto insurance, neobank internal IT, consulting IT/HR support; 12 proprietary + open-weight LLMs × 20 trials/task.

Strongest model: **65.36% pass@1** but only **25.25% pass^20** (all-20 success) — large **discovery–reliability gap** (succeeds ≥1/20 on 91.12% of tasks). Many failed trials show **clean termination and valid state-changing actions**. Failure taxonomy (avg): Tool Usage 77.5% (fail to recover from env feedback — often continue as if a failed action succeeded), Wrong State Update 12.1%, Incomplete User Resolution 7.9%, No State-Changing Action 2.5%. DeepSeek-V4-Pro appears in the evaluated table (69.8% tool-usage / 24.7% incomplete-resolution failure shares).

| Verdict | **ADOPT**: isolated MCP sessions + traces + terminal-state checks for harness eval; one success ≠ reliability; tool-call/response validity ≠ end-to-end stateful completion. **GO REFERENCE** MIT clone `.local/adopts/thinkingbox`. Pairs K239 / K275 / K277. |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.19741-one-success-isn-t-reliability-thinkingbox-a-sand.pdf` |
