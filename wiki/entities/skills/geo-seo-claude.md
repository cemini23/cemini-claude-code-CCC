---
title: geo-seo-claude (zubair-trabzada) — generative-engine SEO Claude Code skill
type: entity
tags: [skill, claude-code, geo, aeo, generative-engine-optimization, citability, schema-markup, mit]
keywords: [geo-seo-claude, zubair-trabzada, citability scoring, AI crawler analysis, JSON-LD validation, AEO, GEO, brand authority signals]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/commands/plugin.md
  - entities/skills/claude-seo-agrici.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/mcp-servers/anthropic-skills.md` — SKILL.md spec
- `@entities/commands/plugin.md` — install path
- `@entities/skills/claude-seo-agrici.md` — sibling skill (geographic SEO; this one is generative-engine SEO)

Cross-wiki: `@seo-wiki/entities/tools/geo-seo-claude.md` is the operator-facing canonical write-up. `@seo-wiki/sources/github-repo-audit-2026-05-07.md` is the Phase-0 GO verdict.

## Narrative

`github.com/zubair-trabzada/geo-seo-claude` — MIT, ~6.7K stars, last commit 2026-04-30. A Claude Code Agent Skill focused on **Generative Engine Optimization (GEO) / Answer Engine Optimization (AEO)** — making a website citable by ChatGPT, Claude, Perplexity, and Google AI Overviews.

This is the second of the two-part SEO skill pair Cemini installs:

- `@entities/skills/claude-seo-agrici.md` — geographic SEO (local pack, NAP, GBP)
- `@entities/skills/geo-seo-claude.md` — generative-engine SEO (citability, AI crawlers, schema-markup)

### What it does

- **Citability scoring** — analyzes a URL's ingestibility by AI engines (schema clarity, content structure, mention density, brand-authority signals)
- **AI-crawler analysis** — verifies OAI-SearchBot, PerplexityBot, ClaudeBot, Googlebot can fetch + parse cleanly
- **Schema-markup validation** — JSON-LD presence + correctness audit
- **Brand-authority heuristics** — cross-mention density signals AI engines weight for citation

### Install

```
/plugin marketplace add zubair-trabzada/geo-seo-claude
/plugin install <slug from repo README>
```

### Why Cemini tracks this skill in CCC (not just SEO wiki)

- **Real example of an AI-aware skill** — most Claude Code skills target classic web/UX tasks; this one is meta, optimizing content *for AI consumption*. Conceptually close to CCC's own audience.
- **Active maintenance evidence** — recently fixed issue #16 (WebFetch stripping `<head>` content). Kind of debugging discipline that distinguishes maintained skills from abandoned ones — a key Phase-0 audit criterion.
- **`/seo:*` namespace overlap with claude-seo-agrici** — both skills expose `/seo:*` commands. Verify install order or rename if collisions surface.

### Operationalizes the Aggarwal et al. 2024 GEO paper

The seminal GEO paper measured which content modifications drive citation visibility:
- **+41%** Quotation Addition
- **+33%** Statistics Addition
- **+28%** Cite Sources / Fluency Optimization
- **NEGATIVE** Keyword Stuffing

This skill provides the **measurement and audit side** — it tells you whether your site has the structure (citations, statistics, quotations) the paper validated as citation-driving. The actual *content rewriting* is a separate task (often paired with `@entities/skills/marketingskills.md`).

### Failure modes (per SEO-wiki audit)

- **Citability scores are heuristic, not ground truth** — track actual citations (direct query of each AI engine) as the ground-truth metric.
- **Engine churn** — generative engines change retrieval logic monthly. Re-score quarterly minimum.
- **`/seo` namespace conflict** — if both `claude-seo-agrici` and `geo-seo-claude` are installed, namespace conflicts may occur. Verify install order or rename.

## Dead Ends

- **Treating citability score as deterministic of citation** — it's correlated, not deterministic.
- **Running citability scoring before fixing schema markup** — the score is structurally bound by JSON-LD presence; fix schema first (Yoast or hand-coded), then score.
