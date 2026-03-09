---
name: review-code
description: Generate a structured code review with categorized feedback
arguments:
  - name: target
    description: The file, PR, or diff to review
    required: true
---

Perform a structured code review on: $ARGUMENTS.target

Follow the eng-code-review-guide skill guidelines. Include:
1. Summary of the change and overall assessment
2. Blockers (must fix) with specific fix suggestions
3. Major issues with improvement suggestions
4. Minor issues and nits
5. What was done well
6. Testing gaps with specific test case suggestions

Categorize every finding by severity. Be constructive and specific.
