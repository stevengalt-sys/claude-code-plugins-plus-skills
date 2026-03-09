---
name: design-system-spec
description: |
  Create design system specifications with tokens, component inventories, and
  usage guidelines. Use when defining or documenting a design system, component
  library, or style guide for a product.
  Trigger with phrases like 'design system', 'component spec', 'style guide', 'design tokens', 'component library'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Design System Spec

## Overview

Creates comprehensive design system specifications covering design tokens, component inventory, usage guidelines, and accessibility requirements. Produces implementation-ready documentation for developers and designers.

## Prerequisites

- Brand guidelines or existing visual identity (colors, typography)
- Target platforms (web, mobile, both)
- Existing component inventory if migrating or extending

## Instructions

1. Define design tokens: colors, typography, spacing, elevation, border radius, breakpoints
2. Establish a naming convention for tokens (semantic vs. primitive)
3. Inventory all components with their variants, states, and sizes
4. Specify component anatomy: required props, optional props, slots/children
5. Document interaction states: default, hover, focus, active, disabled, loading, error
6. Define accessibility requirements per component (ARIA roles, keyboard nav, contrast)
7. Provide do/don't usage examples for each component
8. Specify responsive behavior and breakpoint adaptations

## Output Format

```markdown
# Design System: [Name]

**Version:** [Semver]
**Platforms:** [Web / iOS / Android]
**Last Updated:** [Date]

## Design Tokens

### Colors
| Token | Value | Usage |
|-------|-------|-------|
| `color-primary` | #2563EB | Primary actions, links |
| `color-primary-hover` | #1D4ED8 | Primary hover state |

### Typography
| Token | Value | Usage |
|-------|-------|-------|
| `font-heading-1` | 32px/40px, 700 | Page titles |

### Spacing
| Token | Value |
|-------|-------|
| `space-xs` | 4px |
| `space-sm` | 8px |

## Components

### [Component Name]
**Category:** [Navigation / Input / Feedback / Layout]

#### Variants
| Variant | Description | Use When |
|---------|-------------|----------|

#### Props
| Prop | Type | Default | Required | Description |
|------|------|---------|----------|-------------|

#### States
| State | Visual Change | Behavior |
|-------|--------------|----------|

#### Accessibility
- **Role:** [ARIA role]
- **Keyboard:** [Tab, Enter, Escape behaviors]
- **Contrast:** [Minimum ratio]

#### Do / Don't
- Do: [Correct usage]
- Don't: [Common misuse]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Inconsistent tokens | Ad-hoc values used instead of tokens | Audit existing code for hardcoded values and map to tokens |
| Missing states | Component lacks disabled or error state | Enumerate all interaction states for every component |
| Accessibility gaps | No ARIA or keyboard spec | Add WCAG 2.1 AA requirements for each interactive component |

## Examples

**Example: SaaS Product Design System**
Request: "Create a design system spec for our B2B dashboard application"
Result: Token definitions, 15-component inventory with variants, accessibility specs, and responsive breakpoint rules

**Example: Mobile App Style Guide**
Request: "Document the design system for our iOS and Android app"
Result: Platform-specific tokens, native component mappings, touch target sizes, and dark mode token overrides
