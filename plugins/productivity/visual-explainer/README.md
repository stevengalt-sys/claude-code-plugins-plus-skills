# Visual Explainer

Turn complex terminal output into styled HTML pages you actually want to read.

Coding agents default to ASCII art and box-drawing characters for diagrams and
tables. Visual Explainer generates **self-contained HTML** instead — real
typography, dark/light themes, and interactive Mermaid diagrams with zoom and
pan. Every page is a single file with embedded CSS and JS, written to
`~/.agent/diagrams/` and opened in your browser.

## What you get

- **Diagrams** — architecture overviews, flowcharts, sequence/ER/state/class/C4
  diagrams rendered as interactive Mermaid (zoom, pan, click-to-expand).
- **Diff reviews** — a visual, color-coded review of a branch, commit, range, or
  PR with file map, architecture impact, risk review, and a merge recommendation.
- **Plan reviews** — compare an implementation plan against the current codebase.
- **Visual plans** — turn an implementation plan into a readable HTML page.
- **Slide decks** — magazine-quality, one-viewport slides with keyboard nav.
- **Project recaps** — context-switching snapshots of where a project stands.
- **Fact-check** — verify a generated document against the actual code and git
  history.
- **Data tables** — comparisons, audits, and status matrices as semantic HTML.

## Commands

| Command | Description |
|---|---|
| `/generate-web-diagram` | Generate a standalone HTML diagram and open it in the browser |
| `/generate-visual-plan` | Generate a visual implementation plan |
| `/generate-slides` | Generate a slide deck as a self-contained HTML page |
| `/diff-review` | Generate a visual diff review for code changes |
| `/plan-review` | Compare an implementation plan against the current codebase |
| `/project-recap` | Generate a visual project recap for context switching |
| `/fact-check` | Verify a generated document against actual code and git history |

The `visual-explainer` skill also auto-activates whenever output is inherently
visual — a table with 4+ rows or 3+ columns, an architecture request, a diagram,
and so on.

## Installation

### Option 1: Install from Marketplace (Recommended)

```bash
# Step 1: Add the marketplace to Claude Code
/plugin marketplace add jeremylongshore/claude-code-plugins

# Step 2: Install visual-explainer
/plugin install visual-explainer@claude-code-plugins-plus
```

### Option 2: Install directly from the source repository

```bash
/plugin marketplace add nicobailon/visual-explainer
/plugin install visual-explainer@visual-explainer-marketplace
```

## Requirements

A browser to view generated HTML. Optional `surf-cli` for AI image generation in
hero banners and conceptual illustrations.

## Credits

Created and maintained by [nicobailon](https://github.com/nicobailon).
Source: <https://github.com/nicobailon/visual-explainer>. Licensed under MIT (see
`LICENSE`). Mirrored into this marketplace with attribution.
