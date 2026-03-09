---
name: lms-capability-framework
description: |
  Enterprise Learning Management System capability framework for designing, building,
  and evaluating LMS platforms. Use when working on LMS architecture, course management,
  user role design, assessment systems, certification workflows, learning analytics,
  SCORM integration, or enterprise learning solutions.
  Trigger phrases: "LMS", "learning management", "course management", "elearning platform",
  "training system", "certification system", "SCORM", "learning paths", "enrolment system".
allowed-tools: Read, Write, Edit, Bash(cmd:*), Glob, Grep, WebSearch
version: 1.0.0
author: SpillwaveSolutions
license: MIT
---

# LMS Capability Framework

Enterprise Learning Management System design framework covering 8 functional modules, entity architecture, MVP roadmap, and implementation patterns.

## Module 1: Course Management & Content Delivery

Manages how learning is structured and delivered.

### Core Functions

- Create and manage courses, modules, lessons, and learning paths
- Support content types: video, PDF, SCORM packages, links, downloadable files, live session references
- Organize content by category, topic, audience, business unit, mandatory vs optional
- Version control for course updates
- Course publishing, archiving, and expiry settings
- Prerequisites and sequencing rules
- Enrolment logic: self-enrolment, assigned learning, cohort-based enrolment

### Recommended Fields

| Field | Purpose |
|-------|---------|
| Course title | Display name |
| Description | Summary of learning objectives |
| Category | Classification for discovery |
| Delivery type | Online, blended, instructor-led |
| Duration | Expected time to complete |
| Owner | Responsible person or team |
| Status | Draft, published, archived |
| Version | Content version tracking |
| Mandatory flag | Required vs optional learning |
| Prerequisite course(s) | Sequencing dependencies |
| Target audience | Intended learner group |
| Completion rules | What constitutes completion |

---

## Module 2: User & Role Management

Controls who can access what and what they can do.

### Primary Roles

| Role | Responsibility |
|------|---------------|
| **Admin** | Full system control |
| **Instructor / Facilitator** | Manage delivery, attendance, assessment |
| **Manager** | Monitor team learning |
| **Learner / Student** | Consume content and complete assigned learning |
| **Content Author** | Create and maintain learning content |
| **Compliance Reviewer** | Audit records and completion evidence |

### Core Functions

- User profile creation and maintenance
- Team/business unit mapping
- Role-based permissions
- Group and cohort management
- Access control by course, pathway, and report
- SSO / identity integration support
- Bulk import/export of users
- Manager hierarchy support

### Key Access Rules

- Learners see only their own learning
- Managers see direct reports or assigned groups
- Instructors see their courses and sessions
- Admins see all users, courses, and reports

---

## Module 3: Assessment & Certification

Validates that learning has occurred and allows formal recognition.

### Assessment Types

- Quizzes
- Knowledge checks
- Assignments
- Facilitator-marked tasks
- Practical sign-off
- Evidence upload
- Pass/fail or graded assessment

### Core Functions

- Question banks
- Randomised quizzes
- Attempts and retry rules
- Pass marks and grading thresholds
- Manual and automatic marking
- Assignment submission workflow
- Evidence upload and approval
- Certificate generation
- Certificate expiry / renewal tracking

### Certificate Fields

| Field | Purpose |
|-------|---------|
| Learner name | Certificate holder |
| Course name | What was completed |
| Completion date | When completed |
| Expiry date | When renewal is required |
| Certificate ID | Unique identifier |
| Issued by | Issuing authority |
| Verification status | Valid, expired, revoked |

---

## Module 4: Reporting & Analytics

Gives visibility into performance, compliance, and engagement.

### Core Reporting Areas

- Course completion rates
- Overdue mandatory training
- Learner progress by pathway
- Assessment performance
- Engagement metrics
- Facilitator workload
- Completion by business unit / team / role
- Onboarding progress for new starters

### Role-Based Dashboards

**Admin dashboard**: total learners, active courses, overdue mandatory items, compliance rate

**Manager dashboard**: team completion status, upcoming due dates, overdue training

**Instructor dashboard**: upcoming sessions, attendance trends, assessment outcomes

**Learner dashboard**: assigned learning, completed courses, certificates, next due items

### Analytics Metrics

| Metric | What it measures |
|--------|-----------------|
| Completion % | Learning completion rate |
| Average assessment score | Assessment quality indicator |
| Time to completion | Learning efficiency |
| Course dropout rate | Engagement health |
| Average session attendance | Live session engagement |
| Content usage by type | Content format effectiveness |

---

## Module 5: Integration Capabilities

Ensures the LMS operates within a broader digital ecosystem.

### Key Integrations

- HRIS / workforce systems
- Identity providers / SSO
- Microsoft Teams
- Zoom
- Outlook / email services
- SharePoint / document libraries
- Content libraries / SCORM repositories
- BI tools such as Power BI
- CRM or case systems if learning needs to align with operational capability

### Integration Use Cases

- Auto-create learner accounts from HR system
- Assign onboarding learning based on new starter status
- Sync managers and reporting lines
- Launch virtual training sessions in Teams or Zoom
- Store evidence in SharePoint
- Send reminders and completion notifications
- Expose completion data to reporting tools

### Technical Expectations

- REST API support
- Webhook/event support
- Import/export endpoints
- Secure authentication
- Audit logs

---

## Module 6: Content Authoring

Covers creation and maintenance of learning materials.

### Built-in Authoring

- Simple pages with text, images, video embeds
- Quizzes
- Downloadable resources

### Integrated Authoring Tools

- Articulate Rise
- Articulate Storyline
- Adobe Captivate
- External SCORM tools

### Governance Controls

| Control | Purpose |
|---------|---------|
| Draft / review / approved / published lifecycle | Content quality gate |
| Content owner | Accountability |
| Next review date | Currency tracking |
| Compliance sign-off | Regulatory approval |
| Superseded version archive | Version history |

---

## Core Entity Architecture

When designing the data model, use these entity groups:

### Users
- Learner, Instructor, Manager, Admin, Author

### Learning
- Course, Module, Lesson, Pathway, Content Asset

### Delivery
- Session, Enrolment, Attendance

### Assessment
- Quiz, Question Bank, Assignment, Submission, Certificate

### Tracking
- Completion Record, Progress Log, Evidence Record, Audit Log

### Integration
- Sync Job, External Source Mapping, API Event Log

---

## MVP vs Phase 2 Roadmap

### MVP Scope

- Course catalogue
- User and role management
- Assigned learning
- Video/PDF/SCORM content support
- Quiz and pass/fail completion
- Certificates
- Dashboard and standard reports
- Teams/Zoom links
- CSV import/export

### Phase 2 Scope

- Advanced content authoring
- Full API integration layer
- HRIS sync
- Manager approval workflows
- Evidence review workflow
- Recertification automation
- Advanced analytics
- Learning recommendations

---

## Implementation Architecture Options

### Option 1: Microsoft Ecosystem LMS

Best for rapid rollout in a business environment.

| Component | Technology |
|-----------|-----------|
| Content and records | SharePoint |
| User interface | Power Apps |
| Assignment, reminders, approvals | Power Automate |
| Reporting | Power BI |
| Live learning | Teams integration |
| Resources, certificates | SharePoint libraries |

### Option 2: Custom Web LMS

Best for a true platform product.

| Component | Technology |
|-----------|-----------|
| Frontend | Next.js |
| Database | PostgreSQL |
| Auth | Role-based authentication |
| Content playback | SCORM player integration |
| File storage | Cloud storage for resources and certificates |
| Reporting | Dashboard layer |
| External systems | API integration layer |

---

## Formal Requirements Statement

> The LMS must provide course management and content delivery capabilities for videos, PDFs, links, and SCORM content; role-based user and access management; assessment and certification functionality; reporting and analytics for learner activity and compliance; integration capabilities with enterprise systems and collaboration tools; and content authoring or content-authoring integrations to support ongoing learning development and maintenance.

## Functional Module Summary

1. Course Management & Content Delivery
2. User & Role Management
3. Learning Paths & Enrolment
4. Assessment & Certification
5. Reporting & Analytics
6. Integration Hub
7. Content Authoring
8. Administration & Governance

## Instructions

When helping with LMS design or implementation:

1. **Identify the module** — determine which of the 8 modules the user's question falls under
2. **Reference the entity model** — use the core entity groups to guide data model design
3. **Follow the MVP/Phase 2 split** — recommend MVP features first, Phase 2 as follow-up
4. **Choose the right architecture** — Microsoft ecosystem for enterprise rapid rollout, custom web for platform products
5. **Apply role-based access** — always design with the 6 primary roles in mind
6. **Include governance** — content lifecycle, versioning, audit logs, and compliance controls
7. **Plan integrations early** — REST API, webhooks, SSO, and HRIS sync should be in the architecture from day one even if Phase 2
