---
title: "alumnium — AI-native end-to-end testing wrapper for browser automation (MCP server)"
type: entity
category: tool
tags: [entity, tool, e2e-testing, mcp-server, browser-automation, ai-native, k44, adopt-doc-level-pending-phase-0]
keywords: [alumnium, accessibility-tree, mcp-server, claude-mcp-add, playwright, selenium, appium, mit-license, ui-validation]
related: []
maturity: adopt-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A TypeScript+Python testing-infrastructure wrapper around Playwright/Selenium/Appium that compacts application accessibility trees and routes them to LLMs for autonomous UI interaction. **Installs as an MCP server (`claude mcp add alumnium`)**. MIT, claimed 655 stars, last commit 2026-05-13 per K44 doc-level eval.

K44 verdict: **Adopt**. Primary fit: CCC. Cross-route: Cemini-financial (AI-driven UI validation on trading dashboards).

## Narrative

The architectural pivot is the accessibility-tree-to-LLM routing: instead of brittle CSS selectors, the LLM operates on a semantic DOM compactified by ARIA roles. This eliminates the rigidity that has historically made E2E tests fragile during UI refactors.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/alumnium-hq/alumnium`)
- G2: License (MIT confirmed)
- G3: `claude mcp add alumnium` smoke test on a known target
- G4: `changeAnalysis` parameter latency on high-frequency UI updates (K44 NEEDS VERIFICATION)
- G5: Cost-per-test (LLM call per test step is the price; need acceptable $/run)

**Cross-route to Cemini-financial**: trading-dashboard front-end (React, per K44 alumnium reasoning) historically lacks deep E2E coverage; alumnium would close that gap.

## Snippets

> "Alumnium introduces a paradigm shift in end-to-end testing by compacting application accessibility trees and routing them to LLMs for autonomous interaction. By operating as an MCP server (claude mcp add alumnium), it integrates flawlessly into the CCC-wiki's terminal-native orchestration environment."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶85]
