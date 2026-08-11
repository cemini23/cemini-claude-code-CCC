---
title: K269 — Taboo decoding-time diagnostic (2608.09900)
type: brief
target: claude.ai
created: 2026-08-11
---

## Target

claude.ai · Claude Desktop · hands-on (scoped eval). Wiki: `@concepts/decoding-level-taboo-diagnostic.md` + `@sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md`.

## Summary

**Taboo** = zero-prompt, runtime **logit-space** diagnostic that quantifies whether an LLM's multi-step reasoning survives being forced off its preferred decoding path. At each word-initial decoding step it masks the top-`i` candidate logits to `−∞` (machine circumlocution); mid-word subwords are never masked (isolates semantic stress from tokenization corruption). REFERENCE (Zenodo CC-BY-4.0 `taboo-decoder.zip`, ~234KB) — not a jailbreak, not an attack. Wire **K269** → lab-redteam + agent-audit.

## Body

### The primitive

- Mask top-`i` logits at **word boundaries only** (`W=1`); re-select greedy. Mid-word masking corrupts tokenization (accuracy → 0.01–0.05), so Taboo isolates *semantic* off-path robustness.
- Dose = **Injected Surprisal** `∆S` (bits); normalized `∆S̄` across architectures/tokenizers. Implemented as a `TabooLogitsProcessor` (HF transformers); generations lengthen ~1.4× at i=1.

### What results mean

- **Robustness is learned, not given** — instruct checkpoints retain far more baseline-correct items than base, but only on multi-step generative reasoning, and only in some families.
- **Scale compounds alignment** — Qwen2.5-32B-instruct retains 93% at i=1; base collapses. Largest base ≠ most robust (72B-base < 32B-base on GSM8K).
- **Family recipes differ mechanistically** — Llama-3.1-8B shows no base/instruct gap (instruct doesn't sharpen its distribution); the gain reappears at 70B without distribution sharpening.
- **Formal syntax is a hard bound** — HumanEval → ~0 (reserved keywords have no synonyms). Use as the "do not overclaim off-path capability" control.

### Lab use cases (K269)

1. **Refusal-surface audit** — mask top refusal tokens on an adversarial prompt; immediate policy-violating output ⇒ alignment is a shallow top-token preference, not latent safety.
2. **Pre-deployment reliability check** — run across the prompt/system/JSON constraints a lane actually uses; derailment (repetition loops, no-termination, confident-wrong) under dose ⇒ fragile in production.
3. **Synthetic CoT diversity** — Taboo sampling yields diverse, logically coherent off-path trajectories for distillation / verifier-RL.
4. **Structured-output stress** — mask preferred top tokens inside a JSON/function-call schema to test genuine schema understanding vs memorized templates.

### Caveats

- **Diagnostic/eval primitive, not a fix.** It reveals fragility; taboo-guided alignment is the fix direction, not the mask itself.
- **Not** a generic "safety benchmark" for pass/fail release gates — require negative controls (HumanEval floor, MCQ-floor MMLU).
- 4-bit quantization matches bf16 within sampling variance (median |Δacc| 0.03).

### Ref / wire

- Concept: `decoding-level-taboo-diagnostic.md` · Source: `arxiv-2608-09900-taboo-decoding-level-diagnostic.md` · Wire: `cemini-cybersec-lab-redteam.mdc` + `cemini-cybersec-agent-audit.mdc` (K269).

## Sources

- arXiv:2608.09900 (19 pp) + Zenodo `taboo-decoder.zip` (CC-BY-4.0) — `wiki/sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md`
