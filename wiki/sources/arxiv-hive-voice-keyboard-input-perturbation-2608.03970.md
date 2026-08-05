---
title: "HIVE — voice vs keyboard input perturbation for LLMs"
type: source
tags: [source, arxiv, voice, keyboard, input, robustness, k247]
keywords: [2608.03970, HIVE, transcription, QWERTY, constructive-tasks]
related:
  - concepts/voice-vs-keyboard-agent-input-robustness.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- `@concepts/voice-vs-keyboard-agent-input-robustness.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | HIVE |
| **arXiv** | 2608.03970 |
| **Repo** | None found (Phase-0) |
| **Retrieved** | 2026-08-05 |

## Narrative

HIVE: voice transcription perturbations + QWERTY keyboard perturbations.

**Seven findings:**

(i) Voice transcription lowers accuracy on every instruction-tuned model tested; **structure** of transcription not fillers carries the cost.

(ii) QWERTY costs less; models absorb many typos before accuracy falls.

(iii) Shared cause: how many question tokens **survive**; destroying a token hurts, adding tokens costs little.

(iv) Channel gap only where answer must be constructed/deduced; none on multiple choice.

(v) Harm is not solely test-set contamination.

(vi) Cannot be trained away with lightweight adaptation.

(vii) Thinking budget recovers keyboard almost entirely but leaves spoken registers untouched; compressed speech is worse with it.

| Verdict | **ADOPT** prefer typed input for constructive agent tasks; expect voice/dictation accuracy drop; thinking budget ≠ voice fix. **NO-GO** install. Concept-only. |
