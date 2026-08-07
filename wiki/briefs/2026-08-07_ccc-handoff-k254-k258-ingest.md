---
title: CCC handoff — K254–K258 hardware keystore + READ + TrajDebug + AV-AIVAT + PTC
type: brief
tags: [brief, handoff, k254, k255, k256, k257, k258]
related:
  - sources/brief-k254-k258-keystore-read-trajdebug-avaivat-ptc-2026-08-07.md
  - sources/arxiv-hardware-keystores-ai-agent-signing-2608.06130.md
  - sources/arxiv-beyond-topk-read-agentic-retrieval-2608.06305.md
  - sources/arxiv-trajdebug-error-lifecycle-2608.06346.md
  - sources/arxiv-av-aivat-anytime-valid-agent-eval-2608.06362.md
  - sources/arxiv-bitter-lesson-tool-calling-2608.06370.md
  - concepts/hardware-confined-agent-signing.md
  - concepts/interpretable-agentic-document-ops.md
  - concepts/trajectory-error-lifecycle-attribution.md
  - concepts/anytime-valid-agent-eval-stopping.md
  - concepts/programmatic-vs-json-tool-calling.md
  - entities/tools/hardware-keystore-mcp-signing.md
  - entities/tools/read-agentic-document-search.md
  - entities/tools/trajdebug.md
  - entities/tools/av-aivat.md
  - entities/tools/programmatic-tool-calling-ptc.md
  - concepts/phase1-adopt-wire.md
created: 2026-08-07
---

## Summary

Five-paper ingest. Hardware-confined PKCS#11 agent signing (anonymous artifact); READ MCP document ops (MIT clone); TrajDebug error-lifecycle (MIT skeleton); AV-AIVAT anytime-valid poker eval stopping; programmatic tool calling vs JSON.

## Local

- `.local/adopts/READ` (~8.4MB MIT) — GO REFERENCE
- `.local/adopts/TrajDebug` (~4.2MB MIT skeleton, 0 `.py`) — GO shelf / wait for code
- Hardware keystore — NO-GO (anonymous only)
- AV-AIVAT / PTC — no public code

## Routing

- Prod briefs `briefs/2026-08-07_k254-*` … `k258-*` + hands-on
- Cybersec: hardware keystore + local-abliterated lab
- Poker: AV-AIVAT primary
- Atto / GuruWatcher: PTC + document-ops light steals / no-fit notes
