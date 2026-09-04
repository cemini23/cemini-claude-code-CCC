---
title: "Measurement integrity in MCP security evaluation — labels ≠ endpoints (K277)"
type: concept
tags: [concept, mcp, security-eval, measurement-integrity, construct-validity, k277]
keywords: [2608.12880, treatment-leakage, integrity-chain, endpoint-integrity-linter, treatment-blind, ATTACK_SUCCESS]
related:
  - sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md
  - entities/patterns/treatment-blind-endpoint-integrity.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
  - entities/tools/intersage.md
  - sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md
  - "@cybersecurity-wiki/concepts/measurement-integrity-mcp-security-eval.md"
  - concepts/agentified-eval-evidence-tree-harness.md
  - sources/arxiv-harnesseval-w-visual-worlds-2608.16859.md
  - concepts/terminal-state-eval-discovery-reliability-gap.md
  - entities/tools/thinkingbox.md
  - sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md
  - concepts/bounded-authority-auditable-trajectories.md
  - sources/arxiv-llm-agents-software-systems-security-slr-2608.28490.md
  - concepts/knowledge-commons-governance-multi-agent.md
  - sources/arxiv-research-swarm-cheating-whistleblowing-2609.04170.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-14
updated: 2026-09-04
---

## Relations

- `@sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md`
- `@entities/patterns/treatment-blind-endpoint-integrity.md`
- `@concepts/mcp-claim-validation-and-parameter-grounding.md`

## Raw Concept

How do you know an MCP agent-security eval label means what it claims? When the grader's class assignment is gated by treatment metadata rather than observed behavior, the endpoint (behavior) and the label (claim) diverge.

## Narrative

K277 is a **campaign-bounded measurement audit** of a preserved MCP security-eval: 10,200 execution rows → 180 model-bound requests → 45 semantic requests → 15 observable stimuli. The historical grader exhibited **direct treatment leakage** — `ATTACK_SUCCESS` was gated on treatment metadata, so identical fixed behavior could change class under treatment relabeling. A treatment-blind reconstruction corrected **58** historical `ATTACK_SUCCESS` / `HIJACK_ATTEMPT` labels to authorized benign completions while preserving the 3 verified protected-data transfers + 1 unauthorized-forwarding case. The locked v2 census contains **exactly zero `ATTACK_SUCCESS`** records.

### Steal (ADOPT)

1. **Labels are not behavioral endpoints.** A label ("attack") is a claim about behavior + authorization + outcome rule + analysis unit. Bind all five before interpreting the label.
2. **Treatment-blind grading.** Graders must not see treatment metadata when assigning outcome classes; treatment invariance is necessary (though not sufficient — codebook ambiguity remains).
3. **Seven-link Integrity Chain** — a procedural audit framework: each link has a verification question, minimum evidence, and a fail-closed condition (treatment bytes → executed behavior → authorization → outcome rule → analysis unit). A failed link halts the stated inference.
4. **Endpoint-integrity linter** — mechanically testable measurement defects, scope-bounded.
5. **Scope honesty.** A measurement audit is not a population attack-rate, model-ranking, defense-efficacy, or causal estimate. Don't convert campaign counts into security claims they can't support.

| Verdict | **ADOPT** Integrity Chain + treatment-blind grading. No public product; policy/measurement discipline only. Cybersec brief (eval integrity for security benchmarks). |

## Snippets

> "An agent does not encounter a tool as an abstract capability. It encounters a name, a schema, and prose explaining what that tool is for." — [Source: arXiv 2608.12880 p.1]

> "The Treatment–Behavior–Endpoint Integrity Chain turns that discipline into a checkable workflow." — [Source: arXiv 2608.12880 p.20]
