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

**Status: LEAD, Phase-0 run 2026-10-08 — still not an adoption, but the blocker moved.** The k284
brief set the boundary as **"MCP install = human-gated. Treat as a lead."** That stands. What
changed is *which* question blocks it.

## Phase-0 (2026-10-08)

**Data direction — the question that mattered, and it is the benign one.** Refero's own description:
*"Explore real website styles and their **AI-readable DESIGN.md files**. Compare screenshots, colors,
typography, and spacing to find a direction for your project."* and *"Your favorite sites, in
DESIGN.md."* It is a **library of pre-authored style definitions**, not an ingest point. The flow is
**service → agent**: it *serves* a `DESIGN.md`; it does **not receive** the project's design tokens.
**Your tokens do not leave the machine.** That removes the exfiltration concern I had assumed, and
licence was never the real question for a hosted service.

| Connector | Reachable | Nature | Notes |
|-----------|-----------|--------|-------|
| `styles.refero.design` | **200** | DESIGN.md library (hosted) | Serves style definitions; terms page present |
| `21st.dev` | **200** | **Commercial** component registry | 12,000+ React components; **pricing and privacy policy present** |
| `uiverse.io` | **403 to this probe** | CSS/Tailwind controls | Bot-blocked; could not verify from here — check in a browser |

**The actual Phase-0 finding — and it is bigger than the licence question.** If Refero serves a
`DESIGN.md`, then a `DESIGN.md` is **natural-language instructions an agent will follow**. Installing
this connector wires **unvetted third-party prompt content** into the frontend workstream, under a
filename that reads like inert configuration. That is an **indirect prompt-injection surface**, and it
lands squarely on the rule CCC already holds from K421: **the model is not a security boundary** —
content the agent merely reads can redirect what it does. `21st.dev` is the same shape with a
marketplace in front of it, and a commercial one.

**Verdict: `wont_wire` at runtime; LEAD retained.** Install stays human-gated. The specific gate is no
longer "check the licence" — it is **"decide whether to let third-party prose into the context as a
contract."** No clone, no install.

**Why it is still worth tracking.** The *shape* remains the interesting part: **a design token file
as an MCP-served artifact** is a contract the agent can be held to, the same movement as
`@concepts/schema-bound-mcp-tool-surface.md` — move the constraint out of the prompt and into
something checkable. The safe version of this idea is a `DESIGN.md` the project **authors itself** and
serves locally; the unsafe version is one fetched from a third party and followed on trust.

## Remaining questions before any install

- Read the actual terms of service on both reachable connectors (a terms *link* existing is not a
  terms *read*).
- Confirm the served `DESIGN.md` is versioned and attributable, so a change to it is detectable.
- `uiverse.io` unverified — 403 to a scripted probe.
- Whether registry content is served live or vendored (catalog-churn risk — see
  `@concepts/mcp-server-catalog-curation.md`).

## Snippets

> "Agent-written frontends drift because the agent has no design contract." [Source:
> `@briefs/2026-10-07_k284-ccc-design-registries.md`]

## Dead Ends

- **Not installed, not cloned.** Recorded as a lead so the next frontend-facing workstream does not
  rediscover it.
