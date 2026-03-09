---
name: ops-runbook-builder
description: |
  Build operational runbooks and standard operating procedures (SOPs). Use when
  creating step-by-step procedures, playbooks, or operational guides for recurring tasks.
  Trigger with phrases like 'create runbook', 'write SOP', 'build playbook', 'operational procedure'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Ops Runbook Builder

## Overview

Creates structured, actionable runbooks and SOPs that teams can follow consistently. Outputs documents with clear steps, decision trees, escalation paths, and rollback procedures.

## Prerequisites

- A description of the operational task or process
- Any existing documentation or tribal knowledge about the procedure

## Instructions

1. Gather context about the operation: what triggers it, who performs it, what systems are involved
2. Define prerequisites and access requirements
3. Write numbered steps with explicit expected outcomes for each step
4. Add decision points with clear branching logic (if X then go to step Y)
5. Include verification checks after critical steps
6. Document rollback procedures for each irreversible action
7. Add escalation contacts and conditions for escalation
8. Include a troubleshooting section for common failure modes

## Output Format

```markdown
# Runbook: [Operation Name]

**Owner:** [Team/Person]
**Last Updated:** [Date]
**Frequency:** [How often this runs]
**Estimated Duration:** [Time]

## Prerequisites
- [ ] Access requirement 1
- [ ] Tool requirement 1

## Procedure
### Step 1: [Action]
**Expected outcome:** [What success looks like]
**If failed:** [What to do]

## Rollback
## Escalation
## Troubleshooting
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Missing context | Insufficient input about the process | Ask clarifying questions about triggers, systems, and owners |
| Overly complex steps | Compound actions in single step | Break into atomic sub-steps with individual verification |
| No rollback path | Irreversible operations not identified | Flag irreversible steps and require explicit rollback plan |

## Examples

**Example: Database Migration Runbook**
Request: "Create a runbook for deploying database migrations to production"
Result: Step-by-step procedure with pre-flight checks, migration execution, validation queries, and rollback via backup restore

**Example: On-Call Handoff SOP**
Request: "Write an SOP for on-call shift handoff"
Result: Checklist covering open incidents, pending alerts, recent changes, escalation contacts, and handoff acknowledgment
