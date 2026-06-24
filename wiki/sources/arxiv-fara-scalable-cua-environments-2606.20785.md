---
title: Fara-1.5 scalable CUA learning environments (arXiv 2606.20785)
type: source
tags: [source, arxiv, computer-use, cua, microsoft, k124]
keywords: [2606.20785, faragen, browser-agent, verifiers]
related:
  - concepts/scalable-cua-training-pipeline.md
  - entities/tools/fara.md
  - concepts/cli-anything-agent-native-computer-use.md
  - entities/tools/webwright.md
  - concepts/agent-completion-verification-gates.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@entities/tools/fara.md` — microsoft/fara repo (MIT)
- `@concepts/scalable-cua-training-pipeline.md` — FaraGen1.5 env/solver/verifier synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Fara-1.5: Scalable Learning Environments for Computer Use Agents |
| **Authors** | Awadallah et al. (Microsoft) |
| **arXiv** | 2606.20785v1 [cs.AI] |
| **Code** | https://github.com/microsoft/fara (MIT) |
| **Models** | https://ai.azure.com/catalog/models/Fara1.5-9B |
| **Location** | `raw-sources/arxiv-2606.20785-2606-20785v1-fara-1-5-scalable-learning-environm.pdf` |
| **Retrieved** | 2026-06-24 |
| **Read status** | read (FaraGen1.5 pipeline + benchmark results) |

## Narrative

**FaraGen1.5** — modular data pipeline for computer-use agents: **environments** (live sites + synthetic auth-gated simulators), **solvers** (frontier teacher harness incl. GPT-5.4 + user simulator for multi-turn), **verifiers** (task correctness, efficiency, critical-point adherence).

Trains **Fara1.5** native CUAs (4B/9B/27B on Qwen3.5). Fara1.5-9B: 63.4% Online-Mind2Web, 86.6% WebVoyager — SOTA for size class.

**CCC relevance:** verifier triple + synthetic environment pattern for browser automation eval. **REFERENCE** for CUA training — Cemini uses cursor-ide-browser / Webwright for harness verification, not native CUA fine-tuning.

## Snippets

> "FaraGen1.5 uses both live websites and synthetic environments that faithfully simulate domains gated by authentication or that require irreversible actions."
> — [Source: arxiv-2606.20785-2606-20785v1-fara-1-5-scalable-learning-environm.pdf, retrieved 2026-06-24]
