---
id: user-stories-edge
skill: user-stories
input:
  prompt: "Create user stories for a notification preferences feature in our SaaS app."
  context: "Product: TeamSync (B2B project-management SaaS). No design files available yet. Multiple user roles exist but none are specified by the requester."
expected:
  - "Skill asks for or infers distinct user personas before writing stories (e.g., Admin, Team Member, Guest)"
  - "Each story uses 'As a [specific persona], I want [action], so that [outcome]' — no generic 'user' persona"
  - "Design field is present on every story and set to 'N/A' since no link was provided"
  - "Stories cover at least two distinct personas (e.g., Admin managing org-level settings, Team Member managing personal preferences)"
  - "Every acceptance criterion is testable without reference to undisclosed design files"
rubric:
  correctness: 0.35
  completeness: 0.25
  persona_specificity: 0.25
  actionability: 0.15
weight: 1.0
---

Edge-case scenario: no design link and no explicit user roles. Guards against the skill writing stories with a generic "user" persona, omitting the Design field entirely, or producing acceptance criteria that reference unavailable assets. Also checks that the skill handles the multi-role case by decomposing stories per role rather than writing one monolithic story.
