---
title: "jcode — Rust multi-session AI harness with memory-vector sideagent + 1800× faster mermaid renderer"
type: entity
category: tool
tags: [entity, tool, rust, multi-session, semantic-memory, cosine-similarity, mermaid-renderer, k44, steal-from-doc-level-pending-phase-0]
keywords: [jcode, memory-sideagent, semantic-vector-recall, persistent-memory-graph, mermaid-rs-renderer, slint-ui, mit-license, ultra-low-latency]
related: []
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Rust+Slint multi-session AI harness with two notable subcomponents: a **memory-sideagent** that embeds conversational turns as semantic vectors and recalls context via cosine-similarity over a persistent memory graph (no primary-token burn for recall); and a **`mermaid-rs-renderer`** that bypasses headless-browser overhead, claimed **1800× faster** than standard pipelines. **MIT, claimed 6,100 stars**. K44 verdict: **Steal-from**.

## Narrative

Two extraction targets, both standalone-portable per the K44 eval:

1. **memory-sideagent** — pattern for offloading conversational-context recall to a vector store rather than feeding it back through primary-LLM tokens. Saves $/conversation in long-running agent loops.
2. **mermaid-rs-renderer** — replaces Puppeteer/headless-Chrome dependency for diagram rendering. Tactical fit: CCC-wiki documentation and Claude-Code-emitted diagrams currently depend on browser-launch overhead.

**Phase-0 gates**:
- G1: Star + maturity verification (6,100 stars high for solo maintainer "1jehuang" — verify authenticity via `gh api repos/1jehuang/jcode`)
- G2: License (MIT confirmed)
- G3: Benchmark mermaid-rs-renderer claim (1800× faster) — set a real baseline before quoting it
- G4: Memory-sideagent isolation — confirm extractable without pulling in Slint UI or Rust app skeleton
- G5: SVG compilation in headless Linux environments (K44 NEEDS VERIFICATION) — required for server-side use

**Skepticism elevated**: 6,100 stars from "1jehuang" warrants explicit Phase-0 star-authenticity verification (star/fork ratio, issue ratio, contributor count). Same red-flag pattern as geo-seo-claude before its Phase-0 cleared.

## Snippets

> "Its defining feature is an advanced 'memory sideagent' that embeds conversational turns as semantic vectors, utilizing cosine similarity checks against a persistent memory graph to recall context without burning primary tokens. Furthermore, its custom mermaid-rs-renderer bypasses headless browser overhead, generating diagrams 1800x faster than standard pipelines."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶265]
