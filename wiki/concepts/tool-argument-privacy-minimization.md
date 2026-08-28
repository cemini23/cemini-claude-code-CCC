---
title: "Tool-argument privacy minimization — rewrite, don't only allow/block (CCC K315)"
type: concept
tags: [concept, privacy, tool-calls, data-minimization, middleware, k315]
keywords: [ToolMinimize, PSD, argument rewriting, schema-aware necessity, minimum necessary, 2608.24957]
related:
  - sources/arxiv-toolminimize-privacy-args-2608.24957.md
  - concepts/step-level-tool-guardrails.md
  - concepts/authorization-to-effect-closure.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-toolminimize-privacy-args-2608.24957.md`
- `@concepts/step-level-tool-guardrails.md`
- `@concepts/authorization-to-effect-closure.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

The question: allow/block gates decide *whether* a tool call happens, but they never decide *what data* the tool receives. How do we minimize privacy-sensitive data (PSD) in tool-call arguments without losing task validity? Answer from ToolMinimize [Source: wiki/sources/arxiv-toolminimize-privacy-args-2608.24957.md]: schema-aware rewriting middleware.

## Narrative

Tool call **over-sharing** is the systematic inclusion of PSD beyond what the invoked tool requires — crossing a trust boundary to a third-party service on every invocation. Measured: 81–88% of calls over-share under default prompts; explicit privacy prompts leave 36–76%. Prompting alone cannot fix this.

Existing defenses and their gap:

| Defense | Mechanism | Gap |
|---------|-----------|-----|
| Call-level gating (AudAgent, PrivacyChecker) | allow/block per call | can't rewrite values — leaks or loses task |
| Argument-level gating (Progent) | JSON Schema allow/block with fallback | still binary, not graduated |
| Information-flow control (Fides, RTBAS, CaMeL) | label propagation + capability deny | no field-level graduated rewriting |
| PII detection (Presidio, Comprehend) | token pattern matching | misses implicit PSD (a hospital name that implies a diagnosis) |

The ToolMinimize pattern (ADOPT policy):

1. **Intercept** tool calls between agent and tool — no LLM/framework/tool changes.
2. **Classify** PSD in arguments; compute a quantitative privacy cost.
3. **Rewrite** to minimum necessary via four operations: **removal, generalization, substitution, truncation** (1.77 ms median latency).
4. **Validate** task validity — 100% argument-level validity (TOST p<0.001) at 81.2–92.0% privacy-cost reduction; 79.0% on unannotated MCP schemas without `minimum_necessary` metadata.

CCC policy: for high-blast tool surfaces, minimize **values**, not only allow the call. Pairs `@concepts/step-level-tool-guardrails.md` (gate the step) and `@concepts/authorization-to-effect-closure.md` (admission ≠ effect). This is a middleware *design* reference — Cemini does not run a tool-call proxy; the principle wires into policy (allow/deny → "what data may cross").

| Confidence | `[CONFIRMED]` — controlled measurement + live validation in paper; policy adoption, not yet reproduced in CCC |
|------------|------------|

## Snippets

> "No existing system performs schema-aware, argument-level data minimization by rewriting tool-call fields while preserving task validity." [Source: arXiv 2608.24957 §I]

> "A weather query naming a cancer-treatment center either proceeds and leaks the facility or is refused, losing the task." [Source: arXiv 2608.24957 §I, paraphrase]
