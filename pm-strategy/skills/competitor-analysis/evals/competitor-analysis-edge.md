---
id: competitor-analysis-edge
skill: competitor-analysis
input:
  prompt: "Analyze competitors for our AI meeting-notes tool for solo consultants. The category is new and most rivals are early-stage with little public data."
  context: "Emerging space. Pricing pages exist but no analyst reports; several rivals are stealth or pre-launch. B2B, solo/micro consultants, global."
expected:
  - "Scopes the market and still assembles a direct competitive set, tagging maturity (leader/challenger/niche) despite thin data"
  - "Marks unsourced reads as (inference) and explicitly flags unknowns (e.g. pricing unknown) rather than inventing figures"
  - "Distinguishes early-stage direct rivals from adjacent/general-purpose alternatives"
  - "Still extracts 3-5 evidence-tied differentiation opportunities appropriate to a thin-data read"
  - "Positioning recommendation acknowledges uncertainty and names what to monitor as the space matures"
rubric:
  correctness: 0.30
  completeness: 0.20
  evidence_cited: 0.30
  actionability: 0.20
weight: 1.0
---

Edge case: sparse public data on an emerging category. Guards against fabricated
pricing/strengths and forces honest (inference)/unknown labeling while still
producing a usable wedge and watchlist.
