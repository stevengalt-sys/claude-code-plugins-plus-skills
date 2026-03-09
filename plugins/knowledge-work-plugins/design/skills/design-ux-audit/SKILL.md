---
name: design-ux-audit
description: |
  Conduct UX audits evaluating usability, accessibility, and design consistency.
  Use when reviewing interfaces for usability issues, heuristic violations, or
  accessibility compliance gaps.
  Trigger with phrases like 'UX audit', 'usability review', 'accessibility audit', 'heuristic evaluation', 'UX review'.
allowed-tools: Read, Write, Edit, Glob, Grep, WebFetch
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Design UX Audit

## Overview

Produces structured UX audit reports evaluating interfaces against Nielsen's heuristics, WCAG accessibility guidelines, and design consistency standards. Categorizes findings by severity and provides actionable remediation.

## Prerequisites

- UI to audit (screenshots, URLs, or component code)
- Target user personas or audience description
- Any existing design guidelines or style guide

## Instructions

1. Evaluate against Nielsen's 10 usability heuristics
2. Check WCAG 2.1 AA compliance: contrast, keyboard nav, screen reader support, alt text
3. Assess design consistency: spacing, typography, color usage, component patterns
4. Review information architecture: navigation clarity, content hierarchy, labeling
5. Evaluate interaction design: feedback, affordances, error prevention, recovery
6. Check responsive behavior across breakpoints
7. Score each area and assign severity to findings (critical, major, minor, cosmetic)
8. Provide specific remediation with before/after descriptions

## Output Format

```markdown
# UX Audit: [Screen/Feature Name]

**Date:** [Date]
**Auditor:** [Name]
**Scope:** [What was reviewed]
**Standard:** Nielsen Heuristics + WCAG 2.1 AA

## Executive Summary
[Overall assessment and top 3 priorities]

## Scorecard
| Category | Score | Status |
|----------|-------|--------|
| Usability | B | 3 major issues |
| Accessibility | C | 5 WCAG violations |
| Consistency | A | Minor spacing issues |
| Information Architecture | B | Navigation gaps |

## Heuristic Evaluation
### H1: Visibility of System Status
- **Score:** [Pass / Fail]
- **Findings:** [Details]
- **Recommendation:** [Fix]

### H2: Match Between System and Real World
...

## Accessibility Findings
| Issue | WCAG Criterion | Severity | Element | Remediation |
|-------|---------------|----------|---------|-------------|

## Consistency Findings
| Issue | Location | Expected | Actual | Fix |
|-------|----------|----------|--------|-----|

## Prioritized Remediation
| Priority | Issue | Impact | Effort | Category |
|----------|-------|--------|--------|----------|
| P1 | [Critical issue] | High | Low | Accessibility |
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| No visual reference | Cannot see the UI | Request screenshots, URLs, or describe the UI in detail |
| Unknown target audience | Cannot assess usability in context | Ask for user personas or primary use cases |
| No style guide | Cannot assess consistency baseline | Note deviations from common patterns and internal inconsistencies |

## Examples

**Example: Dashboard UX Audit**
Request: "Audit the UX of our analytics dashboard"
Result: Heuristic evaluation finding poor error feedback, 4 contrast failures, inconsistent button styles, and prioritized fix list

**Example: Onboarding Flow Review**
Request: "Review the signup and onboarding flow for usability issues"
Result: Step-by-step walkthrough identifying cognitive overload at step 3, missing progress indicator, and unclear error messages
