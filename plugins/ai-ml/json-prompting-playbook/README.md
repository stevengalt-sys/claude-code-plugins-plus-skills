# JSON Prompting Playbook Plugin

Convert natural language image descriptions into structured JSON prompts for AI image generation with reproducible, high-quality results.

## Installation

```bash
/plugin install json-prompting-playbook@claude-code-plugins-plus
```

## Usage

Describe what you want in plain English and the skill converts it into a structured JSON prompt using one of three schemas:

- **Schema A (Photographer)** — Portraits, editorial, fashion
- **Schema B (Full Production)** — Commercial work, reproducible generation
- **Schema C (Minimal)** — Beginners, objects, product shots

## Features

- Natural language to structured JSON prompt conversion
- Three schema levels for different complexity needs
- Color restriction controls for palette consistency
- Material-aware lighting with `madeOutOf` field
- Seed locking for reproducible, iterative generation
- Camera and lens simulation for realistic photography effects

## Based On

The JSON Prompting Playbook by Duncan Rogoff, based on community research across r/promptingmagic, GitHub, and 1,000+ Nano Banana Pro prompts.

## License

MIT
