---
title: agentgateway — OSS agentic proxy for MCP / AI agents
type: entity
tags: [tool, mcp, gateway, proxy, apache, k190]
keywords: [agentgateway, solo.io, Apache-2.0, MCP proxy, AgentCore peer]
related:
  - sources/arxiv-scalable-mcp-cloud-gateway-2607.15593.md
  - concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md
  - entities/tools/lazy-tool.md
  - concepts/mcp-context-optimization.md
  - sources/arxiv-agentic-ai-5g6g-survey-2607.16066.md
  - concepts/slm-agent-orchestration-gateway.md
maturity: draft
created: 2026-07-20
updated: 2026-07-31
wire_status: wont_wire
wire_target: "REFERENCE MCP proxy study — not prod/TipDrop LIVE"
---

## Relations

- `@sources/arxiv-scalable-mcp-cloud-gateway-2607.15593.md` — cites agentgateway among cloud MCP peers
- `@concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md` — pattern this implements in OSS form
- `@entities/tools/lazy-tool.md` — client-side peer (different hop)
- `@concepts/mcp-context-optimization.md` — token/cost context

## Raw Concept

Phase-0 for `github.com/agentgateway/agentgateway` after K190 ingest. Paper's Alibaba gateway is closed; this is the open peer (~3.9k★, Apache-2.0, ~42MB shallow clone).

## Narrative

### Phase-0

| Check | Result |
|-------|--------|
| License API | **Apache-2.0** [CONFIRMED] |
| Maturity | Active (pushed 2026-07-20); high star count |
| Size | ~42MB depth-1 clone — under 500MB adopt budget |
| Failure mode | Fleet proxy blast radius — do not put on prod path without operator review |
| Local | `.local/adopts/agentgateway` |

### Verdict

**CONDITIONAL-GO (REFERENCE)** — clone for study of MCP proxy / session routing. **Do not** wire into Cemini prod or TipDrop LIVE without a dedicated adopt ticket. Complements lazy-tool (client) rather than replacing it.

## Dead Ends

- Treating Alibaba paper code as available — it is not; agentgateway is a *related* OSS project, not the paper artifact.
