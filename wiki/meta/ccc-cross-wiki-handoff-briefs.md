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
  - briefs/2026-07-04_ccc-handoff-hcp-execution-control-ingest.md
  - briefs/2026-07-07_ccc-handoff-steerability-substrate-ingest.md
  - briefs/2026-07-07_ccc-handoff-hexstrike-client-orchestration-ingest.md
  - briefs/2026-07-09_ccc-handoff-adi-spellsmith-ingest.md
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/agent-data-injection-attacks.md
maturity: validated
created: 2026-06-29
updated: 2026-07-09
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
| `2026-07-04_ccc-handoff-hcp-execution-control-ingest.md` | Cybersec | HCP MCP execution-control invariants |
| `2026-07-07_ccc-handoff-steerability-substrate-ingest.md` | Cybersec | Substrate constraints for coding-agent oversight |
| `2026-07-07_ccc-handoff-hexstrike-client-orchestration-ingest.md` | Cybersec | Client-first-order tool orchestration (HexStrike) |
| `2026-07-09_ccc-handoff-adi-spellsmith-ingest.md` | Cybersec | ADI trusted/untrusted isolation + SpellSmith MCP taint mitigation |

Prod deploy briefs (K109–K139) live in gitignored `/briefs/` with discoverability stubs under `wiki/sources/brief-k*.md`.
