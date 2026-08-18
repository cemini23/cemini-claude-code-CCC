---
title: "VibeWorlding-Gym — 3D world-agent RL sandbox (HKUST(GZ) / Tencent)"
type: entity
tags: [entity, tool, multimodal, 3d, mcp, agentic-rl, no-license, k286]
keywords: [k286, VibeWorlding-Gym, VWE-Bench, null-SPDX, NO-GO, MCP sandbox, rubric verifier]
related:
  - sources/arxiv-vibeworlding-3d-open-worlds-2608.15265.md
  - concepts/vibeworlding-multimodal-3d-world-agents.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
  - "@game-dev-wiki/concepts/vibeworlding-3d-agent-stub.md"
maturity: draft
wire_status: wont_wire
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-vibeworlding-3d-open-worlds-2608.15265.md`
- `@concepts/vibeworlding-multimodal-3d-world-agents.md`
- `@game-dev-wiki/concepts/vibeworlding-3d-agent-stub.md`

## Raw Concept

Phase-0 entity for CCC K286 — VibeWorlding-Gym (3D world-agent RL framework).

## Narrative

Repo `github.com/usail-hkust/VibeWorlding-Gym` — **NO-GO clone** (null SPDX, no LICENSE file). A joint multimodal RL post-training framework for 3D world construction: a sandbox unifying asset retrieval/edit/render as **MCP tools**, plus a **dual-constraint verifier** (physical feasibility + intent fulfillment) reused as the RL reward service. Companion artifacts: VWE-Bench dataset (2,616 assets / 323 seed worlds / 6,828 queries) and VibeWorlder models (8B / 30B-A3B) on Hugging Face.

Steal (WATCH): unify fragmented 3D tooling under one MCP sandbox; reuse a rubric verifier as both eval scorer and RL reward (single environment/reward definition); trace the bottleneck via capability analysis. **`wont_wire`** on CCC/Image-gen/3D — pattern only; game-dev stub deepens.

**Phase-0:** `scripts/adopt_k286_phase0.sh` (no clone — null SPDX)
