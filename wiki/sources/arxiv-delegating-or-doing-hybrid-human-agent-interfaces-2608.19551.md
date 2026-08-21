---
title: "Delegating or Doing? — hybrid HAI + MCP CMS study (N=73)"
type: source
tags: [source, arxiv, hci, mcp, delegation, hybrid, k295]
keywords: [2608.19551, delegAgents, hybrid interface, ICC, CRUD, effort-vs-duration]
related:
  - concepts/hybrid-human-agent-delegation-effort-vs-duration.md
  - entities/tools/delegating-or-doing-hybrid-hai.md
  - concepts/hybrid-gui-mcp-tool-adoption-gap.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@concepts/hybrid-human-agent-delegation-effort-vs-duration.md`
- `@entities/tools/delegating-or-doing-hybrid-hai.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Delegating or Doing? Understanding User Behavior in Hybrid Human–Agent Interfaces |
| **arXiv** | 2608.19551 |
| **Authors** | Dizon, Sta. Maria, Deja, Sumi (Future University Hakodate / De La Salle) |
| **Venue** | HAI '26 (ACM), Osaka — 9 pp |
| **Code** | None public (delegAgents study app) → **policy only** |
| **Retrieved** | 2026-08-21 |

## Narrative

Between-subjects study (**N=73**) on a web CMS ("delegAgents") augmented with an LLM agent through MCP; three modes: **Traditional-Only / AI-First / Hybrid**, 16 CRUD scenarios. AI-assisted interaction **significantly cut clicks, page navigations, and scrolls** (NB-GLM; e.g. clicks μ 5.71 AI-First vs 9.99 Traditional), but **task duration did not differ significantly** across conditions (AI-First descriptively fastest at 46.6 s). No significant link between CRUD operation risk and delegation (χ²(3)=6.60, p=.086); **delegation variance is person > task** — by-participant random intercept ≈ half the variance in chat interactions (latent-scale **ICC = .50**, unchanged after adding condition). Even under an explicit "use the assistant" directive (AI-First), chat use stayed sparse and uneven — occasional high-leverage handoffs, not sustained conversation.

| Verdict | **ADOPT** pattern: measure effort vs duration separately; do not treat MCP presence as speedup; hybrid availability ≠ high-risk auto-delegate. No public repo → **policy only** (`policy_wired`). Pairs K245 / K247. |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.19551-delegating-or-doing-understanding-user-behavior.pdf` |
