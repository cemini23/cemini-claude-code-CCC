---
title: "Treatment-blind endpoint integrity — labels ≠ endpoints in security eval (K277)"
type: entity
tags: [entity, pattern, mcp, security-eval, measurement-integrity, k277]
keywords: [k277, integrity-chain, treatment-blind, endpoint-integrity-linter, construct-validity, labels-are-not-endpoints]
related:
  - sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md`
- `@concepts/measurement-integrity-mcp-security-eval.md`

## Raw Concept

Phase-0 entity for CCC K277 — the treatment-blind endpoint-integrity measurement pattern.

## Narrative

Pattern entity for the **seven-link Integrity Chain** + **endpoint-integrity linter** from K277. A security-eval label is a claim over (treatment bytes, executed behavior, authorization, outcome rule, analysis unit); the Integrity Chain makes each link mechanically checkable and fail-closed. No public product — policy/measurement discipline only. Cybersec dual-interest (eval integrity for security benchmarks).

**Phase-0:** `scripts/adopt_k277_phase0.sh`
