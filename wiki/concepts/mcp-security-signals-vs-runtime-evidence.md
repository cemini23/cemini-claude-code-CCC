---
title: MCP security — semantic signals vs runtime evidence
type: concept
tags: [concept, mcp, security, evidence, verification, k189]
keywords: [2607.14754, FlowGuard, TRIAGE, RECON, STRIKE, placeholder credentials]
related:
  - sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/safeclawbench-staged-security-endpoints.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
  - sources/brief-k189-flowguard-mcp-evidence-2026-07-18.md
  - briefs/2026-07-18_ccc-handoff-flowguard-mcp-security.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- `@sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md` — K189 provenance
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — K162: execution feedback > LLM judges
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — K172 validation-before-bind
- `@concepts/multi-agent-evidence-artifact-layers.md` — typed evidence before narrative

## Raw Concept

When is an MCP tool “unsafe” — because a description *looks* like it leaks secrets, or because a probe *proved* command injection / FS / SSRF?

## Narrative

### Steal checklist

1. Split findings: **execution-path** (need runtime evidence) vs **semantic** (metadata / returned instructions).
2. Never escalate placeholder-looking credential strings to “confirmed leak” without adjudication.
3. Prefer schema-valid, recon-guided probes over blind LLM fuzz of MCP tools.
4. Record probe budget + history so refinement does not loop (pair SearchOS Failure Memory / K180).
5. Before connecting a new MCP in TipDrop/prod: triage Discovery schemas; treat Invocation as Prebind-class (K151/K179 family).

### Cemini mapping

| Surface | Practice |
|---------|----------|
| Claude Code / Cursor MCP allowlists | Require evidence class on any “block this server” decision |
| TipDrop Discord/scanner MCP | Schema triage + deny auto-approve of high-risk tools (shell/FS/network) |
| Poker arena | Low MCP surface; if added, same evidence bar |
| Cybersec wiki | Owns offensive MCP scanner taxonomy deepen |

### Verdict

**ADOPT** signals≠evidence discipline for MCP security reviews. **REFERENCE** FlowGuard empirics. **NO-GO** install (no public FlowGuard repo at Phase-0). Do **not** clone unrelated `mcp-flowguard` name-collision repos without SPDX + identity check.

## Snippets

> "credential-like strings may simply be placeholders rather than actual leakage" — Abstract
