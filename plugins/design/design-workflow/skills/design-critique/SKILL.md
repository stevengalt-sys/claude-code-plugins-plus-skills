---
name: design-critique
description: |
  Provide structured design critique and feedback on UI/UX designs.
  Use when reviewing designs, analyzing visual hierarchy, evaluating usability, or giving feedback on mockups and prototypes.
  Trigger phrases: "critique this design", "review my UI", "give feedback on this mockup", "analyze the visual hierarchy", "evaluate this layout".
allowed-tools: Read, Glob, Grep, WebFetch
version: 1.0.0
author: Claude Code Plugin Hub <[email protected]>
---

# Design Critique

Provide structured, actionable design feedback. Works with screenshots, Figma links, or text descriptions.

## Critique Framework

Evaluate every design across these dimensions, scoring each 1-5:

### 1. Visual Hierarchy
- Is the most important element immediately obvious?
- Do size, color, and spacing guide the eye correctly?
- Is there a clear reading order?
- Are CTAs prominent without being overwhelming?

### 2. Usability
- Can a new user accomplish the primary task without instructions?
- Are interactive elements clearly distinguishable from static content?
- Is the navigation predictable and consistent?
- Are error states and edge cases handled gracefully?

### 3. Consistency
- Do similar elements look and behave the same way?
- Is spacing, typography, and color usage systematic?
- Does the design follow platform conventions (iOS/Android/Web)?
- Are patterns reused rather than reinvented?

### 4. Accessibility
- Is there sufficient color contrast (WCAG AA minimum: 4.5:1 for text)?
- Are interactive targets at least 44x44px?
- Does the design work without color as the sole indicator?
- Is the content structure logical for screen readers?

### 5. Content & Copy
- Is the copy clear, concise, and action-oriented?
- Are labels descriptive enough to stand alone?
- Is the tone consistent with the brand?
- Are error messages helpful and specific?

## Output Format

Structure every critique as:

```
## Design Critique Summary

**Overall Score:** X/25

### Strengths
- [What works well and why]

### Issues Found
1. **[Issue]** (Severity: High/Medium/Low)
   - What: [Description]
   - Why it matters: [Impact on users]
   - Fix: [Specific recommendation]

### Quick Wins
- [Easy improvements with high impact]

### Strategic Recommendations
- [Longer-term improvements]
```

## Principles

- Be specific — "the button is too small" is less useful than "the primary CTA at 32px height doesn't meet the 44px touch target minimum"
- Prioritize by impact — lead with issues that affect the most users
- Always explain why — connect every critique to a user outcome
- Provide alternatives — don't just identify problems, suggest solutions
- Acknowledge strengths — note what works well to reinforce good patterns
