---
title: IGAC intent-governed tool auth — prod-mcp handoff
type: brief
tags: [brief, authorization, mcp, igac, least-privilege]
created: 2026-06-24
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
updated: 2026-06-29
---

## Target

hands-on | prod-mcp / lazy-tool | multi-integration copilots

## Summary

arXiv:2606.22916: static OAuth scopes are necessary but insufficient. **IGAC** narrows manifest + validates payloads against session **intent certificate**. OpenPort pilot: static auth still allowed **85.71%** of high-risk requests.

## Body

### Three-layer auth stack

```
Static credential scope (can integration call tool?)
  → Intent certificate (does current user request justify tool?)
    → Runtime guard (AIRGuard / ChainCaps on execution)
```

### Implementation checklist

1. Parse user turn → **intent certificate** (monotone — only narrows)
2. Filter MCP manifest / tool list exposed to planner
3. Pre-invoke **intent–tool–payload** consistency check
4. Audit log: intent_id + tool + args hash

### prod-mcp mapping `[TENTATIVE]`

| IGAC component | lazy-tool analog |
|----------------|------------------|
| Intent certificate | Per-chat scope derived from user message + engagement brief |
| Manifest filter | `allowed_tools` intersection with intent |
| Payload check | prod-mcp param validator |

### Phase-0

IGAC on OpenPort — **Reference** (no standalone OSS repo 2026-06-24)

## Sources

- @sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md
- @concepts/intent-governed-tool-authorization.md
