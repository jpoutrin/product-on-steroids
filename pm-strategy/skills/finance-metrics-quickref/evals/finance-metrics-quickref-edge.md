---
id: finance-metrics-quickref-edge
skill: finance-metrics-quickref
input:
  prompt: "I'm reading our P&L and there's a line called EBITDA — what is it and how's it calculated?"
  context: "PM mid-document; wants just this term, not the whole glossary."
expected:
  - "Returns a single focused row/answer for EBITDA, not the full 12-term sheet"
  - "Keeps the same four-column shape: Term / Definition / Formula / Why a PM cares"
  - "Definition is plain-language and does not just restate the formula"
  - "Formula is correct (operating income + depreciation & amortization, or equivalent before interest & tax)"
  - "The 'Why a PM cares' ties EBITDA to a product/operating decision, not a generic statement"
rubric:
  correctness: 0.4
  scoping: 0.35
  actionability: 0.25
weight: 1.0
---

Edge: single-term lookup mid-document. Guards against dumping the entire sheet
when one term was asked, while still holding the four-column shape and a correct
EBITDA formula.
