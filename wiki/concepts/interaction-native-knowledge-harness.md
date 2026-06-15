---
title: Interaction-native knowledge harness — passive injection + wiki audit (InKH)
type: concept
tags: [concept, knowledge-harness, wiki, passive-injection, context-engineering]
keywords: [2606.01886, inkh, temporal-graph, wiki-audit, financial-cognition-friction]
related:
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - osint-wiki/concepts/interaction-native-knowledge-harness.md
  - osint-wiki/sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - entities/mcp-servers/llm-wiki-compiler.md
  - concepts/context-engineering.md
  - concepts/federated-daily-research-digest.md
  - entities/tools/claude-mem.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/agents-k1-agent-native-knowledge-orchestration.md
  - sources/arxiv-agents-k1-knowledge-orchestration-2606.13669.md
maturity: draft
created: 2026-06-04
updated: 2026-06-13
---

## Relations

- `@sources/arxiv-interaction-native-knowledge-harness-2606.01886.md` — arXiv 2606.01886
- `@entities/mcp-servers/llm-wiki-compiler.md` — Karpathy LLM Wiki compiled-knowledge pattern (paper §2)
- `@concepts/context-engineering.md` — passive injection vs agent wiki-walk retrieval
- `@concepts/federated-daily-research-digest.md` — event-stream ingest cadence
- `@entities/tools/claude-mem.md` — session observation vs InKH persistent graph
- `@osint-wiki/concepts/interaction-native-knowledge-harness.md` — financial temporal graph + governance (ingested 2026-06-04)
- `@osint-wiki/sources/arxiv-interaction-native-knowledge-harness-2606.01886.md` — OSINT source mirror
- OSINT handoff brief: `briefs/2026-06-04_inkh-financial-knowledge-harness-osint-handoff.md` (financial deployment)
- `@concepts/agents-k1-agent-native-knowledge-orchestration.md` — agent-native multimodal KG pipeline (K114)
- `@sources/arxiv-agents-k1-knowledge-orchestration-2606.13669.md` — Scholar-KG / GraphAnything provenance

## Raw Concept

2606.01886 **InKH** architecture: absorb **financial cognition friction** by making the harness continuously compile interaction traces into governed knowledge — graph for retrieval, **wiki for human audit**.

## Narrative

### Layers (CCC steal-from) [TENTATIVE — financial paper, harness patterns generalize]

| Component | InKH role | Cemini analog |
|-----------|-----------|---------------|
| Event stream | User/market/tool updates | `wiki/log.md`, daily sweeps, claude-mem observations |
| Working context buffer | Passive injection under token budget | `hot.md` + static `CLAUDE.md` + lazy MCP |
| Temporal knowledge graph | Low-latency retrieval substrate | conductor + librarian kb-server (OSINT); local `wiki/` graph |
| Wiki audit surface | Human-readable governance | CCC ingest + `wiki_lint.py` + maturity tags |
| Invalidation + maturity | Write-time decay, governance gates | `[RETRACTED]` tags, skill-vetting tiers |

### Passive vs agent-driven retrieval

Paper Proposition 1: **passive injection** beats agent-driven wiki-walk when planning/search overhead exceeds irrelevant-context penalty. CCC already biases toward static-at-start prompts (`@concepts/context-engineering.md`) and conductor fan-out for wide reads — not letting the parent re-index entire vaults each turn.

### Posture

| Scope | Verdict |
|-------|---------|
| CCC federation wikis | **REFERENCE** — wiki-as-audit-surface + ingest/lint discipline |
| CeminiSuite trading stack | **OSINT** — full InKH financial graph + governance (see `briefs/2026-06-04_inkh-financial-knowledge-harness-osint-handoff.md`) |

**Do not** implement temporal-graph trading memory on prod without OSINT EMS/RBAC review.

## Snippets

> "The graph should serve online retrieval, while the wiki remains the audit surface."

> "Retrieval is not solely a query-time decision made by the agent."

> — [Source: arxiv-2606.01886 p.4–5, retrieved 2026-06-04]
