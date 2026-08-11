---
title: "SHE — Trajectory-driven Safety Harness Evolution"
type: source
tags: [source, arxiv, safety, harness, evolution, k265]
keywords: [2608.09885, SHE, RainbowQTT, Rule-Bank, Tool-Policy, Agent-SafetyBench]
related:
  - concepts/trajectory-driven-safety-harness-evolution.md
  - entities/tools/she-safety-harness.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
---

## Relations

- `@concepts/trajectory-driven-safety-harness-evolution.md`
- `@entities/tools/she-safety-harness.md`
- `@concepts/failed-trajectory-harness-repair.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SHE: Trajectory-driven Safety Harness Evolution for LLM Agents |
| **arXiv** | 2608.09885 |
| **Repo** | `RainbowQTT/SHE` — Apache-2.0 |
| **Retrieved** | 2026-08-11 |

## Narrative

Decomposes harness into **System Prompt / Rule Bank / Safety Memory / Tool Policy**; attribution-guided evolution from trajectory failures; safety–utility validation. Agent-SafetyBench ASR 8.6%→5.5%; transfers across models. OSINT already Extract-cloned; CCC shelf `.local/adopts/SHE` (~5MB).

| Verdict | **ADOPT** four-artifact + attribution loop. **GO** Apache REFERENCE. **HITL only** — never auto-mutate prod. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.09885-she-trajectory-driven-safety-harness-evolution-f.pdf`
