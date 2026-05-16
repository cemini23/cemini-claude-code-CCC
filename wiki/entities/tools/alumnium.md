---
title: "alumnium — AI-native end-to-end testing wrapper for browser automation (MCP server)"
type: entity
category: tool
tags: [entity, tool, e2e-testing, mcp-server, browser-automation, ai-native, k44, go-phase-0-2026-05-14, changeanalysis-cost-unverified]
keywords: [alumnium, accessibility-tree, mcp-server, claude-mcp-add, playwright, selenium, appium, mit-license, ui-validation, stdio-transport, 13-llm-providers, change-analysis]
related:
  - entities/tools/claude-code.md
maturity: validated
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @entities/tools/claude-code.md — installs as a Claude Code MCP server (`claude mcp add alumnium`); AI-native E2E testing surface
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A TypeScript+Python testing-infrastructure wrapper around Playwright/Selenium/Appium that compacts application accessibility trees and routes them to LLMs for autonomous UI interaction. **Installs as an MCP server (`claude mcp add alumnium`)**. MIT, claimed 655 stars, last commit 2026-05-13 per K44 doc-level eval.

K44 verdict: **Adopt**. Primary fit: CCC. Cross-route: Cemini-financial (AI-driven UI validation on trading dashboards).

## Narrative

The architectural pivot is the accessibility-tree-to-LLM routing: instead of brittle CSS selectors, the LLM operates on a semantic DOM compactified by ARIA roles. This eliminates the rigidity that has historically made E2E tests fragile during UI refactors.

### Phase-0 audit verdict (2026-05-14): GO

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `alumnium-hq/alumnium` resolved; 24 contributors; created 2024-10-28 (~18mo old) |
| G1 | Star + maturity | **PASS** | 665★ (vs claimed 655, +10 minor drift), 72 forks (ratio 9.2 — healthy), 20 open issues, last commit 1h before audit (highly active) |
| G2 | License | **PASS** | MIT verbatim (LICENSE.md), copyright Alexey Rodionov + Tatiana Shepeleva |
| G3 | MCP server contract | **PASS** | `bin: alumnium` CLI in `package.json`; `alumnium mcp` subcommand registers stdio transport via @modelcontextprotocol/sdk; `claude mcp add alumnium` works; 13 LLM providers supported (Anthropic default, Claude Haiku 4.5) |
| G4 | LLM cost-per-test | **CONDITIONAL** | 8 retries default + 90s timeout. Cost-per-test **undocumented** (no README budget guidance). Each `.do()` / `.check()` / `.get()` = 1+ LLM call. Client-side caching (sqlite) but no LLM-level token cache visible |
| G5 | Accessibility-tree compaction | **CONDITIONAL** | Trees extracted via CDP (Chromium) / XCUITest (iOS) / UIAutomator2 (Android) → XML. **No compaction benchmarks shipped** — the "10-100x compaction" claim from K44 is unverified at source. Interactive semantics preserved (clickable/fillable/focusable roles) |
| G6 | `changeAnalysis` parameter | **PASS-but-uncosted** | Found at `startMcpTool.ts`: boolean, default `false`, documented as "enable UI changes analysis agent". **Latency tradeoff still undocumented** — K44 NEEDS VERIFICATION flag stands. Cost impact unknown. On/off toggle only |
| G7 | Trading-dashboard E2E fit | **PASS** | Modal/popover, form validation, drag-drop, file-upload, real-time DOM updates all supported. `WaitForElementTool` + retry logic handles dynamic content. **High-frequency tick environment unprofiled** — changeAnalysis recommended OFF by default for sub-second redraws |
| G8 | Failure-mode mitigation | **PASS** | Retry (8 attempts, configurable backoff), no global state (per-instance isolation), structured logging (logtape + OpenTelemetry). No LLM-failure fallback path (no CSS-selector heuristic on LLM error) |

**Verdict: GO** for CCC-wiki adoption + Cemini-financial trading-dashboard E2E.

### Critical caveats for Cemini-financial adoption

1. **Default changeAnalysis OFF** — Enable only for explicit change-detection tests (modal-appear, validation-error-text). For high-frequency price-tick dashboards, leave OFF or test cost impact first.
2. **Cost baseline missing** — Publish typical test cost ($0.01-0.05 with Haiku, 3-15 retries per action, ~200 tokens/tree) before opening to wider Cemini test-suite adoption.
3. **Deterministic seed support is incomplete** — Code comment indicates seed param is deprecated/missing in LangChain integration. Tests are inherently non-deterministic — rely on retry budget + per-test timeout (5 min suggested) as safety rail.
4. **Compaction benchmarks unverified** — K44's "accessibility tree to LLM" innovation claim has no quantitative backing in repo. Should profile a real Cemini dashboard tree to measure actual token savings vs raw HTML.

**Cross-route to Cemini-financial**: trading-dashboard front-end (React, per K44 alumnium reasoning) historically lacks deep E2E coverage; alumnium closes that gap **subject to the caveats above**.

## Snippets

> "Alumnium introduces a paradigm shift in end-to-end testing by compacting application accessibility trees and routing them to LLMs for autonomous interaction. By operating as an MCP server (claude mcp add alumnium), it integrates flawlessly into the CCC-wiki's terminal-native orchestration environment."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶85]
