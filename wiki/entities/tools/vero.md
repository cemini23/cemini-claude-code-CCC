---
title: "Vero — repo-level verified code+proof synthesis benchmark (UC Berkeley)"
type: entity
tags: [entity, tool, benchmark, formal-verification, lean, apache-2.0, k280, reference]
keywords: [k280, Vero, Lean4, code-and-proof, unsat-audit, sunblaze-ucb, apache-2.0, repository-scale]
related:
  - sources/arxiv-vero-repo-verified-code-proof-2608.13522.md
  - concepts/repo-level-verified-code-proof-eval.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
  - sources/brief-k237-meta-harness-vero-misevolution-2026-08-14.md
maturity: draft
wire_status: wont_wire
created: 2026-08-14
updated: 2026-08-15
---

## Relations

- `@sources/arxiv-vero-repo-verified-code-proof-2608.13522.md`
- `@concepts/repo-level-verified-code-proof-eval.md`
- `@concepts/verifiable-deterministic-agent-benchmarking.md`

## Raw Concept

Phase-0 entity for CCC K280 — Vero benchmark.

## Narrative

Repo `github.com/sunblaze-ucb/vero` — **Apache-2.0** LICENSE file on disk, ~2MB → cloned to `.local/adopts/vero` as **GO REFERENCE**. First benchmark for **joint implementation + proof synthesis at repository level**: 43 multi-module Lean 4 instances (Python/Dafny/Verus/Coq origins), proof-only + code-and-proof modes, and an **unsat/incorrectness audit** (agents may prove the provided spec unsatisfiable or reference code incorrect). Runtime **`wont_wire`** — Lean toolchain bench, not a runtime tool.

**Phase-0:** `scripts/adopt_k280_phase0.sh`
