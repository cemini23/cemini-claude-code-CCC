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
phase_0_verdict: STEAL-FROM-CONFIRMED
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

- Trust Layer enforcement mechanism — **resolved by Phase-0.** The eval's "license gates" framing was imprecise: there is no licensing-constraint gate. The actual mechanism is a two-part *trust* gate (see Phase-0 below). Question closed.

## Phase-0 Audit (2026-05-16)

Clone: `git clone --depth 50 https://github.com/anthropics/claude-for-legal /tmp/claude-for-legal-audit/`. INSPECT-only — Steal-from tier, lighter audit.

**License — CONFIRMED Apache-2.0.** Root `LICENSE` is the verbatim Apache License 2.0 text; GitHub `licenseInfo.key` = `apache-2.0`. Apache-2.0 explicitly permits extracting and adapting patterns/code into other works (including commercial / IP-sale surfaces), with attribution and NOTICE preservation. Pattern extraction into Cemini's CCC workflow is therefore cleanly licensed.

**Provenance — CONFIRMED official Anthropic repo.** Owner is the GitHub organization `anthropics` (`isInOrganization: true`, org id `MDEyOk9yZ2FuaXphdGlvbjc2MjYzMDI4`) — the genuine Anthropic org, not a look-alike personal account. Commit authors are Anthropic staff (Matt Piccolella, Tobin South, Mark Pike). This is the real `anthropics/claude-for-legal`.

**Maturity — observed vs claimed:**
- Stars: **6,361** (eval claimed ~6,100 — accurate, slightly grown).
- Open issues: **6** (eval claimed ~6 — accurate; signals an actively curated repo).
- Repo created **2026-04-21**, last push **2026-05-16** — young (~1 month) but actively maintained; 21 commits in the shallow window, all from a small Anthropic team (14 Matt Piccolella, 3+2 Tobin South, 2 Mark Pike).
- Stack: Python + Shell (GitHub `languages`), plus Markdown/YAML/JSON plugin payloads and MCP connectors — matches "Python/Shell/MCP".

**Patterns worth extracting — all CONFIRMED present in the tree:**
1. **Managed-agent cookbooks** — `managed-agent-cookbooks/` ships five concrete cadence-job templates: `reg-monitor`, `docket-watcher`, `launch-radar`, `renewal-watcher`, `diligence-grid`. Each is a parameterized `agent.yaml` + `steering-examples.json` + a `subagents/` set of role-scoped `*.yaml` (e.g. `feed-reader.yaml` + `digest-writer.yaml`). This is exactly the template-per-monitor-class shape the eval flagged — directly transferable to Cemini's Tier-2 sweep / inbox cadence jobs.
2. **Cold-start interview** — `legal-builder-hub/skills/cold-start-interview/SKILL.md`: a profile-interview skill that front-loads context acquisition (role + 5 questions) before recommending/installing a starter pack. Confirms the eval's `/goal`-shaped pattern.
3. **Trust Layer (injection-detection guardrail)** — present, and *more concrete than the eval implied*. It is **not** a "license gate"; it is a two-part trust mechanism in `legal-builder-hub/skills/skill-installer/SKILL.md` + `references/allowlist.md`:
   - **AI-side structural trust check** — the installer runs fetch/analysis inside a *read-only subagent* (Read + WebFetch + Glob only — no Write/Bash), shows the RAW SKILL.md in full, and flags injection patterns (ignore/override/system-prompt/authority claims, external URLs, hidden unicode, out-of-scope writes) before any privileged tool is available.
   - **Admin-side allowlist gate** — an administrator-controlled `allowlist.yaml` (`mode: permissive|restrictive`, trusted registries, permitted MCP connectors) that Claude reads *before any analysis runs*, so enforcement does not depend on Claude correctly analyzing a possibly-injected skill.
   - This separation — defense-in-depth where the structural gate does not trust the AI analysis — is the genuinely valuable steal-from for `@concepts/subagent-orchestration.md`. The SKILL.md itself candidly notes the limits of AI-mediated trust, which makes the pattern more, not less, worth extracting.
4. **MCP-connector reference architecture** — `CONNECTORS.md` + `external_plugins/` document the MCP-server-bridges-to-system-of-record pattern (legal connectors Ironclad/DocuSign/Everlaw are out of Cemini scope, but the connector shape is the reference).

**Decision — STEAL-FROM-CONFIRMED.** Pattern extraction is cleared: Apache-2.0 permits it, provenance is the genuine Anthropic org, and all four target patterns concretely exist in the tree (with the Trust Layer being richer than the eval described). Do **not** adopt the suite — the legal payload, practice-area plugins, and legal connectors remain out of Cemini scope. Extract: the cookbook template structure for cadence jobs, the cold-start interview for skill bootstrapping, and especially the read-only-subagent + admin-allowlist Trust Layer for subagent orchestration. Preserve Apache-2.0 attribution/NOTICE when porting code verbatim.

## Snippets

> Practice-area plugins are deployed via the Claude Managed Agents API; MCP connectors bridge Claude Code to external systems of record (Ironclad, DocuSign, Everlaw). The legal-builder-hub ships a "Trust Layer" performing security review for hidden-content / prompt-injection detection.
[Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md]
