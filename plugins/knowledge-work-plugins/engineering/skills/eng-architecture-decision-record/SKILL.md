---
name: eng-architecture-decision-record
description: |
  Create Architecture Decision Records (ADRs) to document significant technical
  decisions. Use when recording why a technology, pattern, or approach was chosen.
  Trigger with phrases like 'write ADR', 'architecture decision', 'document decision', 'record technical choice'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Engineering Architecture Decision Record

## Overview

Creates Architecture Decision Records (ADRs) following the Michael Nygard format. Documents the context, decision, and consequences of significant architectural choices for future reference.

## Prerequisites

- A technical decision that has been made or needs to be made
- Context about the problem space and constraints
- Knowledge of alternatives that were evaluated

## Instructions

1. Assign a sequential ADR number
2. Write a short, descriptive title in the form "Use X for Y"
3. Document the context: what forces are at play, what constraints exist
4. State the decision clearly in one sentence
5. List the consequences: positive, negative, and neutral
6. Mark the status: proposed, accepted, deprecated, or superseded
7. Link to related ADRs if applicable

## Output Format

```markdown
# ADR-[NNN]: [Title]

**Date:** [YYYY-MM-DD]
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Deciders:** [Names/Teams]

## Context

[What is the issue that we're seeing that is motivating this decision or change?
What forces are at play (technical, business, political)?]

## Decision

We will [decision].

## Consequences

### Positive
- [Benefit 1]
- [Benefit 2]

### Negative
- [Trade-off 1]
- [Trade-off 2]

### Neutral
- [Observation 1]

## Alternatives Considered

### [Alternative 1]
[Description and why it was not chosen]

### [Alternative 2]
[Description and why it was not chosen]

## Related
- ADR-XXX: [Related decision]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Decision too vague | Not specific enough to be actionable | Rewrite as "Use [specific tech] for [specific purpose]" |
| Missing consequences | Only positive outcomes listed | Always include at least one negative consequence or trade-off |
| No alternatives | Decision appears unjustified | Document at least 2 alternatives, including "status quo" |

## Examples

**Example: Database Choice ADR**
Request: "Write an ADR for choosing PostgreSQL over MongoDB for our user service"
Result: ADR covering relational data needs, ACID requirements, team expertise, and trade-offs around schema flexibility

**Example: Monorepo Decision ADR**
Request: "Document our decision to move to a monorepo"
Result: ADR addressing code sharing, CI complexity, tooling requirements, and migration plan from polyrepo
