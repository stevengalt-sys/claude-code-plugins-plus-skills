# Responsive Design Calculations Reference

## Breakpoint System

| Name | Width | Media Query | Target Device |
|------|-------|-------------|---------------|
| xs | 0px | default | Small phones (320px+) |
| sm | 480px | `@media (min-width: 480px)` | Large phones |
| md | 640px | `@media (min-width: 640px)` | Tablets (portrait) |
| lg | 768px | `@media (min-width: 768px)` | Tablets (landscape), small laptops |
| xl | 1024px | `@media (min-width: 1024px)` | Desktops |
| 2xl | 1280px | `@media (min-width: 1280px)` | Large screens |

### CSS Implementation

```css
/* Mobile-first approach */
.container { padding: var(--space-4); }

@media (min-width: 480px) { .container { padding: var(--space-6); } }
@media (min-width: 640px) { .container { padding: var(--space-8); } }
@media (min-width: 768px) { .container { max-width: 720px; margin: 0 auto; } }
@media (min-width: 1024px) { .container { max-width: 960px; } }
@media (min-width: 1280px) { .container { max-width: 1200px; } }
```

## Fluid Typography

### Clamp Formula

```
font-size: clamp(min, preferred, max);
```

Where preferred uses viewport units:
```
preferred = min + (max - min) × ((100vw - minViewport) / (maxViewport - minViewport))
```

### Simplified Calculation

For a range between 320px and 1200px viewport:

```
preferred = minSize + (maxSize - minSize) × (100vw - 320px) / (1200px - 320px)
```

Convert to rem + vw:
```
preferred = (minRem) + ((maxPx - minPx) / (1200 - 320)) × 100vw
```

### Pre-calculated Fluid Scales

```css
:root {
  /* Display */
  --fluid-display: clamp(2.5rem, 1.5rem + 4.5vw, 5rem);

  /* Headings */
  --fluid-h1: clamp(2rem, 1rem + 3.6vw, 4rem);
  --fluid-h2: clamp(1.75rem, 1rem + 2.3vw, 3rem);
  --fluid-h3: clamp(1.5rem, 1rem + 1.4vw, 2.25rem);
  --fluid-h4: clamp(1.25rem, 1rem + 0.9vw, 1.75rem);
  --fluid-h5: clamp(1.125rem, 1rem + 0.5vw, 1.375rem);
  --fluid-h6: clamp(1rem, 0.95rem + 0.2vw, 1.125rem);

  /* Body */
  --fluid-body: clamp(1rem, 0.95rem + 0.2vw, 1.125rem);
  --fluid-body-sm: clamp(0.875rem, 0.85rem + 0.1vw, 0.9375rem);
  --fluid-caption: clamp(0.75rem, 0.7rem + 0.2vw, 0.875rem);
}
```

## Responsive Spacing

### Spacing Scale by Breakpoint

| Token | xs (0) | sm (480) | md (640) | lg (768) | xl (1024) |
|-------|--------|----------|----------|----------|-----------|
| --space-sm | 4px | 4px | 8px | 8px | 8px |
| --space-md | 8px | 12px | 16px | 16px | 16px |
| --space-lg | 16px | 16px | 24px | 24px | 32px |
| --space-xl | 20px | 24px | 32px | 32px | 48px |
| --space-2xl | 32px | 40px | 48px | 48px | 64px |
| --space-section | 40px | 48px | 64px | 80px | 120px |

### Fluid Spacing with Clamp

```css
:root {
  --fluid-space-sm: clamp(0.25rem, 0.2rem + 0.2vw, 0.5rem);
  --fluid-space-md: clamp(0.5rem, 0.3rem + 0.9vw, 1rem);
  --fluid-space-lg: clamp(1rem, 0.5rem + 1.8vw, 2rem);
  --fluid-space-xl: clamp(1.25rem, 0.5rem + 2.7vw, 3rem);
  --fluid-space-section: clamp(2.5rem, 1rem + 5.5vw, 7.5rem);
}
```

## Grid System

### 12-Column Grid

```css
.grid {
  display: grid;
  gap: var(--space-4);
}

/* Auto-responsive grid */
.grid-auto {
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
}

/* Explicit columns by breakpoint */
.grid-cols-1 { grid-template-columns: 1fr; }

@media (min-width: 640px) {
  .grid-cols-md-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-cols-md-3 { grid-template-columns: repeat(3, 1fr); }
}

@media (min-width: 1024px) {
  .grid-cols-xl-3 { grid-template-columns: repeat(3, 1fr); }
  .grid-cols-xl-4 { grid-template-columns: repeat(4, 1fr); }
}
```

### Container Queries

```css
.card-container {
  container-type: inline-size;
  container-name: card;
}

@container card (min-width: 400px) {
  .card-content { flex-direction: row; }
}

@container card (min-width: 600px) {
  .card-content { gap: var(--space-6); }
}
```

## Touch Target Sizing

| Element | Minimum Size | Recommended |
|---------|-------------|-------------|
| Button | 44 × 44px | 48 × 48px |
| Link (inline) | 44px height | With padding |
| Icon button | 44 × 44px | 48 × 48px |
| Checkbox/Radio | 44 × 44px | Including label |
| Form input | 44px height | 48px height |

Spacing between touch targets: minimum 8px gap.
