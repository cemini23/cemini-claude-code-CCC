---
title: "RAC — reference-aware activation compression for split LLM inference"
type: source
tags: [source, arxiv, split-inference, privacy, activation-compression, k251]
keywords: [2608.04991, RAC, split-inference, TTFT, TPOT, local-head, cloud-middle]
related:
  - concepts/split-inference-activation-compression.md
  - entities/tools/rac-split-inference.md
  - concepts/local-first-mcp-multi-agent-workbench.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- `@concepts/split-inference-activation-compression.md`
- `@entities/tools/rac-split-inference.md`
- `@concepts/local-first-mcp-multi-agent-workbench.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | RAC (Reference-aware Activation Compression) |
| **arXiv** | 2608.04991 |
| **Repo** | None found (Phase-0) |
| **Domain** | Split LLM inference (local head/tail/tools + cloud middle) |
| **Retrieved** | 2026-08-06 |

## Narrative

Reference-aware activation compression for **split LLM inference** (local head/tail/tools + cloud middle). TTFT Raw-to-RAC 1.24–2.72×; TPOT 1.01–2.79×; task scores −0.40 to +2.50.

| Verdict | **ADOPT** awareness — split inference needs boundary-compression; privacy-sensitive agents benefit from local head/tools. **NO-GO** install. Concept-only; entity `wont_wire`. |
