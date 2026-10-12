---
title: "Typed-judgement desk — code fetches, the model judges, code decides (K286 + K288)"
type: concept
tags: [concept, k286, k288, decision-models]
keywords: [jev, typed-judgement, decision-model, pplx-decider, unsloth]
related:
  - concepts/nomos-compiled-tool-call-gate.md
  - concepts/overclaiming-propensity-agent-measurement.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-12_k286-k288-ccc-route.md
  - briefs/2026-10-12_ccc-k445-k448-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-12
updated: 2026-10-12
---

## Relations

- `@concepts/nomos-compiled-tool-call-gate.md`
- `@concepts/overclaiming-propensity-agent-measurement.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-12_k286-k288-ccc-route.md`

## Raw Concept

Routed inbound via `@osint-wiki` K286 / K288 (CCC-home desks), delivered in `briefs/`. Canon stays
on OSINT.

## Narrative

**Code fetches, the model judges, code decides.** A **typed decision engine** replaces the agent seat's prose opinion: send state + typed questions, receive typed answers with probabilities. Three question types are the whole API — `noul` (an if, with probability), `choice` (a switch), `score` (a rank). The caller reads a number, applies a threshold, and writes **no parser**. **Four rules:** arithmetic stays in code; **facts kill before judgements** (cheap free/trade/chain kills before one soft-kill judgement call); **question sets, not single questions** (state is charged once per call, output is free); and **shadow mode with disagreement rows** (log would-be actions plus what the old logic did, and read only the disagreements). **K288 update — it became a category:** the pattern went industry-wide in two days (OpenAI Decisions API, Microsoft-Decision-1, Perplexity `pplx-decider-v1.1-27b`, Cloudflare `clef`, Liquid `d1`, vLLM Semantic Router Decision 2.0, LangSmith), and the recipe is now **portable to a 4B model on 8GB VRAM** (Unsloth) — the desk does **not** need a vendor API. **Two numbers to keep:** routing each task to the cheapest adequate model cut median Open SWE cost per task by **64%**; and **agent teams cost 1.8–5.1× more for little gain** (Vals AI: only Sol at medium effort improved) — *the judge is worth it; a bigger team of judges is not*. **The gap it names in our desk:** we run Jev (`jev-mcp`) and the Grok Bot charters, but **no charter routes its judgement through the engine** — every seat judges in prose. **Boundary:** advisory only; **no trading egress** (Jev is a judgement service, not execution); no `/route` swap. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "The judge row is the gap. Our seats take the model's opinion; the pattern replaces it with a typed probability." [Source: OSINT K286/K288 briefs (retrieved 2026-10-12)]
