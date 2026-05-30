---
title: multi-codex — CODEX_HOME env-var isolation pattern
type: concept
tags: []
keywords: []
related:
  - concepts/subagent-orchestration.md
  - concepts/codex-side-fork-workflow.md
  - sources/trading-posts-compilation-k84-2026-05-30.md
maturity: draft
created: 2026-05-15
updated: 2026-05-30
cross-wiki-source: "@osint-wiki/sources/eval-github-repos-2026-05-13.md"
---

# multi-codex — CODEX_HOME env-var isolation pattern

## Relations

- @concepts/subagent-orchestration.md — the multi-agent orchestration cluster this isolation pattern feeds
- @concepts/codex-side-fork-workflow.md — K84 Codex `/side`/`/fork` thread isolation (OpenAI harness)
- @sources/trading-posts-compilation-k84-2026-05-30.md — K84 provenance stub
- @osint-wiki/sources/eval-github-repos-2026-05-13.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

`Spielewoy/multi-codex` runs multiple OpenAI Codex CLI instances side-by-side using a **`CODEX_HOME` environment-variable isolation trick** — each instance is pointed at its own config/state directory, so parallel Codex CLIs coexist without config collision.

Surfaced in the 2026-05-13 14-repo GitHub eval (`@osint-wiki/sources/eval-github-repos-2026-05-13.md`) as **DEFER** (upstream license unverified). The extractable insight is the **isolation pattern itself**: per-instance `CODEX_HOME` (analogous to per-agent home directories) generalises to any agent CLI that keeps state in a fixed home path. Relevant to ccc-wiki's multi-agent orchestration cluster even if the upstream repo's license proves fatal.

`[NEEDS VERIFICATION 2026-05-15]` upstream license.
