---
id: positioning-ideas-happy
skill: positioning-ideas
input:
  prompt: "Help us brainstorm positioning ideas for our product."
  context: |
    Product: Loomflow — a B2B SaaS async video tool for engineering teams.
    Core capability: teams record, annotate, and share short screen recordings
    linked directly to Jira tickets and GitHub PRs. Transcripts are
    auto-generated and searchable.
    Target audience: engineering managers and senior engineers at 50–500-person
    tech companies.
    Competitors: Loom (broad audience, consumer-friendly, not dev-workflow-integrated),
    Vidyard (sales-focused), Scribe (text/screenshot walkthroughs, not video),
    internal Slack clips (unstructured, unsearchable).
    No current positioning — team describes it as "Loom for developers."
    Constraint: avoid positioning against Loom by name (legal preference).
expected:
  - "Output contains at least 5 positioning concepts, each as a distinct section with a title"
  - "Every concept includes angle type, tagline sketch, rationale, and trade-offs"
  - "All five angle archetypes are represented: category creation, competitive repositioning, problem reframing, audience reframing, value reframing"
  - "No two concepts are minor variations of each other — each opens a different competitive frame"
  - "Context Summary accurately reflects Loomflow as dev-workflow-integrated async video, flags 'avoid naming Loom' constraint"
  - "Recommendation names a single concept with a one-paragraph rationale"
  - "No concept relies on generic uncopyable claims like 'best' or 'most user-friendly'"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy-path scenario: a real product with clear differentiation hooks (dev-workflow
integration, searchable transcripts, ticket linkage) in a crowded but
generalist-dominated category. Guards against the skill producing shallow or
overlapping concepts when the input is rich. The "avoid naming Loom" constraint
tests whether the skill applies strategic constraints across all concepts rather
than ignoring them.
