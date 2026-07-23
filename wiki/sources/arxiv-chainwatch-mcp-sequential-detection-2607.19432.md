---
title: "ChainWatch — kill-chain sequential MCP attack detection"
type: source
tags: [source, arxiv, mcp, security, kill-chain, hmm, k206]
keywords: [2607.19432, ChainWatch, MCP kill chain, sequential detection, multi-step attacks]
related:
  - concepts/mcp-session-sequential-attack-detection.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - sources/brief-k206-k209-mcp-slm-rag-ethics-2026-07-23.md
  - "@cybersecurity-wiki/concepts/chainwatch-mcp-kill-chain-detection.md"
  - "@cybersecurity-wiki/sources/arxiv-chainwatch-mcp-sequential-detection-2607.19432.md"
maturity: draft
created: 2026-07-23
updated: 2026-07-23
---

## Relations

- `@concepts/mcp-session-sequential-attack-detection.md` — CCC steal
- `@concepts/mcp-security-signals-vs-runtime-evidence.md` — FlowGuard peer (K189)
- Cybersec deepen: `@cybersecurity-wiki/concepts/chainwatch-mcp-kill-chain-detection.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems |
| **Author** | Om Narayan, Rashmi Jyoti, Ramkinker Singh |
| **arXiv** | 2607.19432 |
| **Pages** | 6 |
| **Retrieved** | 2026-07-23 |
| **Code** | none public — **NO-GO** install |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.19432-chainwatch-a-kill-chain-aligned-sequential-detec.pdf` |

## Narrative

Per-call MCP defenses miss multi-step attacks (>90% success when undefended) that compose innocent tool calls. ChainWatch: six-stage MCP kill chain + HMM over sessions + 20-dim features; Direct Sequential / Indirect Injection / Hybrid categories.

**CCC steal:** session-level progression detection, not only per-invocation triage. **Cybersec** owns kill-chain ops deepen.
