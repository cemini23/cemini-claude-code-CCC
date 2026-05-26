---
title: "Skill vetting — Phase-0 audit checklist for third-party Claude Code skills"
type: concept
tags: [concept, claude-code, skills, phase-0, audit, methodology]
keywords: [skill-vetting, phase-0-audit, skill-md, malicious-skill, catalog-churn, instructa-removal, do-not-depend-on-catalog]
related:
  - entities/mcp-servers/anthropic-skills.md
  - entities/tools/claude-code-ultimate-guide.md
  - entities/commands/plugin.md
  - concepts/agent-vm-sandboxing.md
  - entities/tools/defenseclaw.md
  - entities/skills/src-hunter-skill.md
  - concepts/code-as-agent-harness.md
  - entities/tools/open-design.md
  - concepts/tools-we-dont-use.md
  - concepts/html-as-claude-code-output-format.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - entities/tools/ai-engineering-roadmap.md
  - entities/tools/agents-best-practices.md
  - entities/tools/cursor-community-plugins.md
  - entities/tools/everything-claude-code.md
  - concepts/claude-premortem-skill.md
  - sources/k67-explorax-100-repos-reference.md
  - entities/tools/centaur.md
  - entities/tools/google-eng-practices.md
  - entities/tools/purple-cli.md
maturity: draft
created: 2026-05-17
updated: 2026-05-26
---

## Relations

- @entities/mcp-servers/anthropic-skills.md — parent entity; this concept extracts the audit checklist embedded in that page into its own concept-level write-up
- @entities/tools/claude-code-ultimate-guide.md — source of the 28-CVE catalog + 655 malicious-skill patterns referenced in step 4
- @entities/commands/plugin.md — install path; vetting happens before `/plugin install <name>`
- @concepts/agent-vm-sandboxing.md — first-run isolation surface for unvetted skills
- @entities/tools/defenseclaw.md — automated realisation of this checklist as infrastructure (MCP scanner, skill scanner, CodeGuard static checks)
- @entities/skills/src-hunter-skill.md — 305-payload SKILL.md that stress-tests this checklist's scalability assumptions
- @concepts/code-as-agent-harness.md — verifiable harness changes gate through Phase-0 before adoption
- @entities/tools/open-design.md — modular skill Markdown patterns still require full vetting before install
- @concepts/tools-we-dont-use.md — permanent skips (ToS bypass, archived spam tools)
- @concepts/skillrae-retrieval-augmented-execution.md — skill-graph compilation assumes vetted skills only
- @concepts/claude-premortem-skill.md — internal harness/skill **authoring** gate before Phase-0 on third-party installs

## Raw Concept

Extracted 2026-05-17 from the audit-checklist section of @entities/mcp-servers/anthropic-skills.md. Promoted to its own concept page because (a) the checklist is referenced from multiple CCC pages (tools, mcp-servers, patterns) and inline duplication would create drift, and (b) Cemini's adoption stance — "adopt the SKILL.md spec, do not depend on catalog content" — deserves its own page distinct from the marketplace entity page.

Note: an OSINT-side `concepts/skill-vetting.md` exists but is `[RETRACTED]` (the proposed Postgres-backed vetting-ledger does not exist in code). The CCC version is a different concept — a manual Phase-0 checklist applied to skills before adoption, not an automated ledger.

## Narrative

A Claude Code "skill" is a plain markdown file with YAML frontmatter that the LLM can be made to follow. Two failure modes make vetting non-optional:

1. **Catalog churn** — instructa/agent-skills HEAD removed `package-security-check` on 2026-05-12, 12 days after Cemini's K42 eval. Any skill snapshot ages within weeks.
2. **Malicious-skill class** — @entities/tools/claude-code-ultimate-guide.md catalogs 655 malicious-skill patterns observed in the wild. A skill's body is executable instructions to the LLM; prompt-injection-as-skill is real.

### The checklist (5 steps; ~15-30 min per skill)

1. **License + provenance** — `gh api repos/<owner>/<repo> --jq '.license.spdx_id'`. README claims are not enough (see the OSINT workspace's `LESSONS.md` 2026-05-11 entry on the no-LICENSE-file pattern — file lives at the OSINT workspace root, outside the `wiki/` alias surface). Reject if no LICENSE file at root.
2. **SKILL.md frontmatter compliance** — every skill in the repo has `name`, `description`, optional `license`, optional `metadata` block. Frontmatter that diverges from the spec is a signal of churn or pre-spec authorship.
3. **Read the skill body** — every word of every `.md` file the skill ships. The body is what the LLM executes; do not skim. Flag any: shell-out instructions, network-fetch instructions, credential-read instructions, `Bash` invocations of `curl | sh`-style remote-exec, instructions to disable hooks.
4. **Cross-check against the malicious-skill catalog** — @entities/tools/claude-code-ultimate-guide.md's 655 patterns + 28 CVEs cover the known-bad surface. Pattern-match the body against this catalog.
5. **First-run in isolation** — if maturity ≥ "promising" after steps 1-4, first invocation runs in an agent-VM (see @concepts/agent-vm-sandboxing.md) with action tracing on. If no agent-VM is wired, run only after a manual read-through of the skill body.

### Verdict

- **GO** — all 5 steps pass; skill enters Cemini's `~/.claude/skills/` or project `.claude/skills/`.
- **CONDITIONAL-GO** — passes steps 1-4 but step 5 surfaces noisy behavior; pin the SHA and re-audit on each upgrade.
- **NO-GO** — any of steps 1-4 fails, or step 5 surfaces malicious behavior. Record the failure in @entities/mcp-servers/anthropic-skills.md § Dead Ends with the date and reason.

### Why "do not depend on catalog content"

Per CCC `LESSONS.md` 2026-05-13 (workspace root, outside the `wiki/` alias surface): the marketplace is the source of truth; mirroring its content into this wiki creates a stale shadow catalog. The audit checklist is the wiki's contribution — a methodology that's stable across catalog churn.

## Dead Ends

- **Automating step 3 with an LLM** — tried mentally; rejected. The LLM that audits a skill is the same LLM the skill targets for injection. The audit must be done by the human operator, not by the harness.
