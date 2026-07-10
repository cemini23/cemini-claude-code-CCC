---
title: Agent five-gate org chart — Intake through Memo (K98)
type: concept
tags: [concept, multi-agent, subagents, conductor, k98]
keywords: [voxyz-ai, intake, specialist, adversary, lead, memo, tradingagents, org-chart]
related:
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - entities/patterns/scatter-gather.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/agent-completion-verification-gates.md
  - concepts/claude-code-subagent-templates.md
  - sources/trading-posts-compilation-18-2026-06-04.md
  - "@osint-wiki/concepts/agent-team-five-gate-decision-memo.md"
  - "@osint-wiki/sources/tradingagents.md"
  - concepts/cage-1-enterprise-agent-governance-eval.md
maturity: draft
created: 2026-06-04
updated: 2026-07-10
cross-wiki-source: "@osint-wiki/concepts/agent-team-five-gate-decision-memo.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — dispatch primitives for Specialist gates
- `@entities/tools/conductor-mcp.md` — Lead + cross-wiki specialist routing
- `@entities/patterns/scatter-gather.md` — parallel Specialist fan-out
- `@entities/patterns/tier1-tier2-agent-model.md` — scope envelope per gate
- `@concepts/agent-completion-verification-gates.md` — Memo gate = done criteria + audit trail
- `@sources/trading-posts-compilation-18-2026-06-04.md` — K98 Post 1 (@Voxyz_ai)
- `@osint-wiki/concepts/agent-team-five-gate-decision-memo.md` — OSINT canon (TradingAgents anchor)

## Raw Concept

K98 Post 1 (@Voxyz_ai): multi-agent research beats single-chat persona cosplay when **five structural gates** are explicit. CCC maps gates to existing harness patterns — no TradingAgents / Bloome / AI Hedge Fund install without Phase-0.

## Narrative

| Gate | Role | Cemini analog |
|------|------|---------------|
| **Intake** | Reframe vague asks (horizon, risk, universe, constraints) | `/goal` section 0 + explicit scope in user prompt before prod-touching work |
| **Specialist** | One judgment angle per agent (filters, not cosplay) | `conductor_query` fan-out; Explore/Plan subagents with narrow briefs |
| **Adversary** | Forced disagreement (bull/bear, Buffett/Graham filters) | Brief-audit pass; `@entities/patterns/glasswing-deliberate-disagreement.md` |
| **Lead** | Assigns work, synthesizes — no hot takes | Parent Claude Code session; conductor coordinator |
| **Memo** | Decision record + invalidation + next steps | `wiki/log.md` ingest entries; briefs with GO/NO-GO verdicts |

### Posture

| Repo cited in post | Verdict |
|---------------------|---------|
| TauricResearch/TradingAgents | **REFERENCE** — academic org-chart anchor on OSINT |
| AI Hedge Fund (59k★) | **DEFER** — Phase-0 license + overlap with conductor |
| Bloome | **NO-GO install** until Phase-0 [NEEDS VERIFICATION 2026-06-04] |

**Gap [TENTATIVE]:** formal **Intake gate** script before expensive prod briefs — not yet a slash command; steal into `/goal` template preamble.

## Snippets

> "Without Memo, you make the same mistake next time."

> "The upgrade is the org chart."

> — [Source: Posts.docx K98 Post 1, @Voxyz_ai; @osint-wiki/sources/trading-posts-compilation-18-2026-06-04.md]
