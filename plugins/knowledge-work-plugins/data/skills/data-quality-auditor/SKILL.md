---
name: data-quality-auditor
description: |
  Audit data quality and generate validation reports with completeness, accuracy,
  consistency, and freshness checks. Use when assessing dataset health, validating
  data migrations, or building data quality frameworks.
  Trigger with phrases like 'data quality', 'audit data', 'validate data', 'data health check', 'data profiling'.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*), Bash(node:*)
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Data Quality Auditor

## Overview

Generates comprehensive data quality audit reports covering the six dimensions of data quality: completeness, accuracy, consistency, timeliness, uniqueness, and validity. Produces actionable scorecards with remediation priorities.

## Prerequisites

- Dataset or database table to audit
- Expected schema or data dictionary
- Business rules for validation (if available)
- Acceptable thresholds for quality metrics

## Instructions

1. Profile the dataset: schema, row count, column types, distributions
2. Assess completeness: null rates, missing required fields, sparse columns
3. Assess accuracy: values within expected ranges, format compliance
4. Assess consistency: cross-field rules, referential integrity, duplicates
5. Assess timeliness: data freshness, stale records, timestamp gaps
6. Assess uniqueness: duplicate detection on key columns
7. Assess validity: enum compliance, regex patterns, business rule adherence
8. Score each dimension and compute an overall quality score
9. Prioritize remediation actions by impact

## Output Format

```markdown
# Data Quality Audit: [Dataset Name]

**Date:** [Date]
**Auditor:** [Name]
**Dataset:** [Source and table/file]
**Records:** [Total count]

## Quality Scorecard
| Dimension | Score | Status | Details |
|-----------|-------|--------|---------|
| Completeness | 92% | Pass | 3 columns below threshold |
| Accuracy | 87% | Warning | Date formats inconsistent |
| Consistency | 95% | Pass | 2 orphaned foreign keys |
| Timeliness | 78% | Fail | 22% records stale > 7 days |
| Uniqueness | 99% | Pass | 12 duplicate records |
| Validity | 91% | Pass | 4 enum violations |
| **Overall** | **90%** | **Warning** | |

## Detailed Findings

### Completeness
| Column | Null Rate | Threshold | Status |
|--------|-----------|-----------|--------|

### Accuracy
| Check | Expected | Actual | Records Affected |
|-------|----------|--------|-----------------|

### Consistency
| Rule | Description | Violations |
|------|-------------|-----------|

## Remediation Plan
| Priority | Issue | Impact | Remediation | Effort |
|----------|-------|--------|-------------|--------|
| P1 | [Issue] | [Impact] | [Fix] | [Estimate] |

## Monitoring Recommendations
- [ ] [Automated check to add]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| No data dictionary | Unknown expected schema | Profile data first and infer expected types and ranges |
| No thresholds defined | Cannot determine pass/fail | Use industry defaults: 95% completeness, 99% uniqueness |
| Large dataset | Cannot scan full table | Use statistical sampling with confidence intervals |

## Examples

**Example: Customer Database Audit**
Request: "Audit data quality of our customers table before the CRM migration"
Result: Scorecard showing 15% email null rate, 200 duplicate phone numbers, and 3% records with invalid state codes, with prioritized cleanup plan

**Example: Post-Migration Validation**
Request: "Validate that the data migration from legacy to new system preserved data integrity"
Result: Row count comparison, column-level diff analysis, referential integrity checks, and list of discrepancies to resolve
