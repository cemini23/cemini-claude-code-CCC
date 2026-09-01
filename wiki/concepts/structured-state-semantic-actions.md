---
title: "Structured state + semantic actions — GUI automation done right (CCC K321)"
type: concept
tags: [concept, gui, mcp, semantic-actions, structured-state, k321]
keywords: [ASIL, screenshot-and-click, JSON observations, semantic actions, deepest access path, GUI-MCP, 2608.26991]
related:
  - sources/arxiv-asil-structured-state-semantic-actions-2608.26991.md
  - entities/tools/hybrid-gui-mcp-osworld.md
  - entities/tools/cua.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
  - sources/arxiv-lifeplanner-geospatial-agents-2608.25039.md
  - concepts/domain-grounded-tool-orchestration.md
  - sources/arxiv-domain-grounded-tool-orchestration-2608.30696.md
maturity: draft
created: 2026-08-28
updated: 2026-09-01
---

## Relations

- `@sources/arxiv-asil-structured-state-semantic-actions-2608.26991.md`
- `@entities/tools/hybrid-gui-mcp-osworld.md`
- `@entities/tools/cua.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`
- `@concepts/domain-grounded-tool-orchestration.md`
- `@sources/arxiv-domain-grounded-tool-orchestration-2608.30696.md`

## Raw Concept

The question: when software only exposes a GUI, is screenshot-and-click the right agent interface? Answer from ASIL [Source: wiki/sources/arxiv-asil-structured-state-semantic-actions-2608.26991.md]: no — expose structured JSON observations and code-executable semantic actions through the deepest feasible access path.

## Narrative

**Screenshot-and-click is an incomplete state projection.** A screenshot is software's visible projection, not its state — it omits hidden panels, background processes, document structure, internal metadata — and forces repeated multimodal inference over a presentation layer. GUI actions are brittle and semantically weak, poorly matched to long-horizon planning.

The ASIL pattern (ADOPT policy):

1. **Structured observations** — JSON state instead of pixels (what is true, not what is rendered).
2. **Code-executable semantic actions** — "open invoice #42", not "click at (312, 88)".
3. **Deepest feasible access path per app** — API → CLI/script → service → accessibility/GUI; screenshot only as last resort.

Results: ASIL >80 with closed models at <5 actions/task vs 6.6/26.6 strict success for screenshot-click on the same tasks; exceeds LibreOffice UNO API by 28–38 strict points; matches draw.io's MCP content contract. Structured modality also trains better (SFT 58.0→72.1 on Qwen3.5-2B).

CCC application: keep `@entities/tools/hybrid-gui-mcp-osworld.md` (K245) as the MCP-first stance; do **not** add CUA-style computer-use as a default (see `@entities/tools/cua.md` — VM sandbox candidate, not a GUI-control default). When a tool surface needs automation, prefer semantic actions over pixel-clicking.

| Confidence | `[CONFIRMED]` — paper results across 15 apps / 380 tasks; pattern adoption, not reproduced in CCC |
|------------|------------|

## Snippets

> "A screenshot is not software state but only its visible projection, omitting hidden panels, background processes, document structure, and internal metadata." [Source: arXiv 2608.26991 §1]
