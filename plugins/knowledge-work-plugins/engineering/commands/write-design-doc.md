---
name: write-design-doc
description: Write a technical design document or RFC for a proposed change
arguments:
  - name: topic
    description: The feature, system, or change to design
    required: true
---

Write a comprehensive technical design document for: $ARGUMENTS.topic

Follow the eng-design-doc-writer skill guidelines. Include:
1. Problem statement and motivation
2. Goals and non-goals
3. Current state of the system
4. Proposed solution with detailed design
5. At least 2 alternatives considered with trade-offs
6. Risks and mitigations
7. Success metrics
8. Rollout plan
9. Open questions

Output as a polished Markdown document ready for engineering review.
