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
  - entities/tools/metatrader-mcp-server.md
  - entities/tools/open-claude-code.md
  - entities/tools/mercury-agent-skills.md
  - entities/tools/solo-founder-superpowers.md
  - entities/tools/andrej-karpathy-skills-multica.md
  - entities/tools/bmad-creative-intelligence-suite.md
  - concepts/claude-plugins-catalog-patterns.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - sources/multi-wiki-tool-eval-25url-2026-05-28.md
  - concepts/k73-phase0-audit-decisions.md
  - entities/tools/mermaid-skill.md
  - entities/tools/tvscreener.md
  - entities/tools/webwright.md
  - entities/tools/skill-seekers.md
  - entities/tools/book-to-skill.md
  - entities/tools/cc-thinking-skills.md
  - entities/tools/claude-skill-registry.md
  - entities/tools/alirezarezvani-claude-skills.md
  - entities/tools/jezweb-claude-skills.md
  - entities/tools/skillnet.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - concepts/claude-code-skills-md-institutional-memory.md
  - entities/tools/npxskillui.md
  - entities/tools/claude-trading-skills.md
  - entities/tools/obsidian-second-brain-eugeniughelbur.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - sources/arxiv-muse-autoskill-2605.27366.md
  - concepts/agent-skills-taxonomy.md
  - entities/tools/tool-forge.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/agent-skills-progressive-disclosure.md
  - sources/arxiv-agent-skills-architecture-security-2602.12430.md
  - entities/tools/scienceaix-agentskills.md
  - concepts/cross-wiki-tool-adoption-routing.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - "@cybersecurity-wiki/concepts/mcp-security-posture.md"
  - "@cybersecurity-wiki/sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md"
  - "@cybersecurity-wiki/briefs/2026-05-31_ccc-handoff-k100-spi-skill-vetting-checklist.md"
  - entities/skills/cursor-audit.md
maturity: draft
created: 2026-05-17
updated: 2026-06-05
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
- @entities/skills/cursor-audit.md — **internal** Cursor harness skill (authored in-repo); Phase-0 checklist does not apply — track via git + wiki page instead

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
3b. **Optional automated pre-screen (defenseclaw)** [CONFIRMED 2026-06-04] — `skill-scanner scan <skill-dir>/` from `@entities/tools/defenseclaw.md` before step 4. Trial: project skills `webwright` SAFE (INFO), `agents-best-practices` SAFE (1 MEDIUM). Does **not** replace human read in step 3.
4. **Cross-check against the malicious-skill catalog** — @entities/tools/claude-code-ultimate-guide.md's 655 patterns + 28 CVEs cover the known-bad surface. Pattern-match the body against this catalog.
5. **First-run in isolation** — if maturity ≥ "promising" after steps 1-4, first invocation runs in an agent-VM (see @concepts/agent-vm-sandboxing.md) with action tracing on. If no agent-VM is wired, run only after a manual read-through of the skill body.
6. **Validation-carrying metadata** [Steal-from @entities/tools/tool-forge.md Phase-0 2026-06-02] — before cataloging a skill or MCP tool, record `validation_status` (draft/approved/blocked), `version_pin`, and `last_reviewed`. Reject skills that instruct bypassing hooks or fetching remote executables without pinned SHA.
7. **MCP catalog discipline (K98)** — viral MCP lists (@concepts/mcp-server-catalog-curation.md) follow the same checklist; add `@concepts/seclaw-agent-security-evaluation.md` trajectory eval before write-capable MCP GO.
8. **Skill Trust tiers (2602.12430)** — four-tier gate-based permission model mapping skill **provenance → graduated deployment** [TENTATIVE]. Aligns with Tier-1/Tier-2 agent model; empirical baseline: **26.1%** of community skills contain vulnerabilities per concurrent studies cited in 2602.12430.

### K100 — cross-session stored prompt injection (SPI) [2026-05-31]

Source: `@cybersecurity-wiki/sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md`. SPI = poison persists across **session reset** (stored-XSS analog). Benchmark: **32–42% E2E-ASR**; fact manipulation **74–82%**. Session-only guards are insufficient.

9. **Persistence channel map** — before GO, list every **long-lived write path** this skill/MCP can touch: agent memory (claude-mem, stash), file-backed context (`.cursor/rules`, `AGENTS.md`, `CLAUDE.md`, workspace files), tool descriptions (strong persistence), tool-written artifacts. **NO-GO** if skill instructs uncontrolled writes to strong-persistence paths.

10. **Session-reset activation probe** (lab, authorized workspace) — (a) injection session with benign canary payload; (b) new chat / cleared history, workspace preserved; (c) activation session with unrelated task; **pass** if canary never influences behavior. Record channel + outcome. Full procedure: `@cybersecurity-wiki/briefs/2026-05-31_ccc-handoff-k100-spi-skill-vetting-checklist.md`.

11. **Write-path governance (mcp-attested steal-from)** — closed **per-server tool allowlist**; deny tools not allowlisted even if advertised [Source: arxiv-2605.24248]. Re-scan on MCP version bump (DCI — 9.93% description≠code) [Source: arxiv-2606.04769]. Cross-link: `@cybersecurity-wiki/concepts/mcp-security-posture.md`.

**SPI-aware verdicts:** GO requires steps 1–8 **and** 9–10 pass; CONDITIONAL-GO if write paths exist but gated (Tier-2, operator confirm, re-run step 10 on upgrade).

### HarnessFix steal-from (K100)

When a vetted skill still causes recurring session failures, tag the flaw with an **ETCLOVG layer** (`@concepts/etclovg-harness-layers.md`) before re-audit — e.g. Tool Interface (schema drift), Governance (permission bypass instructions). Full diagnosis/repair loop: `@concepts/failed-trajectory-harness-repair.md` (manual flaw records; no HarnessFix install).

### Verdict

- **GO** — all 5 steps pass; skill enters Cemini's `~/.claude/skills/` or project `.claude/skills/`.
- **CONDITIONAL-GO** — passes steps 1-4 but step 5 surfaces noisy behavior; pin the SHA and re-audit on each upgrade.
- **NO-GO** — any of steps 1-4 fails, or step 5 surfaces malicious behavior. Record the failure in @entities/mcp-servers/anthropic-skills.md § Dead Ends with the date and reason.

### Why "do not depend on catalog content"

Per CCC `LESSONS.md` 2026-05-13 (workspace root, outside the `wiki/` alias surface): the marketplace is the source of truth; mirroring its content into this wiki creates a stale shadow catalog. The audit checklist is the wiki's contribution — a methodology that's stable across catalog churn.

## Dead Ends

- **Automating step 3 with an LLM** — tried mentally; rejected. The LLM that audits a skill is the same LLM the skill targets for injection. The audit must be done by the human operator, not by the harness.
