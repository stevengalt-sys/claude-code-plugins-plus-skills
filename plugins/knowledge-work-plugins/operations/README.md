# Operations

**Operational workflow toolkit for Claude Code. Build runbooks, map processes, and conduct incident reviews using structured knowledge-work patterns.**

---

## Features

### Auto-Invoked Skills
- **Runbook Builder**: Create step-by-step operational runbooks and SOPs with decision trees, rollback procedures, and escalation paths
- **Process Mapper**: Document workflows with actors, handoffs, SLAs, and Mermaid flowchart diagrams
- **Incident Reviewer**: Generate blameless postmortems with 5 Whys root cause analysis and prioritized action items

### Slash Commands
- `/build-runbook` - Create an operational runbook or SOP
- `/incident-review` - Generate a blameless incident review
- `/map-process` - Document and visualize a workflow

---

## Installation

```bash
/plugin install operations@claude-code-plugins
```

---

## Usage

### Runbook Builder
```
Create a runbook for deploying database migrations to production
```

### Process Mapper
```
Map the deployment process from PR merge to production
```

### Incident Reviewer
```
Write a postmortem for the 2-hour API outage caused by a bad config push
```

---

## License

MIT
