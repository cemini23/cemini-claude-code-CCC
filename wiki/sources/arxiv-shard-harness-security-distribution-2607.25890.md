---
title: "SHarD — distributing security controls through harness engineering"
type: source
tags: [source, arxiv, harness, security, sandbox, skill-scan, k225]
keywords: [2607.25890, SHarD, OWASP agentic, Pi harness, skill scanning]
related:
  - concepts/distributed-harness-security-controls.md
  - entities/tools/shard-secure-harness-distribution.md
  - concepts/etclovg-harness-layers.md
  - concepts/skill-vetting.md
  - concepts/agent-vm-sandboxing.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@concepts/distributed-harness-security-controls.md`
- `@entities/tools/shard-secure-harness-distribution.md`
- `@concepts/skill-vetting.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Distributing Security Controls Through Harness Engineering |
| **Author** | William R. Gore (Georgia Tech) |
| **arXiv** | 2607.25890 |
| **Pages** | — |
| **Retrieved** | 2026-07-30 |
| **Code** | `wrgore/agent-security-lab` MIT (~944KB); `wrgore/shard-demo` MIT (~23MB) — **GO** REFERENCE |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.25890-distributing-security-controls-through-harness-e.pdf` |

## Narrative

SHarD embeds OS sandbox + skill scan + tool restriction in a distributable Pi-based harness. OWASP-agentic **23-test** suite; SHarD adjusted score **100%** matching best secured commercial agent. Notes model non-determinism → inconsistent security outcomes. **ADOPT** harness-distributed controls; **GO** MIT clones under `.local/adopts/` (do **not** pipe `install.sh` to shell — clone only).
