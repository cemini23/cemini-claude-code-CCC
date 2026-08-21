---
title: "RL-Trotter — RL for long-time quantum simulation (OOD)"
type: source
tags: [source, arxiv, quantum, physics, ood, k297]
keywords: [2608.20139, RL-Trotter, quantum simulation, Trotter, out-of-domain]
related:
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/brief-k295-k299-harness-wave-2026-08-21.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Reinforcement Learning to Harness Approximation Errors for Long-Time Quantum Simulation |
| **arXiv** | 2608.20139 |
| **Authors** | Shi, Heyl, Moessner, Bukov, Zhao (Peking U / NUS / Augsburg / MPIPKS) |
| **Code** | None public |
| **Retrieved** | 2026-08-21 |

## Narrative

**OOD physics stub.** RL-Trotter treats unavoidable Trotter approximation errors in digital quantum simulation as resources: an RL agent adapts the next Trotter step size from low-dimensional conservation-law signals (energy / energy variance), without access to the target wavefunction, discovering self-correcting sequences where later errors compensate earlier ones. Robust to measurement noise; transfers from small classically-simulable systems to systems ~10× larger; classical pretraining → deployment / limited fine-tuning on quantum hardware.

| Verdict | **OOD** — source stub only, **no** concept depth, **`wont_wire`**. Brief-over-stub (see `briefs/2026-08-21_ccc-k295-k299-sip-ready.md`). Do **not** deep-ingest or wire Atto/3D. |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.20139-reinforcement-learningtoharness-approximation-er.pdf` |
