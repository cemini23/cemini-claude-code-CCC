---
title: CCC cross-wiki handoff briefs (wiki/briefs/)
type: concept
tags: [meta, brief, cross-wiki, handoff]
keywords: [cybersec-handoff, agent-security, ingest-batch]
related:
  - concepts/cross-wiki-routing.md
  - concepts/seclaw-agent-security-evaluation.md
  - briefs/2026-06-24_ccc-handoff-agent-security-ingest-batch.md
  - briefs/2026-06-24_tool-guard-isolated-planning-prod-mcp-handoff.md
  - briefs/2026-06-24_clawaudit-openclaw-runtime-audit-checklist.md
  - briefs/2026-06-24_portico-lingering-authority-coding-agent-handoff.md
  - briefs/2026-06-24_igac-intent-governed-tool-auth-handoff.md
  - briefs/2026-06-25_agent-phishing-tier2-eval-checklist.md
  - briefs/2026-06-25_agentic-red-team-secure-architecture-handoff.md
  - briefs/2026-06-26_ccc-handoff-sharelock-toxicity-ingest.md
  - briefs/2026-06-27_ccc-handoff-aohp-toolbench-craas-ingest.md
  - briefs/2026-06-03_k97-ccc-agent-harness-from-osint.md
  - briefs/2026-07-01_ccc-handoff-ai-infra-guard-technical-report-ingest.md
  - briefs/2026-07-02_ccc-handoff-robust-to-confidence-orchestration-ingest.md
  - briefs/2026-07-03_ccc-handoff-cognitive-heuristics-vuln-detection-ingest.md
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
maturity: validated
created: 2026-06-29
updated: 2026-07-03
---

## Relations

- `@concepts/cross-wiki-routing.md` — brief vs stub discipline
- `@concepts/seclaw-agent-security-evaluation.md` — security eval anchor

## Raw Concept

Catalog of **durable handoff briefs** staged under `wiki/briefs/` (distinct from gitignored `briefs/` prod drops). These route cybersec/OSINT ingests into CCC harness vocabulary without duplicating primary wiki pages.

## Narrative

| Brief | Source wiki | Topic |
|-------|-------------|-------|
| `2026-06-03_k97-ccc-agent-harness-from-osint.md` | OSINT | K97 agent harness expansion |
| `2026-06-24_ccc-handoff-agent-security-ingest-batch.md` | Cybersec | Five-paper security batch |
| `2026-06-24_tool-guard-isolated-planning-prod-mcp-handoff.md` | Cybersec | MCP planner quarantine |
| `2026-06-24_clawaudit-openclaw-runtime-audit-checklist.md` | Cybersec | OpenClaw runtime audit |
| `2026-06-24_portico-lingering-authority-coding-agent-handoff.md` | Cybersec | Subgoal authority revocation |
| `2026-06-24_igac-intent-governed-tool-auth-handoff.md` | Cybersec | Session intent narrowing |
| `2026-06-25_agent-phishing-tier2-eval-checklist.md` | Cybersec | Tier-2 phishing eval |
| `2026-06-25_agentic-red-team-secure-architecture-handoff.md` | Cybersec | Red-team architecture |
| `2026-06-26_ccc-handoff-sharelock-toxicity-ingest.md` | Cybersec | Sharelock toxicity |
| `2026-06-27_ccc-handoff-aohp-toolbench-craas-ingest.md` | Cybersec | AOHP + ToolBench-X + CraaS |
| `2026-07-01_ccc-handoff-ai-infra-guard-technical-report-ingest.md` | Cybersec | AI-Infra-Guard layer-paradigm red team |
| `2026-07-02_ccc-handoff-robust-to-confidence-orchestration-ingest.md` | Cybersec | Robust-TO confidence tool routing |
| `2026-07-03_ccc-handoff-cognitive-heuristics-vuln-detection-ingest.md` | Cybersec | Cognitive bias in LLM vuln scanners |

Prod deploy briefs (K109–K137) live in gitignored `/briefs/` with discoverability stubs under `wiki/sources/brief-k*.md`.
