---
title: "External reference monitor — authenticated source routing + capability-gated execution (CCC K326)"
type: entity
tags: [entity, pattern, security, enforcement, reference-monitor, capability-gating, policy-only, k326]
keywords: [k326, external reference monitor, authenticated source routing, HMAC-SHA256, capability-gated tools, fail-closed, semantic authorization, confused deputy]
related:
  - sources/arxiv-recognition-without-enforcement-2608.28502.md
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - concepts/untrusted-model-delegation-governance.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/step-level-tool-guardrails.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
wire_status: policy_wired
created: 2026-08-31
updated: 2026-09-02
---

## Relations

- `@sources/arxiv-recognition-without-enforcement-2608.28502.md`
- `@concepts/recognition-vs-enforcement-instruction-arbitration.md`
- `@concepts/untrusted-model-delegation-governance.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/step-level-tool-guardrails.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

What prompted this page: K326 (arXiv 2608.28502) shows model self-arbitration is a capability, not a security boundary, and implements the enforcement layer that actually rejects forged/tampered/replayed/unsigned requests — the pattern CCC adopts as policy.

## Narrative

**Verdict: ADOPT policy — `policy_wired` (no runtime artifact; no clone).** The external reference monitor is the enforcement half of the recognition–enforcement gap (see `@concepts/recognition-vs-enforcement-instruction-arbitration.md`):

1. **Authenticated source routing** — per-record HMAC-SHA256 MACs on memory/tool-channel records; deterministic rejection of forged/tampered/replayed/unsigned requests under EUF-CMA (0/900 test cases, 3 model families; 452/452 captured-token replays rejected; legitimate throughput 64–100%).
2. **Capability-gated tool execution** — in-context advisory capability token (model may ignore) **plus** fail-closed external execution-layer verification (model cannot bypass); single-use nonce-bound tokens; channel-agnostic.
3. **Residual boundary = semantic authorization** — authentication proves *who signed*, not whether content *carries authority*; a confused deputy with signing access still needs capability-minting separation.

CCC wires this as policy: for high-blast tool surfaces, enforcement must be external and fail-closed; the model's recognition is advisory. Pairs K333 untrusted-model delegation (external broker), K285 Mandato signed mandates, K312 StepGate step gating, K310 pre-auth intent. No attack text / no PoCs. Do not clone InstructionArbitrationBench (no SPDX).

| Wire | Target | Status |
|------|--------|--------|
| External enforcement for high-blast tools | `.cursor/rules/ccc-k325-k327-phase1-wires.mdc` + shared policy §K326 | `policy_wired` |
