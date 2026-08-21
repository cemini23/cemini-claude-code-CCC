---
title: "Thinkingbox — MCP sandbox + benchmark for stateful business workflows (Microsoft)"
type: entity
tags: [entity, tool, sandbox, benchmark, mcp, stateful, mit, k296, reference]
keywords: [2608.19741, Thinkingbox, MIT, GO REFERENCE, pass@1, pass^20, terminal-state]
related:
  - sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md
  - concepts/terminal-state-eval-discovery-reliability-gap.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md`
- `@concepts/terminal-state-eval-discovery-reliability-gap.md`

## Raw Concept

Phase-0 entity for CCC K296 — Microsoft Thinkingbox sandbox + 507-task stateful business benchmark; MIT.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| Thinkingbox sandbox + bench | `microsoft/thinkingbox` | **MIT** → **GO REFERENCE** clone |

**Phase-0:** `scripts/adopt_k296_phase0.sh` — clone `.local/adopts/thinkingbox` (MIT LICENSE on disk).

Terminal-state eval + side-effect judging + discovery–reliability gap (65.36% pass@1 vs 25.25% pass^20). Policy pattern wired via concept; benchmark substrate **`wont_wire`** as a CCC runtime MCP.

## Phase-1

Concept `terminal-state-eval-discovery-reliability-gap` → `policy_wired` (`.cursor/rules/cemini-phase1-policy-wires.mdc` §K296); clone = REFERENCE only. Pairs K239 / K275 / K277.
