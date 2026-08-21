# CCC — Cemini Claude Code Wiki

Welcome. This is Cemini’s public knowledge hub on **how we operate Cursor and Claude Code** — agent orchestration, context and token economics, MCP servers, hooks, skills, slash commands, and the `/goal` · Ralph · OpenSpec prompting patterns.

Whether you’re forking the wiki, borrowing a workflow, or just curious how a multi-wiki research stack stays coherent: you’re in the right place.

```bash
git clone https://github.com/cemini23/cemini-claude-code-CCC.git
cd "cemini-claude-code-CCC"
```

CCC is the agent-harness meta-wiki in the Cemini federation, alongside `osint-wiki`, `gambling-wiki`, `game-dev-wiki`, `cybersecurity-wiki`, `image-gen-wiki`, `seo-wiki`, and `3d-printing-wiki`.

## Quickstart

```bash
# Lint the wiki
python3 scripts/wiki_lint.py

# Check inbox for duplicates before ingesting
python3 scripts/preingest_check.py
```

Read [`CLAUDE.md`](CLAUDE.md) for the full schema (LLM-facing). Active workstreams live in [`ROADMAP.md`](ROADMAP.md). Meta-lessons live in [`LESSONS.md`](LESSONS.md). Session state lives in `hot.md` (gitignored).

## Structure

- `wiki/` — canonical wiki (markdown + YAML frontmatter)
- `scripts/` — `wiki_lint.py`, `preingest_check.py`, and related maintainers’ tooling
- `prompts/` — reusable prompt templates
- `docs/` — internal phase / harness briefs (not required for casual browsing)
- `briefs/` — staged deliverables (gitignored)
- `raw-sources/` — archived source corpus (gitignored)
- `research to be indexed/` — transient drop zone (gitignored)

## Adding content

1. Drop a new source into `research to be indexed/`
2. Run `python3 scripts/preingest_check.py`
3. Read, discuss takeaways, then create `wiki/sources/<slug>.md` and update related entity/concept pages
4. Update `wiki/index.md` and append to `wiki/log.md`
5. Archive the raw file out of the inbox (`raw-sources/` on a local fork; maintainers also push to egress-fi)
6. Run `python3 scripts/wiki_lint.py` and fix any errors

Full ingest workflow: [`CLAUDE.md`](CLAUDE.md) → Operations.

## Cemini wiki federation

**Eight** wikis + **Cemini Financial Suite** (private trading stack). Cross-links use `@<alias>/path/to/page.md` (see `CLAUDE.md` → Related Wikis). Lint resolves those paths on a maintainer machine with all repos checked out.

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| **`ccc-wiki`** | **This repo** | **Public** | Cursor / Claude Code workflow, MCP, skills, multi-wiki eval prompts (`prompts/`) |
| `osint-wiki` | `llm-wiki-by-cemini` *(private)* | **Private** | Financial research; conductor / librarian architecture canon |
| `gambling-wiki` | [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) | **Public** | Sports betting, casino, poker, DFS, best ball |
| `game-dev-wiki` | [Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki) | **Public** | Hobby game dev — castle/RTS, Godot evals, agent harness |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | Public | Image / video / voice generation |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Public | Local SEO, GEO/AEO, creator marketing |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | Public | FDM/FFF, Bambu, slicers |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Public | Pentest, SOC, certifications |
| *Cemini Financial Suite* | `Cemini-Financial-Suite` *(private)* | **Private** | Production trading stack (not a wiki) |

**Privacy:** **`ccc-wiki` is public** (this repository). **`osint-wiki`** and **Cemini Financial Suite** are private — cross-wiki links to them may appear in prose, but those repos are not public deliverables.

**Canonical prompt:** [prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md](prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md) — revenue-first URL evaluation; co-primary projects include family-tree/genealogy (castle-sim deprioritized), TipDrop.io, XSP, poker arena, CeminiDFS.

## Related

- Products: [Atto](https://youratto.com) · [GuruWatcher](https://guruwatcher.com)
- Newsletter: [Outlier Weekly](https://outlierweekly.substack.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Agent toolkit: [vet](https://github.com/cemini23/vet) · [wikilint](https://github.com/cemini23/wikilint) · [phase0](https://github.com/cemini23/phase0) · [agent-toolkit-demo](https://github.com/cemini23/agent-toolkit-demo) · [ara-schema](https://github.com/cemini23/ara-schema) · [cursor-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/cursor-audit) · [super-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/super-audit)
- Public wikis: [Gambling](https://github.com/cemini23/Gambling-wiki) · [Game Dev](https://github.com/cemini23/Game-Dev-wiki) · [SEO/GEO](https://github.com/cemini23/SEO-GEO-B-M-Wiki) · [Cybersecurity](https://github.com/cemini23/Cybersecurity-wiki) · [3D Printing](https://github.com/cemini23/3D-Printing-Wiki) · [Image Gen](https://github.com/cemini23/uncensored-image-gen-wiki)
- Trading: [world-cup-bot](https://github.com/cemini23/world-cup-bot)
- Donation wallets (canonical): [SUPPORT.md](SUPPORT.md)

## Support

Thank you for your support — stars, issues, shares, and tips all help keep this wiki and the broader Cemini open-research stack alive.

If you’d like to tip, use the **donation-only** addresses below (not trading or production wallets). Prefer following the work? These are the best places to start:

| Project | Link |
|---------|------|
| **Outlier Weekly** (methodology newsletter) | [outlierweekly.substack.com](https://outlierweekly.substack.com) |
| **Atto** — organize Italian family documents on your computer | [youratto.com](https://youratto.com) |
| **GuruWatcher** — Discord alerts for your newsletter’s price levels | [guruwatcher.com](https://guruwatcher.com) |
| **YouTube** | [@Cemini23](https://www.youtube.com/@Cemini23) |

| Chain family | Address |
|--------------|---------|
| **X Money** (fiat, US) | Request [@Cemini23](https://x.com/Cemini23) in the X app — scan the Request QR |
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |
| **Polymarket** (referral) | [polymarket.com/?r=Cemini23](https://polymarket.com/?r=Cemini23) |
| **Hyperliquid** (referral) | [app.hyperliquid.xyz/join/CEMINI23](https://app.hyperliquid.xyz/join/CEMINI23) |

Full wallet note: [SUPPORT.md](SUPPORT.md).

## License

MIT — see [LICENSE](LICENSE).
