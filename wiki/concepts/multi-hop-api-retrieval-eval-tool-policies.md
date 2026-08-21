---
title: "Multi-hop API + retrieval eval under tool-use policies — VAKRA axes (K275)"
type: concept
tags: [concept, benchmark, tool-policy, multi-hop, eval, k275]
keywords: [2608.12282, VAKRA, API-hops, multi-source, NL-policy-constraints, re-exec-verify]
related:
  - sources/arxiv-vakra-multi-hop-api-retrieval-2608.12282.md
  - entities/tools/vakra.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
  - concepts/phase1-adopt-wire.md
  - sources/arxiv-convergent-detour-hijacking-cdh-2608.12273.md
  - sources/arxiv-role-specialization-model-rsm-2608.12311.md
  - concepts/terminal-state-eval-discovery-reliability-gap.md
  - entities/tools/thinkingbox.md
  - sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-13
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-vakra-multi-hop-api-retrieval-2608.12282.md`
- `@entities/tools/vakra.md`
- `@concepts/verifiable-deterministic-agent-benchmarking.md`

## Raw Concept

What should an enterprise-agent eval measure when reasoning spans structured APIs, document collections, and natural-language tool-use policies in a single chain?

## Narrative

K275 transfers VAKRA's **eval design** (not its dataset/code — CC-BY-NC-SA) to Cemini harness evals. The benchmark composes three settings of increasing difficulty and verifies correctness by **re-executing predicted tool calls against live APIs**, accommodating multiple valid paths.

### Steal (ADOPT — eval axes)

1. **API interaction paradigm inverts model rankings** — endpoint-style vs compositional BI APIs favor different models. Don't benchmark one interaction style.
2. **Reasoning depth collapses accuracy** — most models lose >50% as hops increase (2–5 hop chains). Track accuracy by depth, not aggregate.
3. **Language-mediated reasoning is the bottleneck**, not tool-invocation mechanics — entity disambiguation, cross-source grounding, schema alignment.
4. **Policy-constrained / unanswerable queries are the hardest signal** — frontier models score 2.4% on unanswerable-with-policy questions. Eval must include refusal/unanswerable detection, not just answer accuracy.
5. **Fixed-harness isolation** — hold the agent architecture (ReAct) constant to isolate model capability from scaffolding (pairs K262 scaffolding > interface).

| Verdict | **ADOPT** eval axes + re-exec verification. **NO-GO** clone (`IBM/vakra`, CC-BY-NC-SA 4.0 — non-commercial). HF dataset WATCH only. |

## Snippets

> "most models lose over 50% accuracy as reasoning depth increases"

> "failures concentrate at language-mediated reasoning — entity disambiguation, cross-source grounding, rather than tool invocation mechanics"

[Source: arXiv 2608.12282 p.1]
