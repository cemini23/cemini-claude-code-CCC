---
title: ttok — token-counter CLI for LLM cost awareness
type: entity
tags: [tool, tokens, cost, cli, python, claude-code]
keywords: [ttok, token counter, tiktoken, claude tokens, anthropic tokens, cost preview, pip install]
related:
  - entities/tools/claude-code.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/context-engineering.md
  - concepts/mcp-context-optimization.md
  - entities/tools/repomix.md
  - concepts/claude-code-large-codebase-workflow.md
  - concepts/deepseek-coding-cost-routing.md
maturity: draft
created: 2026-05-13
updated: 2026-06-01
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@concepts/token-economics-and-prompt-caching.md` — direct cost-discipline support
- `@concepts/context-engineering.md` — preview before paste = context hygiene

Cross-wiki: `@seo-wiki/entities/tools/claude-code-tool-stack.md` (Tool 4 of the SEO-side stack reference).

## Raw Concept

`pip install ttok` — Simon Willison's tiny Python CLI for counting tokens before sending. Standard tiktoken under the hood. Installs in 30 seconds; pays for itself the first time it stops you from pasting a 30 K-token file into a session you didn't budget for.

## Narrative

The smallest possible cost-discipline tool. Use it when you're about to paste:

- A long file into a Claude Code session
- A repo-tree dump into a prompt envelope
- An API response from a previous tool run
- Any blob whose size you can't eyeball

```bash
ttok < some-file.md
# 12,847

cat some-file.md | ttok
# 12,847

ttok "shorter inline string"
# 5
```

For Anthropic models specifically the tokenizer is approximate (Anthropic doesn't publish their tokenizer; ttok uses tiktoken which is OpenAI's). The number is within ~10% for English prose, less reliable for code or non-English content. Good enough for "is this 3K or 30K?" decisions; not good enough for "is this 28K or 32K?" precision.

### Where Cemini uses it

- Before pasting research-doc content into a `/goal` envelope — confirm it fits within the budget the session has earmarked
- Before deciding whether to dispatch a subagent — if the input is >10K tokens, subagent dispatch usually wins (`@concepts/subagent-orchestration.md`)
- When auditing a session's per-turn cost — pipe a turn's input through ttok to see what was actually billed

### Where ttok doesn't help

- Counting cached tokens — tokens served from the prompt cache are billed at ~10% the normal rate (`@concepts/token-economics-and-prompt-caching.md`); ttok counts tokens, not cache state.
- Anthropic-specific tokenization edge cases — for precise Anthropic billing, the only ground truth is the API response's `usage` field.

### Companion ranking

For Cemini's Claude Code stack, ttok lives alongside:

- `@entities/tools/lazy-tool.md` (cuts MCP-tool-catalog tokens)
- `@entities/tools/claude-code-router.md` (cuts model-cost via routing)
- `@entities/tools/claude-mem.md` (compresses session memory; sibling concern)
- `@entities/tools/claude-code-ultimate-guide.md` (tracks the broader CC reference catalog)

It's the cheapest member of that family — and the easiest to install.

## Dead Ends

- **Trusting ttok numbers as ground truth for Anthropic billing** — within ~10% is good for decisions, not precise. Use the API's `usage` field for billing reconciliation.
- **Counting tokens after the fact** — the value is in *previewing*. Post-hoc counting is just a slower way to read the API receipt.
