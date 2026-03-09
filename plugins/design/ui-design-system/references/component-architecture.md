# Component Architecture Reference

## Atomic Design Methodology

### Hierarchy

```
Atoms → Molecules → Organisms → Templates → Pages
```

| Level | Definition | Examples |
|-------|-----------|---------|
| Atoms | Smallest UI elements, single purpose | Button, Input, Icon, Label, Badge, Avatar |
| Molecules | Groups of atoms working together | FormField, SearchBar, Card, ListItem, Tooltip |
| Organisms | Complex sections of UI | Header, Footer, DataTable, Modal, Sidebar |
| Templates | Page-level layouts | DashboardLayout, AuthLayout, SettingsLayout |
| Pages | Template instances with real data | Dashboard, Login, UserProfile |

### Naming Convention

```
[Level]-[Component]-[Variant]

Examples:
  atom-button-primary
  molecule-form-field-error
  organism-data-table-sortable
  template-dashboard-sidebar
```

## Component Props Pattern

### Base Props Interface

```typescript
interface BaseComponentProps {
  className?: string;
  children?: React.ReactNode;
  id?: string;
  testId?: string;
}
```

### Size Variants

```typescript
type Size = 'sm' | 'md' | 'lg';

const sizeMap = {
  sm: { height: '32px', paddingX: '12px', fontSize: '14px' },
  md: { height: '40px', paddingX: '16px', fontSize: '16px' },
  lg: { height: '48px', paddingX: '20px', fontSize: '18px' },
};
```

### Color Variants

```typescript
type Variant = 'primary' | 'secondary' | 'ghost' | 'danger';

const variantMap = {
  primary:   { bg: 'primary-500', text: 'white', hover: 'primary-600' },
  secondary: { bg: 'neutral-100', text: 'neutral-900', hover: 'neutral-200' },
  ghost:     { bg: 'transparent', text: 'neutral-700', hover: 'neutral-100' },
  danger:    { bg: 'error-base', text: 'white', hover: 'error-dark' },
};
```

## State Management

### Interactive States

| State | Visual Change | Token Applied |
|-------|--------------|---------------|
| Default | Base appearance | variant base tokens |
| Hover | Slight darkening/highlight | variant hover token |
| Active/Pressed | Further darkening | variant -700 shade |
| Focus | Visible ring outline | --color-ring + offset |
| Disabled | Reduced opacity | opacity: 0.5, cursor: not-allowed |
| Loading | Spinner replaces content | animation tokens |

### Focus Indicators

```css
/* Visible focus ring for keyboard navigation */
:focus-visible {
  outline: 2px solid var(--color-ring);
  outline-offset: 2px;
}

/* Remove default outline for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}
```

## Token-to-Component Mapping

### Button

```css
.btn {
  font-family: var(--font-fontFamily-sans);
  font-weight: var(--font-fontWeight-medium);
  border-radius: var(--border-radius-default);
  transition-duration: var(--animation-duration-normal);
  transition-timing-function: var(--animation-easing-easeInOut);
}

.btn-sm {
  height: 32px;
  padding: 0 var(--space-3);
  font-size: var(--font-fontSize-sm);
}

.btn-md {
  height: 40px;
  padding: 0 var(--space-4);
  font-size: var(--font-fontSize-base);
}

.btn-lg {
  height: 48px;
  padding: 0 var(--space-5);
  font-size: var(--font-fontSize-lg);
}
```

### Input

```css
.input {
  font-family: var(--font-fontFamily-sans);
  border: var(--border-width-default) solid var(--color-surface-input);
  border-radius: var(--border-radius-default);
  background: var(--color-surface-background);
  transition-duration: var(--animation-duration-normal);
}

.input:focus {
  border-color: var(--color-surface-ring);
  box-shadow: 0 0 0 2px var(--color-primary-200);
}
```

### Card

```css
.card {
  background: var(--color-surface-card);
  color: var(--color-surface-cardForeground);
  border: var(--border-width-default) solid var(--color-surface-border);
  border-radius: var(--border-radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
}
```

## Accessibility Requirements

- All interactive elements must have visible focus indicators
- Touch targets minimum 44×44px
- Color must not be the only means of conveying information
- Use semantic HTML elements (`<button>`, `<input>`, `<nav>`)
- Include ARIA labels where visual labels are absent
- Support keyboard navigation (Tab, Enter, Escape, Arrow keys)
