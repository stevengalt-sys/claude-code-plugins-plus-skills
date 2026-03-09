# Design Workflow

A comprehensive design productivity plugin for Claude Code. Accelerates design workflows including critique, design system management, UX writing, accessibility audits, research synthesis, and developer handoff.

Works standalone with descriptions or screenshots, and becomes more powerful when connected to Figma or other design tools via MCP.

Inspired by [Anthropic's knowledge-work-plugins design plugin](https://github.com/anthropics/knowledge-work-plugins/tree/main/design).

## Skills (auto-activate when relevant)

| Skill | Triggers on |
|-------|-------------|
| **design-critique** | Design review, UI feedback, visual hierarchy analysis |
| **ux-writing** | Interface copy, microcopy, error messages, button labels |
| **design-system-review** | Component library audit, naming conventions, consistency checks |
| **research-synthesis** | User research analysis, interview synthesis, insight extraction |
| **dev-handoff** | Design specs, implementation notes, component documentation |

## Commands

| Command | Description |
|---------|-------------|
| `/design-critique` | Get structured feedback on a design |
| `/accessibility-audit` | Run a WCAG accessibility audit |
| `/ux-copy-review` | Review and improve interface copy |
| `/design-system-audit` | Audit component library consistency |
| `/dev-handoff` | Generate developer handoff documentation |

## Getting Started

1. Install the plugin
2. Share a design via screenshot, Figma link, or text description
3. Use slash commands for explicit actions, or let skills activate automatically

## Connectors

For enhanced functionality, connect design tools via MCP servers:

- **Figma** — Pull design data, components, and styles directly
- **Storybook** — Access component documentation and variants
- **Zeplin / InVision** — Sync design specs and assets

## Contributors

- Claude Code Plugin Hub
