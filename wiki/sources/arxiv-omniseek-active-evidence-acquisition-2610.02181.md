---
title: "OmniSeek: Native Tool Integration for Multi-turn Audio-Visual Reasoning (CCC K418)"
type: source
tags: [source, arxiv, k418]
keywords: [2610.02181, k418]
related:
  - concepts/active-evidence-acquisition-multimodal.md
  - briefs/2026-10-02_ccc-k416-k420-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-02
---

## Relations

- `@concepts/active-evidence-acquisition-multimodal.md`
- `@briefs/2026-10-02_ccc-k416-k420-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | OmniSeek: Native Tool Integration for Multi-turn Audio-Visual Reasoning |
| **arXiv** | 2610.02181 (2026-10) |
| **Retrieved** | 2026-10-02 |

## Narrative

**Verdict: REFERENCE (multimodal; 2 ideas transfer).**

**OmniSeek — make evidence acquisition part of the reasoning, not a preprocessing step.** Omni-LLMs normally ingest an entire audio-visual stream in one forward pass; as context grows, brief acoustic events and fine visual details are diluted and the model falls back on language priors. OmniSeek instead runs an explicit **`<think>` → `<tool_call>` → `<observe>` loop**, deciding *which* modality to inspect and *which* time window, then appending the retrieved raw segment back into context. The training contribution worth noting is the **Audio-Visual Necessity objective**: an RL reward that credits trajectories whose answer genuinely depends on **both** modalities, which **discourages single-modality shortcuts** without extra rollouts. The paper also documents a clean **failure mode under context overflow**: past the window, the agent **loses tool invocation entirely** and degenerates into a repetitive `<think>` loop, **hallucinating observations it never retrieved** rather than calling the tool. That is the same failure K410 warns about — control state collapsing under unbounded history. **CCC relevance is partial** — the domain is audio-visual, so this is REFERENCE, but two ideas transfer: **modality-decoupled retrieval as an explicit loop**, and an **anti-shortcut reward term**. Pairs K410 agentic meta-reasoning (bounded controller state) / `@concepts/context-engineering.md` / K418's own failure mode with K387 KV working-set. **No repo surfaced.** Runtime **`wont_wire`**; concept **`policy_wired`** awareness.

## Snippets

> "As the context overflows, the agent loses the ability to invoke tools. Instead, it falls into a repetitive <think> loop, hallucinating sensory evidence directly within its internal reasoning blocks." [Source: arXiv 2610.02181 (retrieved 2026-10-02)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.02181-omniseek-native-tool-integration-for-multi-turn.pdf` |
