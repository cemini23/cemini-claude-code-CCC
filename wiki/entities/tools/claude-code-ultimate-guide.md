---
title: claude-code-ultimate-guide — 24k-line CC reference + 28-CVE catalog + 655 malicious-skill patterns
type: entity
tags: [tool, reference, claude-code, cve-catalog, skill-vetting, cc-by-sa, defensive-security]
keywords: [claude-code-ultimate-guide, FlorianBruniaux, 28 cve catalog, 655 malicious skill patterns, cc-by-sa-4.0, agentic security]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/hooks-for-automation.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — host harness this guide documents
- `@entities/mcp-servers/anthropic-skills.md` — the malicious-skill patterns vet skills before install
- `@concepts/hooks-for-automation.md` — the CVE catalog informs PreToolUse hook design

Cross-wiki: `@cybersecurity-wiki/entities/tools/claude-code-ultimate-guide.md` carries the cross-routed cybersec adoption notes. `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` is the eval origin (URL 17 in that batch).

## Raw Concept

`github.com/FlorianBruniaux/claude-code-ultimate-guide` — CC-BY-SA-4.0. ~24,000-line reference guide for Claude Code spanning 7 modules + 181 templates + an MCP search subsection. Two databases inside the guide are uniquely valuable:

- **28-CVE catalog** specific to AI coding assistants
- **655 malicious-skill-pattern detection rules** — pre-built signatures for catching skill-injection / supply-chain compromise in skill libraries

## Narrative

Most "Claude Code reference" repos are README-grade — install steps, basic config, a few examples. claude-code-ultimate-guide is the outlier: 24k lines, organized into modules, with two cybersec-grade databases that warrant separate treatment.

### What's in the guide (selected)

- **Module 1-7** — installation, configuration, MCP wiring, skill authoring, hook recipes, slash-command authoring, advanced workflow patterns
- **181 templates** — TDD prompt templates, code-review templates, refactor templates, doc-generation templates
- **MCP search subsection** — patterns for evaluating + selecting MCP servers
- **28-CVE catalog** — vulnerabilities specific to AI coding assistant deployments (prompt injection, tool abuse, credential exfiltration, etc.)
- **655 malicious-skill-pattern signatures** — heuristic rules for detecting supply-chain attacks on skill libraries (typosquatting, install-time exfiltration, prompt poisoning, etc.)

### Cemini's adoption posture

Cemini does not depend on the guide as a reference (CCC's own pages and Anthropic's official docs cover Cemini's needs). The guide is referenced in CCC because:

1. **The CVE catalog and malicious-skill patterns are unique** — no other source consolidates them at that scale. Useful as a Phase-0 input when auditing a third-party skill or MCP server.
2. **Cemini's `@entities/mcp-servers/anthropic-skills.md` Phase-0 audit pattern** can borrow the 655 signatures as a checklist.
3. **The CC-BY-SA-4.0 license matters** — Cemini can extract CVE/pattern *identifiers* and *categorical understanding* freely; full database files copied verbatim trigger SA copyleft. Don't replicate the databases into Cemini repos; cite the URL and reference specific CVE IDs / pattern numbers.

### License caveat (load-bearing)

CC-BY-SA-4.0 Share-Alike on documentation means:
- ✅ Fair use: extracting CVE IDs, learning the patterns, applying the principles
- ❌ Triggers SA copyleft: copying full database files into Cemini's wiki

Practical rule: treat the guide as a reference-only source. Phase-0 audits cite specific CVE numbers and pattern IDs; never copy 50+ entries verbatim.

### Where to use it

- **Skill audits** (`@entities/mcp-servers/anthropic-skills.md` Phase-0) — cross-check candidate skill against the 655 patterns
- **Hook design** (`@concepts/hooks-for-automation.md`) — PreToolUse hook patterns informed by the CVE catalog
- **MCP-server eval** — the MCP search subsection provides selection criteria

## Dead Ends

- **Replicating the database into Cemini wiki pages** — triggers SA copyleft. Reference by URL and ID.
- **Treating it as canonical Anthropic docs** — it's a community reference; useful but unofficial. Anthropic's `docs.claude.com/en/docs/claude-code` is the source-of-truth on harness behavior.
