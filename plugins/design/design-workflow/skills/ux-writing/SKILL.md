---
name: ux-writing
description: |
  Craft and review UX copy including microcopy, error messages, button labels, onboarding flows, and tooltips.
  Use when writing or reviewing interface text, improving copy clarity, or establishing voice and tone guidelines.
  Trigger phrases: "write UX copy", "review this microcopy", "improve error message", "write button label", "onboarding copy".
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0.0
author: Claude Code Plugin Hub <[email protected]>
---

# UX Writing

Write clear, concise, and helpful interface copy that guides users through tasks.

## Core Principles

1. **Clarity over cleverness** — Users scan, they don't read. Say exactly what you mean.
2. **Front-load the important word** — "Save changes" not "Changes will be saved"
3. **Use the user's language** — Match mental models, avoid jargon
4. **Be consistent** — Same action = same label everywhere
5. **Write for the worst moment** — Error states need the most care

## Copy Types

### Button Labels
- Use verbs: "Save", "Send", "Create", not "OK" or "Submit"
- Be specific: "Delete account" not just "Delete"
- Match the action to the outcome: "Publish post" not "Confirm"
- Primary action first, secondary action second

### Error Messages
Follow this pattern:
1. **What happened** — "Your password is too short"
2. **Why it happened** — "Passwords must be at least 8 characters"
3. **What to do** — "Add more characters and try again"

Avoid: "Error 403", "Invalid input", "Something went wrong"

### Empty States
- Explain what will appear here
- Tell users how to populate it
- Include a clear CTA
- Example: "No projects yet. Create your first project to get started." [Create project]

### Confirmation Dialogs
- Title: State the action — "Delete this file?"
- Body: State the consequence — "This will permanently remove the file and its contents."
- Primary button: Repeat the action verb — "Delete file"
- Secondary button: "Cancel" (not "No" or "Go back")

### Loading & Progress
- Tell users what's happening: "Uploading your photo..." not "Loading..."
- Set expectations: "This usually takes about 30 seconds"
- Celebrate completion: "Upload complete" with a clear next step

### Tooltips & Help Text
- Keep under 150 characters
- Explain why, not just what
- Use when the label alone isn't enough context

## Voice & Tone Guidelines

| Context | Tone | Example |
|---------|------|---------|
| Success | Confident, brief | "Changes saved" |
| Error | Helpful, calm | "We couldn't save your changes. Check your connection and try again." |
| Onboarding | Encouraging, clear | "You're all set. Here's how to get started." |
| Destructive action | Direct, serious | "This will permanently delete your account and all data." |
| Empty state | Friendly, guiding | "No results found. Try adjusting your filters." |

## Review Checklist

When reviewing existing copy:
- [ ] Is it scannable? (Under 30 words for body copy)
- [ ] Does it use active voice?
- [ ] Is the most important information first?
- [ ] Are labels consistent across the interface?
- [ ] Does it work for screen readers?
- [ ] Is it free of jargon and technical terms?
- [ ] Does it handle pluralization correctly?
- [ ] Is it localization-ready? (No concatenated strings, no embedded formatting)
