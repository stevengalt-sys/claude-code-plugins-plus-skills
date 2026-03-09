#!/usr/bin/env python3
"""Design Token Generator - Generates a complete design token system from a brand color.

Usage:
    python design_token_generator.py <brand_color> [style] [format]

Arguments:
    brand_color  Primary brand color in hex format (e.g., "#0066CC")
    style        Design style preset: modern (default), classic, playful
    format       Output format: json (default), css, scss, summary

Examples:
    python design_token_generator.py "#0066CC"
    python design_token_generator.py "#8B4513" classic css
    python design_token_generator.py "#FF6B6B" playful summary
"""

import colorsys
import json
import math
import sys


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple (0-255)."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    """Convert RGB tuple to hex color."""
    return "#{:02x}{:02x}{:02x}".format(
        max(0, min(255, int(r))),
        max(0, min(255, int(g))),
        max(0, min(255, int(b))),
    )


def rgb_to_hsl(r, g, b):
    """Convert RGB (0-255) to HSL (h: 0-360, s: 0-100, l: 0-100)."""
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return round(h * 360, 1), round(s * 100, 1), round(l * 100, 1)


def hsl_to_rgb(h, s, l):
    """Convert HSL (h: 0-360, s: 0-100, l: 0-100) to RGB (0-255)."""
    r, g, b = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
    return round(r * 255), round(g * 255), round(b * 255)


def relative_luminance(r, g, b):
    """Calculate relative luminance per WCAG 2.1."""
    rs, gs, bs = r / 255.0, g / 255.0, b / 255.0
    r_lin = rs / 12.92 if rs <= 0.03928 else ((rs + 0.055) / 1.055) ** 2.4
    g_lin = gs / 12.92 if gs <= 0.03928 else ((gs + 0.055) / 1.055) ** 2.4
    b_lin = bs / 12.92 if bs <= 0.03928 else ((bs + 0.055) / 1.055) ** 2.4
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def contrast_ratio(rgb1, rgb2):
    """Calculate WCAG contrast ratio between two RGB colors."""
    l1 = relative_luminance(*rgb1)
    l2 = relative_luminance(*rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def generate_color_scale(hex_color):
    """Generate a 10-step color scale from a base color."""
    r, g, b = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(r, g, b)

    scale = {}
    steps = [
        (50, 97),
        (100, 93),
        (200, 86),
        (300, 74),
        (400, 62),
        (500, None),  # original lightness
        (600, 42),
        (700, 32),
        (800, 22),
        (900, 12),
    ]

    for step, lightness in steps:
        if lightness is None:
            scale[str(step)] = hex_color
        else:
            sat = min(100, s * (0.6 + step / 1500.0)) if step < 500 else min(100, s * 1.1)
            new_r, new_g, new_b = hsl_to_rgb(h, sat, lightness)
            scale[str(step)] = rgb_to_hex(new_r, new_g, new_b)

    return scale


def complementary_hue(h):
    """Get complementary hue."""
    return (h + 180) % 360


def generate_tokens(brand_color, style="modern"):
    """Generate complete design token system."""
    r, g, b = hex_to_rgb(brand_color)
    h, s, l = rgb_to_hsl(r, g, b)

    # Style presets
    styles = {
        "modern": {
            "fontSans": "Inter, system-ui, -apple-system, sans-serif",
            "fontSerif": "Merriweather, Georgia, serif",
            "fontMono": "Fira Code, Consolas, monospace",
            "radiusDefault": "8px",
            "radiusSm": "4px",
            "radiusMd": "8px",
            "radiusLg": "12px",
            "radiusXl": "16px",
            "radiusFull": "9999px",
            "shadowStyle": "layered",
        },
        "classic": {
            "fontSans": "Helvetica Neue, Helvetica, Arial, sans-serif",
            "fontSerif": "Georgia, Times New Roman, serif",
            "fontMono": "Courier New, Courier, monospace",
            "radiusDefault": "4px",
            "radiusSm": "2px",
            "radiusMd": "4px",
            "radiusLg": "6px",
            "radiusXl": "8px",
            "radiusFull": "9999px",
            "shadowStyle": "single",
        },
        "playful": {
            "fontSans": "Poppins, Nunito, sans-serif",
            "fontSerif": "Lora, Playfair Display, serif",
            "fontMono": "Source Code Pro, monospace",
            "radiusDefault": "16px",
            "radiusSm": "8px",
            "radiusMd": "16px",
            "radiusLg": "24px",
            "radiusXl": "32px",
            "radiusFull": "9999px",
            "shadowStyle": "soft",
        },
    }

    preset = styles.get(style, styles["modern"])

    # Generate secondary color (complementary)
    sec_h = complementary_hue(h)
    sec_r, sec_g, sec_b = hsl_to_rgb(sec_h, s, l)
    secondary_hex = rgb_to_hex(sec_r, sec_g, sec_b)

    # Neutral based on desaturated primary
    neutral_r, neutral_g, neutral_b = hsl_to_rgb(h, max(5, s * 0.1), 50)
    neutral_hex = rgb_to_hex(neutral_r, neutral_g, neutral_b)

    # Colors
    colors = {
        "primary": generate_color_scale(brand_color),
        "secondary": generate_color_scale(secondary_hex),
        "neutral": generate_color_scale(neutral_hex),
        "semantic": {
            "success": {"base": "#16a34a", "light": "#dcfce7", "dark": "#15803d", "contrast": "#ffffff"},
            "warning": {"base": "#f59e0b", "light": "#fef3c7", "dark": "#d97706", "contrast": "#000000"},
            "error": {"base": "#dc2626", "light": "#fee2e2", "dark": "#b91c1c", "contrast": "#ffffff"},
            "info": {"base": "#2563eb", "light": "#dbeafe", "dark": "#1d4ed8", "contrast": "#ffffff"},
        },
        "surface": {
            "background": "#ffffff",
            "foreground": "#0a0a0a",
            "card": "#ffffff",
            "cardForeground": "#0a0a0a",
            "muted": "#f5f5f5",
            "mutedForeground": "#737373",
            "border": "#e5e5e5",
            "input": "#e5e5e5",
            "ring": brand_color,
        },
    }

    # Typography - 1.25 ratio scale
    ratio = 1.25
    base_size = 16
    typography = {
        "fontFamily": {
            "sans": preset["fontSans"],
            "serif": preset["fontSerif"],
            "mono": preset["fontMono"],
        },
        "fontSize": {
            "xs": f"{round(base_size / ratio**2)}px",
            "sm": f"{round(base_size / ratio)}px",
            "base": f"{base_size}px",
            "lg": f"{round(base_size * ratio)}px",
            "xl": f"{round(base_size * ratio**2)}px",
            "2xl": f"{round(base_size * ratio**3)}px",
            "3xl": f"{round(base_size * ratio**4)}px",
            "4xl": f"{round(base_size * ratio**5)}px",
            "5xl": f"{round(base_size * ratio**6)}px",
        },
        "fontWeight": {
            "light": "300",
            "normal": "400",
            "medium": "500",
            "semibold": "600",
            "bold": "700",
            "extrabold": "800",
        },
        "lineHeight": {
            "none": "1",
            "tight": "1.25",
            "snug": "1.375",
            "normal": "1.5",
            "relaxed": "1.625",
            "loose": "2",
        },
        "letterSpacing": {
            "tighter": "-0.05em",
            "tight": "-0.025em",
            "normal": "0em",
            "wide": "0.025em",
            "wider": "0.05em",
            "widest": "0.1em",
        },
    }

    # Spacing - 8pt grid
    spacing = {
        "0": "0px",
        "0.5": "2px",
        "1": "4px",
        "1.5": "6px",
        "2": "8px",
        "2.5": "10px",
        "3": "12px",
        "3.5": "14px",
        "4": "16px",
        "5": "20px",
        "6": "24px",
        "7": "28px",
        "8": "32px",
        "9": "36px",
        "10": "40px",
        "11": "44px",
        "12": "48px",
        "14": "56px",
        "16": "64px",
        "semantic": {
            "xs": "4px",
            "sm": "8px",
            "md": "16px",
            "lg": "24px",
            "xl": "32px",
            "2xl": "48px",
            "3xl": "64px",
        },
    }

    # Sizing
    sizing = {
        "container": {
            "sm": "640px",
            "md": "768px",
            "lg": "1024px",
            "xl": "1280px",
            "2xl": "1536px",
        },
        "button": {
            "sm": {"height": "32px", "paddingX": "12px", "fontSize": "14px"},
            "md": {"height": "40px", "paddingX": "16px", "fontSize": "16px"},
            "lg": {"height": "48px", "paddingX": "20px", "fontSize": "18px"},
        },
        "input": {
            "sm": {"height": "32px", "paddingX": "8px", "fontSize": "14px"},
            "md": {"height": "40px", "paddingX": "12px", "fontSize": "16px"},
            "lg": {"height": "48px", "paddingX": "16px", "fontSize": "18px"},
        },
        "icon": {
            "xs": "12px",
            "sm": "16px",
            "md": "20px",
            "lg": "24px",
            "xl": "32px",
        },
    }

    # Borders
    borders = {
        "radius": {
            "none": "0px",
            "sm": preset["radiusSm"],
            "default": preset["radiusDefault"],
            "md": preset["radiusMd"],
            "lg": preset["radiusLg"],
            "xl": preset["radiusXl"],
            "full": preset["radiusFull"],
        },
        "width": {
            "none": "0px",
            "thin": "1px",
            "default": "1px",
            "thick": "2px",
            "heavy": "4px",
        },
    }

    # Shadows
    if preset["shadowStyle"] == "layered":
        shadows = {
            "none": "none",
            "xs": "0 1px 2px 0 rgba(0,0,0,0.05)",
            "sm": "0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px -1px rgba(0,0,0,0.1)",
            "md": "0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)",
            "lg": "0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)",
            "xl": "0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)",
            "2xl": "0 25px 50px -12px rgba(0,0,0,0.25)",
            "inner": "inset 0 2px 4px 0 rgba(0,0,0,0.05)",
        }
    elif preset["shadowStyle"] == "single":
        shadows = {
            "none": "none",
            "xs": "0 1px 2px rgba(0,0,0,0.08)",
            "sm": "0 2px 4px rgba(0,0,0,0.1)",
            "md": "0 4px 8px rgba(0,0,0,0.12)",
            "lg": "0 8px 16px rgba(0,0,0,0.12)",
            "xl": "0 16px 32px rgba(0,0,0,0.14)",
            "2xl": "0 24px 48px rgba(0,0,0,0.18)",
            "inner": "inset 0 2px 4px rgba(0,0,0,0.06)",
        }
    else:  # soft
        shadows = {
            "none": "none",
            "xs": "0 2px 8px rgba(0,0,0,0.04)",
            "sm": "0 4px 12px rgba(0,0,0,0.06)",
            "md": "0 6px 20px rgba(0,0,0,0.08)",
            "lg": "0 12px 28px rgba(0,0,0,0.1)",
            "xl": "0 20px 40px rgba(0,0,0,0.12)",
            "2xl": "0 28px 56px rgba(0,0,0,0.16)",
            "inner": "inset 0 2px 8px rgba(0,0,0,0.04)",
        }

    # Animation
    animation = {
        "duration": {
            "instant": "0ms",
            "fast": "100ms",
            "normal": "200ms",
            "slow": "300ms",
            "slower": "500ms",
            "slowest": "1000ms",
        },
        "easing": {
            "linear": "linear",
            "easeIn": "cubic-bezier(0.4, 0, 1, 1)",
            "easeOut": "cubic-bezier(0, 0, 0.2, 1)",
            "easeInOut": "cubic-bezier(0.4, 0, 0.2, 1)",
            "spring": "cubic-bezier(0.175, 0.885, 0.32, 1.275)",
        },
    }

    # Breakpoints
    breakpoints = {
        "xs": "0px",
        "sm": "480px",
        "md": "640px",
        "lg": "768px",
        "xl": "1024px",
        "2xl": "1280px",
    }

    # Z-index
    z_index = {
        "base": "0",
        "dropdown": "100",
        "sticky": "200",
        "overlay": "300",
        "modal": "400",
        "popover": "500",
        "toast": "600",
        "tooltip": "700",
        "notification": "800",
    }

    # WCAG contrast info
    primary_500_rgb = hex_to_rgb(brand_color)
    white_contrast = round(contrast_ratio(primary_500_rgb, (255, 255, 255)), 2)
    black_contrast = round(contrast_ratio(primary_500_rgb, (0, 0, 0)), 2)
    contrast_color = "#ffffff" if white_contrast >= 4.5 else "#000000"

    accessibility = {
        "primaryOnWhite": {
            "ratio": white_contrast,
            "aa": white_contrast >= 4.5,
            "aaLarge": white_contrast >= 3.0,
            "aaa": white_contrast >= 7.0,
        },
        "primaryOnBlack": {
            "ratio": black_contrast,
            "aa": black_contrast >= 4.5,
            "aaLarge": black_contrast >= 3.0,
            "aaa": black_contrast >= 7.0,
        },
        "recommendedContrastColor": contrast_color,
    }

    return {
        "meta": {
            "brandColor": brand_color,
            "style": style,
            "generatedBy": "ui-design-system-toolkit",
            "version": "1.0.0",
        },
        "colors": colors,
        "typography": typography,
        "spacing": spacing,
        "sizing": sizing,
        "borders": borders,
        "shadows": shadows,
        "animation": animation,
        "breakpoints": breakpoints,
        "zIndex": z_index,
        "accessibility": accessibility,
    }


def tokens_to_css(tokens):
    """Convert tokens to CSS custom properties."""
    lines = [":root {"]

    def flatten(obj, prefix=""):
        for key, val in obj.items():
            var_name = f"{prefix}-{key}" if prefix else key
            if isinstance(val, dict):
                flatten(val, var_name)
            else:
                lines.append(f"  --{var_name}: {val};")

    # Colors
    lines.append("  /* Colors */")
    flatten(tokens["colors"], "color")

    lines.append("")
    lines.append("  /* Typography */")
    flatten(tokens["typography"], "font")

    lines.append("")
    lines.append("  /* Spacing */")
    for key, val in tokens["spacing"].items():
        if isinstance(val, dict):
            for k, v in val.items():
                lines.append(f"  --space-{k}: {v};")
        else:
            lines.append(f"  --space-{key}: {val};")

    lines.append("")
    lines.append("  /* Borders */")
    flatten(tokens["borders"], "border")

    lines.append("")
    lines.append("  /* Shadows */")
    for key, val in tokens["shadows"].items():
        lines.append(f"  --shadow-{key}: {val};")

    lines.append("")
    lines.append("  /* Animation */")
    flatten(tokens["animation"], "animation")

    lines.append("")
    lines.append("  /* Breakpoints */")
    for key, val in tokens["breakpoints"].items():
        lines.append(f"  --breakpoint-{key}: {val};")

    lines.append("")
    lines.append("  /* Z-Index */")
    for key, val in tokens["zIndex"].items():
        lines.append(f"  --z-{key}: {val};")

    lines.append("}")
    return "\n".join(lines)


def tokens_to_scss(tokens):
    """Convert tokens to SCSS variables."""
    lines = ["// Design Tokens - Auto-generated", "// Do not edit manually", ""]

    def flatten(obj, prefix=""):
        for key, val in obj.items():
            var_name = f"{prefix}-{key}" if prefix else key
            if isinstance(val, dict):
                flatten(val, var_name)
            else:
                lines.append(f"${var_name}: {val};")

    lines.append("// Colors")
    flatten(tokens["colors"], "color")

    lines.append("")
    lines.append("// Typography")
    flatten(tokens["typography"], "font")

    lines.append("")
    lines.append("// Spacing")
    for key, val in tokens["spacing"].items():
        if isinstance(val, dict):
            for k, v in val.items():
                lines.append(f"$space-{k}: {v};")
        else:
            lines.append(f"$space-{key}: {val};")

    lines.append("")
    lines.append("// Borders")
    flatten(tokens["borders"], "border")

    lines.append("")
    lines.append("// Shadows")
    for key, val in tokens["shadows"].items():
        lines.append(f"$shadow-{key}: {val};")

    lines.append("")
    lines.append("// Animation")
    flatten(tokens["animation"], "animation")

    lines.append("")
    lines.append("// Breakpoints")
    for key, val in tokens["breakpoints"].items():
        lines.append(f"$breakpoint-{key}: {val};")

    lines.append("")
    lines.append("// Z-Index")
    for key, val in tokens["zIndex"].items():
        lines.append(f"$z-{key}: {val};")

    return "\n".join(lines)


def tokens_to_summary(tokens):
    """Generate a human-readable summary."""
    lines = [
        "=== Design Token Summary ===",
        "",
        f"Brand Color: {tokens['meta']['brandColor']}",
        f"Style: {tokens['meta']['style']}",
        "",
        "--- Color Palettes ---",
        f"Primary: {tokens['colors']['primary']['500']} (10 shades)",
        f"Secondary: {tokens['colors']['secondary']['500']} (10 shades)",
        f"Neutral: {tokens['colors']['neutral']['500']} (10 shades)",
        f"Semantic: success, warning, error, info",
        "",
        "--- Typography ---",
        f"Sans: {tokens['typography']['fontFamily']['sans']}",
        f"Mono: {tokens['typography']['fontFamily']['mono']}",
        f"Scale: {tokens['typography']['fontSize']['xs']} - {tokens['typography']['fontSize']['5xl']} (1.25 ratio)",
        "",
        "--- Spacing (8pt Grid) ---",
        f"Range: 0px - 64px ({len(tokens['spacing']) - 1} steps + semantic)",
        "",
        "--- Borders ---",
        f"Radius: {tokens['borders']['radius']['sm']} - {tokens['borders']['radius']['xl']}",
        "",
        "--- Shadows ---",
        f"Levels: {len(tokens['shadows'])} (none through 2xl + inner)",
        "",
        "--- Accessibility ---",
        f"Primary on white: {tokens['accessibility']['primaryOnWhite']['ratio']}:1"
        f" {'PASS' if tokens['accessibility']['primaryOnWhite']['aa'] else 'FAIL'} AA",
        f"Primary on black: {tokens['accessibility']['primaryOnBlack']['ratio']}:1"
        f" {'PASS' if tokens['accessibility']['primaryOnBlack']['aa'] else 'FAIL'} AA",
        f"Recommended contrast color: {tokens['accessibility']['recommendedContrastColor']}",
    ]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    brand_color = sys.argv[1].strip().strip("'\"")
    style = sys.argv[2] if len(sys.argv) > 2 else "modern"
    output_format = sys.argv[3] if len(sys.argv) > 3 else "json"

    # Validate hex color
    color = brand_color.lstrip("#")
    if len(color) != 6 or not all(c in "0123456789abcdefABCDEF" for c in color):
        print(f"Error: Invalid hex color '{brand_color}'. Use format #RRGGBB.", file=sys.stderr)
        sys.exit(1)

    if style not in ("modern", "classic", "playful"):
        print(f"Error: Invalid style '{style}'. Use: modern, classic, playful", file=sys.stderr)
        sys.exit(1)

    tokens = generate_tokens(brand_color, style)

    if output_format == "json":
        print(json.dumps(tokens, indent=2))
    elif output_format == "css":
        print(tokens_to_css(tokens))
    elif output_format == "scss":
        print(tokens_to_scss(tokens))
    elif output_format == "summary":
        print(tokens_to_summary(tokens))
    else:
        print(f"Error: Invalid format '{output_format}'. Use: json, css, scss, summary", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
