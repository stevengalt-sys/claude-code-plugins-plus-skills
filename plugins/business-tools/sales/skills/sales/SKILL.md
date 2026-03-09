---
name: sales
description: |
  A comprehensive sales methodology skill for managing pipelines, qualifying leads,
  crafting proposals, handling objections, and closing deals. Trigger with phrases like
  "sales pipeline", "qualify this lead", "write a proposal", "handle objection",
  "close the deal", "MEDDIC qualification", "SPIN selling", "sales forecast",
  "cold outreach", "follow up sequence", or "competitive positioning".
version: 1.0.0
author: Steven Galt <stevengalt-sys@github.com>
license: MIT
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch
---

# Sales Methodology Skill

A structured sales toolkit combining proven frameworks (MEDDIC, SPIN, Challenger Sale) to help you manage your entire sales cycle — from prospecting through close.

## Capabilities

This skill assists with the following sales activities:

1. **Lead Qualification** — Score and qualify leads using MEDDIC or BANT
2. **Pipeline Management** — Track deals, stages, and forecast revenue
3. **Proposal Generation** — Craft compelling proposals and SOWs
4. **Objection Handling** — Respond to common objections with proven techniques
5. **Cold Outreach** — Write personalized cold emails and call scripts
6. **Competitive Positioning** — Build battle cards and differentiation talking points
7. **Follow-Up Sequences** — Design multi-touch follow-up cadences
8. **Deal Strategy** — Plan account strategies and stakeholder maps

---

## Framework 1: MEDDIC Qualification

Use this framework to rigorously qualify opportunities. Walk the user through each element:

| Element | Question to Ask |
|---------|----------------|
| **M**etrics | What quantifiable business outcomes does the prospect want? |
| **E**conomic Buyer | Who has the authority and budget to approve this deal? |
| **D**ecision Criteria | What criteria will they use to evaluate solutions? |
| **D**ecision Process | What are the steps and timeline to reach a decision? |
| **I**dentify Pain | What specific pain points drive the need for a solution? |
| **C**hampion | Who inside the account will advocate for your solution? |

**Output:** A MEDDIC scorecard rating each element 1-5, with an overall qualification score and recommended next steps.

---

## Framework 2: SPIN Selling

Guide discovery conversations using the SPIN framework:

### Situation Questions
Understand the prospect's current state:
- What tools/processes do you currently use for [area]?
- How is your team structured?
- What does your current workflow look like?

### Problem Questions
Uncover pain points:
- What challenges do you face with your current approach?
- Where do bottlenecks occur?
- What's the biggest frustration your team has?

### Implication Questions
Amplify the cost of inaction:
- What happens if this problem isn't solved in the next 6 months?
- How does this affect other parts of the business?
- What's the revenue impact of the current inefficiency?

### Need-Payoff Questions
Connect your solution to their needs:
- If you could solve [problem], what would that mean for your team?
- How would [outcome] impact your business goals?
- What would it be worth to eliminate [pain point]?

**Output:** A structured discovery notes document with key findings organized by SPIN category.

---

## Framework 3: Challenger Sale

Help the user teach, tailor, and take control:

### Teach
- Identify an insight the prospect hasn't considered
- Reframe their thinking about the problem
- Lead with a provocative point of view

### Tailor
- Map the message to the prospect's specific industry and role
- Customize the value proposition to their metrics
- Align with their strategic priorities

### Take Control
- Set clear next steps and timelines
- Address objections directly
- Guide the commercial conversation with confidence

---

## Pipeline Management

When asked to manage or review a pipeline, create or update a structured pipeline view:

```markdown
## Sales Pipeline — [Date]

### Stage 1: Prospecting
| Company | Contact | Value | Next Step | Last Touch |
|---------|---------|-------|-----------|------------|

### Stage 2: Discovery
| Company | Contact | Value | MEDDIC Score | Next Step |
|---------|---------|-------|-------------|-----------|

### Stage 3: Proposal
| Company | Contact | Value | Decision Date | Confidence |
|---------|---------|-------|--------------|------------|

### Stage 4: Negotiation
| Company | Contact | Value | Blocker | Close Date |
|---------|---------|-------|---------|------------|

### Stage 5: Closed Won / Lost
| Company | Value | Outcome | Reason | Date |
|---------|-------|---------|--------|------|
```

Provide a pipeline summary with total value by stage, weighted forecast, and velocity metrics.

---

## Proposal Generation

When asked to write a proposal, use this structure:

1. **Executive Summary** — 2-3 sentences on the problem and proposed solution
2. **Understanding of Needs** — Reflect back the prospect's stated challenges
3. **Proposed Solution** — Describe your approach and deliverables
4. **Implementation Timeline** — Phase-by-phase breakdown with milestones
5. **Investment** — Pricing with clear value justification
6. **Why Us** — 3-5 differentiators with proof points
7. **Next Steps** — Clear call to action with timeline

---

## Objection Handling

When the user encounters an objection, use the LAER framework:

- **L**isten — Acknowledge the concern without being defensive
- **A**cknowledge — Show empathy and validate their perspective
- **E**xplore — Ask clarifying questions to understand the root cause
- **R**espond — Address with evidence, case studies, or reframing

### Common Objections and Responses

| Objection | Response Strategy |
|-----------|------------------|
| "Too expensive" | Reframe around ROI and cost of inaction |
| "We're happy with current solution" | Share insight they haven't considered (Challenger) |
| "Need to think about it" | Identify the real concern; set a specific follow-up |
| "Not the right time" | Quantify the cost of delay |
| "Need to check with my team" | Offer to present to the team directly |
| "Competitor offers more features" | Shift focus to outcomes, not features |

---

## Cold Outreach Templates

When writing outreach, follow these principles:
- Lead with the prospect's problem, not your product
- Keep emails under 100 words
- Include one clear CTA
- Personalize the first line with research
- Use a conversational, not corporate, tone

### Email Sequence Structure
- **Email 1 (Day 0):** Problem-focused introduction
- **Email 2 (Day 3):** Share a relevant insight or case study
- **Email 3 (Day 7):** Social proof with specific results
- **Email 4 (Day 14):** Breakup email with low-friction CTA

---

## Instructions for Use

1. Ask the user what sales activity they need help with
2. Gather context: product/service, target market, deal size, and stage
3. Apply the most relevant framework
4. Produce structured, actionable output
5. Always recommend specific next steps with timelines
6. When in doubt, qualify first — use MEDDIC before strategy
