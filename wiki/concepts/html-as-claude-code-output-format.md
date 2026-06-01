---
title: "HTML as Claude Code's default output format (vs Markdown)"
type: concept
tags: [concept, claude-code, output-format, html, markdown, anthropic-engineering, design-pattern, thariq, k55-2-osint]
keywords: [html-as-output, html-vs-markdown, html-effectiveness, thariq, trq212, claude-blog, information-density, two-way-interaction, claude-code-html]
related:
  - concepts/context-engineering.md
  - concepts/three-cache-architecture.md
  - concepts/skill-vetting.md
  - "@osint-wiki/sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md"
  - "@osint-wiki/entities/people/thariq-trq212.md"
  - concepts/claude-artifacts-app-building.md
  - concepts/agentic-pm-review-artifacts.md
maturity: validated
created: 2026-05-21
updated: 2026-06-01
---

## Relations

- @concepts/context-engineering.md — output-format choice is a context-engineering decision (richness, sharability, two-way interaction)
- @concepts/three-cache-architecture.md — HTML output costs 2-4× more tokens than markdown; relevant tradeoff for the cost-aware authoring layer
- @concepts/skill-vetting.md — Thariq explicitly warns against turning his pattern into a `/html` skill prematurely
- @osint-wiki/sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md — original ingest source (Post 4)
- @osint-wiki/entities/people/thariq-trq212.md — author entity stub

## Raw Concept

What prompted this page: cross-routed from osint-wiki (K55-2 Post.docx ingest 2026-05-21). Thariq Shihipar's essay "Using Claude Code: The Unreasonable Effectiveness of HTML" — Anthropic engineer, also published on the Claude Blog — argues that HTML should replace Markdown as Claude Code's default output format for non-trivial work. Belongs in CCC wiki because it is fundamentally a Claude Code design pattern, not an OSINT financial research artifact.

## Narrative

### The thesis

> Markdown has become the dominant file format used by agents to communicate with us. It's simple, portable, has some rich text capability and is easy for you to edit ... But as agents have become more and more powerful, I have felt that markdown has become a restricting format. I find it difficult to read a markdown file of more than a hundred lines.

Thariq's argument is structural, not stylistic:

1. **Markdown's "easy to edit" advantage erodes** when users stop hand-editing and start prompting Claude to edit. The advantage was for the human author; the new mode is human-as-reviewer.
2. **Claude Code outputs are getting larger** — full implementation plans, comprehensive reviews, multi-source research syntheses. >100-line markdown files do not get read.
3. **HTML provides expressiveness that markdown can only approximate**: tables, CSS-driven design, SVG diagrams, code blocks with syntax highlighting, interactive elements, mobile-responsive layout, embedded canvases, image tags, sliders, knobs.
4. **HTML files are shareable as links** (upload to S3, send URL) — markdown is not natively rendered in most browsers, often requires attaching as a file.
5. **HTML supports two-way interaction** — sliders for adjusting algorithmic parameters, drag-and-drop reordering, copy-as-JSON exports back into prompts.

### Why HTML beats markdown on each axis

| Axis | Markdown | HTML | Verdict |
|------|----------|------|---------|
| **Information density** | Limited to text + ASCII art + maybe tables | Tables + CSS + SVG + JS + canvas + responsive layout | HTML |
| **Reading length tolerance** | Drops sharply past ~100 lines | Visual organization scales to long docs | HTML |
| **Shareability** | File attachments; manual rendering | Upload to S3; send link | HTML |
| **Interactivity** | None (static) | Sliders, knobs, drag-drop, copy-back-to-prompt buttons | HTML |
| **Generation speed** | Fast | 2-4× slower | Markdown |
| **Token cost** | Lower | Higher; offset by 1M context in Opus 4.7 | Markdown (marginal) |
| **Version control** | Clean diffs | Noisy diffs (whitespace, attribute reorder) | Markdown |
| **Default rendering** | Most editors render markdown inline | Browser-only | Markdown |

The conclusion isn't that markdown is wrong — it's that the **default has shifted** as the model's capabilities and the typical Claude Code task grew.

### Use-case taxonomy (from the essay)

Thariq groups HTML output into five families with example prompts:

1. **Specs, planning, exploration** — "Generate 6 distinctly different approaches and lay them out as a single HTML file in a grid so I can compare them side by side"
2. **Code review & understanding** — "Render the actual diff with inline margin annotations, color-code findings by severity"
3. **Design & prototypes** — "Create a HTML file with several sliders and options for me to try different options on this animation, give me a copy button"
4. **Reports, research & learning** — "Produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a 'gotchas' section"
5. **Custom editing interfaces** — "Each ticket as a draggable card across Now / Next / Later / Cut columns ... Add a 'copy as markdown' button"

The unifying pattern: **the HTML file is purpose-built for one specific cognitive task and ends with an export back into prompt-pastable form**.

### The "don't make it a /html skill" warning

Thariq explicitly cautions against immediate skill-ification:

> I'm a little bit afraid that people will read this article and turn it into a /html skill or something. While there might be some value in that, I want to emphasize that you don't need to do much to get Claude to do this. You can just ask it to "make a HTML file" or "make a HTML artifact". The trick is knowing what you want the artifact to do and how you might use it.

This aligns with @concepts/skill-vetting.md — skills should encode hard-won workflow knowledge, not just shortcut a one-line prompt. Premature skill-ification ossifies what should remain fluid.

### Tradeoffs honestly stated

- **2-4× generation time** vs markdown ("but I've found the results are worth it")
- **HTML diffs are noisy** — version control suffers; this is "honestly one of the biggest downsides"
- **Higher token cost** — with 1M context Opus 4.7, "not really noticeable in the context window" in practice
- **Style/taste matching** — solve via a single design-system HTML file generated by pointing Claude at the company's existing codebase, then reference it from other HTML outputs

### Implications for Cemini workflows

The Cemini stack already does some of this — `visual-explainer:*` skills generate HTML output (project recap, slide decks, diff review, fact-check). But the **default mode** of CCC and OSINT workflows is markdown:

- **OSINT wiki authoring** — markdown is the right default for the wiki itself (curated, durable, federation-friendly). HTML would break the wiki's text-grep-able semantic structure.
- **Briefs distributed to claude.ai** — could shift to HTML if downstream consumption is via Claude Desktop / Web (renders inline) rather than as paste-into-prompt.
- **CeminiSuite outputs to /opt/cemini/briefs/** — server-Claude review currently parses markdown; HTML would require a render-step on the server side.
- **Plan / spec docs during long-running work** — Thariq's primary use-case. Direct fit for `/make-plan` outputs, `/visual-explainer:*` upgrades, and engineering-discussion artifacts.

**Recommended posture**: keep the **wiki + brief + log** layer in markdown (durability + grep-ability + cross-wiki link parsing); use HTML on a per-task basis for **plans, code reviews, exploratory designs, and report artifacts** where the artifact is the deliverable and the durability is secondary.

### Reference URLs

- Examples gallery: `https://thariqs.github.io/html-effectiveness`
- Playgrounds post (two-way interaction examples): `https://x.com/trq212/status/2017024445244924382`
- Author handle: `@trq212`
- Published also on the official Claude Blog (per the essay's opening sentence)

## Snippets

> "I've started preferring HTML as an output format instead of Markdown and increasingly see this being used by others on the Claude Code team." [Source: @trq212 / Claude Blog — "Using Claude Code: The Unreasonable Effectiveness of HTML"]

> "I would go so far as to say that there is almost no set of information that Claude can read that you cannot fairly efficiently represent with HTML." [Source: @trq212 / Claude Blog]

> "In practice, I've found I tend to not actually read more than a 100-line markdown file, and I certainly am not able to get anyone else in my organization to read it. But HTML documents are much easier to read." [Source: @trq212 / Claude Blog]

> "The chance of someone actually reading your spec, report or PR writeup is much much higher if it's in HTML." [Source: @trq212 / Claude Blog]

> "While markdown often uses fewer tokens, I've found the added expressiveness of HTML and the much higher likelihood of me reading it means I get overall better output. With the 1MM context window in Opus 4.7, the increased token usage is not really noticeable in the context window." [Source: @trq212 / Claude Blog]

> "I'm a little bit afraid that people will read this article and turn it into a /html skill or something … The trick is knowing what you want the artifact to do and how you might use it. You may over time make a skill, but for now I'd suggest just prompting from scratch to get a hang of how to use it in different cases." [Source: @trq212 / Claude Blog]
