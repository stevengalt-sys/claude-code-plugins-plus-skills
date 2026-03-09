---
name: data-pipeline-designer
description: |
  Design data pipelines and ETL/ELT workflows with source-to-destination mappings,
  transformations, and scheduling. Use when planning data ingestion, transformation,
  or orchestration architectures.
  Trigger with phrases like 'design pipeline', 'ETL workflow', 'data pipeline', 'ELT architecture', 'data ingestion'.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: ClaudeCodePlugins <plugins@claudecodeplugins.io>
license: MIT
---

# Data Pipeline Designer

## Overview

Designs structured data pipeline specifications with source definitions, transformation logic, destination schemas, scheduling, monitoring, and failure handling. Outputs implementation-ready pipeline documents.

## Prerequisites

- Source system descriptions (databases, APIs, files, streams)
- Destination or target system requirements
- Data freshness and latency requirements
- Volume estimates

## Instructions

1. Define all data sources with connection details, formats, and access patterns
2. Map source fields to destination schema with transformation rules
3. Specify data quality checks at each stage (ingestion, transform, load)
4. Design the execution DAG with dependencies between tasks
5. Set scheduling cadence and SLAs
6. Define error handling: retries, dead-letter queues, alerting
7. Plan for backfill and reprocessing scenarios
8. Document monitoring and observability requirements
9. Generate a Mermaid diagram of the pipeline flow

## Output Format

```markdown
# Data Pipeline: [Name]

**Owner:** [Team]
**Schedule:** [Cron expression / event-driven]
**SLA:** [Freshness target]
**Volume:** [Estimated rows/day]

## Sources
| Source | Type | Format | Frequency | Auth |
|--------|------|--------|-----------|------|

## Transformations
| Step | Input | Logic | Output | Quality Check |
|------|-------|-------|--------|---------------|

## Destination
| Table/Topic | Schema | Partitioning | Retention |
|-------------|--------|-------------|-----------|

## Pipeline DAG
\```mermaid
flowchart LR
    A[Source A] --> T1[Transform 1]
    B[Source B] --> T1
    T1 --> Q1{Quality Gate}
    Q1 -->|Pass| L1[Load]
    Q1 -->|Fail| DLQ[Dead Letter Queue]
\```

## Error Handling
| Failure Mode | Detection | Response | Recovery |
|-------------|-----------|----------|----------|

## Monitoring
| Metric | Threshold | Alert |
|--------|-----------|-------|

## Backfill Strategy
[How to reprocess historical data]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Unknown source schema | Source not documented | Profile the source and document schema before designing transforms |
| Unclear SLA | No freshness requirement stated | Ask whether near-real-time, hourly, or daily freshness is needed |
| Missing volume estimate | Cannot size infrastructure | Estimate from source system metrics or request sample data |

## Examples

**Example: Event Analytics Pipeline**
Request: "Design a pipeline to ingest clickstream events into our data warehouse"
Result: Pipeline spec with Kafka source, schema validation, sessionization transform, BigQuery destination, and 15-minute SLA

**Example: CRM Data Sync**
Request: "Design ETL to sync Salesforce data to our PostgreSQL analytics DB"
Result: Pipeline with API extraction, incremental CDC, deduplication, SCD Type 2 handling, and daily refresh schedule
