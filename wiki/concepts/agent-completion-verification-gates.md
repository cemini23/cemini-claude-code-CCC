---
title: Agent completion verification gates — stop babysitting agent runs
type: concept
tags: [concept, claude-code, verification, harness, k72]
keywords: [ericosiu, completion-proof, verification-gate, agent-babysitting, done-criteria]
related:
  - concepts/claude-premortem-skill.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/openspec.md
  - concepts/subagent-orchestration.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/continual-harness-online-self-improvement.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@concepts/claude-premortem-skill.md` — pre-ship review; this page is **runtime completion** proof
- `@entities/patterns/full-prompt-goal-template.md` — explicit done criteria in `/goal` envelopes
- `@entities/tools/openspec.md` — acceptance criteria before merge
- `@concepts/subagent-orchestration.md` — parent must verify subagent return, not assume success

Cross-wiki: K72 Post 0 (@ericosiu).

## Raw Concept

K72 — **agent completion proof**: operators should not babysit every tool call; harness must expose verifiable **done** signals (tests green, lint clean, artifact exists) before the session claims completion.

## Narrative

### Pattern [TENTATIVE]

| Gate | Example |
|------|---------|
| Objective test | `pytest`, `wiki_lint.py`, build |
| Artifact check | file path + hash in response |
| Human checkpoint | only for irreversible prod writes |

### CCC fit

Pair with `@concepts/claude-premortem-skill.md` (what could fail) and `@entities/patterns/full-prompt-goal-template.md` (what done looks like).

| Verdict | **REFERENCE (adopt in rules/skills)** |

## Snippets

> "Agent completion proof / stop babysitting."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 0]
