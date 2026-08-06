---
id: analyze-feature-requests-happy
skill: analyze-feature-requests
input:
  prompt: "We've collected 28 feature requests from support, sales, and community. Please analyze and prioritize them."
  context: "Product: a project management SaaS for remote teams. Current strategy: improve collaboration and reduce context-switching. Requests span Q3 & Q4 2025. Customers: SMBs (5–50 people) and a few mid-market accounts. Resource constraint: 1 senior + 2 junior engineers for 12 weeks."
expected:
  - "Clusters the 28 requests into 4–6 coherent themes (e.g., Real-Time Collaboration, Mobile, Integrations, Reporting)"
  - "Scores each theme on Impact, Effort, Risk, and Strategic Alignment using a consistent 1–5 scale"
  - "Identifies the top 3–5 priorities ranked by Opportunity Score or a clear trade-off logic"
  - "Articulates the rationale for each priority (e.g., 'High impact on SMBs, low effort, aligns with collaboration goal')"
  - "Acknowledges at least one deferred or low-scoring request and explains why (e.g., high effort, out of scope)"
  - "Output follows the template structure: Summary, Thematic Clusters, Opportunity Scoring, Top Priorities, Declining & Deferred"
rubric:
  clustering: 0.25
  scoring_clarity: 0.25
  prioritization_logic: 0.30
  actionability: 0.20
weight: 1.0
---

Happy path: structured dataset, clear product context, reasonable scope. Guards against superficial triage and for deliberate clustering and scoring logic.
