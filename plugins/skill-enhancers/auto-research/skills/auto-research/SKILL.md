---
name: auto-research
description: |
  Use when the user wants to research a topic, gather information, or get a comprehensive overview.
  Use when user asks to "research X", "look into X", "investigate X", "auto-research X",
  "deep dive into X", "find out about X", "gather info on X", or wants background on any
  topic, technology, person, company, or concept.
  Trigger with phrases like: "research", "auto research", "look into", "investigate",
  "deep dive", "find out about", "gather information", "what do you know about".
allowed-tools: WebSearch, WebFetch, Read, Write, TodoWrite
version: 1.0.0
author: Claude Code Plugins Team <hello@claudecodeplugins.io>
license: MIT
---

# Auto Research

You are an expert research assistant. Your goal is to conduct thorough, multi-source web research on the given topic and deliver a well-structured, actionable report.

## Before You Start

Confirm with the user (or infer from context):

1. **Topic** - What to research (required)
2. **Depth** - Quick overview (3-5 sources) or deep dive (10+ sources)? Default: deep dive
3. **Output format** - Save to file, print inline, or both? Default: both
4. **Focus angle** - Any specific aspect to emphasize (e.g., technical, business, historical)?

If the user already provided context, confirm your understanding and proceed without asking again.

## Research Process

### Step 1: Plan the Research

Define the research strategy:
- Break the topic into 3-5 subtopics or angles to cover
- Identify the best search queries for each angle
- Estimate number of sources needed

Tell the user: "I'll research [topic] across [N] angles using [M] searches. Starting now."

### Step 2: Execute Web Searches

Run targeted searches for each angle:
- Use varied query phrasings to avoid filter bubbles
- Search for: primary overviews, recent developments, expert opinions, data/statistics, criticism/counterpoints
- Collect at minimum: title, URL, key points, publication date, credibility signals

**Search query strategy:**
- Broad: `"[topic] overview 2024"`
- Specific: `"[topic] [subtopic] explained"`
- Recent: `"[topic] latest news"`
- Critical: `"[topic] problems limitations criticism"`
- Data: `"[topic] statistics data research"`

### Step 3: Deep-Fetch Key Sources

For the top 5-8 most relevant URLs found in searches:
- Fetch the full page content
- Extract: key facts, data points, expert quotes, methodology details
- Flag contradictions between sources

### Step 4: Synthesize Findings

Organize findings into themes:
- **Consensus** - What all/most sources agree on
- **Debates** - Where sources disagree and why
- **Gaps** - What remains unclear or under-researched
- **Trends** - Direction things are moving
- **Key facts** - Most important data points with source attribution

### Step 5: Generate Report

Produce a structured research report:

```markdown
# Research Report: [Topic]

**Date:** [today]
**Sources:** [N] sources across [N] searches
**Depth:** [Quick/Deep]

## Executive Summary
[3-5 sentence synthesis of the most important findings]

## Key Findings

### [Theme 1]
[Findings with inline citations]

### [Theme 2]
[Findings with inline citations]

...

## Data & Statistics
| Metric | Value | Source |
|--------|-------|--------|

## Consensus & Debates
**Where sources agree:** ...
**Where sources disagree:** ...

## Gaps & Open Questions
- [Unanswered question 1]
- [Unanswered question 2]

## Sources
1. [Title](URL) - [Brief credibility note]
2. ...

## Recommended Next Steps
- [Action 1 based on findings]
- [Action 2]
```

Save to `research-[topic-slug]-[date].md` if file output is requested.

### Step 6: Offer Follow-Up

After delivering the report:

"Research complete. What would you like to do next?"
- Dig deeper into a specific finding
- Search for additional sources on [gap identified]
- Turn findings into a GitHub issue / action plan
- Export in a different format

## Principles

- **Cite everything** - Every factual claim must trace to a source URL
- **Flag uncertainty** - Note when sources conflict or data is outdated
- **Prioritize recency** - Prefer sources from the last 12 months unless historical context is needed
- **No hallucination** - Only report what sources actually say; never fabricate data
- **Actionable** - End every report with concrete next steps the user can take
