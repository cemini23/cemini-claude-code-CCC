---
title: "MemSecBench — memory poisoning Write–Execute–Forget lifecycle"
type: source
tags: [source, arxiv, memory, security, poisoning, k228]
keywords: [2607.27080, MemSecBench, Write-Execute-Forget, Mem0, OpenClaw]
related:
  - concepts/memory-poisoning-write-execute-forget-lifecycle.md
  - concepts/agent-data-injection-attacks.md
  - concepts/hidden-user-state-recovery-audit.md
  - concepts/hierarchical-bounded-agent-memory.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@concepts/memory-poisoning-write-execute-forget-lifecycle.md`
- `@concepts/agent-data-injection-attacks.md`
- `@concepts/hidden-user-state-recovery-audit.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair |
| **Author** | Chen et al. (ZJUT) |
| **arXiv** | 2607.27080 |
| **Pages** | 28 |
| **Retrieved** | 2026-07-30 |
| **Code** | no public artifact at Phase-0 — **NO-GO** |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.27080-memsecbench-tracking-agent-memory-poisoning-from.pdf` |

## Narrative

**310** cases × **24** harness×memory×LLM configs. Malicious memory persists **84.2%**; full Write–Execute **50.3%**; selective repair **56.1%** among poisoned. **ADOPT** WEF lifecycle checklist for memory backends; **NO-GO** code.
