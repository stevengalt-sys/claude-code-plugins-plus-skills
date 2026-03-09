#!/usr/bin/env python3
"""Validate markdown conversion quality against source PDF.

Usage:
    # Basic validation
    uv run --with pymupdf validate_output.py document.pdf output.md

    # Generate HTML report
    uv run --with pymupdf validate_output.py document.pdf output.md --report report.html
"""

import argparse
import html
import os
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    print("Error: pymupdf is required. Install with: pip install pymupdf", file=sys.stderr)
    sys.exit(1)


def extract_pdf_text(pdf_path: str) -> dict:
    """Extract text and structural elements from PDF."""
    doc = pymupdf.open(pdf_path)
    data = {
        "pages": len(doc),
        "text": "",
        "tables": 0,
        "images": 0,
        "headings": 0,
        "words": 0,
    }

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        data["text"] += text
        data["images"] += len(page.get_images(full=True))

    data["words"] = len(data["text"].split())
    doc.close()
    return data


def analyze_markdown(md_path: str) -> dict:
    """Analyze markdown file structure."""
    content = Path(md_path).read_text(encoding="utf-8")
    data = {
        "text": content,
        "words": len(content.split()),
        "headings": len(re.findall(r"^#{1,6}\s", content, re.MULTILINE)),
        "tables": content.count("\n|"),
        "images": len(re.findall(r"!\[.*?\]\(.*?\)", content)),
        "code_blocks": content.count("```") // 2,
        "links": len(re.findall(r"\[.*?\]\(.*?\)", content)) - len(re.findall(r"!\[.*?\]\(.*?\)", content)),
        "lines": content.count("\n"),
    }
    return data


def calculate_quality_score(pdf_data: dict, md_data: dict) -> dict:
    """Calculate quality score comparing PDF source to markdown output."""
    scores = {}

    # Word coverage (how much text was preserved)
    if pdf_data["words"] > 0:
        coverage = min(md_data["words"] / pdf_data["words"], 1.5)
        scores["word_coverage"] = min(coverage * 100, 100)
    else:
        scores["word_coverage"] = 100

    # Image preservation
    if pdf_data["images"] > 0:
        scores["image_preservation"] = min(md_data["images"] / pdf_data["images"] * 100, 100)
    else:
        scores["image_preservation"] = 100

    # Structure quality (headings, tables)
    structure_score = 0
    if md_data["headings"] > 0:
        structure_score += 30
    if md_data["tables"] > 0:
        structure_score += 30
    if md_data["code_blocks"] > 0:
        structure_score += 20
    if md_data["links"] > 0:
        structure_score += 20
    scores["structure_quality"] = min(structure_score, 100)

    # Overall score (weighted average)
    scores["overall"] = (
        scores["word_coverage"] * 0.5
        + scores["image_preservation"] * 0.25
        + scores["structure_quality"] * 0.25
    )

    return scores


def print_report(pdf_data: dict, md_data: dict, scores: dict):
    """Print a text validation report."""
    print("\n" + "=" * 60)
    print("CONVERSION QUALITY REPORT")
    print("=" * 60)

    print(f"\n{'Metric':<30} {'PDF Source':<15} {'MD Output':<15}")
    print("-" * 60)
    print(f"{'Words':<30} {pdf_data['words']:<15} {md_data['words']:<15}")
    print(f"{'Images':<30} {pdf_data['images']:<15} {md_data['images']:<15}")
    print(f"{'Headings':<30} {'-':<15} {md_data['headings']:<15}")
    print(f"{'Tables':<30} {'-':<15} {md_data['tables']:<15}")
    print(f"{'Code Blocks':<30} {'-':<15} {md_data['code_blocks']:<15}")

    print(f"\n{'Score':<30} {'Value':<15} {'Rating':<15}")
    print("-" * 60)
    for name, value in scores.items():
        rating = "Excellent" if value >= 90 else "Good" if value >= 70 else "Fair" if value >= 50 else "Poor"
        label = name.replace("_", " ").title()
        print(f"{label:<30} {value:>6.1f}%       {rating}")

    print(f"\n{'Overall Quality:':<30} {scores['overall']:.1f}%")
    print("=" * 60)


def generate_html_report(pdf_path: str, md_path: str, pdf_data: dict, md_data: dict, scores: dict, output: str):
    """Generate an HTML quality report."""
    report = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Conversion Quality Report</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }}
h1 {{ color: #333; }} table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
th {{ background: #f5f5f5; }}
.score {{ font-size: 2rem; font-weight: bold; text-align: center; padding: 1rem; border-radius: 8px; }}
.excellent {{ background: #d4edda; color: #155724; }}
.good {{ background: #fff3cd; color: #856404; }}
.fair {{ background: #ffeaa7; color: #856404; }}
.poor {{ background: #f8d7da; color: #721c24; }}
</style></head><body>
<h1>Conversion Quality Report</h1>
<p><strong>Source:</strong> {html.escape(pdf_path)}<br>
<strong>Output:</strong> {html.escape(md_path)}</p>

<div class="score {'excellent' if scores['overall'] >= 90 else 'good' if scores['overall'] >= 70 else 'fair' if scores['overall'] >= 50 else 'poor'}">
Overall Quality: {scores['overall']:.1f}%
</div>

<h2>Metrics</h2>
<table>
<tr><th>Metric</th><th>PDF Source</th><th>MD Output</th></tr>
<tr><td>Words</td><td>{pdf_data['words']}</td><td>{md_data['words']}</td></tr>
<tr><td>Images</td><td>{pdf_data['images']}</td><td>{md_data['images']}</td></tr>
<tr><td>Headings</td><td>-</td><td>{md_data['headings']}</td></tr>
<tr><td>Tables</td><td>-</td><td>{md_data['tables']}</td></tr>
</table>

<h2>Scores</h2>
<table>
<tr><th>Category</th><th>Score</th><th>Rating</th></tr>"""

    for name, value in scores.items():
        rating = "Excellent" if value >= 90 else "Good" if value >= 70 else "Fair" if value >= 50 else "Poor"
        label = name.replace("_", " ").title()
        report += f"\n<tr><td>{label}</td><td>{value:.1f}%</td><td>{rating}</td></tr>"

    report += """
</table></body></html>"""

    Path(output).write_text(report, encoding="utf-8")
    print(f"HTML report written to {output}")


def main():
    parser = argparse.ArgumentParser(description="Validate markdown conversion quality")
    parser.add_argument("pdf", help="Source PDF file")
    parser.add_argument("markdown", help="Output markdown file")
    parser.add_argument("--report", help="Generate HTML quality report")

    args = parser.parse_args()

    for f in [args.pdf, args.markdown]:
        if not os.path.isfile(f):
            print(f"Error: File not found: {f}", file=sys.stderr)
            sys.exit(1)

    print(f"Analyzing PDF: {args.pdf}")
    pdf_data = extract_pdf_text(args.pdf)

    print(f"Analyzing Markdown: {args.markdown}")
    md_data = analyze_markdown(args.markdown)

    scores = calculate_quality_score(pdf_data, md_data)
    print_report(pdf_data, md_data, scores)

    if args.report:
        generate_html_report(args.pdf, args.markdown, pdf_data, md_data, scores, args.report)


if __name__ == "__main__":
    main()
