---
title: "Hardware keystore MCP signing (AgentKernel pattern)"
type: entity
tags: [entity, tool, security, mcp, keystore, k254]
keywords: [2608.06130, PKCS11, policy_wired, anonymous-artifact]
related:
  - sources/arxiv-hardware-keystores-ai-agent-signing-2608.06130.md
  - concepts/hardware-confined-agent-signing.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-hardware-keystores-ai-agent-signing-2608.06130.md`
- `@concepts/hardware-confined-agent-signing.md`

## Raw Concept

Phase-0 entity for K254 hardware-confined agent signing.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| AgentKernel / paper artifact | anonymous.4open only | **NO-GO** clone |

**Phase-0:** `scripts/adopt_k254_phase0.sh`

## Phase-1

`policy_wired` → hardware keys / no env private keys for irreversible sign ops.
