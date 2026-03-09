---
name: build-runbook
description: Create an operational runbook or SOP for a recurring task or procedure
arguments:
  - name: topic
    description: The operation or procedure to document
    required: true
---

Build a comprehensive operational runbook for: $ARGUMENTS.topic

Follow the ops-runbook-builder skill guidelines. Include:
1. Prerequisites and access requirements
2. Step-by-step procedure with expected outcomes
3. Decision points with branching logic
4. Verification checks after critical steps
5. Rollback procedures
6. Escalation paths
7. Troubleshooting section

Output as a well-structured Markdown document ready for team use.
