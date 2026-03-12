---
name: superpowers
description: |
  Use when the user needs multi-file refactoring, comprehensive test generation,
  or deep codebase analysis. Trigger with "refactor across files", "generate tests",
  "analyze codebase", "find complexity", "map dependencies", or "superpower".
allowed-tools: Read, Write, Edit, Bash(npm:*), Glob, Grep, TodoWrite
version: 1.0.0
license: MIT
author: Claude Plugins Official <plugins@claudecodeplugins.io>
---

# Superpowers Skill

You have enhanced capabilities for complex coding tasks. Apply these patterns automatically when relevant.

## Multi-File Refactoring Protocol

When performing refactors that span multiple files:

1. **Discovery** - Use Grep and Glob to find ALL references to the target (functions, types, imports, tests, docs)
2. **Impact analysis** - Map the dependency chain: what calls what, what imports what, what tests cover what
3. **Checkpoint** - Create a TodoWrite checklist of every file that needs changes before editing anything
4. **Execute** - Edit files in dependency order (leaf nodes first, then dependents)
5. **Verify** - After all edits, grep again to confirm no stale references remain

Always track progress with TodoWrite. Never edit a file without reading it first.

## Smart Test Generation Protocol

When generating tests:

1. **Analyze the target** - Read the function/module, identify:
   - Input types and valid ranges
   - Edge cases (empty, null, boundary values, overflow)
   - Error paths and exception handling
   - Side effects and external dependencies
2. **Design test cases** - Group by:
   - Happy path (normal operation)
   - Edge cases (boundaries and special values)
   - Error cases (invalid input, failures)
   - Integration points (if applicable)
3. **Generate with mocks** - Stub external dependencies, use appropriate test framework conventions
4. **Validate** - Run the tests to ensure they pass

## Codebase Analysis Protocol

When analyzing a codebase:

1. **Structure mapping** - Glob for key patterns (`**/*.ts`, `**/*.py`, etc.) to understand project layout
2. **Entry points** - Find main files, route handlers, exported APIs
3. **Dependency graph** - Trace imports to build a mental model of module relationships
4. **Complexity hotspots** - Look for:
   - Files with many imports (high coupling)
   - Large functions (>50 lines)
   - Deep nesting (>3 levels)
   - Repeated patterns that could be abstracted
5. **Report** - Summarize findings with specific file:line references

## General Principles

- Read before you write. Always understand existing code before modifying it.
- Track complex tasks with TodoWrite to ensure nothing is missed.
- Prefer targeted edits over full rewrites.
- When in doubt, analyze more before acting.
