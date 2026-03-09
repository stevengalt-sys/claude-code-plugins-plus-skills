---
name: plan-wireframe
description: Plan a wireframe layout with content hierarchy and interaction annotations
arguments:
  - name: screen
    description: The screen or page to wireframe
    required: true
---

Plan a detailed wireframe for: $ARGUMENTS.screen

Follow the design-wireframe-planner skill guidelines. Include:
1. Screen purpose and user goal
2. Content hierarchy (primary, secondary, tertiary)
3. ASCII layout sketches for desktop and mobile
4. Interaction annotations for all interactive elements
5. Edge cases: empty, loading, error, and overflow states
6. Navigation flow connections to other screens

Output as a structured Markdown wireframe plan ready for design handoff.
