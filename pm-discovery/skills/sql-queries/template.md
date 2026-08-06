# SQL Query: <Business Question / Metric Name>

## SQL Query

```sql
-- <One-line summary of what this query answers>
-- Tables: <comma-separated>
-- Key filters: <WHERE clause summary>

<query here with inline comments explaining each logical block>
```

## Plain-English Interpretation

<Describe what the query returns and what each column means. 1–2 paragraphs.
Example:
"This query returns one row per user who signed up in the selected period. 
The 'signup_date' is the user's account creation time; 'days_to_first_use' is 
the number of days between signup and the user's first interaction with 
the feature, or NULL if they never used it. To find the funnel conversion rate, 
count rows where days_to_first_use IS NOT NULL and divide by the total row count.">

## Safety Notes

- **Read-only:** This query contains only SELECT; it does not modify the database.
- **Data volume:** <Note any large table scans, missing WHERE filters, or performance considerations.>
- **Schema assumptions:** <List any assumptions (e.g., "assumes created_at is indexed").>

## Test / Validation Suggestion

<Describe a quick sanity check. Example:
"Compare the total user count in the result against users created in the date range 
from the users table directly. If the query is working, the counts should match. 
Also spot-check 2–3 users: manually verify that their first feature use date is 
within 7 days of signup.">
