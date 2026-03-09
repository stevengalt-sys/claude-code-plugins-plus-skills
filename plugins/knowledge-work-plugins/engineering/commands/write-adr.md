---
name: write-adr
description: Create an Architecture Decision Record documenting a technical choice
arguments:
  - name: decision
    description: The architectural decision to document
    required: true
---

Create an Architecture Decision Record for: $ARGUMENTS.decision

Follow the eng-architecture-decision-record skill guidelines. Include:
1. Descriptive title in "Use X for Y" format
2. Context and forces at play
3. Clear decision statement
4. Positive, negative, and neutral consequences
5. Alternatives considered with rationale for rejection
6. Related decisions if applicable

Output as a Markdown ADR ready for team review.
