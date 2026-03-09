---
name: dev-handoff
description: |
  Generate developer handoff documentation from designs including specs, implementation notes, component breakdowns, and interaction details.
  Use when preparing designs for development, writing implementation specs, or documenting component behavior.
  Trigger phrases: "developer handoff", "create dev specs", "implementation notes", "design to dev", "component specs".
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: Claude Code Plugin Hub <[email protected]>
---

# Developer Handoff

Generate clear, complete developer handoff documentation that bridges design and implementation.

## Handoff Document Structure

### 1. Component Breakdown
For each UI component in the design:

```
## [Component Name]

**Type**: [New component / Existing component modification / Composition of existing]
**Design system component**: [Map to existing component or note as new]

### Visual Specs
- Width: [fixed/fluid] [value]
- Height: [fixed/auto] [value]
- Padding: [top right bottom left]
- Margin: [top right bottom left]
- Border: [width style color radius]
- Background: [token or value]
- Shadow: [token or value]

### Typography
- Font: [family]
- Size: [value/token]
- Weight: [value/token]
- Line height: [value]
- Color: [token]

### States
| State | Visual Change | Trigger |
|-------|--------------|---------|
| Default | — | — |
| Hover | [changes] | Mouse enter |
| Active | [changes] | Mouse down |
| Focus | [changes] | Keyboard focus |
| Disabled | [changes] | Prop |
| Loading | [changes] | Async state |
| Error | [changes] | Validation |
```

### 2. Layout & Responsive Behavior
Document how the layout responds to viewport changes:

| Breakpoint | Layout | Key Changes |
|-----------|--------|-------------|
| Mobile (<768px) | [description] | [what changes] |
| Tablet (768-1024px) | [description] | [what changes] |
| Desktop (>1024px) | [description] | [what changes] |

### 3. Interaction Specifications
For each interactive element:

```
### [Interaction Name]
**Trigger**: [click/hover/scroll/keyboard/gesture]
**Animation**: [duration]ms [easing] [property]
**Behavior**:
1. [Step-by-step interaction flow]
2. [Include edge cases]

**Accessibility**:
- Keyboard: [how to trigger via keyboard]
- Screen reader: [announcement]
- Focus management: [where focus moves]
```

### 4. Data & Content Requirements
- **Dynamic content**: List all fields that come from APIs or user input
- **Character limits**: Maximum lengths for text fields
- **Empty states**: What to show when there's no data
- **Loading states**: Skeleton screens or spinners
- **Error states**: What to show when things fail

### 5. API & Data Dependencies
- List endpoints needed
- Note any new data not currently available
- Specify loading/error handling per data source

## Handoff Checklist

Before handing off, verify:
- [ ] All component states documented (default, hover, active, focus, disabled, loading, error)
- [ ] Responsive behavior specified for all breakpoints
- [ ] Animation/transition details included (duration, easing, properties)
- [ ] Accessibility requirements noted (keyboard, screen reader, focus)
- [ ] Edge cases covered (long text, missing data, slow connection)
- [ ] Design tokens referenced (not hardcoded values)
- [ ] Assets exported and linked (icons, images, illustrations)
- [ ] Copy is final and approved

## Output Format

Generate the handoff as a structured markdown document that developers can reference during implementation. Include:
1. Overview with screenshots/mockup references
2. Component tree (visual hierarchy)
3. Detailed specs per component
4. Interaction specifications
5. Responsive behavior table
6. Data requirements
7. Open questions or decisions needed
