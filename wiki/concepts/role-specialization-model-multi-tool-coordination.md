---
title: "Role Specialization Model — multi-tool LLM coordination in agentic SE (K276)"
type: concept
tags: [concept, agentic-se, multi-tool, role-coordination, hitl, k276]
keywords: [2608.12311, RSM, role-specialization, prompt-hardening, SE-3.0, ISO-25010]
related:
  - sources/arxiv-role-specialization-model-rsm-2608.12311.md
  - entities/patterns/role-specialization-model.md
  - concepts/code-as-agent-harness.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/marc-clinical-multi-agent-coordination.md
  - entities/tools/marc-v1.md
  - sources/arxiv-marc-v1-clinical-multi-agent-2608.13476.md
  - concepts/persona-hat-claude-code-sdlc.md
  - sources/brief-k238-persona-hat-claude-gcp-2026-08-15.md
  - concepts/enterprise-conversational-multi-agent-analytics.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-13
updated: 2026-08-20
---

## Relations

- `@sources/arxiv-role-specialization-model-rsm-2608.12311.md`
- `@entities/patterns/role-specialization-model.md`
- `@concepts/code-as-agent-harness.md`

## Raw Concept

How should a human orchestrator divide responsibility across multiple LLM tools so their capabilities complement rather than overlap, and what breaks in practice?

## Narrative

K276 transfers the **Role Specialization Model** — separation-of-concerns applied to assistive tools, not code — to Cemini's multi-tool workflow (claude-ds worker, route skill, subagents). Case study: Antigravity (architect/designer) + Gemini CLI (data/docs/pipelines) + Qwen Code (local code, privacy) building a Python desktop app.

### Steal (ADOPT)

1. **Explicit role distribution per tool** with stated responsibility domains — but expect drift: absent scope boundaries, capability overlap, and context-switching cost break the plan. The human orchestrator actively manages deviations.
2. **HITL verification of agent outputs remains indispensable** — review/approve before integrating into the repo (no pure vibe coding for durable artifacts).
3. **Prompt-hardening via explicit negative constraints** — when an agent with tool access tries unavailable internal tools, negate explicitly: "DO NOT run commands / Do NOT use tools / write plain text." (pairs K244 clarify-before-act, K262).
4. **Failure-backed instructions only** — over-detailed rule files reduce success and raise inference cost; add a rule only after a demonstrated recurrent error (pairs K273 ACM baseline discipline).
5. **CoT paradox awareness** — explicit step-by-step reasoning can degrade simple instruction-following; match prompting to task complexity.

| Verdict | **ADOPT** role coordination + HITL + prompt-hardening. Case study — no product install; pattern only. |

## Snippets

> "role specialization is a valid design principle for multi-tool LLM coordination but requires explicit scope boundaries to prevent unintended overlaps"

> "prompt hardening through explicit negative constraints was found to be a critical technique … for ensuring agent output integrity in environments with system-tool access"

[Source: arXiv 2608.12311 p.19]
