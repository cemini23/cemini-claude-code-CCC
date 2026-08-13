---
title: "VAKRA — multi-hop API/retrieval benchmark (IBM)"
type: entity
tags: [entity, tool, benchmark, tool-policy, k275, reference]
keywords: [k275, VAKRA, IBM, multi-hop, tool-use-policy, CC-BY-NC-SA]
related:
  - sources/arxiv-vakra-multi-hop-api-retrieval-2608.12282.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- `@sources/arxiv-vakra-multi-hop-api-retrieval-2608.12282.md`
- `@concepts/multi-hop-api-retrieval-eval-tool-policies.md`

## Raw Concept

Phase-0 entity for CCC k275 — VAKRA benchmark.

## Narrative

Repo `github.com/IBM/VAKRA` — **CC BY-NC-SA 4.0** (LICENSE verified; `gh api` NOASSERTION because CC is non-standard SPDX). **NO-GO clone** for any commercial/`local adopt` shelf; **`wont_wire`** runtime. HF dataset `ibm-research/VAKRA` **WATCH only**. Reference for **eval axes** — API hops, multi-source grounding, NL policy constraints, re-exec verification. Dual-interest with osint-wiki `entities/tools/vakra.md` (same verdict, reference-only) and cybersec K235 benchflow brief.

**Phase-0:** `scripts/adopt_k275_phase0.sh`
