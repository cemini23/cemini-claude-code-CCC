---
title: Agent sandbox — Lambda to Unikraft microVM isolation
type: concept
tags: [concept, agent-sandbox, unikraft, security, k69]
keywords: [larsencc, unikraft, lambda, agent-isolation, microvm, tier2]
related:
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/tools/cua.md
  - entities/tools/claude-code.md
  - concepts/cross-wiki-routing.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - concepts/embedded-agent-modular-edge-architecture.md
  - sources/arxiv-embedded-agent-modular-edge-2606.02862.md
maturity: draft
created: 2026-05-27
updated: 2026-06-03
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md"
---

## Relations

- @entities/patterns/tier1-tier2-agent-model.md — sandbox placement for execution-capable agents
- @entities/tools/cua.md — macOS VM sandbox already in CCC stack (different isolation class)
- @entities/tools/claude-code.md — harness that would invoke sandboxed tool runs
- @sources/trading-posts-compilation-20-2026-05-27.md — Post 3 (@larsencc)

## Raw Concept

K69 Post 3 (@larsencc): agent **sandbox infrastructure** — moving from serverless Lambda-style wrappers toward **Unikraft microVM** isolation for untrusted agent code/tool execution. Cybersec-adjacent; CCC records the pattern for Tier-2 execution design.

## Narrative

### Pattern [TENTATIVE]

1. **Problem** — agents run shell, MCP, and fetched code; process-level isolation is insufficient for hostile inputs.
2. **Direction** — microVM per task (Unikraft) vs shared Lambda runtime — faster boot + stronger boundary cited in post.
3. **Cemini mapping** — aligns with `@entities/patterns/tier1-tier2-agent-model.md`: read-only research = Tier 1; execution MCP / prod writes = Tier 2 with isolation.

### CCC posture

| Question | Answer |
|----------|--------|
| Adopt Unikraft on prod now? | **No** — `[NEEDS VERIFICATION 2026-05-27]` ops cost + Hetzner fit |
| Value | **Reference** when scoping execution MCP hardening (polymarket-mcp-server class) |
| Existing stack | `@entities/tools/cua.md` covers desktop VM pattern; Unikraft is server-side analogue |

### Cross-wiki

OSINT flagged Post 3 for cybersec-wiki brief — not ingested there yet; CCC owns harness/sandbox **design** reference.

## Snippets

> Agent sandbox infra: Lambda → Unikraft microVM isolation. [TENTATIVE — @larsencc, Posts.docx K69 Post 3]
