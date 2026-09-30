---
title: "Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475 of 500 on LongMemEval-S (CCC K407)"
type: source
tags: [source, arxiv, k407]
keywords: [2609.38021, k407]
related:
  - concepts/deterministic-retrieval-chain-reader-swap.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
  - concepts/headless-claude-code-controlled-eval-lane.md
maturity: draft
read_status: deep-read
created: 2026-09-30
updated: 2026-09-30

---

## Relations

- `@concepts/deterministic-retrieval-chain-reader-swap.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`
- `@concepts/headless-claude-code-controlled-eval-lane.md` — headless Claude Code controlled eval lane (K407/K410)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475 of 500 on LongMemEval-S |
| **arXiv** | 2609.38021 (2026-09) |
| **Repo** | `cjchanh/longmemeval-evidence` |
| **Retrieved** | 2026-09-30 |

## Narrative

**Verdict: REFERENCE + eval-methodology.**

**Auditable long-term memory.** Every stage below the final answer is deterministic code — hybrid candidate retrieval, cross-encoder reranking, packet compilation, mechanical reasoning scaffolds. The LLM appears **once, as a replaceable reader**. Because the lower stages are frozen, the same packets can be handed to any reader and the artifacts released for inspection. Scores 479/475 of 500 on LongMemEval-S, **bracketing** the published 478 — overlapping CIs, so neither superiority nor equivalence is established. **CCC-critical: the headline Opus reader route is the Claude Code CLI with the built-in tools disabled.** **Methodology claim:** the official judge flips 3 verdicts when re-scoring *byte-identical* answers, so **the reportable quantity is the noise band, not the rank**. A pre-committed negative control rejected a verifier that repaired 3 wrong drafts but broke 11 correct ones. Retrieval/rerank/scaffold sources are **held** — the chain is not independently reproducible. Evidence repo `cjchanh/longmemeval-evidence` is **MIT**. Pairs K392 cross-vendor behavior assays / K162 external eval / `verifiable-deterministic-agent-benchmarking` / `anytime-valid-agent-eval-stopping`. Runtime **`wont_wire`**; concept **`policy_wired`** eval-methodology.

## Snippets

> "The headline Opus reader's route: the Claude Code command line, with the built-in tools disabled." [Source: arXiv 2609.38021 (retrieved 2026-09-30)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.38021-auditable-long-term-memory-a-deterministic-retri.pdf` |
