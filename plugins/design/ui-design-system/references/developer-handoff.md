# Developer Handoff Reference

## Token Export Formats

### CSS Custom Properties

```bash
python scripts/design_token_generator.py "#0066CC" modern css > design-tokens.css
```

Output structure:
```css
:root {
  /* Colors */
  --color-primary-50: #f0f7ff;
  --color-primary-500: #0066cc;
  --color-primary-900: #001a33;

  /* Typography */
  --font-fontFamily-sans: Inter, system-ui, sans-serif;
  --font-fontSize-base: 16px;

  /* Spacing */
  --space-4: 16px;

  /* Shadows, Borders, Animation... */
}
```

### SCSS Variables

```bash
python scripts/design_token_generator.py "#0066CC" modern scss > _design-tokens.scss
```

Output structure:
```scss
$color-primary-500: #0066cc;
$font-fontSize-base: 16px;
$space-4: 16px;
$shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
```

### JSON (for tooling)

```bash
python scripts/design_token_generator.py "#0066CC" modern json > design-tokens.json
```

Structured object with nested categories for programmatic access.

## Framework Integration

### React + CSS Variables

```tsx
// Import tokens at app root
import './design-tokens.css';

// Use in components
function Button({ variant = 'primary', size = 'md', children }) {
  return (
    <button className={`btn btn-${variant} btn-${size}`}>
      {children}
    </button>
  );
}
```

### Tailwind CSS

```javascript
// tailwind.config.js
const tokens = require('./design-tokens.json');

module.exports = {
  theme: {
    colors: {
      primary: tokens.colors.primary,
      secondary: tokens.colors.secondary,
      neutral: tokens.colors.neutral,
      success: tokens.colors.semantic.success.base,
      warning: tokens.colors.semantic.warning.base,
      error: tokens.colors.semantic.error.base,
    },
    fontFamily: {
      sans: [tokens.typography.fontFamily.sans],
      serif: [tokens.typography.fontFamily.serif],
      mono: [tokens.typography.fontFamily.mono],
    },
    borderRadius: tokens.borders.radius,
    boxShadow: tokens.shadows,
  },
};
```

### styled-components / Emotion

```typescript
// theme.ts
import tokens from './design-tokens.json';

export const theme = {
  colors: tokens.colors,
  fonts: tokens.typography.fontFamily,
  fontSizes: tokens.typography.fontSize,
  space: tokens.spacing,
  radii: tokens.borders.radius,
  shadows: tokens.shadows,
};

// Usage in component
const Card = styled.div`
  background: ${({ theme }) => theme.colors.surface.card};
  border-radius: ${({ theme }) => theme.radii.lg};
  padding: ${({ theme }) => theme.space['6']};
  box-shadow: ${({ theme }) => theme.shadows.sm};
`;
```

### Vue 3

```javascript
// main.js
import './design-tokens.css';

// In components, use CSS variables directly
// <style scoped>
// .card {
//   background: var(--color-surface-card);
//   border-radius: var(--border-radius-lg);
// }
// </style>
```

## Figma Integration

### Tokens Studio Plugin

1. Install "Tokens Studio for Figma" plugin
2. Export tokens as JSON: `python scripts/design_token_generator.py "#brand" modern json > tokens.json`
3. In Figma: Plugins > Tokens Studio > Import > Select `tokens.json`
4. Tokens map to Figma styles automatically

### Sync Workflow

```
design_token_generator.py → tokens.json → Tokens Studio → Figma Styles
                                        ↑
                         Git repo (version controlled)
```

### Manual Figma Setup

If not using Tokens Studio:
1. Create color styles matching token names (e.g., `primary/500`)
2. Create text styles for each typography token
3. Use Auto Layout with spacing tokens
4. Create effect styles for shadows

## Handoff Checklist

### Token Delivery
- [ ] Token files generated in required format (CSS/SCSS/JSON)
- [ ] Files added to project repository
- [ ] Import/require statements added to app entry point

### Build Integration
- [ ] CSS/SCSS tokens included in build pipeline
- [ ] JSON tokens imported where needed
- [ ] No hardcoded values in component styles

### Component Library
- [ ] All components use design tokens exclusively
- [ ] Size variants (sm/md/lg) implemented
- [ ] Color variants match token palette
- [ ] States (hover/active/focus/disabled) use token values
- [ ] Transitions use animation tokens

### Quality Assurance
- [ ] WCAG AA contrast verified for all text/background combinations
- [ ] Focus indicators visible on all interactive elements
- [ ] Touch targets meet 44×44px minimum
- [ ] Responsive behavior tested at all breakpoints
- [ ] Dark mode tokens defined (if applicable)

### Documentation
- [ ] Token naming convention documented
- [ ] Component API documented (props, variants, states)
- [ ] Usage examples provided
- [ ] Figma styles synced with code tokens
