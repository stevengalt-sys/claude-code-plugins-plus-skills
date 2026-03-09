# Markdown Tools

Convert documents (PDF, DOCX, PPTX) to high-quality markdown with intelligent multi-tool orchestration.

## Features

- **Quick Mode** — Fast single-tool conversion (default)
- **Heavy Mode** — Multi-tool parallel execution with best-segment merge
- **Image extraction** — Extract images with metadata from PDFs
- **Quality validation** — Validate conversion quality with HTML reports
- **Output merging** — Merge multiple markdown files with segment attribution

## Conversion Tools

| Tool | Best For |
|------|----------|
| pymupdf4llm | LLM-optimized PDF conversion with table detection and image extraction |
| markitdown | Microsoft's universal converter for Office formats |
| pandoc | Structure preservation for DOCX/PPTX |

## Prerequisites

```bash
uv tool install "markitdown[pdf]"
pip install pymupdf4llm
brew install pandoc  # or: apt install pandoc
```

## Usage

```bash
# Quick Mode (default)
uv run --with pymupdf4llm --with markitdown scripts/convert.py document.pdf -o output.md

# Heavy Mode (best quality)
uv run --with pymupdf4llm --with markitdown scripts/convert.py document.pdf -o output.md --heavy

# Extract images
uv run --with pymupdf scripts/extract_pdf_images.py document.pdf -o ./assets

# Validate quality
uv run --with pymupdf scripts/validate_output.py document.pdf output.md --report report.html
```

## Credits

Originally from [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills).

## Contributors

- daymade
