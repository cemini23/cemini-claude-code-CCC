---
title: LLM verification layer — accept / reject / escalate (K264)
type: concept
tags: [concept, verification, harness, hitl, k264]
keywords: [2608.09857, accept-escalate-reject, LLM-as-judge, chief-judge]
related:
  - sources/arxiv-agentic-harnesses-verification-layers-2608.09857.md
  - entities/tools/verification-layers-robot.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/inspectable-tool-region-attribution.md
  - concepts/persona-hat-claude-code-sdlc.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-11
updated: 2026-08-15
---

## Relations

- `@sources/arxiv-agentic-harnesses-verification-layers-2608.09857.md`
- `@entities/tools/verification-layers-robot.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`

## Raw Concept

How should an independent layer gate plans before irreversible tool/MCP execution?

## Narrative

K264: ensemble judges emit **accept / reject / escalate**; chief judge scores judge reasoning (blind to plan). Robotics product OOD — middleware pattern transfers to LIVE/high-blast tool gates.

### Steal (ADOPT)

1. Between plan and high-blast execute: explicit ternary gate (pairs K239 fidelity / K244 clarify).
2. Prefer independent review of **reasoning quality**, not rubber-stamp of the plan text alone.
3. Escalate on judge disagreement / uncertainty — do not silent-accept (pairs trajectory sentinel / K242).

| Verdict | **ADOPT** policy. Robot code **NO-GO** (404). |
