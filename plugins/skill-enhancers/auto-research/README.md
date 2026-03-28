# Auto Research

Automatically conduct deep web research on any topic and synthesize findings into a structured, cited report.

## What It Does

The `auto-research` skill enhances Claude with a structured, multi-step research workflow. Instead of a single web search, Claude executes a full research process: planning subtopics, running targeted queries across multiple angles, deep-fetching key sources, synthesizing findings, and producing a formatted report with citations.

## When It Activates

The skill triggers when you say things like:

- "Research [topic]"
- "Auto-research [topic]"
- "Look into [topic]"
- "Investigate [topic]"
- "Deep dive into [topic]"
- "Gather information on [topic]"

## Output

Each research session produces:

- **Inline report** - Presented directly in the conversation
- **`research-[topic]-[date].md`** - Saved to disk (optional)

Reports include: executive summary, key findings by theme, data table, source consensus/debate analysis, identified gaps, full source list with URLs, and recommended next steps.

## Example Usage

```
User: Research the current state of Model Context Protocol (MCP) adoption
```

Claude will:
1. Plan 3-5 research angles (overview, adoption stats, tooling ecosystem, criticism, future direction)
2. Run 5-10 targeted web searches
3. Fetch and extract content from the top sources
4. Synthesize into a structured report with citations
5. Save to `research-mcp-adoption-2026-03-28.md`

## Install

```bash
ccpi install jeremylongshore/claude-code-plugins
```

## License

MIT
