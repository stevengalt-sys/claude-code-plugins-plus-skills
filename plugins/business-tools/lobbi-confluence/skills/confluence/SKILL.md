---
name: confluence
description: |
  Guide creating, organizing, and maintaining technical documentation in Confluence with Jira integration.
  Provides document templates (TDD, ADR, API docs, runbooks, release notes, meeting notes, retrospectives),
  CQL search patterns, and best practices for discoverable, linked documentation.
  Trigger with "confluence doc", "write confluence page", "confluence template", "CQL search",
  "jira confluence", "technical design doc", "ADR", "runbook", "API documentation".
allowed-tools: "Read, Write, Edit, Grep, Glob, WebFetch, WebSearch"
version: "1.0.0"
author: "lobbi-docs <lobbi-docs@claudecodeplugins.io>"
license: "MIT"
---

# Confluence Documentation Skill

Create, organize, and maintain technical documentation in Confluence with practical Jira integration patterns.

## Document Templates

### Technical Design Document (TDD)

```markdown
# [Feature/System Name] — Technical Design

| Field        | Value                          |
|-------------|--------------------------------|
| Author      | @mention                       |
| Status      | Draft / In Review / Approved   |
| Created     | YYYY-MM-DD                     |
| Jira Epic   | [PROJ-123](jira-link)          |
| Reviewers   | @mention, @mention             |

## Context & Problem Statement
Why this design is needed. Link to the originating Jira epic or product brief.

## Goals & Non-Goals
- **Goal:** What this achieves
- **Non-Goal:** What is explicitly out of scope

## Proposed Solution
High-level architecture and approach.

## Alternatives Considered
| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| A      |      |      | Chosen   |
| B      |      |      | Rejected |

## API Changes
Endpoints, request/response schemas, breaking changes.

## Data Model Changes
Schema migrations, new tables/fields, index changes.

## Rollout Plan
Feature flags, phased rollout, rollback strategy.

## Open Questions
- [ ] Question 1
- [ ] Question 2
```

### Architecture Decision Record (ADR)

```markdown
# ADR-NNN: [Decision Title]

| Field    | Value              |
|----------|--------------------|
| Status   | Proposed / Accepted / Deprecated / Superseded |
| Date     | YYYY-MM-DD         |
| Deciders | @mention, @mention |

## Context
What forces are at play, including technical, business, and social.

## Decision
The change we are proposing or have agreed to implement.

## Consequences
### Positive
- Benefit 1

### Negative
- Trade-off 1

### Neutral
- Side effect 1

## Related
- Supersedes: ADR-NNN
- Related Jira: PROJ-123
```

### API Documentation

```markdown
# [Service Name] API Reference

## Overview
Base URL, authentication, rate limits.

## Authentication
Header format, token types, scopes.

## Endpoints

### `POST /api/v1/resource`

**Description:** Creates a new resource.

**Headers:**
| Header        | Required | Description          |
|--------------|----------|----------------------|
| Authorization | Yes      | Bearer token         |
| Content-Type  | Yes      | application/json     |

**Request Body:**
| Field | Type   | Required | Description     |
|-------|--------|----------|-----------------|
| name  | string | Yes      | Resource name   |
| type  | string | No       | Resource type   |

**Response:** `201 Created`
| Field | Type   | Description           |
|-------|--------|-----------------------|
| id    | string | Unique identifier     |
| name  | string | Resource name         |

**Error Codes:**
| Code | Description              |
|------|--------------------------|
| 400  | Invalid request body     |
| 401  | Unauthorized             |
| 409  | Resource already exists  |
```

### Runbook

```markdown
# [Service/System] Runbook

| Field       | Value                    |
|-------------|--------------------------|
| Owner       | @team                    |
| Last Review | YYYY-MM-DD               |
| On-Call      | [PagerDuty rotation]    |
| Jira Board  | [PROJ board](link)      |

## Service Overview
What it does, dependencies, architecture diagram link.

## Health Checks
- **Endpoint:** `/health`
- **Dashboard:** [Grafana link]
- **Alerts:** [PagerDuty service]

## Common Issues & Remediation

### Issue: High Latency
**Symptoms:** p99 > 500ms on dashboard
**Steps:**
1. Check database connection pool: `SELECT * FROM pg_stat_activity;`
2. Review recent deployments in Jira
3. Scale horizontally if load-related

### Issue: OOM Kills
**Symptoms:** Pod restarts, memory alerts
**Steps:**
1. Check memory usage in Grafana
2. Review heap dumps
3. Increase memory limits or fix leak

## Deployment
- **Pipeline:** [CI/CD link]
- **Rollback:** `kubectl rollout undo deployment/service-name`

## Escalation
1. Primary on-call
2. Team lead
3. Engineering manager
```

### Release Notes

```markdown
# Release v[X.Y.Z] — YYYY-MM-DD

## Highlights
Brief summary of the most impactful changes.

## New Features
- **Feature Name** (PROJ-123): Description

## Improvements
- **Enhancement** (PROJ-456): Description

## Bug Fixes
- **Fix** (PROJ-789): Description

## Breaking Changes
- **Change**: Migration steps required

## Known Issues
- PROJ-999: Description and workaround
```

### Meeting Notes

```markdown
# [Meeting Name] — YYYY-MM-DD

| Field        | Value              |
|--------------|--------------------|
| Attendees    | @mention, @mention |
| Facilitator  | @mention           |
| Note Taker   | @mention           |

## Agenda
1. Topic 1
2. Topic 2

## Discussion
### Topic 1
Key points and decisions.

### Topic 2
Key points and decisions.

## Action Items
| Action | Owner | Due Date | Jira |
|--------|-------|----------|------|
| Task 1 | @name | YYYY-MM-DD | PROJ-123 |

## Next Meeting
Date, time, topics to carry forward.
```

### Retrospective

```markdown
# Sprint [N] Retrospective — YYYY-MM-DD

| Field | Value |
|-------|-------|
| Team  | @team |
| Sprint | YYYY-MM-DD to YYYY-MM-DD |

## What Went Well
- Item 1
- Item 2

## What Could Improve
- Item 1 → **Action:** Description (Owner: @name, Jira: PROJ-123)

## Action Items from Last Retro
| Action | Owner | Status |
|--------|-------|--------|
| Previous item | @name | Done / In Progress |
```

## Confluence Query Language (CQL) Patterns

Use CQL to find and organize content efficiently.

### Common Searches

```
# Pages in a specific space modified recently
space = "ENG" AND type = "page" AND lastModified > now("-7d")

# Pages by a specific author
space = "ENG" AND creator = "user@company.com"

# Pages with a specific label
space = "ENG" AND label = "architecture-decision"

# Pages containing specific text
space = "ENG" AND text ~ "authentication"

# Pages under a specific parent
space = "ENG" AND ancestor = "123456789"

# ADRs created this quarter
label = "adr" AND created > "2026-01-01" AND created < "2026-04-01"

# Recently updated runbooks
label = "runbook" AND lastModified > now("-30d") ORDER BY lastModified DESC

# Pages linked to a Jira project
label = "jira-PROJ" AND type = "page"
```

### Label Strategy

Use consistent labels to make content discoverable:

| Label Pattern      | Purpose                        |
|-------------------|--------------------------------|
| `tdd`             | Technical Design Documents     |
| `adr`             | Architecture Decision Records  |
| `api-docs`        | API documentation              |
| `runbook`         | Operational runbooks           |
| `release-notes`   | Release notes                  |
| `meeting-notes`   | Meeting notes                  |
| `retro`           | Retrospectives                 |
| `jira-PROJ`       | Linked to Jira project PROJ    |
| `team-TEAMNAME`   | Owned by team                  |
| `status-draft`    | Work in progress               |
| `status-approved` | Reviewed and approved          |

## Jira Integration Patterns

### Smart Links

Paste Jira URLs directly into Confluence pages for automatic smart link rendering:
- Issue links: `https://company.atlassian.net/browse/PROJ-123`
- Board links: `https://company.atlassian.net/jira/software/projects/PROJ/boards/1`

### Jira Issue Macro

Embed live Jira issue data in Confluence:

```
Jira macro JQL: project = PROJ AND fixVersion = "1.2.0" AND status = Done
Columns: key, summary, assignee, status
```

### Jira Roadmap Macro

Embed a project roadmap view showing epics and their progress.

### Linking Patterns

- Reference Jira issues in docs: `[PROJ-123](https://company.atlassian.net/browse/PROJ-123)`
- Add Confluence page links to Jira issues via the "Confluence Page" link type
- Use Jira issue keys in Confluence page titles for traceability

## Best Practices

### Page Organization
- Use a consistent space hierarchy: `Team > Area > Document Type`
- Put templates in a dedicated `Templates` section per space
- Archive stale pages quarterly — use CQL to find pages not modified in 90+ days

### Writing Standards
- Start every page with a metadata table (author, status, date, Jira link)
- Use headings consistently — H1 for title only, H2 for sections, H3 for subsections
- Include a "Related" section at the bottom linking to other Confluence pages and Jira items
- Add labels immediately when creating pages

### Review Workflow
1. Author creates page with `status-draft` label
2. Add reviewers via page mentions
3. Reviewers comment inline
4. Author updates and changes label to `status-approved`
5. Link approved page to relevant Jira epic

### Maintenance
- Set quarterly review reminders for runbooks and API docs
- Use CQL to audit pages without labels: `space = "ENG" AND label IS EMPTY`
- Archive or update pages flagged as outdated
