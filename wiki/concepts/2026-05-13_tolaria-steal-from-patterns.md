---
title: tolaria — refactoring-workflow patterns (STEAL-FROM, AGPL-3.0)
type: concept
tags: []
keywords: []
related:
  - entities/tools/openspec.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-github-repos-2026-05-13.md"
---

# tolaria — refactoring-workflow patterns (STEAL-FROM, AGPL-3.0)

## Relations

- @entities/tools/openspec.md — spec-driven-workflow neighbour; tolaria's incremental-migration patterns sit in the same workflow-tool field
- @osint-wiki/sources/eval-github-repos-2026-05-13.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

`refactoringhq/tolaria` is an **AGPL-3.0** refactoring tool. Surfaced in the 2026-05-13 14-repo GitHub eval (`@osint-wiki/sources/eval-github-repos-2026-05-13.md`) as **STEAL-FROM**.

AGPL-3.0 is a poison-pill for Cemini's distribution surface — the upstream-dependency path is closed; only **patterns** are extractable. The interesting patterns are tolaria's approach to **incremental migrations** and its refactoring-workflow design language. Cross-routed to ccc-wiki for the workflow-pattern angle.

Constraint: code must **not** be vendored; patterns may be reimplemented clean-room. See `@osint-wiki/concepts/cemini-license-posture.md` for the AGPL house policy.
