---
name: design-wireframe-planner
description: |
  Plan wireframes and screen layouts with content hierarchy, component placement,
  and user flow annotations. Use when planning UI screens, page layouts, or
  interaction flows before visual design.
  Trigger with phrases like 'wireframe', 'screen layout', 'page layout', 'UI plan', 'mockup plan', 'lo-fi design'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Design Wireframe Planner

## Overview

Creates detailed wireframe plans with ASCII layout sketches, content hierarchy, component placement, interaction annotations, and user flow connections. Bridges the gap between requirements and visual design.

## Prerequisites

- Feature requirements or user stories
- Target device/viewport (desktop, tablet, mobile)
- Existing design patterns or component library (if available)

## Instructions

1. Identify the screen's primary purpose and user goal
2. List all content elements and prioritize by importance
3. Define the content hierarchy: primary, secondary, tertiary
4. Create an ASCII wireframe showing component placement and proportions
5. Annotate interactive elements with their behavior
6. Specify responsive adaptations for different viewports
7. Map navigation and user flow connections to other screens
8. Note edge cases: empty states, loading states, error states, overflow

## Output Format

```markdown
# Wireframe: [Screen Name]

**Purpose:** [What the user accomplishes here]
**Entry Points:** [How users arrive at this screen]
**Device:** [Desktop / Tablet / Mobile]

## Content Hierarchy
1. **Primary:** [Most important element]
2. **Secondary:** [Supporting content]
3. **Tertiary:** [Additional context]

## Layout (Desktop)
\```
┌──────────────────────────────────────────┐
│  Logo    [ Nav Item ] [ Nav Item ] [User]│
├──────────────────────────────────────────┤
│                                          │
│  ┌─ Page Title ──────────────────────┐   │
│  │  Subtitle / Breadcrumb            │   │
│  └───────────────────────────────────┘   │
│                                          │
│  ┌─ Main Content ─────┐  ┌─ Sidebar ─┐  │
│  │                     │  │           │  │
│  │  [Component A]      │  │ [Filters] │  │
│  │  [Component B]      │  │ [Summary] │  │
│  │                     │  │           │  │
│  └─────────────────────┘  └───────────┘  │
│                                          │
│  ┌─ Footer ──────────────────────────┐   │
│  │  Links    Links    Links          │   │
│  └───────────────────────────────────┘   │
└──────────────────────────────────────────┘
\```

## Layout (Mobile)
\```
┌─────────────────────┐
│  Logo    [≡ Menu]   │
├─────────────────────┤
│  Page Title         │
│  Subtitle           │
│                     │
│  [Filters ▼]        │
│                     │
│  [Component A]      │
│  [Component B]      │
│                     │
│  [Summary]          │
│                     │
│  Footer             │
└─────────────────────┘
\```

## Interactions
| Element | Action | Behavior | Target |
|---------|--------|----------|--------|

## Edge Cases
| State | Display |
|-------|---------|
| Empty | [What shows when no data] |
| Loading | [Skeleton / spinner placement] |
| Error | [Error message location and content] |
| Overflow | [Behavior when content exceeds space] |

## Flow Connections
- [Action] → navigates to [Screen]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Unclear requirements | Feature spec is vague | Ask for user stories with acceptance criteria |
| Too many elements | Screen is overloaded | Prioritize by user goal and move secondary items to progressive disclosure |
| No responsive plan | Only one viewport considered | Always plan at least desktop and mobile layouts |

## Examples

**Example: Settings Page Wireframe**
Request: "Plan a wireframe for the account settings page"
Result: ASCII layouts for desktop and mobile with tabbed sections, form fields, save/cancel actions, and validation state annotations

**Example: Search Results Wireframe**
Request: "Design the layout for our product search results page"
Result: Layout with filter sidebar, result cards, pagination, empty state, and sort controls with responsive stacking for mobile
