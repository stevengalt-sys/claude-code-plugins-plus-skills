---
name: analyze-data
description: Generate a structured data analysis report with findings and recommendations
arguments:
  - name: target
    description: The dataset, file, or data source to analyze
    required: true
---

Generate a structured data analysis report for: $ARGUMENTS.target

Follow the data-analysis-report skill guidelines. Include:
1. Executive summary of key findings
2. Methodology and data profiling
3. Key findings with supporting metrics and tables
4. Actionable recommendations with expected impact
5. Data limitations and caveats

Output as a polished Markdown report ready for stakeholder review.
