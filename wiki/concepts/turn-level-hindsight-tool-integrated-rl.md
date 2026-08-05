---
title: Turn-level hindsight for tool-integrated RL (K248)
type: concept
tags: [concept, rl, hindsight, tool-integrated-reasoning, k248]
keywords: [2608.04007, TurnSight, cross-horizon, execution-conditioned, trainer]
related:
  - sources/arxiv-turnsight-hindsight-self-distillation-2608.04007.md
  - entities/tools/turnsight.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- `@sources/arxiv-turnsight-hindsight-self-distillation-2608.04007.md` — K248 provenance
- `@entities/tools/turnsight.md` — NO-GO entity (no SPDX)

## Raw Concept

How should long-horizon tool-integrated RL assign credit at turn granularity using execution-conditioned hindsight?

## Narrative

K248 TurnSight (arXiv **2608.04007**): turn-level hindsight self-distillation for Tool-Integrated Reasoning.

**Mechanism:**

- Execution-conditioned hindsight — not GT answers or retrieved skills
- Multiple lookahead horizons; select via cross-horizon directional agreement
- Normalize across sibling rollouts
- Modulate RL advantages without flipping sign

Repo `quchangle1/TurnSight`: GitHub API license null, no LICENSE in root → **NO-GO** clone/install.

### Cemini steal (ADOPT pattern only)

Turn-level credit assignment for long-horizon tool RL — reference for trainer-stack design, not Cursor harness wiring.

| Verdict | **ADOPT** pattern for turn-level tool RL credit. **NO-GO** install. Trainer stack `wont_wire`. |
