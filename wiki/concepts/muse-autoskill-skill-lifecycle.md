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
maturity: draft
created: 2026-06-01
updated: 2026-06-02
---

## Relations

- `@sources/arxiv-muse-autoskill-2605.27366.md` — arXiv 2605.27366
- `@concepts/skillrae-retrieval-augmented-execution.md` — RAE compiles skills; MUSE evolves them
- `@concepts/skill-vetting.md` — Phase-0 before any skill enters lifecycle
- `@concepts/continual-harness-online-self-improvement.md` — harness refiner peer

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

**Verdict:** **REFERENCE** — steal **unit-test skills before promotion** pattern; no MUSE framework install without Phase-0.

## Snippets

> "Evaluation through unit tests and runtime feedback for continuous refinement."
> — [Source: arxiv-2605.27366-muse-autoskill-self-evolving-agents-via-skill-cr.pdf]
