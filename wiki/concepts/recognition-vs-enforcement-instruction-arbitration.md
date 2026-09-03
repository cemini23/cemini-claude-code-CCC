---
title: "Recognition vs enforcement — instruction arbitration needs an external monitor (CCC K326)"
type: concept
tags: [concept, security, instruction-arbitration, reference-monitor, capability-gating, semantic-authorization, k326]
keywords: [recognition-enforcement gap, instruction arbitration, external reference monitor, HMAC, capability-gated tools, confused deputy, semantic authorization, 2608.28502]
related:
  - sources/arxiv-recognition-without-enforcement-2608.28502.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/mandate-signature-vs-preauth-intent.md
  - concepts/step-level-tool-guardrails.md
  - concepts/bounded-authority-auditable-trajectories.md
  - entities/patterns/external-reference-monitor.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
  - concepts/untrusted-model-delegation-governance.md
  - sources/arxiv-delegation-without-trust-2609.00267.md
  - concepts/attested-capability-leases-execution-time-trust.md
  - sources/arxiv-acle-mcp-attested-capability-leases-2609.02690.md
maturity: draft
created: 2026-08-31
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-recognition-without-enforcement-2608.28502.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/mandate-signature-vs-preauth-intent.md`
- `@concepts/step-level-tool-guardrails.md`
- `@concepts/bounded-authority-auditable-trajectories.md`
- `@entities/patterns/external-reference-monitor.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

The question: when an LLM agent arbitrates among instructions from system prompts, users, memory, and tools, does its *recognition* of provenance give us *enforcement* of trust boundaries? Answer from K326 [Source: wiki/sources/arxiv-recognition-without-enforcement-2608.28502.md]: **no** — recognition (decodable source-format + verbalized detection) is a capability, not a security boundary.

## Narrative

**The gap.** Models linearly decode source-format markers (97.5–100%) and verbalize forged authority on demand, yet still act on spoofed instructions under permissive configurations — one model detects fabricated authority in 98.7% of trials and executes in 99.3%. Fleet-mean execution under diverse novel attacks is only **1.21% [0.5–2.1%]**, but vulnerability concentrates in reproducible prompt–model cells (40–100% deterministic) and shifts up to **47pp across deployment windows**. This defeats both complacency ("average is low") and static certification ("this cell is safe").

**Why prompting fails.** Restrictive policy can drive execution to 0% on the *same* weights — but only for the tested prompt family. Prompt-layer defenses do not generalize across models or adaptive formulations. The enforcement decision must not live in the shared context window the attacker also writes to.

**The external reference monitor (ADOPT policy, K326):**

1. **Authenticated source routing** — per-record MACs (HMAC-SHA256) verify origin + integrity of memory/tool-channel records. Deterministic by construction under EUF-CMA, not an empirical robustness number. Rejects forged/tampered/replayed/unsigned requests (0/900 test cases across 3 model families; 452/452 replays rejected; legitimate throughput 64–100%).
2. **Capability-gated tool execution** — in-context advisory token + **fail-closed external execution-layer verification** the model cannot bypass; single-use nonce-bound tokens; channel-agnostic.
3. **Know the residual boundary: semantic authorization.** Authenticated origin ≠ delegated authority. A confused deputy (legitimate ingestor signing attacker-controlled content) defeats signing alone unless the ingestor cannot mint capability tokens. The remaining problem — does this authenticated message *carry authority* for this action — is semantic, and external signing cannot solve it (pairs `@concepts/mandate-signature-vs-preauth-intent.md`, K310).

**CCC policy lines:**

- Treat any model self-arbitration as a **capability claim**, never a boundary. For high-blast tools, require an external fail-closed check (pairs `@concepts/step-level-tool-guardrails.md`, K312, and `@concepts/signed-mandate-mcp-protocol-enforcement.md`, K285).
- Gate the tool execution layer, not the model's opinion.
- When an authenticated message arrives, ask separately: who signed it (cryptographic) and whether its content is authorized (semantic) — never collapse the two.

**Zero attack text.** This concept and its source page contain no prompts, no jailbreaks, no PoCs. The paper's forthcoming InstructionArbitrationBench releases full verbatim attack prompts; CCC does not clone it (no SPDX) and does not paste them.

| Confidence | `[CONFIRMED]` — fleet measurements + EUF-CMA sketch in paper; CCC policy adoption, not reproduced |
|------------|------------|
