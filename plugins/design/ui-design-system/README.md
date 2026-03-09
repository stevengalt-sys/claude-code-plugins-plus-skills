# UI Design System Toolkit

A comprehensive design system toolkit for generating design tokens, building component architectures, calculating responsive layouts, and preparing developer handoff documentation.

## Features

- **Design Token Generation** - Generate complete token systems (colors, typography, spacing, shadows, borders, animation) from a single brand color
- **Component Architecture** - Atomic design methodology with size/color variants and state management
- **Responsive Design** - Fluid typography, breakpoint system, responsive spacing calculations
- **Developer Handoff** - Export to CSS, SCSS, JSON with framework integration guides (React, Tailwind, Vue, styled-components)
- **WCAG Accessibility** - Contrast ratio checking, AA/AAA compliance validation

## Quick Start

### Generate Design Tokens

```bash
# JSON output (default)
python scripts/design_token_generator.py "#0066CC"

# CSS custom properties
python scripts/design_token_generator.py "#0066CC" modern css

# SCSS variables
python scripts/design_token_generator.py "#8B4513" classic scss

# Summary view
python scripts/design_token_generator.py "#FF6B6B" playful summary
```

### Style Presets

| Style | Sans Font | Radius | Shadows |
|-------|-----------|--------|---------|
| modern | Inter | 8px | Layered, subtle |
| classic | Helvetica | 4px | Single layer |
| playful | Poppins | 16px | Soft, pronounced |

### Token Categories

- **Colors**: Primary, secondary, neutral (10-step scales), semantic, surface
- **Typography**: Font families, size scale (1.25 ratio), weights, line heights
- **Spacing**: 8pt grid system (0-64px) with semantic naming
- **Borders**: Style-dependent radius, width scale
- **Shadows**: 8 levels from none to 2xl
- **Animation**: Duration and easing tokens
- **Breakpoints**: xs through 2xl (0-1280px)
- **Z-index**: Layered from base to notification

## Installation

```
/plugin marketplace add jeremylongshore/claude-code-plugins
```

## Contributors

- Intent Solutions

## License

MIT
