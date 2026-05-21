---
title: "src-hunter-skill — largest SKILL.md in the wild (305 payloads, MIT)"
type: entity
tags: [skill, skill-engineering, skill-md-design, bug-bounty, payload-library, cross-wiki-route]
keywords: [src-hunter-skill, myurikanao, skill-md-engineering, payload-library, bug-bounty, wasm-re, frida, jshookmcp]
related:
  - entities/mcp-servers/anthropic-skills.md
  - concepts/skill-vetting.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-19url-2026-05-20.md"
---

## Relations

- @entities/mcp-servers/anthropic-skills.md — src-hunter-skill is the extreme-scale exemplar of the SKILL.md spec this page documents
- @concepts/skill-vetting.md — src-hunter-skill's scale (305 payloads, 19 playbooks) stress-tests the Phase-0 audit checklist's scalability assumptions
- @osint-wiki/sources/multi-wiki-tool-eval-19url-2026-05-20.md (cross-wiki source)

## Raw Concept

Cross-wiki brief routed from OSINT K55 (19-URL eval, May 2026). `MyuriKanao/src-hunter-skill` (MIT) is the largest single Claude Code skill in the wild by payload count — 305 structured payloads, 19 attack playbooks, 263 WAF bypass variants, integrated MCP server (`jshookmcp`). The offensive-security content is cybersec-wiki's domain; the SKILL.md engineering patterns are CCC's.

## Narrative

### Scale (by the numbers)

- **305 structured payloads** — organised by vulnerability class
- **19 attack playbooks** — step-by-step workflows for specific bug-bounty scenarios
- **263 WAF bypass variants** — parameterised evasion techniques
- **Integrated MCP server** — `jshookmcp` for browser manipulation, Frida memory validation, WASM reverse engineering
- **Opus tier** — designed for Claude Opus's reasoning depth

### Why CCC cares (SKILL.md engineering, not offensive content)

src-hunter-skill is a design exemplar for CCC's SKILL.md engineering practices:

1. **Payload library structure** — how to organise 305 structured payloads inside a SKILL.md without making the file unparseable. The organisational pattern (by vulnerability class → by technique → by variant) is reusable for any large skill.
2. **MCP server integration** — how a skill surfaces an MCP server (`jshookmcp`) as a skill-side capability. The integration pattern (skill declares MCP dependency → MCP server provides browser/RE primitives → skill orchestrates them) is the reference architecture.
3. **Maximum skill scope before fragmentation** — at 305 payloads + 19 playbooks, does the skill remain coherent or should it have been split into multiple skills? Studying the boundary informs CCC's own skill-scoping decisions.
4. **Playbook structure** — 19 step-by-step workflows that combine payloads, WAF bypasses, and MCP-server tool calls into coherent attack narratives. The playbook format is generalisable to any multi-step Claude Code skill.

### Constraint

MIT license (verified via K55 eval). The SKILL.md structural patterns are extractable; the offensive-security payloads themselves are cybersec-wiki's domain. CCC should study the engineering, not the exploit content.

[CONFIRMED] — MIT license verified via K55 cross-wiki source.
