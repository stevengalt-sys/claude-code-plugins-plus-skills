---
description: Deep codebase analysis with architecture mapping, dependency graphs, and complexity hotspots
shortcut: sa
---

# Superpower Codebase Analyzer

You are performing a deep analysis of the codebase. Follow this protocol.

## Step 1: Project Overview

Scan the project structure:
- Use Glob to map the directory layout
- Identify the tech stack from config files (package.json, pyproject.toml, Cargo.toml, etc.)
- Find the entry points (main files, index files, route handlers)
- Note the test setup and build configuration

## Step 2: Architecture Mapping

Trace the high-level architecture:
- **Layers**: Identify architectural layers (routes, controllers, services, models, utilities)
- **Modules**: Map the major modules and their responsibilities
- **Data flow**: Trace how data moves through the system (request to response, input to output)
- **External integrations**: APIs, databases, message queues, file storage

## Step 3: Dependency Analysis

For each major module:
- Count imports (incoming dependencies = how many modules use it)
- Count exports (outgoing dependencies = how much it depends on)
- Identify circular dependencies
- Flag modules with unusually high coupling

## Step 4: Complexity Hotspots

Search for complexity indicators:
- **Large files**: Files with many lines of code (>300 lines)
- **Long functions**: Functions exceeding 50 lines
- **Deep nesting**: More than 3 levels of indentation
- **High branching**: Functions with many if/else or switch cases
- **God objects**: Classes or modules doing too many things
- **Repeated patterns**: Similar code blocks that could be consolidated

## Step 5: Report

Present findings in a structured format:

### Architecture Summary
Brief description of the project's architecture pattern.

### Module Map
List of major modules with their responsibilities and key files.

### Dependency Insights
High-coupling modules, circular dependencies, and import hotspots.

### Complexity Hotspots
Ranked list of the most complex areas with specific file:line references.

### Recommendations
Actionable suggestions for improvement, prioritized by impact.
