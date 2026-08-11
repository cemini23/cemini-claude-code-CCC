---
title: "VectraYX-Vision-1B — Spanish/LATAM cybersecurity VLM with MCP tool tokens"
type: source
tags: [source, arxiv, cybersecurity, vlm, mcp, k261]
keywords: [2608.08477, VectraYX, SigLIP, llama.cpp, Spanish]
related:
  - entities/tools/vectrayx-vision-1b.md
  - concepts/scaffold-over-tool-interface.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
---

## Relations

- `@entities/tools/vectrayx-vision-1b.md`
- `@concepts/scaffold-over-tool-interface.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision–Language Model with Structured Visual Reasoning and Native Tool Use |
| **arXiv** | 2608.08477 |
| **Author** | Juan S. Santillana (Globant) |
| **Retrieved** | 2026-08-11 |

## Narrative

Sub-2B VLM for Spanish cybersecurity imagery (IDA/Ghidra/Wireshark/Nmap/Metasploit/Volatility panes): frozen SigLIP encoder + ~1.04B Spanish decoder, `<|think|>` structured visual reasoning, native MCP `<|tool_call|>` tokens, llama.cpp LLaVA export. Reports a **negative** preliminary visual-grounding result.

**CCC:** thin awareness stub — vision product OOD; cybersec-primary. No model download.

| Verdict | **REFERENCE** awareness. **NO-GO** weights/runtime. Route Cybersecurity wiki. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.08477-vectrayx-vision-1b-a-sub-2b-spanish-latam-cybers.pdf`
