#!/usr/bin/env python3
"""Document to Markdown converter with multi-tool orchestration.

Supports Quick Mode (single best tool) and Heavy Mode (multi-tool parallel
execution with best-segment merge).

Usage:
    # Quick Mode (default)
    uv run --with pymupdf4llm --with markitdown convert.py document.pdf -o output.md

    # Heavy Mode
    uv run --with pymupdf4llm --with markitdown convert.py document.pdf -o output.md --heavy

    # List available tools
    uv run --with pymupdf4llm --with markitdown convert.py --list-tools
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def check_tool(name: str) -> bool:
    """Check if a conversion tool is available."""
    if name == "pymupdf4llm":
        try:
            import pymupdf4llm  # noqa: F401
            return True
        except ImportError:
            return False
    elif name == "markitdown":
        try:
            from markitdown import MarkItDown  # noqa: F401
            return True
        except ImportError:
            return False
    elif name == "pandoc":
        return shutil.which("pandoc") is not None
    return False


def list_tools():
    """Print available conversion tools and their status."""
    tools = {
        "pymupdf4llm": "LLM-optimized PDF conversion with native table detection and image extraction",
        "markitdown": "Microsoft's universal converter, good for Office formats (DOCX, PPTX, XLSX)",
        "pandoc": "Excellent structure preservation for DOCX/PPTX",
    }
    print("Available conversion tools:\n")
    for name, desc in tools.items():
        status = "AVAILABLE" if check_tool(name) else "NOT INSTALLED"
        print(f"  [{status}] {name}")
        print(f"           {desc}\n")


def get_applicable_tools(filepath: str) -> list[str]:
    """Return tools applicable to the given file type."""
    ext = Path(filepath).suffix.lower()
    tools = []
    if ext == ".pdf":
        if check_tool("pymupdf4llm"):
            tools.append("pymupdf4llm")
        if check_tool("markitdown"):
            tools.append("markitdown")
    elif ext in (".docx", ".doc"):
        if check_tool("markitdown"):
            tools.append("markitdown")
        if check_tool("pandoc"):
            tools.append("pandoc")
    elif ext in (".pptx", ".ppt"):
        if check_tool("markitdown"):
            tools.append("markitdown")
        if check_tool("pandoc"):
            tools.append("pandoc")
    elif ext in (".xlsx", ".xls"):
        if check_tool("markitdown"):
            tools.append("markitdown")
    else:
        if check_tool("markitdown"):
            tools.append("markitdown")
        if check_tool("pandoc"):
            tools.append("pandoc")
    return tools


def convert_pymupdf4llm(filepath: str) -> str:
    """Convert using pymupdf4llm."""
    import pymupdf4llm
    return pymupdf4llm.to_markdown(filepath)


def convert_markitdown(filepath: str) -> str:
    """Convert using markitdown."""
    from markitdown import MarkItDown
    md = MarkItDown()
    result = md.convert(filepath)
    return result.text_content


def convert_pandoc(filepath: str) -> str:
    """Convert using pandoc."""
    result = subprocess.run(
        ["pandoc", filepath, "-t", "markdown", "--wrap=none"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


TOOL_FUNCS = {
    "pymupdf4llm": convert_pymupdf4llm,
    "markitdown": convert_markitdown,
    "pandoc": convert_pandoc,
}


def segment_markdown(text: str) -> list[dict]:
    """Parse markdown into segments for quality comparison."""
    segments = []
    current = {"type": "paragraph", "content": "", "lines": 0}

    for line in text.split("\n"):
        if re.match(r"^#{1,6}\s", line):
            if current["content"].strip():
                segments.append(current)
            current = {"type": "heading", "content": line + "\n", "lines": 1}
        elif line.startswith("|") and "|" in line[1:]:
            if current["type"] != "table":
                if current["content"].strip():
                    segments.append(current)
                current = {"type": "table", "content": "", "lines": 0}
            current["content"] += line + "\n"
            current["lines"] += 1
        elif line.startswith("```"):
            if current["type"] == "code":
                current["content"] += line + "\n"
                current["lines"] += 1
                segments.append(current)
                current = {"type": "paragraph", "content": "", "lines": 0}
            else:
                if current["content"].strip():
                    segments.append(current)
                current = {"type": "code", "content": line + "\n", "lines": 1}
        elif line.startswith("!["):
            if current["content"].strip():
                segments.append(current)
            segments.append({"type": "image", "content": line + "\n", "lines": 1})
            current = {"type": "paragraph", "content": "", "lines": 0}
        else:
            if current["type"] in ("heading", "image"):
                segments.append(current)
                current = {"type": "paragraph", "content": "", "lines": 0}
            current["content"] += line + "\n"
            current["lines"] += 1

    if current["content"].strip():
        segments.append(current)

    return segments


def score_segment(segment: dict) -> float:
    """Score a segment based on completeness and structure."""
    score = 0.0
    content = segment["content"]

    # Base score from content length (non-empty content is better)
    score += min(len(content.strip()) / 100, 5.0)

    if segment["type"] == "table":
        # Score tables by row count and column consistency
        rows = [r for r in content.strip().split("\n") if r.strip()]
        if rows:
            score += len(rows) * 0.5
            col_counts = [r.count("|") for r in rows]
            if len(set(col_counts)) == 1:
                score += 2.0  # Consistent columns

    elif segment["type"] == "heading":
        if content.strip():
            score += 3.0

    elif segment["type"] == "image":
        if "![" in content and "](" in content:
            score += 3.0

    elif segment["type"] == "code":
        if content.count("```") >= 2:
            score += 2.0

    return score


def merge_outputs_heavy(results: dict[str, str]) -> str:
    """Merge multiple tool outputs by selecting best segments."""
    segmented = {}
    for tool, text in results.items():
        segmented[tool] = segment_markdown(text)

    # Use the tool with the most segments as the base structure
    base_tool = max(segmented, key=lambda t: len(segmented[t]))
    base_segments = segmented[base_tool]

    merged = []
    for i, base_seg in enumerate(base_segments):
        best_seg = base_seg
        best_score = score_segment(base_seg)

        for tool, segs in segmented.items():
            if tool == base_tool:
                continue
            # Try to find a matching segment by type and position
            for j in range(max(0, i - 2), min(len(segs), i + 3)):
                if segs[j]["type"] == base_seg["type"]:
                    s = score_segment(segs[j])
                    if s > best_score:
                        best_score = s
                        best_seg = segs[j]
                    break

        merged.append(best_seg["content"])

    return "\n".join(merged)


def convert_quick(filepath: str) -> str:
    """Quick Mode: use the single best tool for the file type."""
    tools = get_applicable_tools(filepath)
    if not tools:
        print("Error: No conversion tools available. Install pymupdf4llm, markitdown, or pandoc.", file=sys.stderr)
        sys.exit(1)

    tool = tools[0]  # First tool is the preferred one
    print(f"Quick Mode: Converting with {tool}...")
    return TOOL_FUNCS[tool](filepath)


def convert_heavy(filepath: str) -> str:
    """Heavy Mode: run all tools in parallel and merge best segments."""
    tools = get_applicable_tools(filepath)
    if not tools:
        print("Error: No conversion tools available.", file=sys.stderr)
        sys.exit(1)

    if len(tools) == 1:
        print(f"Only one tool available ({tools[0]}), falling back to Quick Mode...")
        return TOOL_FUNCS[tools[0]](filepath)

    print(f"Heavy Mode: Running {len(tools)} tools in parallel: {', '.join(tools)}...")

    results = {}
    with ThreadPoolExecutor(max_workers=len(tools)) as executor:
        futures = {executor.submit(TOOL_FUNCS[t], filepath): t for t in tools}
        for future in as_completed(futures):
            tool = futures[future]
            try:
                results[tool] = future.result()
                print(f"  [{tool}] Done ({len(results[tool])} chars)")
            except Exception as e:
                print(f"  [{tool}] Failed: {e}", file=sys.stderr)

    if not results:
        print("Error: All tools failed.", file=sys.stderr)
        sys.exit(1)

    if len(results) == 1:
        return next(iter(results.values()))

    print("Merging outputs...")
    return merge_outputs_heavy(results)


def main():
    parser = argparse.ArgumentParser(
        description="Convert documents to high-quality markdown"
    )
    parser.add_argument("input", nargs="?", help="Input document path")
    parser.add_argument("-o", "--output", help="Output markdown file path")
    parser.add_argument(
        "--heavy", action="store_true",
        help="Enable Heavy Mode: multi-tool parallel execution with best-segment merge"
    )
    parser.add_argument(
        "--list-tools", action="store_true",
        help="List available conversion tools and exit"
    )

    args = parser.parse_args()

    if args.list_tools:
        list_tools()
        return

    if not args.input:
        parser.error("Input file is required")

    if not os.path.isfile(args.input):
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if args.heavy:
        result = convert_heavy(args.input)
    else:
        result = convert_quick(args.input)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"Output written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
