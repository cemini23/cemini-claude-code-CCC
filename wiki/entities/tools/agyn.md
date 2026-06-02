---
title: Agyn — open-source agent execution platform (reference)
type: entity
tags: [tool, agent-platform, reference, arxiv]
keywords: [agyn, 2605.27575, serverless-agents, governance]
related:
  - sources/arxiv-agyn-agent-platform-2605.27575.md
  - entities/tools/conductor-mcp.md
  - concepts/agent-vm-sandboxing.md
  - concepts/subagent-orchestration.md
  - "@osint-wiki/entities/tools/agyn-platform.md"
maturity: draft
created: 2026-06-02
updated: 2026-06-02
phase_0_verdict: NO-GO install 2026-06-02 — AGPL-3.0; REFERENCE governance only
---

## Relations

- `@sources/arxiv-agyn-agent-platform-2605.27575.md` — arXiv 2605.27575
- `@entities/tools/conductor-mcp.md` — Cemini orchestration peer (different scope)
- `@concepts/agent-vm-sandboxing.md` — isolation patterns
- `@osint-wiki/entities/tools/agyn-platform.md` — OSINT prod topology comparison (K94)

## Raw Concept

**Agyn** — signal-driven, stateful serverless runtime for production AI agents (open source). arXiv 2605.27575.

## Narrative

| Check | Verdict |
|-------|---------|
| License (`agynio/platform`) | **AGPL-3.0** — NO-GO prod/laptop install without legal review |
| CCC laptop wiki workflow | **NO-GO** — full K8s platform |
| Reference value | **REFERENCE** — isolation + governance checklist vs conductor prod |

**Verdict:** **REFERENCE** — Phase-0 complete; prod checklist via OSINT brief to `cemini-prod`.

## Snippets

> "Agent Definition as a Service" framing — on-demand execution at scale.
> — [Source: arxiv-2605.27575-agyn-an-open-source-platform-for-ai-agents-with.pdf]
