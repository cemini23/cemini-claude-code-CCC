---
title: SHarD / shard-demo — secure harness distribution
type: entity
tags: [entity, tool, harness, security, k225]
keywords: [SHarD, shard-demo, agent-security-lab, Pi harness, MIT]
related:
  - sources/arxiv-shard-harness-security-distribution-2607.25890.md
  - concepts/distributed-harness-security-controls.md
  - concepts/skill-vetting.md
  - concepts/agent-vm-sandboxing.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
wire_status: wont_wire
wire_target: "REFERENCE .local/adopts/shard-demo + agent-security-lab — do not curl|sh"
created: 2026-07-30
updated: 2026-07-31
---

## Relations

- `@sources/arxiv-shard-harness-security-distribution-2607.25890.md`
- `@concepts/distributed-harness-security-controls.md`

## Raw Concept

Phase-0 of Gore 2607.25890 — distributable Pi-based harness with sandbox + skill scan + tool restriction.

## Narrative

| Artifact | SPDX | Size | Verdict |
|----------|------|------|---------|
| `wrgore/agent-security-lab` | MIT | ~944KB | **GO** REFERENCE (paper + test assets) |
| `wrgore/shard-demo` | MIT | ~23MB | **GO** REFERENCE (demo harness) |

Local: `.local/adopts/agent-security-lab`, `.local/adopts/shard-demo`.

**Hands-on:** Do **not** run `curl …/install.sh | sh`. Clone + read. Research demo — not production drop-in for Claude Code/Cursor. Steal patterns into federation sandbox/skill-scan posture.

**Phase-0:** `scripts/adopt_k225_phase0.sh`

## Phase-1

Research demo harness; steal sandbox/skill-scan/tool-restrict patterns only.
