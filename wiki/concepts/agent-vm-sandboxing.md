---
title: "Agent-VM sandboxing — Claude Code isolation pattern for untrusted action surfaces"
type: concept
tags: [concept, sandbox, agent-vm, isolation, claude-code, tier-2, cross-wiki-stub]
keywords: [agent-vm, sandbox, cua, disposable-vm, action-tracing, isolation-boundary, tier-2-gated]
related:
  - entities/tools/cua.md
  - concepts/subagent-orchestration.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/polymarket-mcp-server.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
cross-wiki-source: "@cybersecurity-wiki/concepts/agent-vm-sandboxing.md"
---

## Relations

- @entities/tools/cua.md — current reference implementation on M-series Macs; the CCC-side tool page for the sandbox runtime
- @concepts/subagent-orchestration.md — agent-VM is the natural blast-radius cap for Tier-2 subagent execution
- @entities/patterns/tier1-tier2-agent-model.md — the pattern that prescribes which agent class gets sandboxed and which doesn't
- @concepts/skill-vetting.md — first-run sandbox is step 5 of the Phase-0 skill-vetting checklist
- @entities/mcp-servers/polymarket-mcp-server.md — execution-class MCP server (45-tool exemplar) that should run inside an agent-VM until trust is established
- @cybersecurity-wiki/concepts/agent-vm-sandboxing.md — cross-wiki canonical concept (Cybersec is the primary home; full methodology lives there)

## Raw Concept

CCC-side stub for the agent-VM sandboxing methodology canonicalised in Cybersec. Pulled in because it generalises beyond cybersec — any Claude Code workflow that hands tool execution to a less-trusted agent (third-party skill, untrusted MCP server, Tier-2 subagent with shell access) benefits from the same disposable-VM + action-tracing + explicit-isolation triad. This page documents the Claude-Code-side slice; the full methodology, threat model, and substrate choices (Apple Virtualization.Framework / Firecracker / Hyper-V) live in the Cybersec primary.

## Narrative

**The CCC-relevant slice**: when a Claude Code session needs to run untrusted code, run an unaudited skill, or hand control to a Tier-2 subagent that can `Bash` arbitrarily, the agent-VM pattern is the blast-radius cap. Three properties make it coherent (paraphrased from the Cybersec primary):

1. **Disposable VM substrate** — clean image per run; logs/screenshots persisted out, VM destroyed.
2. **Agent-action tracing** — every action captured (screenshot, accessibility tree, API-call log, network-pcap, filesystem-diff). The trace is the artifact.
3. **Explicit isolation boundary** — no shared filesystem beyond read-only `/host-input/` and write-only `/host-output/`; NAT'd egress with explicit rules.

**Why this matters for CCC**, not just cybersec:

- **Skill audits**: a Phase-0 audit of an unvetted third-party skill is honest only if the skill runs inside a sandbox the first time. See @entities/mcp-servers/anthropic-skills.md § Phase-0 audit pattern.
- **Tier-2 subagent execution**: @entities/patterns/tier1-tier2-agent-model.md prescribes that execution-capable subagents have a narrower trust envelope than Tier-1; an agent-VM is the operationalisation.
- **MCP-server adoption**: an execution-capable MCP server (e.g. @entities/mcp-servers/pmxt-mcp-pattern.md) should run inside an agent-VM until trust is established.

Cemini's reference implementation is @entities/tools/cua.md (Apple Virtualization.Framework on M-series). The Cybersec primary covers Firecracker / Hyper-V alternatives and the full threat model.

## Snippets

> Run untrusted agent actions inside a disposable VM, with end-to-end action tracing, so that (a) the host is uncontaminated and (b) every action is replayable.
[Source: @cybersecurity-wiki/concepts/agent-vm-sandboxing.md]
