---
title: typst — markup PDF compiler
type: entity
tags: [tool, document-generation, k102, phase-0]
keywords: [typst, pdf, briefs, apache-2.0, brew]
related:
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/cross-wiki-tool-adoption-routing.md
  - "@osint-wiki/entities/tools/typst.md"
  - entities/tools/revfactory-harness.md
  - concepts/cross-wiki-tool-adoption-routing.md
maturity: draft
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- `@sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md` — K102 provenance
- `@osint-wiki/entities/tools/typst.md` — OSINT canon (Phase-0 validated)

## Raw Concept

K102 **CONDITIONAL-GO** — `typst/typst` PDF compiler for optional `briefs/` → stakeholder PDF export. **Apache-2.0** [CONFIRMED via OSINT Phase-0]. Not on prod trading path.

## Narrative

| Check | Verdict |
|-------|---------|
| License | **Apache-2.0** |
| CCC use | Laptop-only brief/wiki PDF pipeline |
| Install | `brew install typst` (see `scripts/adopt_k102_phase0.sh`) |
| vs LaTeX | Faster incremental compile — optional deliverable path |

**Verdict:** **CONDITIONAL-GO** — install binary on laptop; wire `scripts/compile_brief_pdf.sh` later if needed.

## Snippets

> "Fast LaTeX alternative for compiling briefs/ and wiki exports to stakeholder PDFs."
> — [Source: @osint-wiki/entities/tools/typst.md]
