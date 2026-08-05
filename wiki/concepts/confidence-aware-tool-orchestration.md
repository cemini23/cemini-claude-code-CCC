---
title: Confidence-aware tool orchestration (Robust-TO pattern)
type: concept
tags: [concept, orchestration, confidence, tool-routing, k129]
keywords: [2606.26904, robust-to, blind-trust, tiered-evidence]
related:
  - sources/arxiv-confidence-aware-tool-orchestration-video-2606.26904.md
  - sources/brief-k129-robust-to-imagegen-handoff-2026-06-27.md
  - concepts/recoverable-tool-reliability-hazards.md
  - concepts/subagent-orchestration.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - entities/tools/conductor-mcp.md
  - entities/tools/lazy-tool.md
  - sources/brief-k129-tool-reliability-orchestration-2026-06-27.md
  - briefs/2026-07-02_ccc-handoff-robust-to-confidence-orchestration-ingest.md
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/cost-aware-tool-acquisition-stopping.md
  - sources/arxiv-cam-df-cost-aware-tool-stopping-2607.27083.md
  - concepts/active-abstraction-programmatic-world-models.md
  - concepts/clarify-before-act-evidence-aligned-close.md
  - concepts/hybrid-gui-mcp-tool-adoption-gap.md
  - sources/arxiv-urbanagent-cross-system-urban-tasks-2608.03018.md
  - sources/arxiv-screenshots-or-tools-gui-mcp-2608.03327.md
maturity: draft
created: 2026-06-27
updated: 2026-08-05
cross-wiki-primary: "@image-gen-wiki/concepts/confidence-aware-tool-orchestration.md"
---

## Relations

- `@sources/arxiv-confidence-aware-tool-orchestration-video-2606.26904.md` — Robust-TO paper
- `@concepts/recoverable-tool-reliability-hazards.md` — complementary hazard diagnosis

## Raw Concept

Question: how should agents route sub-queries to tools when input quality and tool outputs carry unequal reliability?

## Narrative

**Confidence-aware tool orchestration** [TENTATIVE — Robust-TO 2606.26904]: score input reliability before routing; each tool returns `(result, confidence)`; synthesize answers using **three tiers** (high drives conclusion, medium only if consistent, low discarded).

**Steal-from for Cemini harness (generic — not video-specific):**

1. **Blind trust trap** — do not treat all MCP tool returns as equally authoritative
2. **Pre-route quality gate** — skip or downgrade tools when tunnel/schema health is poor (ETCLOVG Tool Interface)
3. **Tiered evidence merge** — Explore subagent low-confidence findings require second-source before wiki ingest narrative
4. **Confidence-cost discipline** — expensive deep_researcher only when high-tier evidence insufficient

**Cross-wiki:** video corruption eval → `@image-gen-wiki/briefs/2026-06-27_k129-robust-to-confidence-tool-orchestration-handoff.md`.

**Verdict:** **REFERENCE** pattern only; no Robust-TO prod install.

### K244 + K245 — clarify loop + adoption gap (2026-08-05)

K244 UrbanAgent adds **clarify-before-act** and **evidence-aligned close** before tiered merge. K245 GUI–MCP shows MCP presence ≠ use — measure **adoption gap** and match model class (reasoning vs non-reasoning sign flip). See `@concepts/clarify-before-act-evidence-aligned-close.md` and `@concepts/hybrid-gui-mcp-tool-adoption-gap.md`.

## Snippets

> "Confidence is computed as the product of the tool's intrinsic certainty and the estimated reliability of its input frames."
> — [Source: arxiv-2606.26904-2606-26904v1-confidence-aware-tool-orchestration.pdf, retrieved 2026-06-27]
