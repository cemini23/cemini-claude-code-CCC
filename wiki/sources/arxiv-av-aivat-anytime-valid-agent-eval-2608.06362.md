---
title: "AV-AIVAT — anytime-valid cheap agent evaluation in IIGs"
type: source
tags: [source, arxiv, poker, evaluation, anytime-valid, k257]
keywords: [2608.06362, AV-AIVAT, AIVAT, PokerSkill, HUNL, confidence-sequence]
related:
  - concepts/anytime-valid-agent-eval-stopping.md
  - entities/tools/av-aivat.md
  - concepts/acem-agentic-cost-estimation.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
maturity: draft
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@concepts/anytime-valid-agent-eval-stopping.md`
- `@entities/tools/av-aivat.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AV-AIVAT: 74× Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games |
| **arXiv** | 2608.06362 |
| **Authors** | Boning Li, Yu Chen, Longbo Huang (Tsinghua IIIS) |
| **Repo** | None found at Phase-0 |
| **Retrieved** | 2026-08-07 |

## Narrative

Combines AIVAT variance reduction with confidence sequences for optional stopping that preserves coverage. HUNL corpus 71,439 paired hands / 15 PokerSkill configs: AIVAT median 54× variance cut; AsympCS median raw-to-AIVAT stopping-time ratio **74×** at ±1 BB, α=0.05. EB-CS needs independent payoff bound (proven for Leduc). Online value model learns only from past games. Poker-primary steal.

| Verdict | **ADOPT** anytime-valid stopping for costly agent evals. **NO-GO** install (no public artifact). Poker Arena brief. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/<basename>` (archived 2026-08-07; local `raw-sources/` copy retained).
