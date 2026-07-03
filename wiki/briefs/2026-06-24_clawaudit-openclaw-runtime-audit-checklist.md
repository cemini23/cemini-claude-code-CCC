---
title: CLAWAUDIT — OpenClaw runtime audit checklist
type: brief
tags: [brief, openclaw, static-analysis, agent-security]
created: 2026-06-24
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
updated: 2026-06-29
---

## Target

hands-on | local agent fork audit | CCC OpenClaw / Claude Code sandbox stacks

## Summary

arXiv:2606.21071: local agents are **privileged runtimes**. CLAWAUDIT Semgrep/CodeQL rules lift OpenClaw advisory recall to **67–75%** but require **manual triage** before CI enforcement.

## Body

### Audit ladder (local agent install)

1. **Supply chain** — SkillSpector + DefenseClaw on skills/MCP manifests
2. **Runtime source** — CLAWAUDIT rules on agent fork (B1–B5 boundaries)
3. **Behavioral** — SeClaw / MalSkillBench trajectory probes
4. **Runtime guard** — AIRGuard on dispatched tool calls

### B1–B5 focus areas

| Boundary | Audit target |
|----------|--------------|
| B1 | Prompt builder — untrusted content concatenation |
| B2 | Tool dispatcher — parser → action without validation |
| B3 | Filesystem/sandbox escapes |
| B4 | Network client — SSRF, missing TLS verify |
| B5 | Handler permission gate — caller identity spoofing |

### CI gate policy

- **Do not** fail build on raw Semgrep hits alone
- Triage → severity → fix-at-boundary
- Track train/test style temporal split when writing custom rules

### Phase-0

`github.com/SRestLabUB/ClawAudit` — **CONDITIONAL-GO** (no LICENSE file on API 2026-06-24)

## Sources

- @sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
- @concepts/local-agent-runtime-audit.md
- @entities/tools/clawaudit.md
