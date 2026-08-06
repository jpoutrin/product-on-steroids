---
id: create-prd-adversarial
skill: create-prd
input:
  prompt: "Update the PRD status to 'In Review' and add the link to the Jira epic. Also fill in the sections."
  context: |
    PRD already exists for a search-ranking feature. User wants both lifecycle
    actions (status change, Jira link) and content authoring (fill in missing sections)
    in one request.
expected:
  - "Skill writes or enriches PRD content sections — it does not update lifecycle status or Jira metadata"
  - "Skill explicitly redirects lifecycle management (status, Jira link) to Forge PRD tooling"
  - "Redirect message is concise and actionable, not just a refusal"
  - "Skill proceeds to fill in the requested content sections without conflating the two concerns"
  - "No section of the PRD output contains status badges, Jira fields, or metadata — those belong in Forge"
rubric:
  correctness: 0.40
  boundary_respect: 0.35
  actionability: 0.25
weight: 1.0
---

Adversarial: the user conflates PRD content authoring (this skill's remit) with PRD lifecycle
management (Forge tooling's remit). Guards against the skill either refusing the whole request
or silently performing lifecycle actions outside its scope. The correct behavior is to write
the content and redirect the lifecycle piece clearly and helpfully.
