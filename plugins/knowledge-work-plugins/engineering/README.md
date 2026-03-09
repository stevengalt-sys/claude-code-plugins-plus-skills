# Engineering

**Software engineering knowledge-work toolkit for Claude Code. Write design docs, architecture decision records, and structured code review guides.**

---

## Features

### Auto-Invoked Skills
- **Design Doc Writer**: Create technical design documents and RFCs with problem statements, proposed solutions, alternatives, and rollout plans
- **Code Review Guide**: Generate structured code review feedback categorized by severity with actionable fix suggestions
- **Architecture Decision Record**: Document significant technical decisions with context, consequences, and alternatives

### Slash Commands
- `/write-design-doc` - Write a technical design document or RFC
- `/write-adr` - Create an Architecture Decision Record
- `/review-code` - Generate structured code review feedback

---

## Installation

```bash
/plugin install engineering@claude-code-plugins
```

---

## Usage

### Design Doc Writer
```
Write a design doc for migrating our auth service to OAuth 2.0
```

### Architecture Decision Record
```
Write an ADR for choosing gRPC over REST for internal services
```

### Code Review Guide
```
Review the changes in src/auth/handler.ts for security issues
```

---

## License

MIT
