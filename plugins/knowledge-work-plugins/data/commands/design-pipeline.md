---
name: design-pipeline
description: Design a data pipeline or ETL/ELT workflow specification
arguments:
  - name: pipeline
    description: The data pipeline or workflow to design
    required: true
---

Design a data pipeline for: $ARGUMENTS.pipeline

Follow the data-pipeline-designer skill guidelines. Include:
1. Source definitions with formats and access patterns
2. Transformation logic and field mappings
3. Destination schema and partitioning
4. Mermaid DAG diagram of the pipeline flow
5. Error handling and dead-letter queue strategy
6. Monitoring metrics and alerting thresholds
7. Backfill and reprocessing strategy

Output as an implementation-ready Markdown specification.
