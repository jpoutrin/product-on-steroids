---
id: competitor-analysis-happy
skill: competitor-analysis
input:
  prompt: "Prepare a competitive brief for our EU SMB e-signature tool against DocuSign, Adobe Acrobat Sign, and Yousign."
  context: "B2B SaaS, EU SMBs. Supplied: DocuSign entry €10/user/mo, Yousign €9/user/mo freemium, Adobe bundled with Acrobat. G2 review export attached."
expected:
  - "Scopes the market and tags each competitor leader / challenger / niche, separating direct from adjacent alternatives"
  - "Profiles each competitor with both 2-4 strengths and 2-4 weaknesses (no all-praise or all-criticism profile)"
  - "Uses the supplied pricing and cites the G2 export; marks unsourced reads as (inference)"
  - "Includes a comparison matrix contrasting the set across positioning, price, key strength, and key gap"
  - "Surfaces 3-5 specific differentiation opportunities drawn from the pattern of gaps, each tied to evidence"
  - "Ends with a positioning recommendation naming 1-3 differentiators and threats to monitor"
rubric:
  correctness: 0.35
  completeness: 0.25
  evidence_cited: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: named competitors and supplied pricing/review data enable full
profiles and a real matrix. Guards against all-praise profiles, uncited claims,
and generic "be better/cheaper" opportunities.
