---
title: "ASIL — structured state + semantic actions over screenshot-click (CCC K321)"
type: source
tags: [source, arxiv, gui, mcp, semantic-actions, structured-state, k321]
keywords: [2608.26991, ASIL, screenshot-and-click, JSON observations, semantic actions, GUI-MCP, deepest access path]
related:
  - concepts/structured-state-semantic-actions.md
  - entities/tools/hybrid-gui-mcp-osworld.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@concepts/structured-state-semantic-actions.md`
- `@entities/tools/hybrid-gui-mcp-osworld.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ASIL: Replacing Screenshot-and-Click with Structured State and Semantic Actions |
| **arXiv** | 2608.26991 (2026-08-27) |
| **Authors** | Rui Xie, Lu Chen (SJTU X-LANCE + BIGAI) |
| **Code** | No public SPDX hunt hit → policy. Project page: sharryxr.github.io/ASIL |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: ADOPT — JSON observations + code-executable semantic actions over screenshot-click** (pairs K245). GUI runtime **`wont_wire`**. Keep cursor-ide-browser; do not add CUA.

Screenshot-and-click is an inefficient interface for software-operating agents: **screenshots are state-incomplete** (a visible projection, omitting hidden panels, background processes, document structure, internal metadata) and **GUI actions are brittle, semantically weak, poorly matched to long-horizon planning**.

ASIL exposes software through **structured JSON observations and code-executable semantic actions**, realized through the **deepest feasible access path** for each application (API → CLI/script → service → accessibility/GUI). Instantiated across 15 applications, 300 single-app + 80 multi-app tasks.

Results:

- ASIL > **80** with closed models, executing **<5 actions per task**.
- Same tasks under screenshot-and-click (repaired runtime, 50-step budget): **6.6 / 26.6 strict success**; 15.0 / 53.3 on an easier OSWorld-comparable band.
- Against app-native interfaces: exceeds LibreOffice UNO API by 28–38 strict points; matches draw.io's MCP content contract.
- Structured modality also suits training: SFT raises Qwen3.5-2B 58.0→72.1 and Qwen3.5-9B 66.6→80.4; on-policy RL → 74.4 / 82.2.

CCC policy: prefer structured state + semantic actions; screenshot-and-click is a fallback, not a design target. No public SPDX → `policy_wired`, no clone.

| Confidence | `[TENTATIVE]` — paper results as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "Screenshots are state-incomplete, and GUI actions are brittle, semantically weak, and poorly matched to long-horizon planning." [Source: arXiv 2608.26991 abstract]

> "ASIL reaches above 80 with closed models while executing fewer than five actions per task." [Source: arXiv 2608.26991 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.26991-asil-replacing-screenshot-and-click-with-structu.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
