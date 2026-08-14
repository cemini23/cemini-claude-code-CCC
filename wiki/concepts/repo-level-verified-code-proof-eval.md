---
title: "Repository-level verified code+proof evaluation (K280)"
type: concept
tags: [concept, evaluation, formal-verification, lean, repo-level, k280]
keywords: [2608.13522, Vero, Lean4, code-and-proof, unsat-audit, incorrectness-audit, repository-scale]
related:
  - sources/arxiv-vero-repo-verified-code-proof-2608.13522.md
  - entities/tools/vero.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@sources/arxiv-vero-repo-verified-code-proof-2608.13522.md`
- `@entities/tools/vero.md`
- `@concepts/verifiable-deterministic-agent-benchmarking.md`

## Raw Concept

Existing verified-codegen benchmarks evaluate individual functions or proof-only modes. Vero asks the harder question: can an agent make **coherent implementation + proof choices across a real multi-module codebase**?

## Narrative

Vero is the first benchmark for **joint implementation + proof synthesis at the repository level**: 43 multi-module instances (Python, Dafny, Verus, Coq) wrapped as Lean 4 repos with fixed API interfaces, curated formal specs, and reference implementations. Two eval modes: proof-only and code-and-proof.

### Steal (ADOPT)

1. **Joint impl+proof eval** — grade the *combination*: implementation satisfies spec, proof checks. Unit tests + human review cannot rule out the bug classes formal verification captures.
2. **Unsat / incorrectness audit** — agents may **prove the provided spec unsatisfiable or the reference code incorrect**. The benchmark itself is challengeable, which surfaces latent curation errors. This is an audit mechanism inside an eval — the eval must survive being told it's wrong.
3. **Repository scale as the unit** — multi-module coherence (not single-function) is the realistic failure surface. Frontiers fully solve 27/43 and close nothing on the hardest repos → we are far from repo-scale verified synthesis.

### Local adopt

`sunblaze-ucb/vero` **Apache-2.0** ~2MB → cloned to `.local/adopts/vero` as **GO REFERENCE**. Runtime **`wont_wire`** (Lean toolchain bench, not a runtime tool).

| Verdict | **ADOPT** joint impl+proof eval + unsat/incorrectness audit; **GO REFERENCE** clone; runtime `wont_wire`. |
