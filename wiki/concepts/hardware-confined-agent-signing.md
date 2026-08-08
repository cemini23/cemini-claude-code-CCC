---
title: Hardware-confined agent signing / Zero-Trust MCP keystores (K254)
type: concept
tags: [concept, security, mcp, hardware, keystore, k254]
keywords: [2608.06130, PKCS11, Zero-Trust, AgentKernel, signing]
related:
  - sources/arxiv-hardware-keystores-ai-agent-signing-2608.06130.md
  - entities/tools/hardware-keystore-mcp-signing.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
  - briefs/2026-08-07_phase1-wire-status-closeout-k254-k258.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-hardware-keystores-ai-agent-signing-2608.06130.md`
- `@entities/tools/hardware-keystore-mcp-signing.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`

## Raw Concept

How do we keep agent signing keys out of software-accessible memory while still allowing MCP tool use?

## Narrative

K254 (arXiv **2608.06130**): raw private keys in env/files/containers are a structural fail under prompt injection. Move generation+sign into PKCS#11 hardware; host sees opaque handles + signatures only. Surround with Zero-Trust layers (session identity, scope bounds, semantic validation, taint, hardware boundary).

### Cemini steal (ADOPT)

1. Never put production signing/SSH/API private keys in agent-readable env or workspace files for LIVE/high-blast agents.
2. Prefer hardware or at least OS-isolated keystores over vault-then-inject-into-memory for irreversible sign ops (pairs K239 execution fidelity).
3. Treat MCP tool surfaces that can read process memory as in-scope for key exfil — harden before LIVE Discord / trading egress.
4. SoftHSM is a reproducibility proxy only — not tamper resistance.

| Verdict | **ADOPT** pattern. **NO-GO** anonymous artifact clone. Cybersec lab brief. Entity `policy_wired`. |
