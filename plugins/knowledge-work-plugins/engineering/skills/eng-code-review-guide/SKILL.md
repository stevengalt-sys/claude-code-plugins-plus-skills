---
name: eng-code-review-guide
description: |
  Generate structured code review checklists and feedback for pull requests.
  Use when reviewing code, creating review guidelines, or providing systematic
  feedback on code changes.
  Trigger with phrases like 'code review checklist', 'review this PR', 'review guidelines', 'code review feedback'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Engineering Code Review Guide

## Overview

Produces structured code review feedback organized by severity. Covers correctness, security, performance, maintainability, and testing. Outputs actionable comments with specific line references.

## Prerequisites

- Code diff or file changes to review
- Context about the project's coding standards (if available)
- Understanding of the feature being implemented

## Instructions

1. Read the full diff to understand the change's intent
2. Check correctness: logic errors, edge cases, off-by-one errors
3. Check security: injection risks, auth gaps, secret exposure, OWASP top 10
4. Check performance: N+1 queries, unnecessary allocations, missing indexes
5. Check maintainability: naming, complexity, duplication, single responsibility
6. Check testing: coverage of happy path, error cases, and edge cases
7. Categorize each finding by severity: blocker, major, minor, nit
8. Provide specific fix suggestions for blockers and majors
9. Call out what was done well

## Output Format

```markdown
# Code Review: [PR Title / Description]

## Summary
[1-2 sentence overview of the change and overall assessment]

## Blockers (Must Fix)
- **[File:Line]** [Issue description]
  - **Why:** [Impact if not fixed]
  - **Fix:** [Specific suggestion]

## Major Issues
- **[File:Line]** [Issue description]
  - **Suggestion:** [How to improve]

## Minor Issues
- **[File:Line]** [Issue description]

## Nits
- **[File:Line]** [Suggestion]

## What Looks Good
- [Positive callout 1]
- [Positive callout 2]

## Testing Gaps
- [ ] [Missing test case 1]
- [ ] [Missing test case 2]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| No context about standards | Missing style guide | Review against general best practices and language idioms |
| Large diff | Too many changes to review thoroughly | Focus on blockers and majors first, suggest splitting the PR |
| Missing tests | No test files in the diff | Flag as a major issue with specific test case suggestions |

## Examples

**Example: API Endpoint Review**
Request: "Review this new REST endpoint for user registration"
Result: Feedback covering input validation, password hashing, rate limiting, error responses, and missing integration tests

**Example: Database Migration Review**
Request: "Review this migration adding an index to the orders table"
Result: Check for lock impact, index strategy, backward compatibility, and rollback plan
