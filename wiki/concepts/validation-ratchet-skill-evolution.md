---
title: "Validation ratchet — keep skill updates only when validation improves (CCC K324)"
type: concept
tags: [concept, skill-evolution, validation, harness, ratchet, k324]
keywords: [RedEvoAgent, validation ratchet, skill update, Deciding-Tool Attribution, tool-effectiveness, 2608.27439]
related:
  - sources/arxiv-redevoagent-redteam-skill-evo-2608.27439.md
  - concepts/stratified-harness-evolution.md
  - concepts/process-constrained-self-evolution.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-redevoagent-redteam-skill-evo-2608.27439.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/process-constrained-self-evolution.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

The question: when a skill evolves from accumulated experience, how do we stop misleading experiences from degrading it? Answer from RedEvoAgent [Source: wiki/sources/arxiv-redevoagent-redteam-skill-evo-2608.27439.md]: a **validation ratchet** — a patch is retained only if it improves validation performance.

## Narrative

RedEvoAgent is a red-teaming agent (Cybersec-primary — CCC ingests only the mechanism, not the attack skills). It distills cross-case attack trajectories into a concise, human-readable skill, and evolves it with two safeguards:

1. **Tool-effectiveness profiling + Deciding-Tool Attribution** — only the tool that actually drove the outcome gets credit for a skill update (fixes unclear tool credit / retrieval bias).
2. **Validation ratchet** — an update is retained **only if validation performance improves**; otherwise it is rejected, keeping the skill from degrading on misleading experiences.

CCC steal (defensive, ADOPT):

- Any **skill-memory patch** — whether from experience distillation, EM–WM coupling (`@concepts/experiential-working-memory-coupling.md`), or trajectory analysis — must clear a validation gate before admission.
- Never auto-evolve `.cursor/skills`; the ratchet is the standing gate (pairs K237/K298/K307/K313/K314 validation-gated updates).

This is the same monotonic-improvement discipline as `@concepts/stratified-harness-evolution.md` (accept few, measured changes) and `@concepts/process-constrained-self-evolution.md`.

| Confidence | `[CONFIRMED]` — ratchet mechanism described in paper; the gate itself is already CCC practice (K313/K314) |
|------------|------------|

## Snippets

> "A validation ratchet that retains only updates improving validation performance." [Source: arXiv 2608.27439 abstract]

> "Such retrieval can reuse misleading experiences due to retrieval bias and unclear tool credit." [Source: arXiv 2608.27439 abstract]
