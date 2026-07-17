# Hallmark

**An anti-AI-slop design skill for Claude Code.** Makes the UIs Claude generates look *made*, not *generated*. Powered by Together AI.

## Overview

Hallmark is an opinionated design skill that refuses the on-distribution defaults every LLM was trained into. For each brief it picks a **macrostructure**, dresses it in one of **twenty themes** (plus a quiet custom branch for briefs with real creative intent), runs **57 slop-test gates** and a pre-emit self-critique, then hands back self-contained HTML + CSS.

The differentiator is **structural variety, not just visual variety**: two pages Hallmark builds for two different briefs feel like different sites, not colour-swaps of the same hero → 3-feature → CTA → footer template.

## Four verbs

| Invocation | What it does |
| --- | --- |
| *(default)* | Build new UI. Picks a macrostructure, applies the rule-set, runs the slop test before handing back. |
| `hallmark audit <target>` | Score existing code against the anti-patterns. Ranked punch list, no edits. |
| `hallmark redesign <target>` | Keep copy + IA + brand, rebuild the visual structure with a different fingerprint. |
| `hallmark study <screenshot \| URL>` | Extract the design **DNA** — macrostructure, type-pairing, colour anchor — from a design you admire. Refuses pixel-clones and paid templates. |

## Installation

Install this plugin from the marketplace:

```
/plugin marketplace add jeremylongshore/claude-code-plugins
/plugin install hallmark
```

The skill auto-activates when you ask Claude Code to build or redesign a page, or when you invoke it by name (`hallmark`, `hallmark audit`, `hallmark redesign`, `hallmark study`).

## What's inside

- `skills/hallmark/SKILL.md` — the rule-set and design flow
- `skills/hallmark/references/` — macrostructures, themes, components, genres, typography, colour, the slop test, and the audit/redesign/study verbs

## Credit

Created by [Hassan El Mghari (nutlope)](https://github.com/nutlope) and Together AI. Source: [github.com/nutlope/hallmark](https://github.com/nutlope/hallmark) · [usehallmark.com](https://www.usehallmark.com). Licensed under MIT.
