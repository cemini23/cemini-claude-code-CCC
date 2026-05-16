---
title: Anthropic Skills marketplace
type: entity
tags: [mcp-server, anthropic, skills, marketplace, skill-md, plugin]
keywords: [anthropic skills, agent skills, skill marketplace, SKILL.md, instructa agent-skills, claude-plugins-official]
related:
  - entities/tools/claude-code.md
  - entities/commands/plugin.md
  - entities/skills/tech-debt-audit.md
  - entities/skills/claude-seo-agrici.md
  - entities/skills/marketingskills.md
  - entities/skills/geo-seo-claude.md
  - entities/tools/claude-code-ultimate-guide.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/tech-debt-skill.md
  - entities/tools/adamsreview.md
  - entities/tools/gtm-agents.md
  - entities/visual-explainer.md
  - entities/tools/claude-for-legal.md
  - entities/tools/skillkit.md
maturity: draft
created: 2026-05-13
updated: 2026-05-16
---

## Relations

- `@entities/tools/claude-code.md` — host harness that loads skills
- `@entities/commands/plugin.md` — install path: `/plugin marketplace add <repo>` + `/plugin install <name>`
- `@entities/skills/tech-debt-audit.md`, `@entities/skills/claude-seo-agrici.md`, `@entities/skills/marketingskills.md`, `@entities/skills/geo-seo-claude.md` — Cemini-installed skills that exemplify the spec
- `@entities/tools/claude-code-ultimate-guide.md` — reference catalog of 28 CVEs + 655 malicious-skill patterns relevant to Phase-0 skill audits
- `@concepts/claude-desktop-vs-claude-code.md` — skills are Claude Code-only
- `@entities/tools/adamsreview.md` — async code-review CC plugin; PEP 723 inline-script + artifact.json architecture
- `@entities/tools/gtm-agents.md` — 244-skill GTM pack; reference example of skill-pack distribution structure
- `@entities/visual-explainer.md` — zero-dependency CC skill generating rich HTML diagrams (Mermaid + Chart.js)
- `@entities/tools/claude-for-legal.md` — Anthropic-official vertical plugin pack; practice-area plugins are a SKILL.md-style packaged distribution
- `@entities/tools/skillkit.md` — management/translation layer atop the SKILL.md spec; governs the same `.claude/skills/` surface

## Raw Concept

The "Anthropic Skills marketplace" is a catch-all for the official + community Claude-Code skills surface: skills shipped by Anthropic, by `claude-plugins-official`, by third parties like `instructa/agent-skills`, and by individual authors (kepano, mvanhorn, etc.). Cemini's stance — per `@LESSONS.md` 2026-05-13 — is **adopt the spec, do not depend on catalog content**. This page documents the spec; per-skill audit pages live as needed in `wiki/entities/skills/`.

## Narrative

A Claude Code "skill" is a plain markdown file with YAML frontmatter, located in one of three search paths:

1. `~/.claude/skills/<name>.md` — user-scoped
2. `<project>/.claude/skills/<name>.md` — project-scoped
3. Plugin-bundled (e.g. `mcp__plugin_claude-mem_mcp-search__*` skills shipped by the `claude-mem` plugin)

**SKILL.md frontmatter spec** (pinned 2026-05-13 snapshot, see the K42 entry in OSINT WORKSPACE's `LESSONS.md` — that file lives at the OSINT workspace root, outside the wiki/ alias surface):

```yaml
---
name: example-skill
description: One-line description shown in the skill list; the LLM matches user requests against this
license: MIT
metadata:
  author: someone
  version: 0.1.0
disable-model-invocation: false
---
```

After the frontmatter, the body is the **skill protocol** — markdown instructions the LLM follows when the skill is invoked. Optionally, a `# Project documentation` section after another `---` divider serves the human reader.

**Why catalog content is excluded from the wiki**:

- **Churn**: instructa/agent-skills HEAD removed `package-security-check` on 2026-05-12, 12 days after Cemini's K42 eval (see OSINT LESSONS 2026-05-13 entry). A wiki page that mirrors catalog content goes stale within weeks.
- **Authority**: the marketplace is the source of truth for catalog content. Mirroring it adds noise without adding signal.
- **Cost**: writing a per-skill audit page for every skill in three catalogs is open-ended; the audit pattern (`@entities/tools/claude-code.md` § Phase-0) handles individual adoptions without a catalog mirror.

**What Cemini does keep in this wiki**:

- The spec (this page)
- Skills Cemini has authored (when they exist, in `wiki/entities/skills/`)
- Skill-audit verdicts on skills Cemini has actually evaluated (in `wiki/entities/skills/<skill>.md`, with a Phase-0 GO/CONDITIONAL/NO-GO decision)

**Marketplace surfaces seen in current Cemini sessions**:

- `claude-mem:*` — plugin-bundled skills (timeline-report, learn-codebase, make-plan, do, version-bump, ...)
- `finance-*:*` — `finance-market-analysis`, `finance-social-readers`, `finance-data-providers`, `finance-startup-tools` — finance-domain catalog (Cemini uses some, audits others)
- `update-config`, `simplify`, `keybindings-help`, `fewer-permission-prompts`, `loop`, `schedule`, `claude-api`, `init`, `review`, `security-review` — Anthropic-shipped utility skills

Cemini's adoption is selective. The trigger for adoption is: a skill solves a problem Cemini has hit ≥3 times. Catalog browsing is not a Cemini workflow.

### Cemini's installed skills (reference set)

| Skill | Role | Page |
|-------|------|------|
| `tech-debt-audit` | Whole-repo audit, file:line citations + "looks bad but fine" section | `@entities/skills/tech-debt-audit.md` |
| `seo` (claude-seo) | Local SEO: GBP, NAP, geo-grid, competitors | `@entities/skills/claude-seo-agrici.md` |
| `marketing-skills` | PAS / brand-voice / localized copy frameworks | `@entities/skills/marketingskills.md` |
| `geo-seo` | Generative-engine SEO: citability, AI-crawler analysis | `@entities/skills/geo-seo-claude.md` |

### Phase-0 skill audit checklist

When evaluating a candidate skill from a marketplace:

1. **License via API** — `gh api repos/<owner>/<repo> --jq '.license.spdx_id'`. README claims aren't enough.
2. **Maintenance signal** — last commit, open-issue responsiveness, recent issue resolutions
3. **Permission footprint** — what Bash patterns does the skill require? Match against `permissions.allow|deny` policy
4. **Malicious-pattern check** — cross-check against `@entities/tools/claude-code-ultimate-guide.md`'s 655 patterns
5. **Spec compliance** — frontmatter has `name`, `description`, `license`, `metadata.author`, `metadata.version`?
6. **Catalog churn risk** — pin to a known-good commit if the skill matters operationally

## Dead Ends

- **Mirroring the marketplace catalog** — high cost, high churn, low durability. See LESSONS 2026-05-13.
- **Treating `description:` as documentation** — it's a *matcher*. The LLM uses it to decide whether to invoke; flowery descriptions delay invocation or mis-trigger.
- **Installing skills without Phase-0 audit** — see `@entities/tools/claude-code-ultimate-guide.md`'s 655 malicious-skill patterns; supply-chain attacks on skill libraries are documented and growing.
