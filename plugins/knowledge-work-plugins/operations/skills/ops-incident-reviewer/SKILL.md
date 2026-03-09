---
name: ops-incident-reviewer
description: |
  Conduct blameless incident reviews and postmortems. Use when analyzing
  outages, failures, or near-misses to extract lessons and action items.
  Trigger with phrases like 'incident review', 'postmortem', 'root cause analysis', 'RCA', 'blameless review'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Ops Incident Reviewer

## Overview

Generates structured, blameless incident review documents following industry best practices. Produces timelines, root cause analysis, contributing factors, and prioritized action items.

## Prerequisites

- Incident description or timeline of events
- Any available logs, alerts, or communication records
- Impact metrics (duration, affected users, revenue impact)

## Instructions

1. Establish the incident timeline with timestamps
2. Identify what was impacted and quantify the impact
3. Determine the root cause using the 5 Whys technique
4. Identify contributing factors (process, tooling, communication gaps)
5. Distinguish between root cause and triggers
6. List what went well during the response
7. List what could be improved
8. Generate prioritized action items with owners and due dates
9. Classify action items: prevent recurrence, improve detection, speed up recovery

## Output Format

```markdown
# Incident Review: [Title]

**Date:** [When it happened]
**Severity:** [S1-S4]
**Duration:** [Total impact time]
**Author:** [Who wrote this review]

## Summary
[2-3 sentence summary]

## Impact
- Users affected: [number]
- Duration: [time]
- Revenue impact: [estimate if available]

## Timeline
| Time | Event |
|------|-------|

## Root Cause
### 5 Whys
1. Why? [First why]
2. Why? [Second why]
...

**Root Cause:** [One sentence]

## Contributing Factors
- [Factor 1]
- [Factor 2]

## What Went Well
- [Item]

## What Could Be Improved
- [Item]

## Action Items
| Priority | Action | Owner | Due Date | Category |
|----------|--------|-------|----------|----------|
| P1 | [action] | [owner] | [date] | Prevention |
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Blame-oriented language | Review focuses on individuals | Reframe around systems and processes |
| Shallow root cause | Stopped asking "why" too early | Continue 5 Whys until reaching a systemic cause |
| No action items | Review is descriptive but not actionable | Ensure every "could be improved" has a corresponding action |

## Examples

**Example: Production Outage Review**
Request: "Write a postmortem for yesterday's 2-hour API outage caused by a bad deploy"
Result: Full incident review with timeline, 5 Whys tracing to missing integration tests, and action items for canary deploys and automated rollback

**Example: Near-Miss Analysis**
Request: "Review the near-miss where staging database was almost dropped in production"
Result: Analysis of permission gaps, environment confusion, and action items for access controls and environment indicators
