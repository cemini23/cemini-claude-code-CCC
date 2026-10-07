---
title: "Design-registry MCP servers — design contract for coding agents (CCC k284)"
type: entity
tags: [entity, mcp-server, design-system, k284, lead]
keywords: [refero, 21st.dev, uiverse, DESIGN.md, design tokens, shadcn, design contract]
related:
  - concepts/mcp-server-catalog-curation.md
wire_status: unwired
maturity: draft
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- `@concepts/mcp-server-catalog-curation.md`

## Raw Concept

Filed from `@briefs/2026-10-07_k284-ccc-design-registries.md` (CCC k284 daily brief, 2026-10-07). Not paper-derived — the brief is the
source, and the brief's own boundary applies.

## Narrative

**The gap.** Agent-written frontends drift because the agent has **no design contract** — it
composes plausible markup with no reference to the project's tokens, spacing scale, or component
library. Three MCP connectors address it, surfaced by `@briefs/2026-10-07_k284-ccc-design-registries.md`:

| Connector | What it exposes |
|-----------|-----------------|
| `styles.refero.design` (Refero Styles) | Streams a **`DESIGN.md`** design-token file into Cursor / Claude / Codex |
| `21st.dev` | **shadcn** component registry over MCP |
| `uiverse.io` | CSS / Tailwind controls (also used by CeminiDFS and CeminiParlays UI) |

**Status: LEAD, not adoption.** The k284 brief sets the boundary explicitly — **"MCP install =
human-gated. Treat as a lead."** No Phase-0 has run: no license check, no transport/auth read, no
review of what these servers read or where they send data. **Do not install.**

**Why it is worth tracking.** The shape is the interesting part, not the vendors: **a design token
file as an MCP-served artifact** is a *contract* the agent can be held to, which is the same
movement as `@concepts/schema-bound-mcp-tool-surface.md` — move the constraint out of the prompt and
into something checkable. If CCC ever does frontend work with an agent, the question is whether the
design system is *stated* in a prompt or *served* as a contract.

**Phase-0 to run before any install:** SPDX licence per connector; stdio vs HTTP transport; what
credentials it reads; whether it transmits the project's design tokens anywhere; and whether the
registry content is mirrored or fetched live (catalog-churn risk — see
`@concepts/mcp-server-catalog-curation.md`).

## Snippets

> "Agent-written frontends drift because the agent has no design contract." [Source:
> `@briefs/2026-10-07_k284-ccc-design-registries.md`]

## Dead Ends

- **Not installed, not cloned.** Recorded as a lead so the next frontend-facing workstream does not
  rediscover it.
