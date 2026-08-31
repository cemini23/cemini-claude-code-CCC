---
title: "Recognition Without Enforcement: Configuration-Dependent Failures in LLM Agent Instruction Arbitration (CCC K326)"
type: source
tags: [source, arxiv, security, instruction-arbitration, reference-monitor, enforcement, k326]
keywords: [2608.28502, recognition-enforcement gap, instruction arbitration, external reference monitor, capability gating, HMAC, semantic authorization, InstructionArbitrationBench]
related:
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/mandate-signature-vs-preauth-intent.md
  - concepts/step-level-tool-guardrails.md
  - entities/patterns/external-reference-monitor.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- `@concepts/recognition-vs-enforcement-instruction-arbitration.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/mandate-signature-vs-preauth-intent.md`
- `@concepts/step-level-tool-guardrails.md`
- `@entities/patterns/external-reference-monitor.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Recognition Without Enforcement: Configuration-Dependent Failures in LLM Agent Instruction Arbitration and External Control |
| **arXiv** | 2608.28502 (cs.CR, 2026-08-28) |
| **Authors** | Jun Wen Leong (Independent Researcher) |
| **Code** | Bench forthcoming as InstructionArbitrationBench — **no public SPDX found; do NOT clone** |
| **Retrieved** | 2026-08-31 |

## Narrative

**Verdict: ADOPT policy — model self-arbitration is a capability, not a security boundary.** The paper identifies a **recognition–enforcement gap**: models can *recognize* instruction provenance (source-format features are linearly decodable from activations, and models verbalize forged authority when prompted) yet still *act* on spoofed instructions under specific configurations.

Key findings:

- **Recognition ≠ enforcement.** Source-format markers decode linearly at 97.5–100% (4 open-weight models); in one dissociation, a model detects fabricated authority in 98.7% of trials yet executes in 99.3% under a permissive prompt. Same-instantiation open-weight testing shows 100% verbalized recognition coexisting with 100% execution.
- **Vulnerability is targeted, heterogeneous, unstable.** Fleet study: 46 model endpoints / 6 vendors (authority spoofing), 48 models (memory conflict), 124,325+ memory-conflict trials, >256,000 total. Average execution under diverse novel attacks: **1.21% [0.5–2.1%]** (model-clustered bootstrap over 14,294 analyzed spoofed trials from 29 models — CI 4.5× wider than naive trial-level pooling). Only 4/29 models above 5%. But deterministic 40–100% execution exists in specific prompt–model cells, and per-fingerprint behavior shifts **up to 47pp across deployment windows**.
- **Configuration, not weights.** Restrictive policy + diverse prompts eliminate structured execution on the same weights (recognition persists at 72% Qwen / 36% Llama while execution drops to 0%). Prompt-layer defenses do not generalize across models or adaptive formulations.
- **External reference monitor.** Authenticated source routing (HMAC-SHA256 per-record MACs) + capability-gated tool execution (in-context advisory token + fail-closed external execution-layer verification; single-use nonce-bound tokens). Deterministic by construction under EUF-CMA (not an empirical robustness measure): 0/900 test cases across 3 model families; legitimate throughput 64–100%. Channel-agnostic; 452/452 captured-token replays rejected.
- **Residual boundary: semantic authorization (confused deputy).** Channel authentication proves *who signed* a record, not that its *content carries authority*. A legitimate ingestor signing attacker-controlled content admits the record; whether execution proceeds depends on whether the ingestor can also mint capability tokens. This is the fundamental limit the paper flags — external signing alone cannot solve delegated-authority semantics.
- **Scope caveat:** behavioral evaluations use benign proxy tasks (file deletion, email routing); transfer to genuinely harmful payloads is hypothesized, not demonstrated.

CCC adoption: treat any prompt-layer "safety" claim as a capability claim until an external, fail-closed control exists. Pairs K285 (Mandato signed mandates), K310 (AP2 pre-auth intent), K312 (StepGate step gating). `policy_wired` — no runtime artifact adopted. Cybersec steal. **No attack templates / no prompts / no PoCs in this page or anywhere in the wiki.** The paper releases full verbatim attack prompts in InstructionArbitrationBench — do not clone until SPDX; do not paste.

| Confidence | `[CONFIRMED]` — controlled fleet measurements + formal sketch (EUF-CMA) in paper; not reproduced in CCC |
|------------|------------|

## Snippets

> "We identify a recognition–enforcement gap: source-format features … are linearly decodable from model activations, and models can explicitly identify forged authority when prompted, yet some configurations still produce the conflicting tool call." [Source: arXiv 2608.28502 abstract]

> "Average execution under diverse novel attacks is 1.21% [0.5–2.1%] …, but vulnerability is concentrated in reproducible cells and shifts substantially across deployment windows (up to 47pp within-window per-fingerprint range)." [Source: arXiv 2608.28502 abstract]

> "We therefore treat model self-arbitration as a capability rather than a security boundary and implement an external reference monitor combining authenticated source routing with capability-gated tool execution." [Source: arXiv 2608.28502 abstract]

> "Channel authentication establishes *who signed* a record, not whether its content carries authority. Distinguishing authenticated origin from delegated authority requires semantic authorization, a harder problem that external signing alone cannot solve." [Source: arXiv 2608.28502 §6.5]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.28502-recognition-without-enforcement-configuration-de.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
