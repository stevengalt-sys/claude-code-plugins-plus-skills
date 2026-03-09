---
name: create-design-system
description: Create a design system specification with tokens, components, and guidelines
arguments:
  - name: product
    description: The product or application to create a design system for
    required: true
---

Create a comprehensive design system specification for: $ARGUMENTS.product

Follow the design-system-spec skill guidelines. Include:
1. Design tokens (colors, typography, spacing, elevation, breakpoints)
2. Component inventory with variants, props, and states
3. Interaction state definitions for each component
4. Accessibility requirements (ARIA, keyboard, contrast)
5. Do/don't usage examples
6. Responsive behavior rules

Output as a polished Markdown specification ready for developer and designer use.
