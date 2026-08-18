---
title: "Signed-mandate MCP proxy pattern (K285)"
type: entity
tags: [entity, pattern, mcp, authorization, governance, signed-mandate, k285]
keywords: [k285, Mandato, signed-mandate, MCP proxy, PDP-PEP, deny-by-default, monotone-attenuation, hash-chained-audit]
related:
  - sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - entities/tools/mandato.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@entities/tools/mandato.md`

## Raw Concept

Reusable pattern extracted from K285 Mandato — signed-authority enforcement at a protocol proxy.

## Narrative

The transferable pattern: (1) **signed authority artifact** (tool scope + parameter constraints + TTL + principal binding, non-Turing-complete constraint language); (2) **non-bypassable proxy enforcement** (terminate both sides; upstream mTLS identity); (3) **separated PDP/PEP** with fail-closed enforcement; (4) **deny-by-default** decision semantics; (5) **monotone attenuation** for delegation; (6) **append-only hash-chained audit** with external anchoring + selective hash commitments. **`policy_wired`** — Atto-priority (extract-solver tool authorization).

**Phase-0:** `scripts/adopt_k285_phase0.sh`
