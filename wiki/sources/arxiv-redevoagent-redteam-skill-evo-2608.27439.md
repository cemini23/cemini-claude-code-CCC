---
title: "RedEvoAgent — red-team skill evolution with validation ratchet (CCC K324)"
type: source
tags: [source, arxiv, red-teaming, skill-evolution, validation-ratchet, cybersec, k324]
keywords: [2608.27439, RedEvoAgent, red-teaming, attack skill, validation ratchet, tool attribution, trajectory retrieval]
related:
  - concepts/validation-ratchet-skill-evolution.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@concepts/validation-ratchet-skill-evolution.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | REDEVOAGENT: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution |
| **arXiv** | 2608.27439 (2026-08-27, preprint) |
| **Authors** | Junjie Zhang, Hui Liu, Kecheng Chen, Xianbo Mo, Changsheng Chen, Haoliang Li (City University of Hong Kong + Shenzhen MSU-BIT) |
| **Code** | None verified — **Cybersec-primary; no attack-skill clone in CCC** |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: Cybersec-primary.** CCC steal: **validation ratchet** — keep skill updates only if validation improves (pairs K237). **No attack-skill clone. No attack/PoC text. `wont_wire` runtime.** Dual-ID with Cybersec's same-day PDF — resolve by file + wiki.

RedEvoAgent is a black-box red-teaming agent that **distills cross-case attack trajectories into a concise, human-readable attack skill**, which adaptively evolves via:

- **tool-effectiveness profiling** and
- **Deciding-Tool Attribution** for skill updates, plus
- a **validation ratchet** that retains only updates improving validation performance.

Motivation: trajectory-based retrieval in prior agentic attackers can **reuse misleading experiences** (retrieval bias, unclear tool credit), and full trajectories add context overhead while reducing interpretability.

CCC steal (defensive): the **validation ratchet** — any skill-memory patch must show validation improvement or it is rejected; never auto-evolve `.cursor/skills`. Applies the same gate Cemini already uses for skill updates (pairs K237/K298/K307/K309/K313/K314). The attack-skill mechanics themselves stay out of CCC (Cybersec-primary).

| Confidence | `[TENTATIVE]` — paper results as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "The attack skill adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance." [Source: arXiv 2608.27439 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.27439-redevoagent-automatic-red-teaming-agent-with-exp.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
