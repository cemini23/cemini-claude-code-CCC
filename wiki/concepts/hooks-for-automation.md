---
title: Hooks for automation — settings.json events, scope, blast radius
type: concept
tags: [concept, hooks, settings, claude-code, automation, sessionstart, stop, userpromptsubmit]
keywords: [hooks, .claude/settings.json, SessionStart hook, Stop hook, UserPromptSubmit hook, PreToolUse, PostToolUse, hook command, hook matcher]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@entities/tools/claude-code.md` — host harness whose lifecycle the hooks tap into
- `@concepts/context-engineering.md` — hooks are one way to inject durable state into the session

## Raw Concept

Question this page answers: **what are Claude Code's hooks, where do they live, and what's the cost of a misconfigured hook?**

## Narrative

A Claude Code "hook" is a shell command that runs in response to a harness event. Hooks live in `~/.claude/settings.json` (user-scoped) or `<project>/.claude/settings.json` (project-scoped). Per-project settings stack on top of user settings.

### Event types

| Event | When it fires | Common uses |
|-------|---------------|-------------|
| `SessionStart` | When a new session boots | Inject context (claude-mem), print resume banner, set goal |
| `Stop` | When the model is about to end its turn | Gate session-end (e.g., `/goal` Stop hook blocks termination until criteria met) |
| `UserPromptSubmit` | When the user submits a prompt | Pre-process / normalize / route prompts |
| `PreToolUse` | Before a tool call | Authorization, audit logging |
| `PostToolUse` | After a tool call | Result processing, audit trail |

### Hook anatomy

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {"type": "command", "command": "claude-mem hook session-start"}
        ]
      }
    ]
  }
}
```

The `matcher` is event-specific (e.g., `startup` for `SessionStart` means "session boot, not resume"). The inner `hooks` array runs in order; each item gets the event payload on stdin and can emit JSON on stdout for harness consumption (e.g., `{"continue": true, "suppressOutput": true}`).

### Blast radius

Misconfigured hooks are the #1 footgun:

1. **Stop hooks that always block** — if the `Stop` hook returns "not yet done" indefinitely, the session loops forever. Always pair a Stop hook with an exit condition you can verify.
2. **SessionStart hooks that fail loudly** — kill the session before any user prompt lands. Test with `--debug` to see hook stderr.
3. **UserPromptSubmit hooks that mutate the prompt** — silently change what the model sees. High surprise factor; reserve for stable transformations only.
4. **PreToolUse hooks that deny aggressively** — block the model from doing its job. Usually wrong; prefer settings-level `permissions.deny` for hard blocks.

### Cemini's hook policy

- **Wide-deploy ban on Stop hooks** without an explicit, measurable exit condition. The `/goal` Stop hook (which gates on goal-condition satisfaction) is the only Stop hook Cemini runs by default; user-authored Stop hooks need a paired test fixture before adoption.
- **SessionStart hooks limited to context injection** (claude-mem, hot.md banner, inbox check). No mutation, no surprises.
- **PreToolUse / PostToolUse hooks** — Cemini doesn't currently run any. Permission policy lives in `.claude/settings.json#permissions.allow|deny` instead, which is declarative and easier to reason about than imperative hook code.

### Permissions vs hooks

| Use case | Use permissions | Use a hook |
|----------|-----------------|------------|
| "Always allow `Bash(ls *)`" | `permissions.allow` | — |
| "Block `Bash(rm -rf *)`" | `permissions.deny` | — |
| "Run `claude-mem hook` on session start" | — | `SessionStart` hook |
| "Block session end until goal met" | — | `Stop` hook |
| "Audit every Bash call to a remote log" | — | `PostToolUse` hook |

Permissions are declarative and stack predictably. Hooks are imperative — harder to reason about, harder to debug, but more powerful.

### Iterating safely

When developing a new hook:

1. Write the hook command as a standalone script first; test it against synthetic stdin payloads.
2. Wire it into `~/.claude/settings.local.json` (gitignored, machine-local) — never start in project settings.
3. Run a session with `--debug` to confirm the hook fires and behaves.
4. Move to `~/.claude/settings.json` or project `.claude/settings.json` only after validation.

### Cross-wiki notes

Cybersecurity-wiki may eventually carry a hook-based audit-logging pattern (`PostToolUse` → security-event sink). When that lands, link from here.

## Dead Ends

- **Stop hooks without an exit condition** — infinite-loop sessions. Always pair with verifiable success criteria.
- **Hooks for permission policy** — use `permissions.allow|deny` instead. Declarative beats imperative.
- **Hooks that write to synced folders without considering Syncthing replication cost** — see `@entities/tools/syncthing.md`.
