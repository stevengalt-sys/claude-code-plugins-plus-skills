# Heavy Mode Guide

Heavy Mode runs multiple conversion tools in parallel and intelligently merges the best segments from each output to produce the highest quality markdown.

## How It Works

### 1. Parallel Execution

All applicable tools for the given file type run simultaneously:
- **PDF**: pymupdf4llm + markitdown
- **DOCX**: markitdown + pandoc
- **PPTX**: markitdown + pandoc

### 2. Segment Analysis

Each tool's output is parsed into typed segments:
- **Headings** — H1-H6 markers
- **Tables** — Pipe-delimited rows
- **Code blocks** — Fenced code sections
- **Images** — Markdown image references
- **Paragraphs** — Body text

### 3. Quality Scoring

Each segment is scored based on:
- **Content length** — Non-empty content scores higher
- **Table consistency** — Uniform column counts score higher
- **Structure completeness** — Proper heading hierarchy, valid image refs
- **Code block integrity** — Properly fenced blocks

### 4. Best Merge

The tool with the most segments serves as the structural base. For each segment position, the highest-scoring version across all tools is selected.

## When to Use Heavy Mode

- Complex PDFs with mixed tables, images, and text
- Documents where layout preservation is critical
- When Quick Mode output has quality issues (broken tables, missing images)
- Final deliverables requiring highest fidelity

## When Quick Mode Suffices

- Simple text-heavy documents
- Quick drafts and initial review
- When speed matters more than perfection
- Single-format documents (all text, all tables)

## Performance

Heavy Mode takes approximately 2-3x longer than Quick Mode due to parallel execution and merge overhead. The quality improvement is most noticeable on complex documents with mixed content types.
