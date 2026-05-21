---
title: "defenseclaw — security governance for agentic AI (Cisco, Apache-2.0)"
type: entity
tags: [tool, security-governance, agentic-ai, mcp-scanner, skill-scanner, admission-control, cisco, cross-wiki-route]
keywords: [defenseclaw, cisco, agent-security, mcp-scanner, skill-scanner, codeguard, admission-control, go-gateway, sidecar]
related:
  - concepts/skill-vetting.md
  - concepts/agent-vm-sandboxing.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/mcp-servers/anthropic-skills.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md"
---

## Relations

- @concepts/skill-vetting.md — defenseclaw is the automated realisation of CCC's manual Phase-0 skill audit checklist
- @concepts/agent-vm-sandboxing.md — admission control + sandboxing are complementary; defenseclaw gates, agent-VM contains
- @entities/patterns/tier1-tier2-agent-model.md — defenseclaw's admission-control model is Tier-2 scope enforcement for external MCP servers
- @entities/mcp-servers/anthropic-skills.md — defenseclaw's skill scanner directly audits the SKILL.md surface this page covers
- @osint-wiki/sources/tool-evaluation-wiki-fit-2026-05-15.md (cross-wiki source)

## Raw Concept

Cross-wiki brief routed from the OSINT 52-URL "Tool Evaluation and Wiki Fit" eval (2026-05-15). `cisco-ai-defense/defenseclaw` (Apache-2.0, 654★) is a Go gateway sidecar providing security governance for agentic AI workloads: MCP server scanning, skill scanning, admission control over external MCP servers, and CodeGuard static checks. Direct exemplar for how Claude Code tools/skills should be audited and sandboxed before local execution.

## Narrative

### What defenseclaw does

A Go-based security gateway that sits between Claude Code (or any agentic AI runtime) and its tool/skill/MCP-server surface:

- **MCP scanner** — inspects MCP server manifests for known-dangerous capability patterns before allowing connection
- **Skill scanner** — audits SKILL.md files for malicious patterns (secrets exfiltration, unsafe deserialization, prompt injection vectors)
- **Admission control** — gates external MCP server access; only servers that pass the scanner are allowed to connect
- **CodeGuard static checks** — secrets detection, unsafe deserialization patterns, prompt injection surfaces in tool code

### Why CCC cares

defenseclaw operationalises CCC's manual Phase-0 skill-vetting checklist (@concepts/skill-vetting.md) as infrastructure:

1. **Skill scanner → automated Phase-0 step 1-3** — the scanner checks for the same failure modes CCC's manual checklist covers (license, provenance, malicious patterns)
2. **MCP scanner → admission control** — the MCP equivalent of skill vetting; CCC currently has no automated MCP-server audit path
3. **CodeGuard → pre-commit hook reference** — static checks for secrets/unsafe patterns are directly adaptable as a Claude Code Git pre-commit hook

### Adoption posture

Apache-2.0 license (verified via OSINT eval). Clean for adoption. However, defenseclaw is Cisco-maintained and may carry Cisco-specific assumptions about infrastructure. Phase-0 audit recommended before installing as a sidecar — but the scanner/CodeGuard patterns are extractable regardless.

[CONFIRMED] — Apache-2.0, 654★, actively maintained (per OSINT eval).
