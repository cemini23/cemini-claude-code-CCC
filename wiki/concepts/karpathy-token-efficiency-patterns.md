---
title: Karpathy token efficiency patterns — 90% savings claims (K72)
type: concept
tags: [concept, token-economics, karpathy, k72]
keywords: [bonsaixbt, karpathy, token-savings, prompt-caching, context-trim]
related:
  - concepts/token-economics-and-prompt-caching.md
  - concepts/twelve-rule-claude-md-template.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/context-engineering.md
  - concepts/karpathy-agent-infrastructure-basics.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/deepseek-coding-cost-routing.md
maturity: draft
created: 2026-05-27
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@concepts/token-economics-and-prompt-caching.md` — canonical CCC token policy
- `@concepts/twelve-rule-claude-md-template.md` — Karpathy CLAUDE.md lineage
- `@concepts/agent-token-discipline-openclaw-hermes.md` — anti-pattern when savings claims ignore quality
- `@concepts/context-engineering.md` — trim context vs dumb compression

Cross-wiki: K72 Post 15 (@bonsaixbt).

## Raw Concept

K72 Post 15 — **Karpathy-style token savings** (~90% claim [TENTATIVE]). CCC treats as **checklist** for scope-lock, caching, and smaller models on Tier-1 tasks — require measurement on Cemini workloads before adopting viral percentages.

## Narrative

| Tactic | CCC mapping |
|--------|-------------|
| Shorter system prompts | `@concepts/twelve-rule-claude-md-template.md` — rules not essays |
| Model routing | `@osint-wiki/concepts/agent-cost-routing-model-orchestra.md` |
| Avoid always-on agents | `@concepts/agent-token-discipline-openclaw-hermes.md` |

| Verdict | **REFERENCE** — benchmark before believing headline % |

## Snippets

> "Token-efficiency (Karpathy) — 90% savings [TENTATIVE]."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 15]
