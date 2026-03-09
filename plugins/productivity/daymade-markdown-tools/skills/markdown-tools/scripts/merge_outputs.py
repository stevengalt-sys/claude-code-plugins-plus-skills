#!/usr/bin/env python3
"""Merge multiple markdown files with segment attribution.

Usage:
    # Basic merge
    python merge_outputs.py output1.md output2.md -o merged.md

    # Verbose mode with segment attribution
    python merge_outputs.py output1.md output2.md -o merged.md --verbose
"""

import argparse
import os
import re
import sys
from pathlib import Path


def parse_segments(text: str) -> list[dict]:
    """Parse markdown into typed segments."""
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
    """Score a segment based on quality metrics."""
    score = 0.0
    content = segment["content"]
    score += min(len(content.strip()) / 100, 5.0)

    if segment["type"] == "table":
        rows = [r for r in content.strip().split("\n") if r.strip()]
        score += len(rows) * 0.5
        col_counts = [r.count("|") for r in rows]
        if len(set(col_counts)) == 1:
            score += 2.0
    elif segment["type"] == "heading":
        score += 3.0 if content.strip() else 0
    elif segment["type"] == "image":
        score += 3.0 if "![" in content and "](" in content else 0
    elif segment["type"] == "code":
        score += 2.0 if content.count("```") >= 2 else 0

    return score


def merge_files(file_contents: dict[str, str], verbose: bool = False) -> str:
    """Merge multiple markdown outputs by selecting best segments."""
    segmented = {name: parse_segments(text) for name, text in file_contents.items()}

    # Use file with most segments as base
    base_name = max(segmented, key=lambda n: len(segmented[n]))
    base_segments = segmented[base_name]

    merged = []
    attributions = []

    for i, base_seg in enumerate(base_segments):
        best_seg = base_seg
        best_score = score_segment(base_seg)
        best_source = base_name

        for name, segs in segmented.items():
            if name == base_name:
                continue
            for j in range(max(0, i - 2), min(len(segs), i + 3)):
                if segs[j]["type"] == base_seg["type"]:
                    s = score_segment(segs[j])
                    if s > best_score:
                        best_score = s
                        best_seg = segs[j]
                        best_source = name
                    break

        merged.append(best_seg["content"])
        if verbose:
            attributions.append(f"<!-- Segment {i + 1} ({best_seg['type']}): from {best_source}, score={best_score:.1f} -->")

    if verbose:
        header = "<!-- Merge Attribution Report -->\n"
        header += "\n".join(attributions) + "\n\n"
        return header + "\n".join(merged)

    return "\n".join(merged)


def main():
    parser = argparse.ArgumentParser(description="Merge multiple markdown files")
    parser.add_argument("inputs", nargs="+", help="Input markdown files")
    parser.add_argument("-o", "--output", required=True, help="Output merged file")
    parser.add_argument("--verbose", action="store_true", help="Include segment attribution comments")

    args = parser.parse_args()

    file_contents = {}
    for f in args.inputs:
        if not os.path.isfile(f):
            print(f"Error: File not found: {f}", file=sys.stderr)
            sys.exit(1)
        file_contents[os.path.basename(f)] = Path(f).read_text(encoding="utf-8")

    if len(file_contents) < 2:
        print("Error: At least 2 input files required for merge", file=sys.stderr)
        sys.exit(1)

    print(f"Merging {len(file_contents)} files...")
    result = merge_files(file_contents, verbose=args.verbose)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(result, encoding="utf-8")
    print(f"Merged output written to {args.output}")


if __name__ == "__main__":
    main()
