---
title: Agentic red-team secure architecture handoff
type: brief
tags: [brief, llm-pentest, red-team, sandbox, tier-2]
created: 2026-06-25
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
updated: 2026-06-29
---

## Target

hands-on | Tier-2 pentest agents | Claude Code / prod-mcp offensive stacks

## Summary

arXiv:2606.24496: 10/12 agentic pentest tools compromised via **agent-phishing** (97.8%) + worker→orchestrator escalation. **Assume worker is malicious** after target contact; never store API keys in worker containers.

## Body

### Architecture checklist (from §9)

| # | Control |
|---|---------|
| 1 | Worker in isolated Docker — **no** docker.sock, **no** `--network=host`, **no** privileged unless task-scoped |
| 2 | **Zero secrets** in worker env — LLM keys + tool tokens on orchestrator only |
| 3 | Tool calls **proxied** through orchestrator APIs (nmap, CS, etc.) |
| 4 | Internal orchestrator APIs: per-user authZ — no blanket inter-service key |
| 5 | Guardrails enforced on **orchestrator**, not worker-only deny lists |
| 6 | Egress proxy (iron-proxy-class) + human gate on write/send/exec |
| 7 | Block worker→orchestrator tool routing (PentestGPT `python_session` pattern) |

### Docker caps audit (Table 4 flags)

Reject or scope: `NET_ADMIN`, `NET_RAW`, `SYS_ADMIN`, `seccomp:unconfined`, `apparmor:unconfined`, host bind mounts of `~/.ssh`, `~/.kube`, `NOPASSWD:ALL` sudo.

### Phase-0

Paper — **Reference** (Cracken audit). Per-tool: re-audit before Tier-2 adoption; see @concepts/agentic-offensive-security-kill-chain.md Table 1.

## Sources

- @sources/arxiv-2606-24496-red-teaming-the-agentic-red-team.md
- @concepts/agentic-offensive-security-kill-chain.md
- @concepts/llm-pentest-automation.md
