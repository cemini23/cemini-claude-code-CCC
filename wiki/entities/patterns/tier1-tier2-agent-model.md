---
title: Tier 1 / Tier 2 agent model — scope-enforcement for execution-capable agents
type: entity
tags: [pattern, agent, tier1, tier2, scope-enforcement, requires_scope, claude-code, security]
keywords: [tier 1 tier 2, advisory vs execution agent, requires_scope, allowed_targets, scope enforcement, structured findings, pentest-ai-agents]
related:
  - entities/tools/claude-code.md
  - entities/tools/cua.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/subagent-orchestration.md
  - concepts/hooks-for-automation.md
  - entities/tools/osmedeus-acp-orchestration.md
  - concepts/agent-vm-sandboxing.md
  - entities/patterns/scatter-gather.md
  - entities/mcp-servers/polymarket-mcp-server.md
  - entities/patterns/citadel-agent-orchestration.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/tools/defenseclaw.md
  - concepts/agent-sandbox-unikraft.md
  - concepts/claude-code-subagent-templates.md
  - concepts/embedded-agent-modular-edge-architecture.md
maturity: validated
created: 2026-05-13
updated: 2026-06-03
---

## Relations

- `@entities/tools/claude-code.md` — host harness whose permission UX enforces the gate
- `@entities/tools/cua.md` — provides the isolation chamber Tier 2 needs
- `@entities/patterns/full-prompt-goal-template.md` — Tier 2 invocations need declared scope; goal-condition is one place scope can live
- `@concepts/subagent-orchestration.md` — Tier 2 dispatch is a special case of subagent dispatch with stricter gating
- `@concepts/hooks-for-automation.md` — PreToolUse hooks are the natural enforcement layer for Tier 2 commands
- `@entities/tools/osmedeus-acp-orchestration.md` — security-orchestration engine; canonical home of execution-capable Tier-2 agents
- `@concepts/agent-vm-sandboxing.md` — Tier-2 subagents naturally run inside the agent-VM sandbox
- `@entities/patterns/scatter-gather.md` — Tier-2 subagents are typical scatter-leg workers
- `@entities/mcp-servers/polymarket-mcp-server.md` — execution-MCP class exemplar that the Tier-2 gate must constrain

Cross-wiki: `@cybersecurity-wiki/concepts/llm-pentest-automation.md` is the canonical write-up of this pattern (originally from `pentest-ai-agents` v3.2). `@cybersecurity-wiki/entities/tools/pentest-ai-agents.md` is the reference implementation.

## Raw Concept

Adapted from `pentest-ai-agents` v3.2 (Cybersec wiki, 2026-05-13). The pattern is generalizable beyond pentest: any Claude Code workflow that mixes **advisory** and **execution-capable** agents benefits from the split.

## Narrative

The split is the safety contract:

- **Tier 1 agents** = advisory-only. Reason, plan, score, draft. Touch nothing external.
- **Tier 2 agents** = execution-capable. Invoke external tooling that has effects (network probes, file writes outside the workspace, API calls with state). Require **declared scope** before they run.

### Tier 1 examples

- Engagement-planning agent (cybersec)
- CVSS-rationale drafter (cybersec)
- Code review agent (Cemini's `code-reviewer` subagent)
- Plan agent (Cemini's built-in `Plan` subagent — read-only, plans only)
- Phase-0 audit drafter (Cemini's modal Phase-0 workflow)

### Tier 2 examples

- nmap probe (cybersec)
- sqlmap injection (cybersec)
- File-system-modifying skill (any wiki ingest workflow)
- API-call-making skill (writes to external services)
- VM-spawning skill (cua-driven sandbox)

### Scope-enforcement mechanism

Tier 2 agents declare a `requires_scope: true` flag in their YAML frontmatter. The agent's `allowed_targets` field is templated against the engagement scope:

```yaml
---
name: nmap-scan
tier: 2
requires_scope: true
allowed_targets: ["{{ engagement.scope_cidrs }}"]
allowed_techniques: [tcp-syn-scan, service-enum]
findings_schema: v1.2
---
```

Two enforcement layers stack:

1. **Agent-policy layer** — the YAML refuses to invoke without declared scope.
2. **Runtime UX layer** — the harness shows the scope before approving.

**Neither is the network-egress layer.** A misconfigured scope still authorizes execution. Always pair with network-level + filesystem-level isolation (engagement VPN with destination ACLs, or cua VM containment, or a dedicated workstation with no path to anywhere except in-scope targets).

### Cemini's CCC-side adoption

CCC currently has **no execution-capable third-party skills installed** that warrant Tier 2 treatment. The pattern is documented because:

1. **Future skill adoptions may require it** — if Cemini ever installs a skill that writes to remote services or executes against networks, that skill becomes Tier 2 and gets the gate.
2. **The Plan subagent + `EnterPlanMode`/`ExitPlanMode` harness pair is structurally Tier 1** — read-only by design, with explicit user approval to "exit plan mode" before any write.
3. **`/goal` Stop hook is a structural ally** — the goal-condition declares what success looks like; pairing it with declared scope before Tier 2 runs is one half of the contract.

### Where the gate sits in Cemini's stack

| Layer | What it enforces |
|-------|------------------|
| Agent YAML `requires_scope` | refusal unless scope declared at invocation |
| Harness permission prompt | human-in-the-loop scope confirmation |
| `.claude/settings.json#permissions.allow|deny` | declarative pattern allow/deny lists |
| PreToolUse hook | imperative gating with custom logic |
| `cua` VM | actual filesystem + network containment |
| host firewall / VPN | network-egress enforcement |

The agent YAML + permission prompt are Claude Code-native. PreToolUse hooks are Claude Code-native but rare in Cemini's setup. cua + host firewall are external — see `@entities/tools/cua.md`.

### Companion: structured findings JSON schema

Tier 2 agents that return findings (cybersec finds; Cemini-adjacent: skill audits, MCP-server audits) benefit from a stable JSON schema for the output. `pentest-ai-agents` ships `findings.sh` with schema v1.2 fields including `finding_id`, `severity`, `cvss_vector`, `affected_asset`, `evidence`, `mitigations[]`, `references[]`. The same idea generalizes:

- Phase-0 audit JSON: `{audit_id, verdict, license, maturity, failure_mode_findings[], decision}`
- Skill-vetting JSON: `{skill_id, name, sha, license, signature_matches[], verdict}`

Stable schemas make findings flow into other tools (wiki source pages, briefs, downstream automation) instead of dying in chat.

## Dead Ends

- **Removing the Tier-2 scope gate "because it's annoying"** — the gate is the safety contract. Without it the system is a one-click disaster machine.
- **Trusting `requires_scope: true` as actual enforcement** — it's policy, not policy + isolation. Pair with network/filesystem containment.
- **Pinning to one model vendor for Tier 2** — the YAML + Markdown protocol is model-agnostic. Other capable models work.
