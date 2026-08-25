---
title: "Mandato — signed-mandate MCP governance proxy (Hyperlabs)"
type: entity
tags: [entity, tool, mcp, authorization, governance, audit, policy-only, k285]
keywords: [k285, Mandato, signed-mandate, MCP proxy, hash-chained audit, PDP-PEP, EU AI Act]
related:
  - entities/tools/aid-guard.md
  - sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - entities/patterns/signed-mandate-mcp-proxy.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
created: 2026-08-18
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@entities/patterns/signed-mandate-mcp-proxy.md`
- `@entities/tools/aid-guard.md`

## Raw Concept

Phase-0 entity for CCC K285 — Mandato (signed-mandate MCP governance proxy).

## Narrative

Author: Giovanni Racioppi (Hyperlabs, Italy). A governance proxy that enforces **digitally signed mandates** on MCP agent actions at the protocol level, with an append-only **hash-chained audit log**. No public repository / SPDX license → **policy only** (no clone). Specification-driven (spec v0.6: 170+ requirements, 22 use cases, milestones M0–M8.5); empirical results are a falsifiable evaluation plan, not reported numbers.

Steal: reify authorization as a signed, machine-readable artifact (scope over tools/parameters/conditions, bounded validity, chained delegation with monotone attenuation, revocation/ratification), enforce at a non-bypassable MCP proxy with separated PDP/PEP, and record every permit/deny into an externally-anchored hash chain for evidentiary use. **`policy_wired`** — no runtime wiring (no code to run).

**Phase-0:** `scripts/adopt_k285_phase0.sh`
