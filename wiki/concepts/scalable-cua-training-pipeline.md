---
title: Scalable CUA training pipeline — env / solver / verifier
type: concept
tags: [concept, computer-use, cua, training, k124]
keywords: [2606.20785, faragen, verifiers, synthetic-environments]
related:
  - sources/arxiv-fara-scalable-cua-environments-2606.20785.md
  - entities/tools/fara.md
  - concepts/cli-anything-agent-native-computer-use.md
  - entities/tools/webwright.md
  - concepts/agent-completion-verification-gates.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@sources/arxiv-fara-scalable-cua-environments-2606.20785.md` — FaraGen1.5 paper
- `@concepts/agent-completion-verification-gates.md` — verifier alignment

## Raw Concept

How do you scale computer-use agent training data when human demos are expensive?

## Narrative

**FaraGen1.5** (2606.20785) modular pipeline:

1. **Environments** — live websites + synthetic simulators for auth-gated / irreversible domains
2. **Solvers** — pluggable teacher harness (frontier models + user simulator for multi-turn)
3. **Verifiers** — task correctness, efficiency, critical-point adherence on trajectories

**CCC steal-from:** triple-verifier discipline for browser automation smoke tests (cursor-ide-browser MCP). Not adopting native CUA fine-tuning — **REFERENCE** only.

## Snippets

> "Collecting computer use data from human demonstrations is expensive and slow, motivating the need for scalable generation strategies."
> — [Source: arxiv-2606.20785, retrieved 2026-06-24]
