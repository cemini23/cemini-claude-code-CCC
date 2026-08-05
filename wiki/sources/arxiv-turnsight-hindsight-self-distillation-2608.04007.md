---
title: "TurnSight — turn-level hindsight self-distillation for tool-integrated RL"
type: source
tags: [source, arxiv, rl, hindsight, tool-integrated-reasoning, k248]
keywords: [2608.04007, TurnSight, quchangle1, cross-horizon, trainer]
related:
  - concepts/turn-level-hindsight-tool-integrated-rl.md
  - entities/tools/turnsight.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- `@concepts/turn-level-hindsight-tool-integrated-rl.md`
- `@entities/tools/turnsight.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TurnSight |
| **arXiv** | 2608.04007 |
| **Repo** | `quchangle1/TurnSight` — GitHub API license null, no LICENSE file in root |
| **Retrieved** | 2026-08-05 |

## Narrative

Turn-level hindsight self-distillation for Tool-Integrated Reasoning. Execution-conditioned hindsight (not GT answers / retrieved skills). Multiple lookahead horizons; select via cross-horizon directional agreement; normalize across sibling rollouts; modulate RL advantages without flipping sign.

| Verdict | **NO-GO** clone/install (no SPDX). Pattern **ADOPT** for turn-level credit in long-horizon tool RL only. Entity `wont_wire`. Trainer stack — do not runtime-wire. |
