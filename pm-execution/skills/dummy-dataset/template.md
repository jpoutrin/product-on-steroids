# Dummy Dataset: <Dataset Type>

## Dataset Specification <!--#dataset-specification-->
- **Domain:** <e.g., customer feedback, e-commerce transactions>
- **Row count:** <number of records>
- **Column definitions:**
  - `<field_name>`: <data type> — <generator or value range>
  - `<field_name>`: <data type> — <generator or value range>

## Realistic Patterns & Constraints <!--#realistic-patterns-constraints-->
- <Distribution or constraint 1 (e.g., rating skew 40% 5-star)>
- <Constraint 2 (e.g., category only with certain ratings)>
- <Constraint 3 (e.g., email domain mix)>

## Output Format: <Python | CSV | JSON | SQL> <!--#output-format-python-csv-json-sql-->

### Sample (first 5 rows) <!--#sample-first-5-rows-->
```
<formatted sample output, 5-10 rows>
```

### Full Dataset <!--#full-dataset-->
```
<complete output or file reference>
```

## Quick Start <!--#quick-start-->
- **Load into pandas:** `df = pd.read_csv("dataset.csv")`
- **Import to database:** `psql mydb < dataset.sql`
- **Use in tests:** `python generate_dataset.py`
