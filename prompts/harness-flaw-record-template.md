# Harness flaw record — log.md template

Copy into `wiki/log.md` when a recurring harness failure warrants cross-session repair (HarnessFix steal-from). Full methodology: `@wiki/concepts/failed-trajectory-harness-repair.md`.

```markdown
## [YYYY-MM-DD] flaw | <short symptom>

- **Six-responsibility (K124):** observation | context | control | action | state | verification-governance
- **ETCLOVG layer:** Execution | Tool Interface | Context | Lifecycle | Observability | Verification | Governance
- **Symptom:** <what the operator saw — e.g. Stop-hook loop, subagent empty summary>
- **TraceStep:** <which tool call / hook / subagent turn failed>
- **Diagnosis:** <root cause in harness artifact, not "model was wrong">
- **Repair spec:** <scoped edit — prompt, skill, hook, MCP schema, rule — with forbidden scope>
- **Acceptance:** ΔD_target = <flaw should not recur on N trials>; R_max = <no new regressions in wiki_lint / smoke>
- **Status:** open | patched | wontfix
```

### Layer quick-pick

| If failure involves… | Six-responsibility | ETCLOVG layer |
|---------------------|-------------------|---------------|
| Tool outputs, snapshots, MCP reads | Observation | Tool Interface |
| hot.md, claude-mem, window bloat | Context | Context |
| Planning, retries, subagents, Stop | Control | Lifecycle |
| Bash, sandbox, browser actions | Action | Execution |
| log.md, git, lifecycle records | State | Context / Lifecycle |
| lint, OpenSpec AC, vetting | Verification/governance | Verification / Governance |
| Missing traces | (cross-cutting) | Observability |
| Permissions, hook bypass | (cross-cutting) | Governance |

Legacy ETCLOVG-only table:

| If failure involves… | Layer |
|---------------------|-------|
| Sandbox, bash, VM boundaries | Execution |
| MCP schema, SKILL.md tools, lazy-tool invoke | Tool Interface |
| hot.md, claude-mem, context loss | Context |
| Subagents, Stop hooks, /goal, termination | Lifecycle |
| Missing logs, can't diagnose | Observability |
| No readiness check before complete | Verification |
| Permissions, vetting bypass | Governance |
