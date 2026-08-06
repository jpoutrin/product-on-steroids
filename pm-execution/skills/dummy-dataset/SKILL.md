---
name: dummy-dataset
description: >
  Generate realistic synthetic datasets for testing, prototyping, and demos without privacy
  concerns. Use when building mockups, testing data pipelines, populating demo environments,
  or creating sample datasets for development and QA.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/dummy-dataset/template.md
---

# Generate Realistic Dummy Datasets

## Purpose
Generate synthetic, realistic test data that mimics real-world patterns without collecting
or using actual user data — eliminating privacy concerns while maintaining data quality
for prototyping, testing, and demos. The output is immediately usable: executable Python
scripts, CSV files, JSON data, or SQL INSERT statements ready to populate test environments.

**When NOT to use:** analyzing or processing real user data (use `data-analytics`),
synthesizing user research (use discovery skills), or generating product copy/messaging
(use marketing skills). This skill exists to *replace* real data with safe synthetic
equivalents in lower environments, not to generate insights from actual behavior.

## Inputs
- **Required:** the dataset type or domain (customer feedback, transactions, user profiles,
  page views, etc.), the approximate volume (rows/records), and the output format preference
  (Python script, CSV, JSON, SQL).
- **Optional:** specific column names or fields needed; data constraints or business rules
  (e.g., "rating skewed 40% 5-star, 30% 4-star"); realistic value patterns ("email domains:
  gmail, yahoo, company.com"); sampling window (e.g., "dates in last 90 days").

## Output Contract
The deliverable is a **ready-to-use dataset** with the following sections (see `template.md`):

1. **Dataset Specification** — domain, row count, column definitions with data types and generators.
2. **Realistic Patterns** — value distributions, constraints, and business logic applied (e.g.,
   rating skew, category-rating dependencies).
3. **Output Format & Sample** — full generated data in the requested format (Python, CSV, JSON, SQL),
   with the first 5–10 rows shown inline.
4. **Quick Start** — how to load or execute the output immediately in common stacks (pandas,
   psql, Node, etc.).

**GOOD (excerpt):**
```
Dataset: Customer Feedback (100 rows)
Columns:
- feedback_id: auto-increment (U001–U100)
- customer_name: realistic first+last names (Faker)
- email: valid format, mixed domains (gmail, yahoo, company.com)
- rating: 1–5, skewed (40% 5-star, 30% 4-star, 20% 3-star, 10% 1–2)
- category: Bug, Feature Request, Complaint, Praise — constrained by rating
  (Bug only 1–3; Feature Request only 3–5)
- feedback_date: dates in last 90 days
- text: realistic feedback (template-based, e.g., "Great product, but..." for 4-star)

Constraints applied:
- Bug category has 60% chance of rating ≤ 3
- Feature Request never with rating 1–2
- Email domain distribution: 50% gmail, 25% yahoo, 25% company.com
```

**BAD (excerpt):**
> "Generate 100 customer records with names, emails, and feedback."
> — fails: no column spec, no pattern guidance, no output format specified, no sample rows shown.

## Process
1. **Clarify dataset domain** — understand the data type and use case (prototyping vs. load testing).
2. **Define columns** — names, data types, realistic generators (names, emails, timestamps, enums,
   numeric ranges).
3. **Apply patterns & constraints** — business logic (skewed distributions, dependencies between
   fields, value ranges).
4. **Choose output format** — Python script (for re-generation), CSV (for spreadsheets/imports),
   JSON (for APIs), or SQL (for databases).
5. **Generate sample** — produce first 5–10 rows inline so the user can validate structure.
6. **Provide full output** — complete dataset as a code block, file reference, or downloadable link.
7. **Add quick-start guide** — how to load/execute in their stack (pandas, psql, Node, etc.).
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The dataset **domain is clear** — the user knows what this data represents and why.
- [ ] **Column definitions are explicit** — each field has a name, type, and realistic generator
      described (e.g., "email: valid format, mixed domains").
- [ ] **Constraints and patterns are stated** — distributions, dependencies, business rules are
      named and justified (not random).
- [ ] **Output format is usable immediately** — Python code runs, CSV is well-formed, JSON is
      valid, SQL is executable.
- [ ] **A sample (5–10 rows) is shown inline** — the user can validate structure without executing.
- [ ] **Quick-start instructions are provided** — load into pandas, import to psql, etc.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `dummy-dataset-happy` (happy path) — standard e-commerce transactions with realistic constraints.
- `dummy-dataset-edge` (edge) — sparse/high-cardinality domain (e.g., rare events, wide date range)
  needing pragmatic sampling strategies.
- `dummy-dataset-adversarial` (adversarial) — vague ask ("generate customer data") that the skill
  must scope down, ask for missing constraints, and refuse to proceed without clarity.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `pre-mortem` — identifying risks in test data or demo environments before launch.
- `user-stories` — use dummy-dataset output to populate acceptance criteria examples.

### External Frameworks
- Faker (Python library) — standard for realistic synthetic data generation
  (https://faker.readthedocs.io/).
- Hypothesis (Python property-based testing) — strategies for synthetic data that satisfy
  constraints (https://hypothesis.readthedocs.io/).
