# Tool Comparison

Comparison of the three conversion tools used by markdown-tools.

## Overview

| Feature | pymupdf4llm | markitdown | pandoc |
|---------|-------------|------------|--------|
| **PDF support** | Excellent | Good | Limited |
| **DOCX support** | No | Good | Excellent |
| **PPTX support** | No | Good | Good |
| **XLSX support** | No | Good | No |
| **Table detection** | Native | Basic | Good |
| **Image extraction** | Yes | Limited | No |
| **LLM optimization** | Yes | No | No |
| **Speed** | Fast | Fast | Medium |

## pymupdf4llm

**Best for:** PDF files, especially those with complex layouts.

- LLM-optimized markdown output with clean formatting
- Native table detection preserves structure without heuristics
- Image extraction with metadata (dimensions, format, position)
- Handles multi-column layouts and footnotes
- Produces token-efficient output ideal for LLM consumption

**Install:** `pip install pymupdf4llm`

## markitdown

**Best for:** Office formats (DOCX, PPTX, XLSX) and general-purpose conversion.

- Microsoft's official document converter
- Broad format support including HTML, CSV, and more
- Good default formatting for most document types
- Active development with regular updates

**Install:** `uv tool install "markitdown[pdf]"`

## pandoc

**Best for:** Structured documents where heading hierarchy and formatting matter.

- Excellent structure preservation for DOCX and PPTX
- Maintains heading levels, list nesting, and block quotes
- Produces clean, standards-compliant markdown
- Extensive configuration options via command-line flags

**Install:** `brew install pandoc` (macOS) or `apt install pandoc` (Linux)

## Choosing the Right Tool

1. **PDF conversion** → Start with pymupdf4llm (Quick Mode default)
2. **Office documents** → markitdown for broad support, pandoc for structure
3. **Mixed quality needs** → Use Heavy Mode to combine strengths
4. **Speed priority** → Quick Mode with any single tool
5. **Quality priority** → Heavy Mode merges best segments from all tools
