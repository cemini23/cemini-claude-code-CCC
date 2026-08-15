---
title: Persona-hat Claude Code SDLC — MCP designs, skills implement (OSINT K238)
type: concept
tags: [concept, claude-code, sdlc, subagents, k238]
keywords: [persona-hat, Nardini, GCP, plan-mode, reviewer-vs-deployer, dual-id]
related:
  - sources/brief-k238-persona-hat-claude-gcp-2026-08-15.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/llm-verification-layer-accept-escalate-reject.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - entities/skills/route.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
---

## Relations

- `@sources/brief-k238-persona-hat-claude-gcp-2026-08-15.md`
- `@osint-wiki/concepts/persona-hat-claude-code-sdlc.md` — full session synthesis (OSINT owns the X/YouTube ingest)
- `@concepts/role-specialization-model-multi-tool-coordination.md`
- `@concepts/agent-skills-progressive-disclosure.md`
- `@concepts/llm-verification-layer-accept-escalate-reject.md`

## Raw Concept

How should CCC steal Ivan Nardini's Code w/ Claude 2026 GCP live build without treating 26 minutes as a production bar?

## Narrative

OSINT **K238** (X-video ingest) ≠ CCC paper-wave **K238** (TokTier). Canon write-up lives on OSINT; this page is the Cursor/Claude harness extract.

### Steal

1. **Split docs-MCP from skills.** MCP (architecture / Knowledge API) designs; SKILL.md implements one verified block. Same split as lazy-tool vs skill (pairs K272 packaging).
2. **Plan mode before UI code.** Think-then-propose; do not dump CSS from a god-agent.
3. **Fan-out by component** (API / ingest / dashboard), not one agent for the whole app. Pair worktrees / `/route` implement lanes.
4. **Reviewer ≠ deployer.** Pre-built security-review is useful; the demo's merge is demo-only. Aligns K239 HITL and K264 accept/reject/escalate.
5. **Vertex ADC** = in-project auth awareness. Do **not** swap `claude-ds` for Vertex because of this talk.
6. **Name collision:** talk "Google Cloud Skills" ≠ `github.com/google/skills` packing repo (K226 Context).

**Do not:** treat 26 minutes as the bar; skip CI/CD/monitoring; vendor GCP skills into federation without skill-vetting/preflight.

| Verdict | **ADOPT** composition. No GCP skill pack install. |
