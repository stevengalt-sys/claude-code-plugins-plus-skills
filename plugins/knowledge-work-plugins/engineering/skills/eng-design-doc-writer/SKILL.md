---
name: eng-design-doc-writer
description: |
  Write technical design documents and RFCs for software projects. Use when
  drafting design docs, technical proposals, or engineering RFCs for new features,
  system changes, or migrations.
  Trigger with phrases like 'write design doc', 'create RFC', 'technical proposal', 'design document'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Engineering Design Doc Writer

## Overview

Creates structured technical design documents following industry-standard RFC/design doc formats. Covers problem statement, proposed solution, alternatives considered, and migration plans.

## Prerequisites

- Clear problem statement or feature request
- Context about the existing system architecture
- Any constraints (timeline, backward compatibility, performance)

## Instructions

1. Define the problem statement and motivation clearly
2. State goals and non-goals explicitly
3. Describe the current state of the system
4. Propose the solution with sufficient technical detail
5. Document at least 2 alternatives considered with trade-off analysis
6. Identify risks and mitigations
7. Define success metrics and how they will be measured
8. Include a rollout plan with milestones
9. List open questions that need resolution

## Output Format

```markdown
# Design Doc: [Title]

**Author:** [Name]
**Status:** Draft | In Review | Approved | Implemented
**Created:** [Date]
**Reviewers:** [Names]

## Problem Statement
[What problem are we solving and why now?]

## Goals
- [Goal 1]

## Non-Goals
- [Non-goal 1]

## Current State
[How does the system work today?]

## Proposed Solution
### Overview
[High-level description]

### Detailed Design
[Technical details, diagrams, data models, API contracts]

## Alternatives Considered
### Alternative 1: [Name]
- **Pros:** [...]
- **Cons:** [...]
- **Why not:** [...]

## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|

## Success Metrics
| Metric | Current | Target | How Measured |
|--------|---------|--------|-------------|

## Rollout Plan
1. Phase 1: [...]
2. Phase 2: [...]

## Open Questions
- [ ] [Question 1]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Vague problem statement | Unclear requirements | Ask for specific user stories or incident examples |
| No alternatives section | Skipped trade-off analysis | Always include at least 2 alternatives, even if "do nothing" |
| Missing metrics | No way to measure success | Define at least one quantitative metric per goal |

## Examples

**Example: Database Migration Design Doc**
Request: "Write a design doc for migrating from PostgreSQL to CockroachDB"
Result: Full RFC with current architecture, migration strategy, dual-write approach, rollback plan, and performance benchmarks

**Example: API Versioning RFC**
Request: "Design doc for introducing API versioning to our REST service"
Result: Proposal comparing URL path, header, and query param versioning with migration timeline
