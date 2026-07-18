---
title: "FlowGuard — from signals to evidence for MCP security detection"
type: source
tags: [source, arxiv, mcp, security, evidence, dynamic-analysis, k189]
keywords: [2607.14754, FlowGuard, TRIAGE, RECON, STRIKE, command injection, SSRF, Fudan]
related:
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/safeclawbench-staged-security-endpoints.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - sources/brief-k189-flowguard-mcp-evidence-2026-07-18.md
  - briefs/2026-07-18_ccc-handoff-flowguard-mcp-security.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- `@concepts/mcp-security-signals-vs-runtime-evidence.md` — synthesized steal
- `@concepts/seclaw-agent-security-evaluation.md` — agent-security eval peer
- `@concepts/safeclawbench-staged-security-endpoints.md` — staged security endpoints peer
- `@concepts/mcp-server-runtime-fault-taxonomy.md` — MCP runtime fault peer
- Cybersec deepen: `@cybersecurity-wiki/concepts/mcp-security-evidence-grounded-detection.md`
- `@sources/brief-k189-flowguard-mcp-evidence-2026-07-18.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | FlowGuard: From Signals to Evidence for MCP Security Detection |
| **Author** | Baichao An, Pei Chen, Geng Hong, Yueyue Chen, Mengying Wu (Fudan) |
| **arXiv** | 2607.14754 |
| **Pages** | 19 |
| **Retrieved** | 2026-07-18 |
| **Code** | none public at Phase-0 (NO-GO install) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.14754-flowguard-from-signals-to-evidence-for-mcp-secur.pdf` |

## Narrative

### Thesis

Existing MCP scanners over-trust **semantic signals** (e.g. credential-like strings that may be placeholders). FlowGuard separates (a) **runtime evidence** for execution-path risks from (b) **semantic analysis** for metadata/returned-content risks.

### Pipeline (Fig. 2)

Five phases over Tool Discovery → Invocation → Response Consumption: **TRIAGE → RECON → STRIKE → ANALYSIS → REFINEMENT**. Schema-valid probes; recon narrows payloads; evidence adjudication; history-guided refinement until verdict, budget exhaust, or no new signal.

### Attack surfaces (Fig. 1)

| Surface | Example risks |
|---------|----------------|
| Metadata (Discovery) | Tool poisoning, rug-pull |
| Execution (Invocation) | Command injection, SSRF, file-system access |
| Response | Credential leakage, response-layer prompt injection |

### Results

1,880-case executable benchmark; F1 **0.879** (command injection) and **0.942** (file-system access); up to **2.23×** lower latency vs prior dynamic scanners; **523** findings on **326** real MCP servers.

### CCC steal

Do not treat MCP scanner / LLM “looks risky” output as a bind-blocking finding without **execution evidence** where the risk is execution-path. Pair with K162 verification hierarchy and K172 validation-before-bind.

## Snippets

> "Existing MCP security scanners primarily reason about suspicious semantic signals rather than real execution behaviors" — Abstract

> "This gap requires runtime evidence for execution-related risks and careful semantic analysis for risks carried in metadata or returned content." — Abstract
