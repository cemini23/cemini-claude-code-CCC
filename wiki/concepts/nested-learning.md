---
title: Nested Learning (Behrouz et al, NeurIPS 2025)
type: concept
tags: []
keywords: []
related:
  - concepts/context-engineering.md
  - entities/tools/claude-mem.md
maturity: draft
created: 2026-05-13
updated: 2026-05-15
cross-wiki-source: @osint-wiki/sources/nl-nested-learning-behrouz-neurips2025.md
---

# Nested Learning (Behrouz et al, NeurIPS 2025)

## Relations

- @concepts/context-engineering.md — the "context at different update rates" discipline this paper provides the literature frame for
- @entities/tools/claude-mem.md — per-session observation memory is one update-frequency layer in Cemini's multi-timescale memory stack
- @osint-wiki/sources/nl-nested-learning-behrouz-neurips2025.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/nl-nested-learning-behrouz-neurips2025.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

## Raw Concept

Cross-routed from osint-wiki 2026-05-13. The Behrouz et al *Nested Learning* paper (NeurIPS 2025) landed in the OSINT workspace inbox (PDF), but the substantive subject matter — multi-timescale memory architecture, self-modifying optimizers, chained MLPs — is ccc-wiki territory (meta-wiki on agent/workflow/conductor design). This page is the primary concept home; OSINT keeps a stub at `@osint-wiki/concepts/nested-learning.md` for cross-reference.

## Narrative

### Core thesis

ML models are best understood as **nested associative memory systems** with per-level optimization at multi-timescale frequencies. Each level updates at a different "Update Frequency" (the paper's load-bearing primitive in Definition 2).

### Key definitions (paper §2-3)

- **Definition 2 — Update Frequency**: rate at which a memory level's parameters change. Lower-level memory (attention weights) updates every forward pass; higher-level (model weights) updates every gradient step.
- **Definitions 3-7 — Nested System / NSAM / Generalized NSAM**: formalize multi-level associative-memory framing. Each level has own optimizer, frequency, addressing scheme.

### Hope architecture (paper §4)

Primary architectural contribution. Hope combines:

1. **Self-modifying Titans** — Titans variant where the model generates its own values and keys via Delta Gradient Descent (DGD) with weight decay. Parameters update on internal signal, not just external gradient.
2. **Continuum Memory System (CMS)** — chain of MLPs at progressively longer chunk sizes / lower update frequencies. Short-chunk MLP captures local context; long-chunk captures session-scale; longest captures world-scale.
3. **M3 optimizer** — combines Adam + Muon + CMS. Different parameter classes get different optimizers, gated by CMS chunk size.

### Empirical results (paper §6)

| Benchmark | Hope result | Baseline |
|-----------|-------------|----------|
| RULER NIAH S-NIAH-1, 16K context | 100% | Transformer 79.8% |
| BABILong 10M context retention | passes | Transformer fails |
| Language modeling, 1.3B params | 58.04 avg | Transformer++ 53.38 |
| Continual translation (Manchu + Kalamang) | passes | Transformer degrades |
| MAD synthetic benchmark | passes | Transformer fails |
| Formal language (parity, aⁿbⁿ) | passes | Transformer fails parity |

### Why this lands in ccc-wiki

The Cemini Conductor + librarian + memory-graph architecture is itself a multi-timescale memory system:
- chroma vectors at one frequency (per query)
- observation graph at another (per session)
- kb-server at another (per ingest)
- wiki source-of-truth at another (per commit)

The Hope/CMS frame is the cleanest existing-literature anchor for this "chain of memories at different update frequencies" pattern that Cemini implements ad-hoc.

### Open transfer questions for Cemini meta-design

1. **Update-Frequency as design primitive** — should Cemini's memory layers be explicitly named/configured by update frequency rather than by storage backend?
2. **Self-modifying via DGD analog** — can subagents modify their own kb-server / observation-graph contents at a higher update frequency than the human operator? What governance is needed if yes?
3. **M3-style optimizer routing** — the M3 idea (different optimizers for different parameter classes gated by chunk size) has an analog in agent design: different memory operations for different time scales gated by query type. Worth formalizing.

### What does NOT transfer

- **The actual training pipeline** — M3 + DGD-with-weight-decay require model-training infrastructure that Cemini doesn't have and isn't proposing to acquire
- **Specific architectural details** of Titans / CMS as PyTorch modules — Cemini operates above the model layer

The takeaway is conceptual + nomenclature, not implementational.

## Snippets

> "ML models are nested associative memory systems with per-level optimization at multi-timescale frequencies." [Source: NL.pdf §1, paraphrased]

> "Hope architecture: self-modifying Titans (DGD with weight decay) + Continuum Memory System (chain of MLPs at chunk sizes/frequencies) + M3 optimizer (Adam + Muon + CMS)." [Source: NL.pdf §4, paraphrased]

## Dead Ends

- **Implementing Hope locally** — Cemini doesn't train models. Conceptual transfer only.
- **Treating NL as a trading paper** — empirical wins are on language/synthetic/formal benchmarks. Trading relevance (if any) is downstream architectural inheritance, not direct.
