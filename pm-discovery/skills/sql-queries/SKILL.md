---
name: sql-queries
description: >
  Generate read-only SQL queries for product analytics questions: funnel
  drop-off, retention, feature adoption, DAU/MAU. Use when drafting or
  reviewing queries, exploring database schema, translating business
  questions into SQL, or analyzing product metrics.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/sql-queries/template.md
---

# Generate SQL Queries for Product Analytics

## Purpose
Transform a PM's business question into a well-commented, read-only SQL query
that retrieves and analyzes product metrics (funnels, retention, adoption, DAU/MAU).
The query includes inline explanations of the logic, making it reviewable and
maintainable by both analysts and engineers. Produces a query the PM can
hand to the analytics team, run directly against the database (if permissioned),
or adapt to a BI tool.

**When NOT to use:** deep statistical modeling (use `cohort-analysis` for
retention interpretation or `ab-test-analysis` for experiment analysis);
writing or modifying data (this skill only produces read-only SELECT queries);
designing schema or performance tuning (those are engineering tasks, not PM
analytics). If you need to understand the *result* of a query you've already
run, use `cohort-analysis` instead.

## Inputs
- **Required:** the business question — e.g., "How many users drop off
  between signup and first feature use?" or "What's the DAU/MAU ratio by
  region?" If absent, ask for it.
- **Required:** database schema — tables, column names, data types, and key
  relationships. Accept it as a SQL DDL file, a diagram description, or
  `<table>(<col>, <col>, <col>)` shorthand. If the PM doesn't provide it,
  ask explicitly and refuse to generate a query without it (guessing schema
  produces wrong queries).
- **Optional:** SQL dialect (BigQuery, PostgreSQL, MySQL, Snowflake, SQL Server;
  default: PostgreSQL). Ask if unclear.
- **Optional:** data volume, time window, or performance constraints.

## Output Contract
The deliverable is a **commented SQL query** with an **explanation guide**, structured as:

1. **SQL Query** — a single SELECT statement (no INSERT/UPDATE/DELETE), with
   inline comments explaining the logic (table joins, filtering, aggregations,
   CTEs). 50–150 lines typical. The query must be runnable as-is.
2. **Plain-English Interpretation** — what each column in the result means and
   how to read it (1–2 paragraphs).
3. **Safety Notes** — reminder that the query is read-only; alert if it scans a
   large table without a WHERE clause or index hint.
4. **Test/Validation Suggestion** — how to spot-check the result (e.g., "compare
   row count against the events table," "check that earliest date is after
   2024-01-01").

See `template.md` for the fill-in structure.

**GOOD (excerpt):**
```sql
-- Funnel step: signup → first feature use within 7 days
SELECT
  u.user_id,
  u.created_at AS signup_date,
  DATEDIFF(DAY, u.created_at, f.event_timestamp) AS days_to_first_use
FROM users u
LEFT JOIN features f
  ON u.user_id = f.user_id
  AND f.feature_id = 'onboarding_tour'
  AND f.event_timestamp <= DATEADD(DAY, 7, u.created_at)
WHERE u.created_at >= '2024-06-01'
ORDER BY u.user_id;
```

**BAD (excerpt):**
```sql
SELECT * FROM users;
```
— fails because: no filtering or aggregation (too broad); doesn't answer the
funnel question; no comments; no safety guard against scanning millions of rows.

## Process
1. **Parse the business question** — extract the metric (funnel/retention/adoption),
   time window, and segment (e.g., by region, cohort, device).
2. **Validate schema** — ask for the schema if missing; confirm table and column
   names before writing the query.
3. **Draft the query** — use CTEs for readability; write comments for each logical
   block; avoid SELECT *, specify columns.
4. **Add safety annotations** — include WHERE filters; note if the query scans
   an unindexed column; flag if there's a potential cartesian product.
5. **Write the explanation** — plain-English summary of what the query returns,
   what each column means, and how to interpret the result.
6. **Suggest a test** — describe how to validate the query (compare counts,
   check date ranges, spot-check a known user).
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The query is **read-only** (SELECT only; no INSERT/UPDATE/DELETE/DROP).
- [ ] The query includes **inline comments** explaining joins, filters, and aggregations.
- [ ] Column names are **explicit** (no SELECT *).
- [ ] The query includes a **WHERE clause** with a date or segment filter to limit
  the result set (or a safety note if the full table scan is intentional).
- [ ] Table and column names **match the provided schema** (no guesses).
- [ ] The **plain-English explanation** defines what each output column means.
- [ ] A **test suggestion** is provided to validate the result.
- [ ] If the output is written to a file, it follows `template.md` — all sections
  present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `sql-queries-happy` — standard funnel query with clear schema (Postgres/BigQuery).
- `sql-queries-edge` — sparse schema with ambiguous column names or missing relationships.
- `sql-queries-adversarial` — vague business question or unsafe request (e.g., "get all data")
  that the skill must clarify or refuse.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `cohort-analysis` — after running this query, use it to interpret retention/churn
  trends in the result.
- `ab-test-analysis` — for A/B test result interpretation (complementary to query
  generation).

### External Frameworks
- Amplitude, Mixpanel, or other product analytics tool docs — for metric definitions
  (funnel, retention, feature adoption).
- Mode SQL Tutorial (https://mode.com/sql-tutorial/) — neutral SQL reference for
  multi-dialect patterns and best practices.
