#!/usr/bin/env python3
"""Extract images from PDF files with metadata.

Usage:
    # Extract images to directory
    uv run --with pymupdf extract_pdf_images.py document.pdf -o ./assets

    # Generate markdown image references
    uv run --with pymupdf extract_pdf_images.py document.pdf --markdown refs.md
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    print("Error: pymupdf is required. Install with: pip install pymupdf", file=sys.stderr)
    sys.exit(1)


def extract_images(pdf_path: str, output_dir: str) -> list[dict]:
    """Extract all images from a PDF with metadata."""
    doc = pymupdf.open(pdf_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    images = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)

        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            if not base_image:
                continue

            ext = base_image["ext"]
            image_bytes = base_image["image"]
            width = base_image.get("width", 0)
            height = base_image.get("height", 0)

            filename = f"page{page_num + 1}_img{img_idx + 1}.{ext}"
            filepath = output_path / filename

            filepath.write_bytes(image_bytes)

            metadata = {
                "filename": filename,
                "page": page_num + 1,
                "index": img_idx + 1,
                "width": width,
                "height": height,
                "size_bytes": len(image_bytes),
                "format": ext,
                "path": str(filepath),
            }
            images.append(metadata)
            print(f"  Extracted: {filename} ({width}x{height}, {len(image_bytes)} bytes)")

    doc.close()
    return images


def generate_markdown_refs(images: list[dict], output_path: str, assets_dir: str):
    """Generate a markdown file with image references."""
    lines = ["# Extracted Images\n"]

    current_page = None
    for img in images:
        if img["page"] != current_page:
            current_page = img["page"]
            lines.append(f"\n## Page {current_page}\n")

        rel_path = os.path.relpath(img["path"], os.path.dirname(output_path))
        alt_text = f"Page {img['page']} Image {img['index']}"
        lines.append(f"![{alt_text}]({rel_path})")
        lines.append(f"*{img['width']}x{img['height']}, {img['format'].upper()}*\n")

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Markdown references written to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Extract images from PDF files")
    parser.add_argument("input", help="Input PDF file path")
    parser.add_argument("-o", "--output", default="./assets", help="Output directory for images")
    parser.add_argument("--markdown", help="Generate markdown reference file")
    parser.add_argument("--json", help="Export metadata as JSON")

    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if not args.input.lower().endswith(".pdf"):
        print("Error: Input must be a PDF file", file=sys.stderr)
        sys.exit(1)

    print(f"Extracting images from {args.input}...")
    images = extract_images(args.input, args.output)

    if not images:
        print("No images found in the PDF.")
        return

    print(f"\nExtracted {len(images)} image(s) to {args.output}")

    if args.markdown:
        generate_markdown_refs(images, args.markdown, args.output)

    if args.json:
        Path(args.json).write_text(json.dumps(images, indent=2), encoding="utf-8")
        print(f"Metadata written to {args.json}")


if __name__ == "__main__":
    main()
