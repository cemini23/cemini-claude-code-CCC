---
title: Agent rubrics — self-evaluation and correction loops (K97)
type: concept
tags: [concept, eval, rubrics, harness, k97]
keywords: [sydneyrunkle, rubrics, self-correction, agent-eval, deepeval]
related:
  - concepts/agent-completion-verification-gates.md
  - concepts/skill-vetting.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/self-healing-agent-sessions.md
  - concepts/worldmemarena-multimodal-agent-memory-eval.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-17-2026-06-03.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md"
---

## Relations

- `@concepts/agent-completion-verification-gates.md` — explicit done criteria before merge
- `@concepts/skill-vetting.md` — rubric rows for skill/MCP Phase-0
- `@entities/patterns/full-prompt-goal-template.md` — success criteria in `/goal` envelopes
- `@concepts/self-healing-agent-sessions.md` — bounded retry vs infinite rubric loops
- `@concepts/worldmemarena-multimodal-agent-memory-eval.md` — eval rubric steal-from (memory MCP)
- `@entities/tools/claude-code.md` — Stop hook + subagent reviewer pattern
- `@sources/trading-posts-compilation-17-2026-06-03.md` — K97 Post 6 (@sydneyrunkle)

## Raw Concept

K97 Post 6 (@sydneyrunkle): **Rubrics** — structured criteria agents use to **self-evaluate and self-correct** before declaring work complete. CCC maps to existing verification gates, not a new eval SaaS install.

## Narrative

### Rubric shape for harness work

| Dimension | Example criterion |
|-----------|-------------------|
| Correctness | Tests pass; linter clean; wiki_lint 0 bidirectional gaps |
| Scope | Diff matches `/goal` acceptance bullets only |
| Provenance | Claims tagged `[CONFIRMED]` / `[TENTATIVE]` / `[NEEDS VERIFICATION]` |
| Safety | No secrets committed; no `--force` git without explicit ask |
| Cost | Subagent used for wide reads; cache-friendly static prompts |

### Integration points [TENTATIVE]

1. **`/goal` template** — section 1 is the rubric (what "done" looks like).
2. **Stop hook** — re-check rubric before session end (`@concepts/hooks-for-automation.md`).
3. **Reviewer subagent** — `code-reviewer` or `@entities/skills/` audit pass on large diffs.
4. **Phase-0 audits** — rubric rows in `@concepts/skill-vetting.md` for MCP/skill adopt.

**Verdict:** **REFERENCE** — steal eval harness ideas; compare to `@entities/tools/deepeval` brief (K55, deferred) before adding eval framework deps.

## Snippets

> Rubrics — agents self-evaluate and self-correct. [TENTATIVE — @sydneyrunkle, Posts.docx K97 Post 6]
