---
title: Cross-model verified agent translation — parser + validator split
type: concept
tags: [concept, cross-model, verification, dual-agent, k123]
keywords: [2606.20120, parser-validator, self-correction-loop]
related:
  - sources/arxiv-dual-agent-cross-model-protocol-translation-2606.20120.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/claim-drift-automated-research.md
maturity: draft
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- `@sources/arxiv-dual-agent-cross-model-protocol-translation-2606.20120.md` — KIMM lab robotics paper
- `@concepts/gatekeeper-layered-agent-evaluation.md` — layered eval peer
- `@concepts/handoff-validity-agent-harness.md` — structured handoff between parser and validator

## Raw Concept

When translating natural-language intent into executable commands, why split **generation** and **verification** across different model families?

## Narrative

**Cross-model verification** [TENTATIVE — 2606.20120]: Parser Agent (NL → structure) + **deterministic rule engine** (platform constraints) + Validator Agent (different LLM) with structured feedback loop.

| Layer | Trust boundary |
|-------|----------------|
| Parser | Probabilistic NL understanding |
| Rule engine | Deterministic, auditable mapping |
| Validator | Independent model checks completeness/order |

**CCC mapping:** writer subagent + `cursor-audit`/`super-audit` on different models; OpenSpec spec as deterministic contract between NL intent and implementation.

**Verdict:** **REFERENCE** — steal parser/validator split + rule layer; no lab robotics install.

## Snippets

> "A 7 Parser × 3 Validator sweep … evaluates how model scale and Validator type affect translation accuracy and pass rates under cross-model verification."
> — [Source: arxiv-2606.20120-2606-20120v1-dual-agent-framework-for-cross-mode.pdf, retrieved 2026-06-23]
