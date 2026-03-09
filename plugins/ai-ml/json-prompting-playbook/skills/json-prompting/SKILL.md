---
name: json-prompting
description: |
  Convert natural language image descriptions into structured JSON prompts for AI image generation.
  Use when a user wants to create AI image prompts, structure image generation parameters,
  or convert plain English descriptions into JSON format for tools like Nano Banana, Midjourney,
  DALL-E, or Stable Diffusion. Trigger with phrases like "create image prompt", "generate JSON prompt",
  "convert to image prompt", "structure my prompt", or "JSON prompting".
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Duncan Rogoff <duncan@nanobananapro.com>
license: MIT
---

# The JSON Prompting Playbook

Convert natural language image descriptions into structured JSON prompts for reproducible, high-quality AI image generation.

## Why JSON Prompting

When you feed an AI image model structured JSON instead of free-form text, it reads categorized data rather than parsing a run-on sentence. Each element gets its own field — background is separate from outfit, lighting is separate from color palette. You can change one thing without breaking everything else.

| Metric | Natural Language | JSON Prompting |
| --- | --- | --- |
| Color accuracy | ~68% | ~92% |
| Inference speed | 500ms-1.2s | 200-700ms |
| Batch processing | Baseline | ~40% faster |
| Reproducibility | Low | High (lock seed) |

## Schema Selection

Choose the right schema based on the user's needs:

### Schema A — Photographer (portraits, editorial, fashion)

Clean, flat structure. Best starting point. The `madeOutOf` field controls how light reflects off surfaces.

```json
{
  "label": "editorial-portrait-01",
  "tags": ["film-aesthetic", "retro", "street"],
  "subject": [
    "28yo woman",
    "short dark hair with curtain bangs",
    "worn denim jacket",
    "neutral expression"
  ],
  "madeOutOf": "cotton twill, worn leather patches, vintage enamel pin",
  "arrangement": "Subject sits centered, cross-legged on concrete steps",
  "lighting": "overcast diffused daylight, soft shadows, no direct sun",
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8"
  },
  "colorRestriction": "Muted earth tones, faded indigo denim, dusty concrete grays"
}
```

### Schema B — Full Production (commercial work, reproducible generation)

Full control over subject, scene, camera, composition, and generation parameters. Lock the seed for reproducible iteration.

```json
{
  "user_intent": "editorial portrait for fashion magazine",
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "ultra_photorealistic",
    "guidance_scale": 7.5,
    "steps": 40,
    "seed": 42
  },
  "subject": [{
    "type": "person",
    "description": "late 20s woman, sharp cheekbones, olive skin",
    "hair": { "style": "curtain_bangs", "color": "dark_brown" },
    "clothing": [{ "item": "blazer", "color": "ivory", "fabric": "silk", "fit": "oversized" }],
    "pose": "leaning against wall, arms crossed",
    "expression": "confident, direct gaze"
  }],
  "scene": {
    "location": "brutalist architecture rooftop",
    "time": "golden_hour",
    "lighting": { "type": "natural_sunlight", "direction": "rim_light" }
  },
  "technical": {
    "camera_model": "Hasselblad X2D",
    "lens": "85mm",
    "aperture": "f/1.4",
    "film_stock": "Kodak Portra 400"
  },
  "advanced": {
    "negative_prompt": ["blurry", "plastic skin", "oversaturated"]
  }
}
```

### Schema C — Minimal (beginners, objects, product shots)

Six categories. No nested arrays. Good for products, environments, and still life.

```json
{
  "style": { "primary": "photorealistic", "rendering_quality": "high-resolution", "lighting": "natural" },
  "technical": { "aperture": "f/1.8", "depth_of_field": "shallow", "exposure": "balanced" },
  "materials": { "primary": "oak wood", "secondary": "glass", "texture": "smooth" },
  "environment": { "location": "modern office", "time_of_day": "morning", "weather": "clear" },
  "composition": { "framing": "rule of thirds", "angle": "eye-level", "focus_subject": "coffee mug on desk" },
  "quality": { "resolution": "4K", "sharpness": "crisp", "post_processing": "cinematic grading" }
}
```

## Instructions

When converting a user's natural language description to a JSON prompt:

1. **Determine the appropriate schema** based on the use case:
   - Portraits/editorial/fashion → Schema A
   - Commercial/reproducible work → Schema B
   - Products/objects/beginners → Schema C

2. **Break subject into a list, not a sentence.** The model weights isolated list items more heavily than adjectives in a string. One trait per line.

   Bad: `"subject": "28 year old woman with dark curtain bangs wearing a denim jacket looking neutral"`

   Good:
   ```json
   "subject": [
     "28yo woman",
     "dark hair with curtain bangs",
     "worn denim jacket",
     "neutral expression"
   ]
   ```

3. **Always define `colorRestriction`.** Without it, models default to high saturation across the full spectrum. Example:
   ```json
   "colorRestriction": "warm tungsten tones, dusty rose, aged cream — no cool blues or greens"
   ```

4. **Use `madeOutOf` to control light behavior.** "Cotton camisole" and "spandex" produce different outputs at identical camera settings. Specify the fabric, not just the garment.

5. **Lock seed, then iterate one variable at a time.** Set seed to any integer (e.g., 42). Change lighting direction, compare. Change outfit color, compare. Controlled experiments instead of rolling dice.

6. **Treat lens choice as a real photography decision:**

   | Lens | Effect | Best For |
   | --- | --- | --- |
   | 16mm | Dramatic distortion, wide environment | Architecture, establishing shots |
   | 35mm | Environmental, natural perspective | Street, lifestyle, editorial |
   | 50mm | Natural field of view, balanced | General purpose |
   | 85mm | Compressed, background separation | Portraits, fashion, beauty |

7. **Use `lighting.direction` as a drama dial:**

   | Direction | Result |
   | --- | --- |
   | rim_light | Halo between subject and background — editorial separation |
   | side_lit | Strong shadows, dramatic, moody |
   | front_lit | Flat, even, commercial — passport photo energy |
   | silhouette | Subject dark, background lit — cinematic |

## Quick Field Reference

### Generation Settings

| Field | Best Options |
| --- | --- |
| quality | ultra_photorealistic, anime_v6, 3d_render_octane |
| aspect_ratio | 9:16 (Reels/vertical), 4:5 (portrait), 16:9 (landscape) |
| guidance_scale | 7.5 default. Go 9-12 for strict literal output. |
| film_stock | Kodak Portra 400 (warm), CineStill 800T (neon/tungsten), Fuji Velvia 50 (vivid nature) |

### Time + Lighting Combos

| time | lighting.type | lighting.direction | Mood |
| --- | --- | --- | --- |
| golden_hour | natural_sunlight | rim_light | Warm, editorial, cinematic |
| blue_hour | neon_lights | side_lit | Urban, moody, cyberpunk |
| midnight | god_rays | overhead | Dramatic, low-key |
| midday | hard_direct_flash | front_lit | Harsh, commercial, flat |

## Translator Prompt

When converting natural language to JSON prompts, follow these rules:
- Convert the description into valid JSON using the appropriate schema
- Infer sensible values for unspecified fields
- Always include: subject, scene/lighting, technical lens and aperture, colorRestriction, and negative_prompt
- Output only valid JSON — no explanation, no markdown fences (unless the user asks for explanation)
- Increase steps (40 to 60) only for complex scenes; for simple subjects it adds latency with no visible gain

## Output Format

Always output the final JSON prompt as a properly formatted code block. If the user provides a vague description, ask clarifying questions about:
- Subject details (age, appearance, clothing, expression)
- Environment/location
- Mood/atmosphere
- Intended use (social media, print, editorial)
- Preferred style (photorealistic, anime, 3D render)
