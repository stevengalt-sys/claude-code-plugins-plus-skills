---
name: incident-review
description: Generate a blameless incident review or postmortem document
arguments:
  - name: incident
    description: Description of the incident to review
    required: true
---

Conduct a blameless incident review for: $ARGUMENTS.incident

Follow the ops-incident-reviewer skill guidelines. Include:
1. Incident summary and impact metrics
2. Detailed timeline of events
3. Root cause analysis using 5 Whys
4. Contributing factors
5. What went well and what could be improved
6. Prioritized action items with owners and categories

Maintain blameless language throughout. Focus on systems and processes, not individuals.
