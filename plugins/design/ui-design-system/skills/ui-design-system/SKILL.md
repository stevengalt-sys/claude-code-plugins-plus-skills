---
name: ui-design-system
description: |
  UI design system toolkit for Senior UI Designer including design token generation,
  component documentation, responsive design calculations, and developer handoff tools.
  Use when user asks to: generate design tokens, create color palette, build typography
  scale, calculate spacing system, create design system, generate CSS variables, export
  SCSS tokens, set up component architecture, document component library, calculate
  responsive breakpoints, prepare developer handoff, convert brand color to palette,
  check WCAG contrast, or build 8pt grid system.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, TodoWrite
version: 1.0.0
author: Intent Solutions
license: MIT
---

# UI Design System Toolkit

Generate design tokens, create color palettes, calculate typography scales, build component systems, and prepare developer handoff documentation.

## Capabilities

### 1. Generate Design Tokens

Generate a complete design token system from a brand color using the included Python script.

**Usage:**
```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/design_token_generator.py "<hex_color>" <style> <format>
```

**Arguments:**
- `hex_color` - Primary brand color (e.g., `#0066CC`)
- `style` - `modern` | `classic` | `playful` (default: `modern`)
- `format` - `json` | `css` | `scss` | `summary` (default: `json`)

**Generated token categories:**
- **Colors**: primary, secondary, neutral (10-step scales), semantic (success/warning/error/info), surface
- **Typography**: fontFamily (sans/serif/mono), fontSize (xs-5xl, 1.25 ratio), fontWeight, lineHeight, letterSpacing
- **Spacing**: 8pt grid system (0-64px), semantic naming (xs-3xl)
- **Sizing**: container, button, input, icon sizes with sm/md/lg variants
- **Borders**: radius (style-dependent), width
- **Shadows**: none through 2xl + inner (style-dependent rendering)
- **Animation**: duration (instant-slowest), easing curves
- **Breakpoints**: xs (0) through 2xl (1280px)
- **Z-index**: base through notification layering
- **Accessibility**: WCAG contrast ratios, AA/AAA compliance, recommended contrast color

### 2. Create Component System

Structure a component library using atomic design methodology:

| Level | Components | Token Dependencies |
|-------|-----------|-------------------|
| Atoms | Button, Input, Icon, Label, Badge | colors, sizing, borders, shadows, typography |
| Molecules | FormField, SearchBar, Card, ListItem | atoms + spacing, layout |
| Organisms | Header, Footer, DataTable, Modal | molecules + z-index, animation |
| Templates | DashboardLayout, AuthLayout | organisms + breakpoints, container |

**Size variants:** sm (32px), md (40px), lg (48px)
**Color variants:** primary, secondary, ghost
**States:** hover, active, focus, disabled

### 3. Responsive Design Calculations

**Breakpoints:**

| Name | Width | Target |
|------|-------|--------|
| xs | 0px | Small phones |
| sm | 480px | Large phones |
| md | 640px | Tablets |
| lg | 768px | Small laptops |
| xl | 1024px | Desktops |
| 2xl | 1280px | Large screens |

**Fluid typography formula:** `clamp(min, preferred, max)`

```css
--fluid-h1: clamp(2rem, 1rem + 3.6vw, 4rem);
--fluid-h2: clamp(1.75rem, 1rem + 2.3vw, 3rem);
--fluid-h3: clamp(1.5rem, 1rem + 1.4vw, 2.25rem);
--fluid-body: clamp(1rem, 0.95rem + 0.2vw, 1.125rem);
```

**Responsive spacing:**

| Token | Mobile | Tablet | Desktop |
|-------|--------|--------|---------|
| --space-md | 12px | 16px | 16px |
| --space-lg | 16px | 24px | 32px |
| --space-xl | 24px | 32px | 48px |
| --space-section | 48px | 80px | 120px |

### 4. Developer Handoff

Export tokens for framework integration:

- **CSS** - Custom properties in `:root`
- **SCSS** - Variables with `$` prefix
- **JSON** - For Figma Tokens Studio, Tailwind config, styled-components

**Framework integration patterns:**
- React + CSS Variables
- Tailwind CSS theme config
- styled-components / Emotion theme
- Figma Tokens Studio sync

### 5. WCAG Accessibility Checks

- AA: 4.5:1 normal text, 3:1 large text
- AAA: 7:1 normal text, 4.5:1 large text
- Large text: >=18pt regular or >=14pt bold
- Touch targets: >=44x44px minimum

### Style Presets

| Aspect | Modern | Classic | Playful |
|--------|--------|---------|---------|
| Sans Font | Inter | Helvetica | Poppins |
| Mono Font | Fira Code | Courier | Source Code Pro |
| Default Radius | 8px | 4px | 16px |
| Shadow Style | Layered, subtle | Single layer | Soft, pronounced |

## Reference Files

Detailed guides available in `${CLAUDE_PLUGIN_ROOT}/references/`:
- `token-generation.md` - Color algorithms, HSV space, WCAG contrast, type scales
- `component-architecture.md` - Atomic design, naming conventions, props patterns
- `responsive-calculations.md` - Breakpoints, fluid typography, grid systems
- `developer-handoff.md` - Export formats, framework setup, Figma sync
