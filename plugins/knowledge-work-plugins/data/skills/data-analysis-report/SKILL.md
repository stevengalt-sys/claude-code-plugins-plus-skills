---
name: data-analysis-report
description: |
  Generate structured data analysis reports with findings, visualizations, and
  recommendations. Use when analyzing datasets, summarizing metrics, or producing
  insight reports from data.
  Trigger with phrases like 'analyze data', 'data report', 'insight report', 'metrics summary'.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*), Bash(node:*)
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Data Analysis Report

## Overview

Produces structured data analysis reports with executive summary, methodology, key findings, visualizations, and actionable recommendations. Works with CSV, JSON, SQL query results, or any tabular data.

## Prerequisites

- Dataset or data source to analyze
- Analysis objective or questions to answer
- Any relevant context about the data domain

## Instructions

1. Understand the analysis objective and key questions
2. Profile the dataset: row count, columns, types, missing values, distributions
3. Perform exploratory analysis: summary statistics, correlations, outliers
4. Identify key findings that answer the stated questions
5. Create supporting tables or chart specifications for each finding
6. Quantify impact or significance of each finding
7. Provide actionable recommendations based on the findings
8. Note data limitations and caveats

## Output Format

```markdown
# Data Analysis Report: [Title]

**Date:** [Date]
**Author:** [Name]
**Data Source:** [Source description]
**Period:** [Time range if applicable]

## Executive Summary
[3-5 sentences covering the most important findings and recommendations]

## Methodology
- **Data Source:** [Where the data came from]
- **Sample Size:** [N records]
- **Time Period:** [Date range]
- **Tools Used:** [Python/SQL/etc.]

## Data Profile
| Column | Type | Non-Null | Unique | Notes |
|--------|------|----------|--------|-------|

## Key Findings

### Finding 1: [Title]
[Description with supporting numbers]

| Metric | Value |
|--------|-------|

### Finding 2: [Title]
[Description with supporting numbers]

## Recommendations
1. **[Action]** - [Expected impact] - [Priority]

## Limitations
- [Caveat 1]

## Appendix
[Additional tables or detailed breakdowns]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Insufficient data | Too few records for meaningful analysis | State minimum sample size needed and flag low confidence |
| Missing values | Nulls or gaps in critical columns | Document missing data percentage and handling strategy |
| No clear objective | Vague analysis request | Ask for specific questions the analysis should answer |

## Examples

**Example: Sales Performance Report**
Request: "Analyze Q4 sales data and identify top-performing regions"
Result: Report with regional breakdown, YoY growth, seasonality patterns, and recommendations for underperforming territories

**Example: User Behavior Analysis**
Request: "Analyze signup funnel data to find drop-off points"
Result: Funnel visualization, step-by-step conversion rates, cohort comparison, and UX improvement recommendations
