---
title: "Hardware Keystores for AI Agent Signing Workflows"
type: source
tags: [source, arxiv, mcp, hardware, keystore, zero-trust, k254]
keywords: [2608.06130, PKCS11, AgentKernel, SoftHSM, TPM, OpenClaw]
related:
  - concepts/hardware-confined-agent-signing.md
  - entities/tools/hardware-keystore-mcp-signing.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@concepts/hardware-confined-agent-signing.md`
- `@entities/tools/hardware-keystore-mcp-signing.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Hardware Keystores for AI Agent Signing Workflows: A Zero-Trust MCP Enforcement Architecture |
| **arXiv** | 2608.06130 |
| **Authors** | Léo Sambrook, Sampo Sovio (Huawei HSSL / EPITA) |
| **Code** | Anonymous artifact only (`anonymous.4open.science/...Artifact-357C`) — no public SPDX repo |
| **Retrieved** | 2026-08-07 |

## Narrative

Software-resident signing keys (env, files, container memory) are exfiltratable via prompt injection (OpenClaw-class incidents). Paper moves keys into PKCS#11 hardware (HSM/TPM/smart card) with a five-layer Zero-Trust MCP stack (SAGA session identity, S_max scope, RAV semantic validation, taint tracking, hardware boundary). AgentDojo ImportantInstructionsAttack eval: baseline ASR 19.3% → protected 0% (Wilson upper 2.0%); zero FPs on benign tasks.

| Verdict | **ADOPT** hardware-confined signing + ZT MCP enforcement pattern. **NO-GO** clone (anonymous artifact only). Cybersec-primary. |

**Location (2026-08-07):** local `raw-sources/<file>` — egress-fi SCP timed out (banner exchange); re-archive when jump is up → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`.
