---
title: "Differential fault injection for LLM modernization (K284)"
type: concept
tags: [concept, fault-injection, llm-modernization, off-nominal, verification, k284]
keywords: [2608.14527, FTINJ, differential-fault-injection, off-nominal-fidelity, silent-data-corruption, measurement-guided-hardening]
related:
  - sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md
  - entities/patterns/differential-fault-injection-validation.md
  - concepts/mutation-consistency-metamorphic-transpiler-testing.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
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
- `@entities/patterns/differential-fault-injection-validation.md`
- `@concepts/mutation-consistency-metamorphic-transpiler-testing.md` — K235
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — K162 verification hierarchy
- `@cybersecurity-wiki/concepts/differential-fault-injection-llm-code-stub.md`

## Raw Concept

A nominal test suite proves an LLM code transform preserves behavior on the *happy path*. How do you verify it preserves the response to faults, perturbations, and reduced precision — the off-nominal behavior trust actually rests on?

## Narrative

K284 (arXiv 2608.14527) applies **differential fault injection** to LLM-modernized scientific code: inject identical, deterministic faults into original and modernized implementations at shared driver-level sites, then compare their responses paired-run by paired-run.

### Steal (ADOPT)

1. **Off-nominal paired validation, not nominal alone.** A passing test suite does not exercise fault response, perturbation absorption, or reduced-precision behavior. A modernization can preserve nominal outputs while silently changing off-nominal behavior. Pair the *differential* comparison: identical marginal outcome distributions can conceal per-run disagreements, so the paired comparison (same fault → same classification/iteration/energy) is the acceptance criterion.
2. **Shared-driver instrumentation isolates the unit under test.** Put every injection site in code *shared* by both trees, at the data interfaces surrounding the converted kernel. The converted kernel becomes the only varying component; injection placement/timing stop being confounds.
3. **Differential compare original vs modernized at the same sites.** For 200 paired injections the modernized kernel matched the original in outcome classification, iteration count, injection count, and final-energy representation — including every silent corruption. That's the off-nominal-equivalence evidence a clean-path suite cannot provide.
4. **Measurement-guided hardening loop with explicit acceptance criteria.** Campaign results localize a weakness → a bounded repair task for the LLM agent → re-measure. Accept only if: no new SDC/CRASH/HANG vs reference, fewer outcomes from the targeted failure mechanism, and no increased absorption cost outside tolerance. Human defines the fault model + acceptance criteria; the agent proposes; the campaign judges.
5. **Match harness *and compilation* configuration.** A residual one-iteration skew was traced to -O1 vs -O2, not the code. Compiler-flag and harness-version skew produce false "differences" — compare per-run provenance logs, not just nominal outputs.
6. **Off-nominal fidelity ≠ absolute resilience.** The differential experiment asks "does the modernization preserve the reference response" — the reference's behavior is not assumed desirable. Hardening is a separate, second question.

### Why this pairs K235 (mutation-consistency) and K162 (verification hierarchy)

K235's metamorphic/mutation-consistency testing verifies transpilers against *intended* input/output relations. K284 generalizes to **off-nominal** perturbations — the input is corrupted, not just transformed, and the acceptance relation is "matches the original's fault response." K162's verification hierarchy warns against trusting self-eval without external verification: here the external authority is the **experimental campaign** with deterministic replay and explicit acceptance criteria — the LLM's modernization claim is adjudicated by measurement, not review.

### Local adopt

No public SPDX `ftinj` clone found → **policy only**. Scientific/GAMESS domain: **`policy_wired`**, no GAMESS runtime on the CCC laptop.

| Verdict | **ADOPT** off-nominal paired differential validation + measurement-guided hardening. Policy only. Cybersec brief stub. |
