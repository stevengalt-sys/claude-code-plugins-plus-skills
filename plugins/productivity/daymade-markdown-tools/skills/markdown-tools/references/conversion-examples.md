# Conversion Examples

Practical examples for common document conversion workflows.

## Single File Conversion

### PDF to Markdown (Quick)

```bash
uv run --with pymupdf4llm --with markitdown scripts/convert.py report.pdf -o report.md
```

### PDF to Markdown (Heavy)

```bash
uv run --with pymupdf4llm --with markitdown scripts/convert.py report.pdf -o report.md --heavy
```

### DOCX to Markdown

```bash
uv run --with markitdown scripts/convert.py document.docx -o document.md
```

### PPTX to Markdown

```bash
uv run --with markitdown scripts/convert.py presentation.pptx -o slides.md
```

## Batch Conversion

### Convert All PDFs in a Directory

```bash
for f in docs/*.pdf; do
  uv run --with pymupdf4llm --with markitdown scripts/convert.py "$f" -o "output/$(basename "$f" .pdf).md"
done
```

### Convert with Validation

```bash
for f in docs/*.pdf; do
  base=$(basename "$f" .pdf)
  uv run --with pymupdf4llm --with markitdown scripts/convert.py "$f" -o "output/${base}.md"
  uv run --with pymupdf scripts/validate_output.py "$f" "output/${base}.md" --report "reports/${base}.html"
done
```

## Image Extraction Workflows

### Extract and Reference

```bash
# Extract images
uv run --with pymupdf scripts/extract_pdf_images.py document.pdf -o ./assets --markdown image-refs.md

# Convert document
uv run --with pymupdf4llm --with markitdown scripts/convert.py document.pdf -o document.md --heavy

# Images are now in ./assets with references in image-refs.md
```

### Extract with JSON Metadata

```bash
uv run --with pymupdf scripts/extract_pdf_images.py document.pdf -o ./assets --json metadata.json
```

## Quality Assurance

### Full QA Pipeline

```bash
# 1. Convert with Heavy Mode
uv run --with pymupdf4llm --with markitdown scripts/convert.py input.pdf -o output.md --heavy

# 2. Extract images separately
uv run --with pymupdf scripts/extract_pdf_images.py input.pdf -o ./assets

# 3. Validate quality
uv run --with pymupdf scripts/validate_output.py input.pdf output.md --report qa-report.html

# 4. Review the HTML report in browser
open qa-report.html
```

### Compare Quick vs Heavy Mode

```bash
# Quick Mode
uv run --with pymupdf4llm --with markitdown scripts/convert.py doc.pdf -o quick.md

# Heavy Mode
uv run --with pymupdf4llm --with markitdown scripts/convert.py doc.pdf -o heavy.md --heavy

# Compare
diff quick.md heavy.md
```
