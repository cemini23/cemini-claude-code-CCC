---
title: "gtm-agents — production GTM / sales / marketing agent skill suite for Claude Code"
type: entity
category: tool
tags: [entity, tool, claude-code-skill-pack, gtm-automation, sales-marketing, k44, skip-phase-0-2026-05-14, single-author-risk, enterprise-scale-mismatch]
keywords: [gtm-agents, go-to-market-automation, sales-workflows, marketing-workflows, customer-success, apache-2-license, 244-skills, 99-percent-single-author, 98-open-issues]
related:
  - entities/mcp-servers/anthropic-skills.md
maturity: validated
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @entities/mcp-servers/anthropic-skills.md — 244-skill GTM pack; reference example of skill-pack distribution structure
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A specialized Claude Code skill pack of production-ready Go-To-Market (GTM) agents for sales, marketing, and customer-success workflows. **Apache-2.0, stars NOT FOUND** in K44 doc-level eval. K44 verdict: **Adopt**. Primary fit: CCC. Cross-route: SEO-wiki (creator marketing, social media automation).

## Narrative

The CCC value is structural: a documented, packaged skill-suite distribution model — useful reference for how Cemini's own skill packs should be structured for distribution.

### Phase-0 audit verdict (2026-05-14): SKIP

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `gtmagents/gtm-agents` resolved (top search result, 206★) |
| G1 | Star + maturity | **CONDITIONAL** | 206★ (K44 missed the count; this is the answer), Apache-2.0, but **single-author** (gtmagents org only, 5 commits in 6mo), 98 open issues |
| G2 | License | **PASS** | Apache-2.0 verbatim |
| G3 | Skill pack structure | **PASS** | 69 plugins / 244 skills, Claude Code conventions (YAML frontmatter, hierarchical layout) |
| G4 | Skill quality | **MIXED** | Marketplace-installable; cold-outreach skill lacks compliance guardrails (EU/CA AI Act); enterprise-scoped (Fortune 500 focus) |
| G5 | Cross-route to SEO | **SUPPLEMENT-ONLY** | See `@seo-wiki/entities/tools/gtm-agents.md` — gtm-agents 244 skills (enterprise) does NOT replace marketingskills.md (19K★, SMB/boutique). Non-overlapping audience tiers |

**Verdict: SKIP for CCC-wiki Adopt-tier.** The structural-reference value (skill-pack distribution model) is real, but lower priority than alumnium / optillm / adamsreview for active CCC-tooling adoption. Reference-only utility.

### What's worth referencing (not adopting)

1. **Skill-pack distribution model** — gtm-agents is a clean example of `/plugin marketplace add <org>/<repo>` + 244-skill packaging. Useful as a **structural template** when Cemini publishes its own skill pack.
2. **Cold-outreach prompt examples** — useful as tactical reference, NOT for direct deployment (compliance guardrails missing).
3. **YAML frontmatter conventions** — confirms Claude Code's standard skill-frontmatter expectations.

**Cross-route to SEO-wiki**: detailed comparison at `@seo-wiki/entities/tools/gtm-agents.md`. The SKIP verdict applies on both sides — does not advance the 30-day GEO/AEO + Polymarket newsletter revenue plan.

## Snippets

> "This repository hosts a specialized, production-ready suite of Go-To-Market (GTM) agents expressly configured for Claude Code. By mapping complex sales and marketing logic into modular skill files, it addresses the CCC-wiki's precise mandate for documenting skill packs and slash commands."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶313]
