---
id: swot-analysis-happy
skill: swot-analysis
input:
  prompt: "Do a SWOT for our B2B expense-management SaaS, relative to Ramp and Brex, to decide whether to double down on SMBs or move upmarket."
  context: "Data available: 82% onboarding completion vs ~55% industry; net revenue retention 96%; team of 40; no enterprise SSO yet; EU e-invoicing mandate lands 2026; incumbents focus on US mid-market."
expected:
  - "Frames the assessment up front: subject, reference point (Ramp/Brex), and the SMB-vs-upmarket decision"
  - "Populates all four quadrants with 4–7 evidenced items each, citing the provided data (e.g. onboarding %, NRR, missing SSO, EU mandate)"
  - "Keeps internal/external discipline: onboarding/NRR/SSO as Strengths/Weaknesses, EU mandate and incumbent focus as Opportunities/Threats"
  - "Produces a TOWS synthesis with SO/ST/WO/WT pairs, each naming the two items it connects"
  - "Delivers 3–5 prioritized moves tagged Build/Defend/Pivot/Exit with owner and metric, each traceable to a TOWS pair"
rubric:
  correctness: 0.30
  tows_synthesis: 0.30
  evidence_and_discipline: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a well-framed, data-rich B2B SWOT. Guards against the skill stopping
at four bland lists instead of cross-referencing them into owned, prioritized moves.
