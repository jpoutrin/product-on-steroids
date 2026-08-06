---
id: sql-queries-edge
skill: sql-queries
input:
  prompt: "What's the funnel drop-off from signup to feature adoption?"
  context: |
    Database: BigQuery (user's first mention of database type)
    Partial schema provided:
    - tables.users (columns: id, signup_ts, tier)
    - tables.feature_interactions (columns: user_id, feature, timestamp)
    - No explicit statement about what "feature adoption" means or which feature_id to use
expected:
  - "Skill asks for clarification: which specific feature to measure and what 'adoption' means (first use vs. N uses)"
  - "Skill confirms the database is BigQuery and adjusts SQL syntax (TIMESTAMP types, date functions)"
  - "Skill asks for time window if not specified; assumes reasonable defaults (e.g., last 90 days)"
  - "Query handles potential NULL values gracefully (LEFT JOIN for non-adopters)"
  - "Plain-English explanation clarifies how adoption is defined in the query result"
rubric:
  correctness: 0.3
  completeness: 0.4
  actionability: 0.3
weight: 1.0
---

Incomplete schema and ambiguous business question. Skill must clarify before
generating. Guards against generating wrong queries due to unstated assumptions.
