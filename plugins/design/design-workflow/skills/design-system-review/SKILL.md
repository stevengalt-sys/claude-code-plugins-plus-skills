---
name: design-system-review
description: |
  Review component libraries and design systems for consistency, completeness, and naming conventions.
  Use when auditing design tokens, component APIs, documentation quality, or system architecture.
  Trigger phrases: "review design system", "audit component library", "check naming conventions", "design token review", "component consistency".
allowed-tools: Read, Glob, Grep, Bash(npx:*)
version: 1.0.0
author: Claude Code Plugin Hub <[email protected]>
---

# Design System Review

Audit design systems and component libraries for consistency, completeness, naming, and documentation quality.

## Audit Dimensions

### 1. Component Inventory
Catalog what exists and identify gaps:
- List all components with their variants
- Map components to usage frequency
- Identify missing primitives (does the system have buttons but no links?)
- Check for redundant components (multiple ways to do the same thing)

### 2. Naming Conventions
Evaluate naming consistency:
- **Components**: PascalCase, descriptive (`PrimaryButton` vs `Btn1`)
- **Props/Variants**: camelCase, consistent patterns (`size="sm"` vs `size="small"` — pick one)
- **Tokens**: Semantic naming (`color-text-primary` not `color-blue-500`)
- **Files**: Match component names to file names

### 3. Token Architecture
Review design tokens for:
- **Color**: Primitive → Semantic → Component token layers
- **Typography**: Scale consistency (is the ratio between steps consistent?)
- **Spacing**: Systematic scale (4px, 8px, 12px, 16px, 24px, 32px, 48px)
- **Elevation**: Shadow hierarchy matches visual importance
- **Animation**: Consistent duration and easing curves

### 4. Component API Consistency
Check that similar components have similar APIs:
- Do all size-able components use the same size prop values?
- Are callback props named consistently (`onClick`, `onChange`)?
- Is the variant pattern consistent across components?
- Are default values sensible and documented?

### 5. Accessibility Compliance
Verify built-in accessibility:
- Do interactive components handle keyboard navigation?
- Are ARIA attributes properly applied?
- Do components support `aria-label` and `aria-describedby`?
- Is focus management handled for modals, popovers, and dropdowns?

### 6. Documentation Quality
Evaluate docs for each component:
- Does it explain when to use (and when not to use) the component?
- Are all props documented with types and defaults?
- Are there live examples for each variant?
- Are accessibility guidelines included?
- Is there migration guidance for breaking changes?

## Output Format

```
## Design System Audit Report

### Summary
- Components audited: X
- Issues found: X (Y critical, Z warnings)
- Coverage score: X/100

### Critical Issues
1. [Issue with impact and fix]

### Warnings
1. [Issue with recommendation]

### Component Inventory
| Component | Variants | Props | Docs | A11y | Status |
|-----------|----------|-------|------|------|--------|
| Button    | 4        | 8     | Yes  | Yes  | OK     |

### Token Review
- Color tokens: X defined, Y semantic
- Typography scale: [assessment]
- Spacing scale: [assessment]

### Recommendations
1. [Priority-ordered improvements]
```

## Common Patterns to Flag

- **Inconsistent spacing**: Components using magic numbers instead of tokens
- **Color overrides**: Hardcoded colors instead of semantic tokens
- **Missing states**: Components without disabled, loading, error, or empty states
- **Typography drift**: Text styles not using the type scale
- **z-index chaos**: No systematic elevation scale
