---
title: DeepScientist (ResearAI) — autonomous research agent
type: entity
tags: [tool, steal-from, k103, research]
keywords: [deep-scientist, researai, hypothesis-loop, ingest]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - entities/tools/autoresearch-claw.md
  - concepts/federated-daily-research-digest.md
  - concepts/monokern-compounding-research-pipeline.md
  - "@osint-wiki/entities/tools/deep-scientist.md"
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/xcientist.md
  - concepts/externalized-research-synthesis-validation.md
  - concepts/claim-drift-automated-research.md
maturity: draft
created: 2026-06-07
updated: 2026-06-22
license_verified: Apache-2.0
---

## Relations

- `@sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md` — Steal-from
- `@entities/tools/autoresearch-claw.md` — sibling research-claw pattern
- `@concepts/federated-daily-research-digest.md` — do not duplicate Tier-3 auto-ingest
- `@osint-wiki/entities/tools/deep-scientist.md` — canonical audit

## Raw Concept

- **URL:** https://github.com/ResearAI/DeepScientist
- **Tier:** Steal-from (CCC-wiki)
- **License:** Apache-2.0 [CONFIRMED 2026-06-07]

## Narrative

Autonomous multi-step research agent — steal **hypothesis loop + citation discipline** for CCC ingest pipeline (discuss takeaways → 3–15 wiki touches → `wiki_lint.py`). No full adopt: overlaps `@concepts/federated-daily-research-digest.md` + Exa-gated OOD workflow.

**Compare K122:** `@entities/tools/xcientist.md` adds **process accountability** (validation contracts, claim-drift taxonomy) beyond hypothesis loop alone.

**Steal targets:** explicit hypothesis → evidence → synthesis steps; refusal to cite without retrieval.

## Snippets

> "Steal hypothesis loop for ingest — no full adopt (overlaps daily digest + Exa gated workflow)." [Source: briefs/2026-06-07_k103-ccc-agent-harness-from-osint.md]
