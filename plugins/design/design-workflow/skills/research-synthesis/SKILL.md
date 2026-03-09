---
name: research-synthesis
description: |
  Synthesize user research data including interviews, surveys, usability tests, and analytics into actionable insights.
  Use when analyzing research findings, creating affinity maps, extracting themes, or writing research reports.
  Trigger phrases: "synthesize research", "analyze interviews", "extract insights", "research findings", "usability test results".
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: Claude Code Plugin Hub <[email protected]>
---

# Research Synthesis

Transform raw user research data into structured, actionable insights.

## Synthesis Process

### Step 1: Organize Raw Data
- Gather all research artifacts (transcripts, notes, recordings, survey data)
- Tag each data point with participant ID and research method
- Separate observations (what happened) from interpretations (what it means)

### Step 2: Code & Categorize
Apply thematic coding:
1. **Open coding** — Label individual observations with descriptive tags
2. **Axial coding** — Group related codes into categories
3. **Selective coding** — Identify overarching themes that connect categories

### Step 3: Identify Patterns
Look for:
- **Frequency** — How many participants encountered this?
- **Severity** — How much did it impact task completion?
- **Breadth** — Does it affect one task or many?
- **Consistency** — Did participants react the same way?

### Step 4: Generate Insights
Transform patterns into insights using this format:
> **Insight**: [What we learned]
> **Evidence**: [X of Y participants...] + [specific quotes/observations]
> **Impact**: [How this affects the user experience]
> **Recommendation**: [What to do about it]

### Step 5: Prioritize
Use an impact/effort matrix:
- **High impact, low effort** — Do first
- **High impact, high effort** — Plan for next sprint
- **Low impact, low effort** — Quick wins if time permits
- **Low impact, high effort** — Deprioritize

## Output Formats

### Research Summary
```
## Research Summary

**Study**: [Name]
**Method**: [Interviews / Usability test / Survey / etc.]
**Participants**: [N] participants, [demographics]
**Date**: [Range]

### Key Findings
1. [Finding with supporting evidence]
2. [Finding with supporting evidence]

### Themes
| Theme | Frequency | Severity | Key Quote |
|-------|-----------|----------|-----------|
| [Theme] | X/Y participants | High/Med/Low | "[Quote]" |

### Recommendations
| Priority | Recommendation | Evidence | Effort |
|----------|---------------|----------|--------|
| P0 | [Action] | [Data] | [Low/Med/High] |
```

### Persona Update
When research reveals user segments, update or create personas with:
- Goals and motivations (backed by data)
- Pain points (with frequency and severity)
- Behavioral patterns (observed, not assumed)
- Quotes that capture the persona's perspective

### Journey Map Input
Structure findings as journey map data:
- **Phase** — Where in the journey this occurs
- **Action** — What the user does
- **Thinking** — What the user expects
- **Feeling** — Emotional state (frustrated, confused, confident)
- **Opportunity** — Where design can improve the experience

## Quality Checks

- Every insight must be backed by evidence from at least 2 participants
- Distinguish between what users say and what they do
- Note sample size limitations honestly
- Flag potential biases in recruitment or methodology
- Include contradictory findings — they're often the most valuable
