---
title: "Validating LLM-modernized scientific software through differential fault injection"
type: source
tags: [source, arxiv, fault-injection, llm-modernization, off-nominal, k284]
keywords: [2608.14527, FTINJ, GAMESS, SCF, differential-fault-injection, silent-data-corruption, off-nominal-fidelity]
related:
  - concepts/differential-fault-injection-llm-modernization.md
  - entities/patterns/differential-fault-injection-validation.md
  - concepts/mutation-consistency-metamorphic-transpiler-testing.md
  - sources/brief-k282-k284-harness-wave-2026-08-17.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - "@cybersecurity-wiki/concepts/differential-fault-injection-llm-code-stub.md"
maturity: draft
created: 2026-08-17
updated: 2026-08-17
---

## Relations

- `@concepts/differential-fault-injection-llm-modernization.md`
- `@entities/patterns/differential-fault-injection-validation.md`
- `@concepts/mutation-consistency-metamorphic-transpiler-testing.md` — K235: metamorphic/mutation testing of transpilers; K284 is off-nominal paired fault injection
- `@cybersecurity-wiki/concepts/differential-fault-injection-llm-code-stub.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Validating LLM-Modernized Scientific Software Through Differential Fault Injection |
| **arXiv** | 2608.14527 |
| **Authors** | Evan Coleman, Yuzhong Shen, Masha Sosonkina, Peng Xu (U. Mary Washington / Old Dominion / Ames Lab + Iowa State) |
| **Code** | **FTINJ** harness described but **no public SPDX clone found** → policy only |
| **Retrieved** | 2026-08-17 |

## Narrative

LLM coding agents are increasingly used to modernize legacy Fortran in production scientific software (GAMESS). Nominal regression tests establish correctness only for the inputs/conditions they exercise — they generally do **not** exercise how an implementation responds to faults, numerical perturbations, or reduced precision. A modernized implementation can preserve nominal outputs without preserving **off-nominal** behavior, which is precisely where trust ultimately rests.

The paper presents **differential fault injection**: identical, deterministic faults are injected into the original and modernized implementations at **shared driver-level sites** (the SCF driver is left untouched; the converted integral kernels are the varying component). This isolates the converted kernels as the unit under test and removes injection-placement/timing as confounds. **FTINJ** provides twelve injection sites in the shared SCF driver, magnitude-parameterized faults (in equivalent bits), phase-aware triggers, deterministic per-rank replay, and full run-level provenance.

**Results.** Across >2,200 runs: transient-fault absorption follows a contraction-based model (predicted 0.74/1.49 it/bit vs measured 0.82/1.50); persistent Fock perturbations give ~factor-of-two energy-error reduction per bit, crossing the SDC threshold near 2⁻²²; reduced precision can **manufacture false convergence** (bf16 truncation declared convergence 7 iterations early with 73 mHa error); large orbital perturbations converge to alternate SCF solutions; rank-local disagreement near the convergence threshold causes parallel deadlocks. A one-line convergence-scalar synchronization change eliminates the deadlock channel (8/10 → 0/10) without altering outcomes outside its scope.

For the primary differential comparison, original and modernized kernels agree in **outcome classification, iteration count, injection count, and final energy for all 200 paired injections** (including 15+25 silent corruptions the modernized code reproduced identically). After matching harness + compilation flags, the composed (modernized + hardened) binary matches the hardened original in **40/40** paired runs.

**Key threat-to-validity lesson:** a one-iteration numerical skew between source trees was traced to a *compilation-flag* difference (-O1 vs -O2), not the modernization — only found by comparing per-run event logs and paired outcomes. Harness/compiler config matching is as critical as the code diff.

| Verdict | **ADOPT** off-nominal paired differential validation for LLM code transforms. No public ftinj SPDX clone → **policy only** (no GAMESS runtime on CCC laptop). Cybersec brief stub. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.14527-validating-llm-modernized-scientific-software-th.pdf`
