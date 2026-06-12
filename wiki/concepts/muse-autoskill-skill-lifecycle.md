---
title: MUSE-Autoskill — unified skill creation and evaluation lifecycle
type: concept
tags: [concept, agent-skills, self-evolving, arxiv]
keywords: [2605.27366, muse, skill-lifecycle, unit-tests, skill-refinement]
related:
  - sources/arxiv-muse-autoskill-2605.27366.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/skill-vetting.md
  - concepts/continual-harness-online-self-improvement.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/claude-code-skills-md-institutional-memory.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - "@osint-wiki/concepts/curator-skills.md"
  - concepts/agent-skills-taxonomy.md
  - concepts/agent-skills-progressive-disclosure.md
  - sources/arxiv-agent-skills-architecture-security-2602.12430.md
  - concepts/skilladaptor-step-level-skill-adaptation.md
  - sources/arxiv-skilladaptor-2606.01311.md
  - concepts/time-series-native-agent-harness.md
  - sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md
  - concepts/bayesian-posterior-guided-skill-evolution.md
  - sources/arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md
  - concepts/skillhone-continual-skill-decision-history.md
  - sources/arxiv-skillhone-continual-skill-evolution-2606.08671.md
maturity: draft
created: 2026-06-01
updated: 2026-06-12
---

## Relations

- `@sources/arxiv-muse-autoskill-2605.27366.md` — arXiv 2605.27366
- `@concepts/skillrae-retrieval-augmented-execution.md` — RAE compiles skills; MUSE evolves them
- `@concepts/skill-vetting.md` — Phase-0 before any skill enters lifecycle
- `@concepts/continual-harness-online-self-improvement.md` — harness refiner peer
- `@concepts/agent-skills-progressive-disclosure.md` — 2602.12430 three-level loading
- `@concepts/skilladaptor-step-level-skill-adaptation.md` — 2606.01311 step-level failure→skill edit peer

## Raw Concept

arXiv **2605.27366** — **MUSE** skill lifecycle: create → store → manage → evaluate (unit tests + runtime feedback) → refine. Opposes treating skills as static drop-in files.

## Narrative

| MUSE phase | CCC analogue |
|------------|--------------|
| Creation | skill-creator / `/goal` briefs → `~/.claude/skills/` |
| Memory | claude-mem + wiki concept pages |
| Management | `@entities/tools/skillkit.md`, lazy-tool, index.md catalog |
| Evaluation | Phase-0 audit + real session smoke test |
| Refinement | ingest passes bump `updated:` + `maturity:` |

**Verdict:** **REFERENCE** — steal **unit-test skills before promotion** pattern; pairs with `@concepts/agent-skills-progressive-disclosure.md` Level-1/2 split; no MUSE framework install without Phase-0.

**Peer (2026-06-06):** `@concepts/skilladaptor-step-level-skill-adaptation.md` (2606.01311) adds **step-level attribution** before refinement — MUSE's evaluation phase answers "is this skill good?"; SkillAdaptor answers "which procedure line caused this failure?"

**Peer (K111):** `@concepts/skillhone-continual-skill-decision-history.md` (2606.08671) adds **persistent decision history** across sessions — MUSE evaluates/refines; SkillHone records diagnosis→revision→evidence→outcome so later sessions do not repeat or regress fixes.

## Snippets

> "Evaluation through unit tests and runtime feedback for continuous refinement."
> — [Source: arxiv-2605.27366-muse-autoskill-self-evolving-agents-via-skill-cr.pdf]
