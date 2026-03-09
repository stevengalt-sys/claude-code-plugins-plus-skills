---
name: audit-data-quality
description: Audit data quality and generate a scorecard with remediation plan
arguments:
  - name: target
    description: The dataset or table to audit
    required: true
---

Perform a data quality audit on: $ARGUMENTS.target

Follow the data-quality-auditor skill guidelines. Include:
1. Quality scorecard across all six dimensions (completeness, accuracy, consistency, timeliness, uniqueness, validity)
2. Detailed findings for each dimension
3. Prioritized remediation plan with effort estimates
4. Monitoring recommendations for ongoing quality checks

Output as a structured Markdown audit report.
