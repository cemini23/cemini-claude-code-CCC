---
title: "Vero — can AI agents build formally verified software repositories?"
type: source
tags: [source, arxiv, benchmark, formal-verification, lean, repo-level, k280]
keywords: [2608.13522, Vero, Lean4, code-and-proof, unsat-audit, incorrectness-audit, repository-scale, sunblaze-ucb]
related:
  - concepts/repo-level-verified-code-proof-eval.md
  - entities/tools/vero.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- `@concepts/repo-level-verified-code-proof-eval.md`
- `@entities/tools/vero.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Vero: Can AI Agents Build Formally Verified Software Repositories? |
| **arXiv** | 2608.13522 |
| **Authors** | Zhe Ye, Hantao Lou, Yuechun Sun, et al. (UC Berkeley / UChicago / Caltech / Stanford / Apodex / AWS) |
| **Code** | `github.com/sunblaze-ucb/vero` — **Apache-2.0** LICENSE file (local clone) |
| **Retrieved** | 2026-08-14 |

## Narrative

**First benchmark for joint implementation + proof synthesis at repository level.** 43 multi-module instances sourced from real-world repositories spanning Python, Dafny, Verus, and Coq (domains from cryptographic protocols to distributed systems). Each instance: a multi-module **Lean 4** repo with predetermined API interfaces, manually curated formal specifications, and reference implementations — supporting both **proof-only** and **code-and-proof** evaluation modes.

Distinctive **audit mechanism**: agents may formally prove **unsatisfiability of a provided specification** or **incorrectness of reference code**, surfacing and correcting latent spec/code errors during curation — i.e. the benchmark can be challenged, not just completed. Frontier coding agents with Lean toolchain access: strongest config **fully solves only 27/43** instances and closes **no specifications** on the hardest repositories.

| Verdict | **ADOPT** joint impl+proof eval + unsat/incorrectness audit. **GO REFERENCE** (`sunblaze-ucb/vero` Apache-2.0 ~2MB → cloned to `.local/adopts/vero`). Runtime **`wont_wire`** (Lean bench, not a runtime tool). |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.13522-vero-can-ai-agents-build-formally-verified-softw.pdf`
