---
title: "MCP-Universe RL — Salesforce RL trainer for MCP tool-use agents (REFERENCE)"
type: entity
tags: [entity, tool, rl, mcp, trainer, apache, reference, k305]
keywords: [2608.22167, MCP-Universe, Apache-2.0, verl, slime, environment orchestration]
related:
  - sources/arxiv-mcp-universe-rl-2608.22167.md
  - concepts/terminal-state-eval-discovery-reliability-gap.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
wire_status: wont_wire
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-mcp-universe-rl-2608.22167.md`
- `@concepts/terminal-state-eval-discovery-reliability-gap.md` (isolated env per trajectory)
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K305 — Salesforce MCP-Universe RL trainer framework; Apache-2.0 REFERENCE clone.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| MCP-U RL framework | `SalesforceAIResearch/MCP-Universe` | **Apache-2.0** → **GO REFERENCE** clone `.local/adopts/MCP-Universe` (~17MB) |

**Phase-0:** `scripts/adopt_k305_phase0.sh` — gh API SPDX `Apache-2.0`, LICENSE on disk, `du -sm` <500.

Environment-orchestration (provision/isolate/recycle per trajectory) + rollout-orchestration (overlap tool stalls) over an MCP interface; veRL/slime backends; gpt-oss-20b SWE/deep-research/general agents all improved.

## Phase-1

Trainer runtime **`wont_wire`** on prod harness — WATCH status only. No GRPO as wired harness; **no HF weights downloads**. Isolation pattern already policy via K296.
