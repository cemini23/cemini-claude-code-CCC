---
title: "Differential fault injection validation — off-nominal paired testing pattern"
type: entity
tags: [entity, pattern, fault-injection, llm-modernization, verification, k284]
keywords: [k284, FTINJ, differential-fault-injection, off-nominal-fidelity, policy-wired]
related:
  - sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md
  - concepts/differential-fault-injection-llm-modernization.md
  - concepts/mutation-consistency-metamorphic-transpiler-testing.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - concepts/phase1-adopt-wire.md
  - "@cybersecurity-wiki/concepts/differential-fault-injection-llm-code-stub.md"
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md`
- `@concepts/differential-fault-injection-llm-modernization.md`
- `@concepts/mutation-consistency-metamorphic-transpiler-testing.md`
- `@cybersecurity-wiki/concepts/differential-fault-injection-llm-code-stub.md`

## Raw Concept

Phase-0 entity for CCC K284 — differential fault injection validation (pattern entity; no public SPDX clone).

## Narrative

FTINJ is a self-contained fixed-form Fortran harness + anchor-based installer + campaign driver for GAMESS SCF fault injection. **No public SPDX clone found** → no `.local/adopts` entry; **`policy_wired`** only. The transferable contribution is the *procedure*, not the artifact: identical deterministic faults at shared driver sites, paired original-vs-modernized comparison, outcome classification (ABSORBED-CLEAN / ABSORBED-DELAY / SDC / BAD-ENERGY / UNCONVERGED / CRASH / HANG), and a measurement-guided hardening loop with explicit acceptance criteria.

Scientific/GAMESS domain: **no runtime wiring** on the CCC laptop.

**Phase-0:** `scripts/adopt_k284_phase0.sh`
