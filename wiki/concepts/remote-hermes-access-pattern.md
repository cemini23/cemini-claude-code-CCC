---
title: Remote Hermes access — hosted agent gateway pattern
type: concept
tags: [concept, hermes, remote, gateway, k90]
keywords: [tonbistudio, remote-hermes, messaging-gateway, reference-only]
related:
  - entities/tools/hermes-agent.md
  - entities/tools/hermes-desktop.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - entities/tools/conductor-mcp.md
  - sources/trading-posts-compilation-16-2026-05-31.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md"
---

## Relations

- `@entities/tools/hermes-agent.md` — runtime reference (NO-GO prod)
- `@entities/tools/hermes-desktop.md` — desktop shell (K90 CONDITIONAL-GO)
- `@entities/tools/conductor-mcp.md` — prod orchestration peer
- `@sources/trading-posts-compilation-16-2026-05-31.md` — K90 Post 11 (@tonbistudio)

## Raw Concept

K90 Post 11 (@tonbistudio): **remote Hermes** access — operate a hosted Hermes instance from phone/messaging surfaces **`[TENTATIVE]`**.

## Narrative

**CCC posture:** messaging-gateway + 24/7 agent = `@concepts/agent-token-discipline-openclaw-hermes.md` anti-pattern for prod. Steal **remote monitoring UX** ideas only; prod stays conductor + Claude Code with explicit session boundaries.

**Verdict:** **REFERENCE** — do not wire prod credentials into remote Hermes gateways.

## Snippets

> Remote Hermes access (@tonbistudio) — reference gateway pattern, not prod adopt.
> — [Source: briefs/2026-05-31_k90-ccc-agent-harness-from-osint.md, Post 11]
