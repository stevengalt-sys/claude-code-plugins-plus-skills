---
name: ops-process-mapper
description: |
  Map and document operational processes and workflows. Use when visualizing
  how work flows through systems, identifying bottlenecks, or documenting
  cross-team handoffs.
  Trigger with phrases like 'map process', 'document workflow', 'process flow', 'value stream'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Ops Process Mapper

## Overview

Documents operational processes as structured workflows with inputs, outputs, owners, and SLAs. Identifies bottlenecks, handoff risks, and automation opportunities.

## Prerequisites

- Description of the process to map
- Knowledge of teams and systems involved

## Instructions

1. Identify the process trigger (what starts it) and the desired end state
2. List all actors (people, teams, systems) involved
3. Map each step: actor, action, input, output, tool/system used
4. Identify handoff points between actors
5. Note SLAs or time expectations for each step
6. Flag bottlenecks, manual steps that could be automated, and single points of failure
7. Generate a Mermaid flowchart diagram of the process
8. Summarize improvement opportunities

## Output Format

```markdown
# Process Map: [Process Name]

**Trigger:** [What starts this process]
**End State:** [What completion looks like]
**Total SLA:** [End-to-end time target]

## Actors
| Actor | Role | System |
|-------|------|--------|

## Process Steps
| # | Actor | Action | Input | Output | SLA | Notes |
|---|-------|--------|-------|--------|-----|-------|

## Flow Diagram
\```mermaid
flowchart TD
    A[Trigger] --> B[Step 1]
    B --> C{Decision}
    C -->|Yes| D[Step 2a]
    C -->|No| E[Step 2b]
\```

## Improvement Opportunities
- [ ] Bottleneck: [description]
- [ ] Automation candidate: [description]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Circular dependencies | Process loops without exit condition | Add explicit loop termination criteria |
| Undefined handoffs | No clear owner for a step | Assign RACI for every step |
| Missing SLAs | No time expectations set | Define target and max duration per step |

## Examples

**Example: Incident Response Process**
Request: "Map our incident response workflow from alert to resolution"
Result: Flowchart with detection, triage, mitigation, communication, and postmortem phases with owners and SLAs

**Example: Deploy Pipeline**
Request: "Document the deployment process from PR merge to production"
Result: Step-by-step map covering CI, staging, approval gates, canary, and full rollout with rollback triggers
