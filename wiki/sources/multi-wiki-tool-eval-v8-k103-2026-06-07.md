---
title: Tool Evaluation and Wiki Fit — 63-URL batch (K103)
type: source
tags: [source, tool-eval, k103, multi-wiki]
keywords: [k103, 63-url, asm, pydantic-ai, application-skills]
related:
  - entities/tools/agent-skill-manager.md
  - entities/tools/pydantic-ai.md
  - entities/tools/deep-scientist.md
  - entities/tools/autoresearch-claw.md
  - entities/tools/application-skills.md
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md"
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/federated-daily-research-digest.md
  - concepts/skill-vetting.md
  - concepts/tools-we-dont-use.md
maturity: draft
read_status: skimmed
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- `@entities/tools/agent-skill-manager.md` — Adopt CONDITIONAL-GO
- `@entities/tools/pydantic-ai.md` — Adopt GO (core MIT only)
- `@entities/tools/deep-scientist.md` — Steal-from
- `@entities/tools/autoresearch-claw.md` — Steal-from
- `@entities/tools/application-skills.md` — Eval Adopt overturned → NO-GO
- `@sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md` — prior batch
- `@concepts/cross-wiki-tool-eval-inventory.md` — receipt row
- `@osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md` — OSINT canon (deep-read + Phase-0)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation Report — *Tool Evaluation and Wiki Fit* |
| **Type** | Internal .docx eval (63 URLs) |
| **sha256** | `6ebbacb83f2980fe042c464d7c029ae86b4d6817a33798e6fb118f71d7331d4a` |
| **Retrieved** | 2026-06-07 |
| **Read status** | skimmed (CCC slice — asm, pydantic-ai, steal-froms, NO-GO overturn) |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation and Wiki Fit.docx` |
| **CCC brief** | `briefs/2026-06-07_k103-ccc-agent-harness-from-osint.md` |

## Narrative

K103 sixty-three-URL eval. **CCC-routed slice:** `luongnv89/asm` (CONDITIONAL-GO), `pydantic/pydantic-ai` (GO — never `pydantic-ai-gateway` AGPL), ResearAI/DeepScientist + aiming-lab/AutoResearchClaw (steal-from), `membranedev/application-skills` demoted **NO-GO** (null repo license + Membrane lock-in). Polymarket/gambling URLs routed to OSINT/gambling wikis.

**Phase-0:** OSINT `scripts/adopt_k103_phase0.sh`; CCC mirror `scripts/adopt_k103_phase0.sh` (laptop pydantic + asm checks only).

## Snippets

> "pydantic-ai-gateway is AGPL-3.0; core pydantic-ai is MIT" — adopt core only. [Source: K103 license spot-check; @osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md]

> "application-skills demoted NO-GO — null repo license + Membrane lock-in." [Source: K103 Phase-0; @osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md]
