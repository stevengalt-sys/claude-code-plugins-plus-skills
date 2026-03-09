---
name: markdown-tools
description: |
  Convert documents to markdown with multi-tool orchestration for best quality.
  Supports Quick Mode (fast, single tool) and Heavy Mode (best quality, multi-tool merge).
  Use when converting PDF/DOCX/PPTX files to markdown, extracting images from documents,
  validating conversion quality, or needing LLM-optimized document output.
  Trigger phrases: "convert to markdown", "pdf to markdown", "extract text from pdf",
  "convert document", "markdown conversion", "docx to markdown".
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
version: 1.0.0
author: daymade <daymade@claudecodeplugins.io>
---

# Markdown Tools

Convert documents to high-quality markdown with intelligent multi-tool orchestration.

## Prerequisites

Install required tools for PDF/DOCX/PPTX support:

```bash
uv tool install "markitdown[pdf]"
pip install pymupdf4llm
brew install pandoc
```

## Conversion Tools

| Tool | Best For | Strengths |
|------|----------|-----------|
| **pymupdf4llm** | PDF files | LLM-optimized conversion, native table detection, image extraction |
| **markitdown** | Office formats | Microsoft's universal converter, good for DOCX/PPTX/XLSX |
| **pandoc** | Structured docs | Excellent structure preservation for DOCX/PPTX |

## Usage

### Quick Mode (Default)

Fast, single best tool conversion. Automatically selects the optimal tool based on file type.

```bash
uv run --with pymupdf4llm --with markitdown scripts/convert.py document.pdf -o output.md
```

### Heavy Mode

Runs multiple tools in parallel and selects the best segments for highest quality output.

```bash
uv run --with pymupdf4llm --with markitdown scripts/convert.py document.pdf -o output.md --heavy
```

Heavy Mode pipeline:
1. **Parallel Execution** — Run all applicable tools simultaneously
2. **Segment Analysis** — Parse each output into segments (tables, headings, images, paragraphs)
3. **Quality Scoring** — Score each segment based on completeness and structure
4. **Best Merge** — Select the highest-scoring version of each segment

### List Available Tools

```bash
uv run --with pymupdf4llm --with markitdown scripts/convert.py --list-tools
```

## Additional Scripts

### Extract Images from PDF

Extract images with metadata:

```bash
uv run --with pymupdf scripts/extract_pdf_images.py document.pdf -o ./assets
```

Generate markdown image references:

```bash
uv run --with pymupdf scripts/extract_pdf_images.py document.pdf --markdown refs.md
```

### Validate Conversion Quality

Check conversion completeness and accuracy:

```bash
uv run --with pymupdf scripts/validate_output.py document.pdf output.md
```

Generate an HTML quality report:

```bash
uv run --with pymupdf scripts/validate_output.py document.pdf output.md --report report.html
```

### Merge Multiple Outputs

Combine markdown files with segment attribution:

```bash
python scripts/merge_outputs.py output1.md output2.md -o merged.md
```

Show segment attribution (verbose):

```bash
python scripts/merge_outputs.py output1.md output2.md -o merged.md --verbose
```

## Workflow Examples

### Single PDF Conversion

```
1. Run Quick Mode: scripts/convert.py report.pdf -o report.md
2. Validate: scripts/validate_output.py report.pdf report.md
3. Review and edit the output markdown
```

### Batch Document Conversion

```
1. Gather all documents in a directory
2. Run convert.py on each with appropriate mode
3. Validate each output
4. Merge if needed with merge_outputs.py
```

### High-Fidelity Conversion

```
1. Run Heavy Mode: scripts/convert.py complex.pdf -o complex.md --heavy
2. Extract images: scripts/extract_pdf_images.py complex.pdf -o ./assets
3. Validate: scripts/validate_output.py complex.pdf complex.md --report report.html
4. Review HTML report for quality issues
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| FontBBox warnings during PDF conversion | Harmless font parsing warnings — output is still correct |
| Images missing from output | Use Heavy Mode for better image preservation, or extract separately with `extract_pdf_images.py` |
| Tables broken in output | Use Heavy Mode (selects most complete table version), or validate with `validate_output.py` |
| Pandoc not found | Install with `brew install pandoc` (macOS) or `apt install pandoc` (Linux) |

## References

- `references/heavy-mode-guide.md` — Detailed Heavy Mode documentation
- `references/tool-comparison.md` — Tool capabilities comparison
- `references/conversion-examples.md` — Batch operation examples
