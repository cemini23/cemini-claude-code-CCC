---
title: "SafeEvolve — harness-policy co-evolution for safety alignment (CCC K340)"
type: source
tags: [source, arxiv, safety, harness-evolution, co-evolution, k340]
keywords: [2609.02786, SafeEvolve, harness-policy co-evolution, safety alignment, skill bank, SFT-RL, AgentDojo]
related:
  - concepts/harness-policy-co-evolution-safety.md
  - entities/tools/safeevolve.md
  - concepts/skill-misevolution.md
  - concepts/trajectory-driven-safety-harness-evolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - briefs/2026-09-03_ccc-k337-k341-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- `@concepts/harness-policy-co-evolution-safety.md`
- `@entities/tools/safeevolve.md`
- `@concepts/skill-misevolution.md`
- `@concepts/trajectory-driven-safety-harness-evolution.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`
- `@briefs/2026-09-03_ccc-k337-k341-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment |
| **arXiv** | 2609.02786 (2026-09-02) |
| **Code** | `MaoPopovich/SafeEvolve` **MIT** ~841KB → GO REFERENCE |
| **Retrieved** | 2026-09-03 |

## Narrative

**Verdict: ADOPT policy with HITL — harness-only and policy-only both fail; co-evolve with bounded, auditable harness updates.**

SafeEvolve drives a continual loop from on-policy trajectories: **harness side** converts safety evidence into bounded updates to safety prompt + hierarchical skill bank (auditable, reversible); **policy side** uses harness-use SFT then harness-augmented RL with verifier-decomposed rewards. Qwen3.5-4B: AgentDojo ASR 2.37%→0.79% with higher benign utility.

CCC policy: co-evolution is a **pattern vocabulary**, not permission to auto-evolve `.cursor/skills` (pairs K237 misevolution, K268 SHE, K162 external eval). Trainer/SFT-RL runtime **`wont_wire`**. REFERENCE clone for packaging study only. Distinct from K237 SAFEEVOLVE delete-only repair sub-method — cross-link, do not duplicate.

## Snippets

> "Harness-only evolution can exceed policy capacity; policy-only evolution transfers poorly — SafeEvolve couples bounded harness refinement with policy optimization." [Source: arXiv 2609.02786 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.02786-safeevolve-harness-policy-co-evolution-from-agen.pdf` |
