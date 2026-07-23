---
title: MCP session sequential attack detection (kill-chain)
type: concept
tags: [concept, mcp, security, kill-chain, session, k206]
keywords: [2607.19432, ChainWatch, multi-step attacks, HMM, per-call gap]
related:
  - sources/arxiv-chainwatch-mcp-sequential-detection-2607.19432.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - concepts/production-agent-deployment-checklist.md
  - sources/brief-k206-k209-mcp-slm-rag-ethics-2026-07-23.md
  - "@cybersecurity-wiki/concepts/chainwatch-mcp-kill-chain-detection.md"
maturity: draft
created: 2026-07-23
updated: 2026-07-23
---

## Relations

- `@sources/arxiv-chainwatch-mcp-sequential-detection-2607.19432.md`
- `@concepts/mcp-security-signals-vs-runtime-evidence.md` — per-call evidence peer
- Cybersec: `@cybersecurity-wiki/concepts/chainwatch-mcp-kill-chain-detection.md`

## Raw Concept

K206: multi-step MCP attacks evade per-call defenses. Detect **session progressions** aligned to a kill chain.

## Narrative

### Steal (ADOPT)

1. TipDrop/prod MCP allowlists: log tool-call **sequences**, not only single invocations.
2. Flag suspicious progressions (recon→privilege→exfil shapes) even when each call looks benign.
3. Pair with K189 evidence bar — sequential rules don't replace runtime evidence for execution-path risks.
4. No ChainWatch code — pattern only.

| Verdict | **ADOPT** session-sequence checklist; **NO-GO** install |
