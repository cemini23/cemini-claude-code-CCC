---
title: Voice vs keyboard agent input robustness (K247)
type: concept
tags: [concept, voice, keyboard, input, robustness, k247]
keywords: [2608.03970, HIVE, transcription, QWERTY, constructive-tasks, thinking-budget]
related:
  - sources/arxiv-health-trust-search-agents-cui-2608.21177.md
  - sources/arxiv-hive-voice-keyboard-input-perturbation-2608.03970.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-hive-voice-keyboard-input-perturbation-2608.03970.md` — K247 provenance
- `@sources/arxiv-health-trust-search-agents-cui-2608.21177.md`

## Raw Concept

How do voice transcription and keyboard typos affect instruction-tuned models on constructive vs recognition tasks?

## Narrative

K247 HIVE (arXiv **2608.03970**): voice transcription perturbations + QWERTY keyboard perturbations. No public code.

### Seven findings (canonical)

(i) Voice transcription lowers accuracy on every instruction-tuned model tested; **structure** of transcription not fillers carries the cost.

(ii) QWERTY costs less; models absorb many typos before accuracy falls.

(iii) Shared cause: how many question tokens **survive**; destroying a token hurts, adding tokens costs little.

(iv) Channel gap only where answer must be constructed/deduced; none on multiple choice.

(v) Harm is not solely test-set contamination.

(vi) Cannot be trained away with lightweight adaptation.

(vii) Thinking budget recovers keyboard almost entirely but leaves spoken registers untouched; compressed speech is worse with it.

### Cemini policy (ADOPT)

- Prefer **typed input** for constructive agent tasks (code, plans, multi-step reasoning)
- Expect accuracy drop on voice/dictation — not fixable by thinking budget alone
- MCQ-style routing less affected; do not generalize voice harm from recognition tasks

| Verdict | **ADOPT** input-channel policy. **NO-GO** install. Concept-only. |
