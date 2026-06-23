---
title: Towards an Agent-First Web — redesigning the web for AI agents (arXiv 2606.19116)
type: source
tags: [source, arxiv, agent-first-web, atml, geo, k119]
keywords: [2606.19116, atml, agents.txt, epistemic-recursion, agent-as-human-proxy]
related:
  - concepts/agent-first-web-framework.md
  - entities/skills/geo-seo-claude.md
  - concepts/internet-of-agentic-ai-ioai.md
  - concepts/mcp-context-optimization.md
  - entities/tools/webwright.md
  - concepts/agentic-web-infrastructure-gap-taxonomy.md
  - sources/arxiv-agentic-web-infrastructure-agentverse-2606.20570.md
maturity: draft
read_status: read
created: 2026-06-19
updated: 2026-06-23
---

## Relations

- `@concepts/agent-first-web-framework.md` — CCC synthesis
- `@entities/skills/geo-seo-claude.md` — GEO/AEO operator surface
- `@concepts/internet-of-agentic-ai-ioai.md` — federation / discovery peer vision
- `@concepts/mcp-context-optimization.md` — agent identification + content delivery economics

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Towards an Agent-First Web: Redesigning the Web for AI Agents |
| **Authors** | Bandara et al. (ODU + industry consortium) |
| **arXiv** | 2606.19116v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.19116-towards-an-agent-first-web-redesigning-the-web-f.pdf` |
| **Retrieved** | 2026-06-19 |
| **Read status** | read (three-layer framework, ten principles, ATML, migration roadmap) |

## Narrative

**Thesis:** The web assumes human consumers; AI agents as intermediaries invalidate access, economic, and content assumptions. Blocking/CAPTCHA treats agents as extraction.

**Three-layer redesign:**

| Layer | Mechanisms |
|-------|------------|
| Access | Agent identification metadata, `agents.txt`, rate limiting over blocking, dual-layer HTML + agent format |
| Economic | Agent-as-human-proxy principle; token-based metering; subscription delegation; commissioned content |
| Content | ATML (Agent Text Markup Language); four-level human supervision tiers; cryptographic provenance chain |

**Epistemic recursion:** AI content consumed by AI agents detaches knowledge from human ground truth — countered by declared supervision + provenance.

**Near-term migration (Phase 1):** agent HTTP headers, `agents.txt`, richer `llms.txt`.

**CCC routing:** publisher/GEO implications → `@seo-wiki`; harness cites ATML/`agents.txt` as **REFERENCE** only.

## Snippets

> "Agents acting on behalf of humans should inherit equivalent access rights — governed by rate limiting and standardized agent identification metadata."

> "ATML — a semantic content format optimized for agent consumption — alongside a four-level human supervision tier model."
