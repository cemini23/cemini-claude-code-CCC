---
title: "Labels Are Not Endpoints — treatment leakage and construct validity in MCP security evaluation"
type: source
tags: [source, arxiv, mcp, security-eval, construct-validity, measurement-integrity, k277]
keywords: [2608.12880, treatment-leakage, integrity-chain, endpoint-integrity-linter, ATTACK_SUCCESS, HIJACK_ATTEMPT, treatment-blind]
related:
  - concepts/measurement-integrity-mcp-security-eval.md
  - entities/patterns/treatment-blind-endpoint-integrity.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - "@cybersecurity-wiki/sources/arxiv-2608-12880-labels-not-endpoints.md"
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@concepts/measurement-integrity-mcp-security-eval.md`
- `@entities/patterns/treatment-blind-endpoint-integrity.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation |
| **arXiv** | 2608.12880 |
| **Authors** | Rana Muhammad Ahmed, Sabahat Abbas (Bahria University, Islamabad) |
| **Code** | None public — campaign-bounded measurement audit; contributes an executable endpoint-integrity linter but no released repo |
| **Retrieved** | 2026-08-14 |

## Narrative

Campaign-bounded measurement audit of a preserved MCP agent-security eval. Traces **10,200 execution rows → 180 model-bound requests → 45 semantic requests → 15 observable stimuli**. Two schema treatments were delivered, but the planned external payload-family corpus was not. The historical grader **leaked treatment**: treatment metadata gated the `ATTACK_SUCCESS` class, so fixed behavior could change class under treatment relabeling.

**Treatment-blind reconstruction** corrects **58 historical `ATTACK_SUCCESS` / `HIJACK_ATTEMPT` labels** to authorized benign completions, while preserving **3 verified protected-data transfers** and **1 separate unauthorized-forwarding case**. The locked v2 census contains **exactly zero `ATTACK_SUCCESS`** records; the forwarding case (EI-067F9857ECE149) remains `HIJACK_ATTEMPT` at a semantic boundary concerning objective completion. Dual-reviewer blinded concordance on the 96 structurally-interpretable requests agreed with reviewer-consensus classes but differed from the locked codebook on **4 construct-boundary cases**.

Contributions: a **seven-link Integrity Chain** (bind treatment bytes → executed behavior → authorization → outcome rule → analysis unit before interpreting) and a **scope-bounded endpoint-integrity linter** for mechanically testable measurement defects. Explicit scope: a measurement audit, **not** a population attack-rate, model-ranking, defense-efficacy, or causal estimate.

| Verdict | **ADOPT** Integrity Chain + treatment-blind grading discipline. Labels ≠ behavioral endpoints. No public product to clone. Cybersec brief. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.12880-labels-are-not-endpoints-treatment-leakage-and-c.pdf`
