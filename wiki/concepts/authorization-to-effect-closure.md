---
title: "Authorization-to-effect closure — revalidate at commit, one reservation, one successor"
type: concept
tags: [concept, security, authorization, mcp, effects, commit-semantics, k302]
keywords: [aid-guard, authorization-to-effect, delivery fence, reservation lineage, duplicate effect, 2608.21159]
related:
  - sources/arxiv-aid-guard-stateful-authorization-2608.21159.md
  - entities/tools/aid-guard.md
  - entities/skills/aid-guard-commit.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
  - concepts/tool-argument-privacy-minimization.md
maturity: draft
created: 2026-08-25
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-aid-guard-stateful-authorization-2608.21159.md`
- `@entities/tools/aid-guard.md`
- `@entities/skills/aid-guard-commit.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Question answered: how do you guarantee one approval ⇒ at most one provider effect across retry, ambiguity, and recovery? Source: arXiv 2608.21159 (CCC K302). Pairs K239 execution fidelity + K285 signed mandates.

## Narrative

Admission-time authorization is not effect-time authority. Between approval and commit, three things go wrong: the request mutates, the response is lost after the effect landed, or recovery logic replays a "new" action from an old approval. Closure protocol:

1. **Commit-time revalidation** — exact approved request *and* current provider state checked at the moment of effect.
2. **Single reservation under ambiguity** — unknown outcome ⇒ keep exactly one reservation alive; never issue a replacement while ambiguous.
3. **Certified release** — release or at most **one successor** only after terminal result or certified no-effect, fenced against late-arriving predecessor effects through the declared recovery horizon.

Evidence (paper): 13 live mutations zero unauthorized effects; 210/210 Stripe contract trials matched predeclared outcomes; zero duplicates across 40 successor schedules, 30 confirm/cancel races, 10 crash recoveries; 44/44 compromise attacks blocked vs 44/44 legitimate admitted. Cost: strict exact-manifest profile costs 35.4–43.8 pp benign utility — closure strength is a dial, not free.

CCC policy: any wired mutation path (MCP write tools, prod scripts) should carry request-hash revalidation at commit; on ambiguous outcomes hold state rather than retrying blind.

## Snippets

> "one reservation therefore yields at most one effect across retry and recovery" [Source: arXiv 2608.21159 abstract]
