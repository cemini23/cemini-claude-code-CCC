# CCC — Cemini Claude Code Wiki

Public knowledge hub on **how Cemini operates Cursor and Claude Code** — agent orchestration, context/token economics, MCP servers, hooks, skills, slash commands, and the `/goal` · Ralph · OpenSpec prompting patterns.

```bash
git clone https://github.com/cemini23/cemini-claude-code-CCC.git
cd "cemini-claude-code-CCC"
```

Agent-harness meta-wiki in the Cemini federation alongside `osint-wiki`, `gambling-wiki`, `cybersecurity-wiki`, `image-gen-wiki`, `seo-wiki`, and `3d-printing-wiki`.

## Quickstart

```bash
# Lint the wiki
python3 scripts/wiki_lint.py

# Check inbox for duplicates before ingesting
python3 scripts/preingest_check.py
```

Read `CLAUDE.md` for the full schema (LLM-facing). Active workstreams live in `ROADMAP.md`. Meta-lessons live in `LESSONS.md`. Session state lives in `hot.md` (gitignored).

## Structure

- `wiki/` — canonical wiki (markdown + YAML frontmatter)
- `scripts/` — `wiki_lint.py`, `preingest_check.py`
- `briefs/` — staged deliverables (gitignored)
- `raw-sources/` — archived source corpus (gitignored)
- `research to be indexed/` — transient drop zone (gitignored)
- `prompts/` — reusable prompt templates

## Adding content

1. Drop new source into `research to be indexed/`
2. `python3 scripts/preingest_check.py`
3. Read, discuss, then create `wiki/sources/<slug>.md` + touch related entity/concept pages
4. Update `wiki/index.md` + append to `wiki/log.md`
5. Move file to `raw-sources/`
6. `python3 scripts/wiki_lint.py` — fix any errors

Full ingest workflow in `CLAUDE.md` § Operations.

## Cemini wiki federation

**Seven** wikis + **Cemini Financial Suite** (private trading stack). Cross-links: `@<alias>/path/to/page.md` (`CLAUDE.md` → Related Wikis). Lint resolves paths on a maintainer machine with all repos checked out.

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| **`ccc-wiki`** | **This repo** | **Public** | Cursor / Claude Code workflow, MCP, skills, multi-wiki eval prompts (`prompts/`) |
| `osint-wiki` | `llm-wiki-by-cemini` *(private)* | **Private** | Financial research; conductor / librarian architecture canon |
| `gambling-wiki` | [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) | **Public** | Sports betting, casino, poker, DFS, best ball |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | Public | Image / video / voice generation |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Public | Local SEO, GEO/AEO, creator marketing |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | Public | FDM/FFF, Bambu, slicers |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Public | Pentest, SOC, certifications |
| *Cemini Financial Suite* | `Cemini-Financial-Suite` *(private)* | **Private** | Production trading stack (not a wiki) |

**Privacy:** **`ccc-wiki` is public** (this repository). **`osint-wiki`** and **Cemini Financial Suite** are private — cross-wiki links to them appear in prose but those repos are not public deliverables.

**Canonical prompt:** [prompts/deep-research-multi-wiki-eval-v6-2026-05-31.md](prompts/deep-research-multi-wiki-eval-v6-2026-05-31.md) — eight-surface URL evaluation (includes `gambling-wiki`; Gemini Deep Research + Cursor spot-check).

## Related

- Methodology newsletter: [Outlier Weekly](https://outlierweekly.substack.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Agent toolkit: [vet](https://github.com/cemini23/vet) · [wikilint](https://github.com/cemini23/wikilint) · [phase0](https://github.com/cemini23/phase0) · [agent-toolkit-demo](https://github.com/cemini23/agent-toolkit-demo) · [ara-schema](https://github.com/cemini23/ara-schema) · [cursor-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/cursor-audit) · [super-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/super-audit)
- Public wikis: [Gambling](https://github.com/cemini23/Gambling-wiki) · [SEO/GEO](https://github.com/cemini23/SEO-GEO-B-M-Wiki) · [Cybersecurity](https://github.com/cemini23/Cybersecurity-wiki) · [3D Printing](https://github.com/cemini23/3D-Printing-Wiki) · [Image Gen](https://github.com/cemini23/uncensored-image-gen-wiki)
- Trading: [world-cup-bot](https://github.com/cemini23/world-cup-bot)
- Donation wallets (canonical): [SUPPORT.md](SUPPORT.md)


## Support

Voluntary tips fund open research and tooling. **Donation-only addresses** — not trading or production wallets.

| Chain family | Address |
|--------------|---------|
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |


## License

MIT — see [LICENSE](LICENSE).
