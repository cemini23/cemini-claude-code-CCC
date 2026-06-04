---
title: SeClaw — trajectory-aware agent security eval (K98)
type: concept
tags: [concept, agent-security, evaluation, seclaw, k98]
keywords: [2606.02302, seclaw, trajectory, docker-testbed, mcp-security]
related:
  - sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md
  - concepts/skill-vetting.md
  - entities/tools/defenseclaw.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - concepts/mcp-server-catalog-curation.md
  - "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
  - "@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md"
  - sources/trading-posts-compilation-18-2026-06-04.md
maturity: draft
created: 2026-06-04
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
---

## Relations

- `@sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md` — arXiv provenance
- `@concepts/skill-vetting.md` — manual Phase-0 checklist SeClaw automates
- `@entities/tools/defenseclaw.md` — Cisco admission-control parallel
- `@entities/tools/lazy-tool.md` — harness surface to regression-test
- `@entities/tools/conductor-mcp.md` — write-tool policy target
- `@osint-wiki/concepts/seclaw-agent-security-evaluation.md` — OSINT canon
- `@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md` — eval methodology depth

## Raw Concept

arXiv 2606.02302 (K98 inbox): **spec-driven security task synthesis** + docker testbed for **trajectory-aware** scoring of tool-using agents — unsafe intermediate steps, not just final-answer politeness.

## Narrative

| Design choice | CCC implication |
|---------------|-----------------|
| Risk specs → tasks | Map to `@concepts/skill-vetting.md` rows before MCP GO |
| Trajectory scoring | Stop hooks + tool audit logs matter; final message "looks fine" is insufficient |
| Docker testbed | Laptop-only regression — not prod dependency |

### Adoption posture

| Check | Status |
|-------|--------|
| Repo | `github.com/seclaw-eval/seclaw-eval` |
| License | **Phase-0 pending** [NEEDS VERIFICATION 2026-06-04] |
| Verdict | **CONDITIONAL-GO** — run against conductor + lazy-tool policies before expanding write MCP |
| vs defenseclaw | SeClaw = benchmark; defenseclaw = runtime gate — complementary |

**Do not** conflate with EMS/trading RBAC audits (OSINT `@concepts/ems-execution-security-gaps.md` scope).

## Snippets

> "trajectory-aware assessment of unsafe actions beyond final responses"
> — [Source: @osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md]
