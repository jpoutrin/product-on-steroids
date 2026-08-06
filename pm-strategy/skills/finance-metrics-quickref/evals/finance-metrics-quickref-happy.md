---
id: finance-metrics-quickref-happy
skill: finance-metrics-quickref
input:
  prompt: "Give me a quick cheat-sheet of the core finance terms I keep hitting in our board deck."
  context: "B2B SaaS PM. Wants a scannable reference, not a deep dive."
expected:
  - "Returns a Markdown table with the four columns Term / Definition / Formula / Why a PM cares"
  - "Covers at least gross margin, net margin, COGS, EBITDA, cash flow, runway, ARR, MRR, CAC, LTV, contribution margin, working capital"
  - "Gross margin formula is (Revenue - COGS) / Revenue and margins are shown as a % of revenue"
  - "Each 'Why a PM cares' names a product or GTM lever, not a generic 'it is important'"
  - "ARR/MRR and CAC/LTV rows point to the deep SaaS skills rather than benchmarking here"
  - "No prose paragraphs between rows; fits roughly one screen"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: full reference request. Guards against prose-instead-of-table,
wrong/omitted formulas, vague "why", and against benchmarking that belongs in the
deep SaaS skills.
