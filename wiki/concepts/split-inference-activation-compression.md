---
title: Split inference activation compression (K251)
type: concept
tags: [concept, split-inference, privacy, activation-compression, local-first, k251]
keywords: [2608.04991, RAC, TTFT, TPOT, local-head, cloud-middle, boundary-compression]
related:
  - sources/arxiv-rac-split-inference-activation-compression-2608.04991.md
  - entities/tools/rac-split-inference.md
  - concepts/local-first-mcp-multi-agent-workbench.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- `@sources/arxiv-rac-split-inference-activation-compression-2608.04991.md` — K251 provenance
- `@concepts/local-first-mcp-multi-agent-workbench.md` — local head/tools peer (K234)

## Raw Concept

When LLM inference is split across local and cloud tiers, what must be compressed at the boundary?

## Narrative

K251 RAC (arXiv **2608.04991**): **reference-aware activation compression** for split LLM inference — local head/tail/tools + cloud middle layers.

| Metric | Raw-to-RAC |
|--------|------------|
| TTFT | 1.24–2.72× |
| TPOT | 1.01–2.79× |
| Task scores | −0.40 to +2.50 |

No public code at Phase-0.

### Cemini awareness (ADOPT)

- Split inference architectures need **boundary-compression** discipline — activations crossing local/cloud are a privacy + latency bottleneck
- Privacy-sensitive agents benefit from **local head + local tools** (pairs `@concepts/local-first-mcp-multi-agent-workbench.md`)
- Awareness only — no RAC install

| Verdict | **ADOPT** awareness. **NO-GO** install. Entity `wont_wire`. |
