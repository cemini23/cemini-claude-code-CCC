---
title: Tool-eval license skepticism patterns — recurring false negatives
type: concept
tags: [concept, tool-eval, license, phase-0, k73]
keywords: [no-license false negative, bsl parsing, additional use grant, phase-0]
related:
  - concepts/skill-vetting.md
  - concepts/tools-we-dont-use.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/andrej-karpathy-skills-multica.md
  - sources/multi-wiki-tool-eval-25url-2026-05-28.md
  - concepts/k73-phase0-audit-decisions.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-25url-2026-05-28.md"
---

## Relations

- `@concepts/skill-vetting.md` — Phase-0 license verification gate
- `@concepts/tools-we-dont-use.md` — policy layer for demotions/rejects
- `@concepts/cross-wiki-tool-eval-inventory.md` — K73 inventory receipt
- `@entities/tools/andrej-karpathy-skills-multica.md` — concrete NO-LICENSE demotion case

Cross-wiki: K73 source on OSINT.

## Raw Concept

K73 25-URL eval repeats two error classes: (1) NO-LICENSE false negatives in doc-level summaries, (2) blanket BSL rejection language without checking Additional Use Grant terms.

## Narrative

### Recurring anti-patterns

| Anti-pattern | Safer action |
|--------------|--------------|
| "No LICENSE" from secondary notes | Verify via `gh api` + inspect repo root files |
| Blanket "BSL is poison" | Read the actual license text + Additional Use Grant |
| Adopt/Steal without source audit | Keep Phase-0 mandatory for every candidate |

### CCC policy

Doc-level evaluations are routing signals, not deploy approvals. Promotion still requires source-level license verification and Phase-0.

## Snippets

> "NO-LICENSE false negatives and blanket BSL rejection language."
> — [Source: briefs/2026-05-28_k73-ccc-tool-eval-license-skepticism.md]
