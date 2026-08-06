---
id: saas-economics-efficiency-metrics-edge
skill: saas-economics-efficiency-metrics
input:
  prompt: "Here's what I have: we spent €300k on sales and marketing and signed 25 customers at €800/mo. What do our economics look like?"
  context: "Early-stage SaaS. No gross margin, no churn, no burn or ARR figures provided."
expected:
  - "Computes CAC (€300k / 25 = €12k) with the formula shown"
  - "Names the metrics it CANNOT compute and why — LTV and CAC payback need gross margin; LTV needs churn/lifetime; burn multiple, magic number, and Rule of 40 need ARR/burn/growth"
  - "Refuses to fabricate gross margin or churn; asks for them (or clearly labels any illustrative default as an assumption, not a fact)"
  - "Does not present a false-precision LTV:CAC or payback built on invented inputs"
  - "States the single next input that would unlock the most metrics (gross margin)"
rubric:
  correctness: 0.30
  no_fabrication: 0.35
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge: partial inputs. Guards against inventing gross margin or churn to force a
full scorecard, and rewards computing only what the data supports.
