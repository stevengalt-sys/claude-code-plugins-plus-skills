---
description: Generate comprehensive test suites with edge cases, mocks, and coverage targets
shortcut: st
---

# Superpower Test Generator

You are generating a comprehensive test suite. Follow this protocol.

## Step 1: Identify the Target

Determine what needs testing:
- A specific function or method
- A module or class
- An API endpoint or route handler
- A full feature or workflow

Read the target code thoroughly before writing any tests.

## Step 2: Analyze Code Paths

For the target, identify:
- **Inputs**: All parameters, their types, and valid ranges
- **Outputs**: Return values, side effects, state changes
- **Branches**: Every if/else, switch case, try/catch, early return
- **Dependencies**: External calls that need mocking (APIs, databases, file system)
- **Edge cases**: Empty inputs, null/undefined, boundary values, large inputs, concurrent access

## Step 3: Design Test Cases

Organize tests into groups:

### Happy Path
- Normal operation with typical inputs
- Expected outputs and state changes

### Edge Cases
- Empty/zero/null inputs
- Boundary values (min, max, off-by-one)
- Special characters or unicode
- Very large or very small inputs

### Error Cases
- Invalid input types
- Missing required fields
- Network/IO failures (when mocking)
- Permission errors
- Timeout scenarios

### Integration (if applicable)
- Component interactions
- Data flow through the system

## Step 4: Generate Tests

Write tests using the project's existing test framework and conventions. Include:
- Descriptive test names that explain the scenario
- Arrange-Act-Assert pattern
- Proper mocking/stubbing of external dependencies
- Cleanup in afterEach/teardown if needed

## Step 5: Run and Validate

Execute the tests and fix any failures. Report coverage if tools are available.
