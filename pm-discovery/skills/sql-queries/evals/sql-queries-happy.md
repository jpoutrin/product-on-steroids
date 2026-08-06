---
id: sql-queries-happy
skill: sql-queries
input:
  prompt: "Generate a query to find the DAU/MAU ratio by region for Q3 2024."
  context: |
    Database: PostgreSQL
    Schema:
    - users (user_id, region, created_at)
    - events (event_id, user_id, event_date, event_type)
expected:
  - "Query is valid, runnable PostgreSQL with explicit column names and SELECT only"
  - "Query includes inline comments explaining the DAU/MAU calculation and date filtering"
  - "Query has WHERE clause filtering events to Q3 2024 and users by region"
  - "Plain-English explanation describes what DAU/MAU ratio means and how to interpret it"
  - "Includes a test suggestion (e.g., spot-check one region's row counts)"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Standard query generation with clear schema and straightforward metric.
Guards against incomplete queries, missing comments, or vague explanations.
