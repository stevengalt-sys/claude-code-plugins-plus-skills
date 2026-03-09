---
name: map-process
description: Document and visualize an operational process or workflow
arguments:
  - name: process
    description: The process or workflow to map
    required: true
---

Map and document the following operational process: $ARGUMENTS.process

Follow the ops-process-mapper skill guidelines. Include:
1. Process trigger and end state
2. All actors and systems involved
3. Step-by-step process table with inputs, outputs, and SLAs
4. Mermaid flowchart diagram
5. Handoff points between teams
6. Bottlenecks and automation opportunities

Output as a structured Markdown document with an embedded Mermaid diagram.
