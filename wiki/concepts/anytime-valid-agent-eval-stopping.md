---
title: Anytime-valid agent evaluation stopping (AV-AIVAT) (K257)
type: concept
tags: [concept, evaluation, poker, anytime-valid, cost, k257]
keywords: [2608.06362, AV-AIVAT, AIVAT, confidence-sequence, HUNL]
related:
  - sources/arxiv-av-aivat-anytime-valid-agent-eval-2608.06362.md
  - entities/tools/av-aivat.md
  - concepts/acem-agentic-cost-estimation.md
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
  - briefs/2026-08-07_phase1-wire-status-closeout-k254-k258.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-07
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-av-aivat-anytime-valid-agent-eval-2608.06362.md`
- `@entities/tools/av-aivat.md`
- `@concepts/acem-agentic-cost-estimation.md`

## Raw Concept

How do we stop costly agent-vs-agent evaluations as soon as evidence suffices without invalidating coverage via peeking?

## Narrative

K257 AV-AIVAT (arXiv **2608.06362**): AIVAT variance reduction + continuously monitored confidence sequences. Online value model must not peek at the current game. Naive fixed-CI optional stopping inflates false positives. Poker HUNL: median **74×** fewer hands to stop under AsympCS with AIVAT vs raw at ±1 BB.

### Cemini steal (ADOPT)

1. Poker Arena / HU Researcher: prefer variance-reduced + anytime-valid stopping over fixed hand budgets when comparing LLM agents.
2. Do not “stop when CI looks good” with an ordinary interval — use CS / declared procedure.
3. Release paired logs + stop metadata so third parties can recheck early-stop claims.
4. ACEM cost framing (K243): early stop = infrastructure+LLM savings with stated error control.

| Verdict | **ADOPT** eval discipline for poker/IIG agents. **NO-GO** code. Poker-primary brief. |
