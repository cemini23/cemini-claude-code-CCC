---
title: CCC handoff — AI-Infra-Guard technical report ingest
type: brief
tags: [brief, ccc-handoff, agent-red-team, mcp-security]
created: 2026-07-01
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
updated: 2026-07-01
---

## Target

Claude Desktop / lazy-tool | MCP + skill vetting + agent lab design

## Summary

Cybersec-wiki ingest 2026-07-01: digest pick **R7** — arXiv **2606.31227** AI-Infra-Guard technical report. New concept **layer-paradigm agent red teaming**; entity refresh on Tencent scanner. Phase-0 **CONDITIONAL-GO** (external Docker; NOTICE §4(d) — no vendoring).

## Body

### Layer model for CCC agent stacks

| Layer | CCC touchpoint |
|-------|----------------|
| Protocol/tool | `@ccc-wiki/concepts/skill-vetting.md` + prod MCP allowlist |
| Agent behavior | Tier-2 worker sandboxes + skill install gates |
| Infrastructure | ComfyUI / local model serving in image-gen cross-wiki |
| Model | Jailbreak harness — optional on model endpoints under test |

Wiki: `@cybersecurity-wiki/concepts/layer-paradigm-agent-red-teaming.md`

### Scanner posture

- Run AI-Infra-Guard as **external Docker** breadth pass — M2 MCP-Scan + M3 Agent-Scan
- **Do not vendor** — Tencent mandatory attribution contaminates IP package
- Complements DefenseClaw + SkillSpector, not replacement

Wiki: `@cybersecurity-wiki/entities/tools/ai-infra-guard.md`

### Staged briefs

- `2026-07-01_ai-infra-guard-layer-paradigm-red-team-handoff.md`
- `2026-07-01_ai-infra-guard-external-scanner-lab-checklist.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2606-31227-ai-infra-guard-technical-report.md
- @cybersecurity-wiki/concepts/layer-paradigm-agent-red-teaming.md
- @cybersecurity-wiki/entities/tools/ai-infra-guard.md
