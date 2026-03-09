# Token Generation Reference

## Color Scale Algorithm

Design tokens use HSL color space to generate consistent 10-step scales from any base color.

### Scale Generation Steps

| Step | Lightness | Saturation Modifier | Use Case |
|------|-----------|---------------------|----------|
| 50 | 97% | base × 0.63 | Subtle backgrounds |
| 100 | 93% | base × 0.67 | Light backgrounds |
| 200 | 86% | base × 0.73 | Hover states (light) |
| 300 | 74% | base × 0.8 | Borders |
| 400 | 62% | base × 0.87 | Disabled states |
| 500 | Original | base × 1.0 | Default / base |
| 600 | 42% | base × 1.1 | Hover (dark) |
| 700 | 32% | base × 1.1 | Active states |
| 800 | 22% | base × 1.1 | Text on light bg |
| 900 | 12% | base × 1.1 | Headings |

### Complementary Color

Secondary palette uses the complementary hue (180° rotation in HSL space) with the same saturation and lightness as the primary color.

### Neutral Palette

Neutral colors are derived from the primary hue with heavily desaturated values (10% of original saturation), giving a cohesive tint to grays.

## WCAG Contrast Ratio

### Formula

```
contrast_ratio = (L1 + 0.05) / (L2 + 0.05)
```

Where L1 is the relative luminance of the lighter color and L2 is the darker.

### Relative Luminance

```
L = 0.2126 × R_lin + 0.7152 × G_lin + 0.0722 × B_lin
```

Where each channel is linearized:
- If C_srgb <= 0.03928: C_lin = C_srgb / 12.92
- Otherwise: C_lin = ((C_srgb + 0.055) / 1.055) ^ 2.4

### Requirements

| Level | Normal Text (< 18pt) | Large Text (>= 18pt or >= 14pt bold) |
|-------|---------------------|--------------------------------------|
| AA | 4.5:1 | 3:1 |
| AAA | 7:1 | 4.5:1 |

## Typography Scale

### Major Third Ratio (1.25)

Each step is multiplied or divided by 1.25 from the 16px base:

```
size = base × ratio^n
```

| Token | n | Calculated | Rounded |
|-------|---|-----------|---------|
| xs | -2 | 10.24 | 10px |
| sm | -1 | 12.8 | 13px |
| base | 0 | 16 | 16px |
| lg | 1 | 20 | 20px |
| xl | 2 | 25 | 25px |
| 2xl | 3 | 31.25 | 31px |
| 3xl | 4 | 39.06 | 39px |
| 4xl | 5 | 48.83 | 49px |
| 5xl | 6 | 61.04 | 61px |

### Alternative Ratios

| Ratio | Name | Character |
|-------|------|-----------|
| 1.067 | Minor Second | Subtle, minimal |
| 1.125 | Major Second | Gentle progression |
| 1.200 | Minor Third | Balanced |
| 1.250 | Major Third | Default, versatile |
| 1.333 | Perfect Fourth | High contrast |
| 1.414 | Augmented Fourth | Dramatic |
| 1.500 | Perfect Fifth | Very dramatic |
| 1.618 | Golden Ratio | Classical |

## 8-Point Grid Spacing

All spacing values are multiples of 4px (half-grid) or 8px (full grid):

```
0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48, 56, 64
```

Benefits:
- Consistent visual rhythm
- Aligns with common screen densities
- Divisible for sub-grids (4px, 2px)
- Scales predictably across breakpoints
