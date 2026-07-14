---
title: TrustX ARC — agent risk classification and tiering
type: concept
tags: [concept, governance, risk, classification, harness, k157]
keywords: [2607.09586, trustx, arc, low medium high, twelve dimensions, coding assistant extension, autonomy]
related:
  - sources/arxiv-trustx-agent-risk-classification-2607.09586.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/agent-completion-verification-gates.md
  - concepts/skill-vetting.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - concepts/agent-data-injection-attacks.md
  - sources/brief-k157-trustx-agent-risk-classification-2026-07-13.md
  - briefs/2026-07-13_ccc-handoff-memory-search-trustx-ingest.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
maturity: draft
created: 2026-07-13
updated: 2026-07-14
---

## Relations

- `@sources/arxiv-trustx-agent-risk-classification-2607.09586.md` — K157 provenance
- `@concepts/cage-1-enterprise-agent-governance-eval.md` — CAGE-1 Prebind (action-time) complements ARC (deploy-time tiering)

## Raw Concept

K157 arXiv **2607.09586** — **TrustX ARC** risk-tiers agentic systems before deployment using a **12-dimension rubric** + autonomy assessment. Outputs **Low / Medium / High** with control recommendations.

## Narrative

### vs CAGE-1 (K151)

| Framework | When | Focus |
|-----------|------|-------|
| **TrustX ARC** | Pre-deploy classification | Risk tier + governance controls |
| **CAGE-1 Prebind** | Per-action bind time | Prove control before consequential action |

Use **both:** classify agent at design time (ARC), enforce Prebind at runtime (CAGE-1).

### Four risk categories (12 dimensions) [from RAI Institute]

1. **Autonomy and Decision Power**
2. **Action Authority and Reach**
3. **Persistence and Control**
4. **Data Authority and Confidentiality**

**Critical-dimension rule:** one high dimension can elevate tier — not diluted by averaging.

### Seven agent types (abbreviated)

Autonomous agents · Coding assistants · Deep research · … (see source)

**Coding Assistant extension** — maps to Claude Code / Cursor harness: shell, git, MCP, settings manipulation risks (pairs K138 substrate, K139 ADI).

### Cemini mapping [TENTATIVE]

| Tier | CCC examples |
|------|--------------|
| **Low** | Read-only wiki query, lint-only subagent |
| **Medium** | Git commit with hooks; MCP read tools |
| **High** | prod SSH, trade execution, customer-facing send |

| Verdict | **REFERENCE** — use interactive TrustX tool + ARC checklist; no product install |

## Snippets

> "A system described as a helpful assistant that executes transactions … is not a low-risk system."
> — [Source: responsible.ai agent risk classification news, retrieved 2026-07-13]
