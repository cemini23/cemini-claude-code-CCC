---
title: "Memory poisoning vs content screening — the boundary, bounded occupancy, and write-path grounding"
type: concept
tags: [concept, security, memory, retrieval, provenance, poisoning, k304]
keywords: [longmemeval, content screening boundary, bounded occupancy, additive provenance, external grounding, 2608.21230]
related:
  - sources/arxiv-agent-memory-poisoning-utility-2608.21230.md
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-agent-memory-poisoning-utility-2608.21230.md`
- `@concepts/reconstructive-agent-memory-vs-verbatim-replay.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Question answered: can write-time content screening or additive provenance ranking protect persistent agent memory from poisoning? Source: arXiv 2608.21230 (CCC K304). Pairs K230 reconstructive memory; dual-ID Cybersec K304.

## Narrative

A **payload-free lie** defeats content screening by construction: a false statement carries no instruction, no trigger, no optimization — so injection detectors tuned to payloads refuse 0/360 of them while being genuinely good at injections (0.832 recall). Truthfulness is not a text property; it requires **external grounding beyond the screened content**. Therefore:

- **Content screening is necessary, not sufficient** — keep it, but never as the memory-integrity plan.
- **Additive provenance ranking has no usable weight** in the measured similarity regime (shipped weight p=0.80 vs none; any attacker-sufficient weight excludes untrusted sources categorically).
- Use provenance as a **bounded occupancy constraint**: cap the share of retrieved context that may come from untrusted channels, instead of scoring trust additively.
- Require **external grounding** before persistent writes: a memory claiming facts about the world needs a verifiable source at write time, not at read time.

Attack economics to internalize: 1.2% poisoned corpus → LongMemEval 0.850 → 0.300. Persistent memory converts a one-request attack into durable utility destruction.

No poison PoCs are stored or reproduced in this wiki (policy).

## Snippets

> "distinguishing a false assertion from a true one generally requires external grounding beyond the text being screened" [Source: arXiv 2608.21230 abstract]
