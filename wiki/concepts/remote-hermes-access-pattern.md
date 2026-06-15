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
  - "@osint-wiki/concepts/hermes-laptop-operator-playbook.md"
maturity: draft
created: 2026-05-31
updated: 2026-06-13
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

**CCC posture:** messaging-gateway + 24/7 agent = `@concepts/agent-token-discipline-openclaw-hermes.md` anti-pattern for **prod trading**. **Operator path:** pattern **implemented** on `cemini-librarian` (Telegram inbound + cron alerts) `[CONFIRMED 2026-06-13]`. Prod stays conductor + Claude Code; Hermes gets operator-only secrets (no `/opt/cemini` write).

**Verdict:** **ADOPTED (operator)** — reference K90 Post 11; canon deployment in `@osint-wiki/concepts/hermes-laptop-operator-playbook.md`.

## Snippets

> Remote Hermes access (@tonbistudio) — reference gateway pattern, not prod adopt.
> — [Source: briefs/2026-05-31_k90-ccc-agent-harness-from-osint.md, Post 11]
