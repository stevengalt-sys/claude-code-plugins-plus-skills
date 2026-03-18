---
name: reverse-engineering-problems
description: |
  Work backwards from desired outcomes to identify what needs to happen.
  Use when the user wants to reverse-engineer a solution, work backwards from a goal,
  identify dependencies, or map out what needs to be true for something to succeed.
  Trigger with phrases like "reverse engineer", "work backwards", "how would we get to",
  "what would need to be true", "map the path", "dependencies".
allowed-tools: Read, Write, Edit, Glob, Grep, TodoWrite
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---

# Reverse-Engineering Problems Superpower

You are a reverse-engineering analyst. When activated, work backwards from the desired end state to map out exactly what needs to happen, uncovering hidden dependencies and blockers along the way.

## Process

### 1. Define the End State
- What does the desired outcome look like in concrete terms?
- What are the measurable success criteria?
- What does "done" look like?

### 2. Identify Immediate Prerequisites
For the end state to exist, what must be true? List every direct prerequisite.

### 3. Chain Backwards
For each prerequisite, ask "What must be true for THIS to exist?" Continue chaining backwards until you reach the current state or an actionable starting point.

### 4. Dependency Map
Organize the chain into a dependency graph:
- What can be done in parallel?
- What is strictly sequential?
- Where are the bottlenecks?

### 5. Surface Hidden Blockers
Look for:
- Circular dependencies
- Implicit assumptions about available resources or capabilities
- Steps that seem simple but have hidden complexity
- External dependencies or approvals needed
- Knowledge gaps that need to be filled first

### 6. Build the Forward Plan
Reverse the backwards chain into a forward execution plan with clear phases and milestones.

## Output Format

```
## Reverse-Engineering: [Goal]

### Desired End State
[Concrete description of what success looks like]

### Backwards Chain
Goal ← [Prerequisite A] ← [Prerequisite A1] ← [Current State]
     ← [Prerequisite B] ← [Prerequisite B1] ← [Current State]

### Dependency Map
Phase 1 (parallel):
  - [ ] [Task] — depends on: nothing
  - [ ] [Task] — depends on: nothing

Phase 2 (after Phase 1):
  - [ ] [Task] — depends on: [Phase 1 tasks]

Phase 3:
  - [ ] [Task] — depends on: [Phase 2 tasks]

### Hidden Blockers & Risks
1. **[Blocker]**: Why it matters + mitigation
2. ...

### Forward Execution Plan
1. [First actionable step]
2. [Next step]
...
```

## Guidelines
- Be specific — vague prerequisites hide complexity
- When reverse-engineering code changes, read the actual codebase to identify real dependencies
- Flag any step where you're uncertain about feasibility
- Distinguish between hard dependencies (must happen first) and soft dependencies (easier if done first)
