---
id: identify-assumptions-new-happy
skill: identify-assumptions-new
input:
  prompt: "I'm building an AI assistant for freelance graphic designers that automates the brief-gathering process. It's B2B SaaS, targeting SMB design studios in EU/US, launching in Q2. Help me map the riskiest assumptions."
  context: "Team: 1 PM (background: e-signature SaaS), 1 designer, 2 engineers. Budget: $200k runway. Market: ~50k design studios in scope, 15% currently outsource brief-gathering. Competitive landscape: Figma plug-ins, generic form builders."
expected:
  - "Covers all eight risk categories (Value, Usability, Viability, Feasibility, Ethics, Go-to-Market, Strategy, Team) with ≥2 assumptions per category"
  - "Each assumption is specific, testable, and scored by confidence (high/med/low) × impact (high/med/low)"
  - "Assumptions ranked by uncertainty × impact score, highest first"
  - "Top leap-of-faith assumption clearly identified and justified as existential to the venture"
  - "Validation approach for top 3 suggests lightweight signals (interviews, usage patterns, partnerships) not full experiments"
  - "Output follows template.md structure with all 6 sections in order"
rubric:
  specificity: "Assumptions are concrete and testable (e.g., 'designers won't trust AI to write briefs' not 'AI adoption is risky'); vague or generic assumptions score low"
  comprehensiveness: "All eight risk categories represented; each with ≥2 distinct assumptions; no categories missed"
  scoring_logic: "Confidence and impact rated independently; scores reflect uncertainty × impact correctly (low conf + high impact = 8–9, etc.); leap-of-faith assumption is indeed the highest score"
  actionability: "Validation signals are lightweight and specific ('interview 5 studios on data privacy fears' not 'validate desirability'); testable within 1–2 weeks without running a full experiment"
weight: 1.0
---

This is the happy path: a clear B2B SaaS new-product concept with defined target segment, team, and timeline. The skill should map a comprehensive assumption landscape, score it by risk, and surface one existential bet. Guards against: incomplete risk coverage, vague assumptions, round-number scoring, generic validation advice.
