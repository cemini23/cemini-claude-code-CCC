---
title: "claude-for-legal — Anthropic's official Claude Code / MCP plugin suite for the legal vertical"
type: entity
tags: [entity, tool, anthropic-official, claude-code-plugin-pack, mcp-connectors, managed-agents, vertical-suite, steal-from, ccc-primary-fit, cross-wiki-route-2026-05-16]
keywords: [claude-for-legal, managed-agent-cookbooks, cold-start-interviews, trust-layer, legal-builder-hub, hidden-content-injection-detection, claude-managed-agents-api, ironclad-docusign-everlaw-connectors, apache-2-license, practice-area-plugins]
related:
  - concepts/subagent-orchestration.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/commands/plugin.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md"
---

## Relations

- @concepts/subagent-orchestration.md — the Trust Layer security review is a guardrail pattern for orchestrated subagents; managed-agent cookbooks are a scheduled-orchestration template
- @entities/patterns/full-prompt-goal-template.md — "cold-start interviews" map onto the `/goal` single-shot meta-prompt: learn the institutional playbook before executing
- @entities/mcp-servers/anthropic-skills.md — practice-area plugins are SKILL.md-style packaged distributions; reference example of a vertical plugin pack
- @entities/commands/plugin.md — practice-area plugins install via the `/plugin` marketplace path
- @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — cross-wiki source (tool-eval ingest verdict)

## Raw Concept

Cross-routed from OSINT workspace tool-eval ingest 2026-05-16. `claude-for-legal` is Anthropic's official suite of Claude Code / MCP plugins targeting the legal vertical. Apache-2.0; ~6,100 stars / 6 open issues. Stack: Python / Shell / Markdown / JSON / MCP. K-cycle tool-eval verdict: **STEAL-FROM**, CCC primary fit — the legal-domain payload is out of scope for any Cemini wiki, but several of its orchestration patterns are directly transferable to how Cemini operates Claude Code.

URL: https://github.com/anthropics/claude-for-legal

## Narrative

The legal content itself is not relevant to Cemini. What is relevant — and the reason this page exists in CCC — are four reusable Claude Code orchestration patterns that Anthropic productized here and that CCC should extract rather than adopt wholesale.

### Patterns worth extracting

1. **Managed-agent cookbooks** — templates for scheduled, "eyes-on-the-feed" workflows: regulatory-feed monitors, docket watchers. These are recurring, low-touch agents that wake on a cadence, scan an external source, and surface deltas. Maps directly onto Cemini's own cadence-driven jobs (Tier-2 arXiv sweeps, inbox checks). The cookbook framing — a parameterized template per monitor class rather than a bespoke prompt each time — is the steal-from value.

2. **Cold-start interviews** — a workflow that *learns an institutional playbook before executing* a complex review. Rather than assuming the operator's conventions, the agent first interviews to capture the institution's standards, then executes against them. This is the same shape as Cemini's `/goal` single-shot meta-prompt (`@entities/patterns/full-prompt-goal-template.md`) and SKILL.md-driven orchestration: front-load the context acquisition so the execution pass is deterministic. For CCC, the cold-start interview is a pattern to fold into how new skills bootstrap.

3. **Trust Layer (legal-builder-hub)** — a security-review layer that performs hidden-content / prompt-injection detection on inbound material. As a guardrail for subagent orchestration this is the most directly portable piece: a subagent that ingests external documents should run them through an injection-detection pass before the content reaches a privileged context. CCC's `@concepts/subagent-orchestration.md` Tier-1/Tier-2 model is the natural home for this guardrail.

4. **Practice-area plugins via the Claude Managed Agents API** — vertical plugins (one per practice area) deployed through Anthropic's Managed Agents API, plus MCP connectors to external systems (Ironclad, DocuSign, Everlaw). The connector pattern — an MCP server bridging Claude Code to a third-party system of record — is the reference architecture; the specific legal connectors are not relevant to Cemini.

### Verdict

STEAL-FROM. Do **not** adopt the suite — the legal payload, practice-area plugins, and legal connectors are entirely out of Cemini scope. Extract the four patterns above: managed-agent cookbooks for cadence jobs, cold-start interviews for skill bootstrapping, the Trust Layer injection guardrail for subagent orchestration, and the MCP-connector reference architecture. Anthropic-official provenance + 6,100 stars makes the patterns trustworthy as a reference; the low open-issue count (6) signals an actively curated repo.

### Open questions

- `[NEEDS VERIFICATION 2026-05-16]` — exact mechanism of the Trust Layer's "license gates": how the legal-builder-hub Trust Layer enforces licensing constraints on hidden-content detection is not documented in the eval. Resolve via repo README / source before relying on the gate as a transferable pattern.

## Snippets

> Practice-area plugins are deployed via the Claude Managed Agents API; MCP connectors bridge Claude Code to external systems of record (Ironclad, DocuSign, Everlaw). The legal-builder-hub ships a "Trust Layer" performing security review for hidden-content / prompt-injection detection.
[Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md]
