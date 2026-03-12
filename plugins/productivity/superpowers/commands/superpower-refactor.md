---
description: Intelligent multi-file refactoring with dependency tracking and rollback safety
shortcut: sr
---

# Superpower Refactor

You are performing an intelligent multi-file refactor. Follow this protocol strictly.

## Step 1: Understand the Request

Ask the user what they want to refactor if not already clear. Common refactors include:
- Renaming a function, class, type, or variable across the codebase
- Extracting shared logic into a new module
- Moving a file/module and updating all imports
- Changing a function signature and updating all call sites
- Converting between patterns (callbacks to async/await, classes to functions, etc.)

## Step 2: Discovery

Use Grep to find every reference to the target across the codebase. Search for:
- Direct usage (function calls, type references)
- Imports and exports
- String references (configs, documentation)
- Test files that exercise the target

Report the full list of affected files to the user.

## Step 3: Plan

Create a TodoWrite checklist with every file that needs changes. Order them by dependency (change leaves first, then dependents). Present the plan to the user for approval.

## Step 4: Execute

Edit each file systematically:
- Read the file first
- Make the minimal necessary change
- Mark the todo item complete
- Move to the next file

## Step 5: Verify

After all edits:
- Grep again for any remaining stale references
- Run existing tests if a test command is available
- Report results to the user
