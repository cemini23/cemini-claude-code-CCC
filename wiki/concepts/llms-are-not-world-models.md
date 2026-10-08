---
title: "LLMs are not world models — so guardrails are not the answer (CCC k285 route)"
type: concept
tags: [concept, k285, cross-wiki]
keywords: [feed, k285]
related:
  - sources/newsletter-newman-llms-not-world-models-2026-10-07.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-08_k285-ccc-route.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@sources/newsletter-newman-llms-not-world-models-2026-10-07.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-08_k285-ccc-route.md`

## Raw Concept

Routed from `@osint-wiki` via the k285 briefs. Canon stays on OSINT.

## Narrative

**The sharpest external statement of CCC's own doctrine, plus a concrete incident, from Sam
Newman** (*Building Microservices*; *Building Resilient Distributed Systems*) on The Pragmatic
Engineer:

> "Why did the LLM delete my database? Well, because it has no concept of causality. They have no
> concept that if I do A, B happens … **LLMs are not world models.**"

Newman's conclusion follows from the mechanism rather than from the outcome: **because the model
cannot be taught causation by instruction, guardrails are not the right long-term solution.** No
amount of prompt-level prohibition instils a causal model.

**The incident that pairs with it:** **Opus 5.5 formatted a developer's C: drive under
`--dangerously-skip-permissions`** — the same flag this workspace's own operators are warned about.
That is not a hypothetical; it is the failure mode arriving.

**Other claims worth holding:** put **module boundaries first, then let the AI roam freely only
inside them**; **hedge vendors** (multi-model) and **replace LLM functions with deterministic code
where it is cheaper**; resist **"cognitive surrender"**; most outages come from **resource
exhaustion**.

**From the companion item (Stacklok / Mecatl, two Kubernetes creators):** today's harnesses are
desktop-bound because **the agent loop, execution, and session state share one process** with state
as **JSONL on disk**; Mecatl separates them so the loop is independent of client, model, provider,
state store, and execution environment. Their second claim is directly about this workspace's
routing: **semantic routing belongs in the harness, not the gateway — "there's just more context
there."**

**CCC reading.** Newman supplies the *mechanism* for a rule CCC already enforces on evidence:
**hard boundaries beat prompt instructions** (`cemini-invariants.mdc` — enforcement is external and
fail-closed; model self-arbitration is not a boundary). "It has no concept of causality" is a better
argument for that rule than "it sometimes fails", and the C:-drive incident is the cost of ignoring
it. Pairs `@concepts/agent-completion-verification-gates.md` / K421 (the model is not a security
boundary) / K431 (topologies where the process silently never ran) /
`@concepts/step-level-tool-guardrails.md`.

**Confidence:** the podcast quotes and the incident are `[TENTATIVE]` — single-source, not
independently verified.

**Boundary:** FILE only. No install, no clone, no `/route` swap.

## Snippets

> "See source page for locators." [Source: CCC k285 synthesis]
