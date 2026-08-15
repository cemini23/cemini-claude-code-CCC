---
title: Local-first MCP multi-agent workbench — CyberNeuro pattern
type: concept
tags: [concept, mcp, multi-agent, local-first, hitl, skill-dag, k234]
keywords: [2607.28841, CyberNeuro, Planner, Validator, Dispatcher, Reporter, pinned execution]
related:
  - sources/arxiv-cyberneuro-privacy-agentic-neuroimaging-2607.28841.md
  - entities/tools/cyberneuro.md
  - concepts/mcp-app-hitl-approval-gap.md
  - sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md
  - briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md
  - sources/arxiv-rac-split-inference-activation-compression-2608.04991.md
  - concepts/split-inference-activation-compression.md
  - entities/tools/rac-split-inference.md
  - concepts/inspectable-tool-region-attribution.md
  - sources/brief-k158-amalthai-tabsom-from-seo-2026-08-14.md
maturity: draft
created: 2026-08-03
updated: 2026-08-15
---

## Relations

- `@sources/arxiv-cyberneuro-privacy-agentic-neuroimaging-2607.28841.md` — K234 CyberNeuro
- `@entities/tools/cyberneuro.md` — Phase-0 entity (wont_wire runtime)
- `@concepts/mcp-app-hitl-approval-gap.md` — HITL verification panel peer

## Raw Concept

How do we run multi-agent MCP workflows with privacy-preserving, local-first defaults and human QC gates?

## Narrative

K234 CyberNeuro (arXiv **2607.28841**) demonstrates a **local-first** agentic workbench: no outbound network by default, four role-specialized agents (Planner, Validator, Dispatcher, Reporter) over a secure MCP bridge with **pinned execution**. Skills declared via SKILL.md + typed contracts compile to a **task DAG**. A HITL verification panel supports biomedical QC.

### Cemini steal (ADOPT)

| Pattern | Harness mapping |
|---------|-----------------|
| Local-first / no outbound default | Federation security preflight; prod MCP egress policy |
| Role-specialized agents + MCP bridge | Task/subagent role graphs; lazy-tool domain routing |
| SKILL.md → typed contract → DAG | OpenSpec + `/goal` acceptance criteria; validate DAG before fan-out (K181) |
| HITL verification panel | Pairs `@concepts/mcp-app-hitl-approval-gap.md` — blocking approval for consequential tools |

**Domain note:** Neuroimaging workflow is OOD — adopt **architecture only**, not product install.

| Verdict | **ADOPT** patterns. **NO-GO** CyberNeuro product/code (gated site; no public repo) |

### K251 RAC — split-inference boundary compression (2026-08-06)

K251 RAC: reference-aware activation compression at local/cloud split boundaries — privacy-sensitive agents benefit from **local head + local tools** with compressed activations to cloud middle. Awareness only; no RAC install. See `@concepts/split-inference-activation-compression.md`.

## Snippets

> NeuroBench held-out domain accuracy 40%→69%; local WandaMind ~10.6% token usage vs NeuroClaw baseline.
> — [Source: arxiv-2607.28841, retrieved 2026-08-03]
