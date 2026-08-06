---
id: gtm-motions-adversarial
skill: gtm-motions
input:
  prompt: "Help us design GTM motions. We're a new B2B enterprise software company with a product that requires deep customization and long implementation. We want to grow fast but don't have a sales team yet."
  context: "Minimal specifics: no ACV stated, no sales cycle stated, no market size, no team composition or size. Conflicting signals: enterprise positioning (long cycle, customization) + no sales team + expectation of fast growth."
expected:
  - "Skill asks clarifying questions or makes reasonable assumptions explicit about ACV, sales cycle, team, and market"
  - "Identifies the conflict (enterprise positioning without sales team) and offers realistic paths (hire sales team, reposition to lower-ACV, or hybrid)"
  - "Does NOT recommend all 7 motions equally or ignore the enterprise/no-sales-team tension"
  - "Motions recommended reflect the reality: e.g., ABM/Outbound NOT viable without sales team; PLG NOT viable for highly customized product; Inbound + Partners as interim"
  - "Playbook is specific about the constraint (e.g., 'hire first sales engineer by week 1 of 90-day sprint') rather than glossing over it"
  - "Assumptions list flags the core tension (e.g., 'enterprise ACV + no sales team = immediate hiring required or reposition product')"
rubric:
  correctness: 0.3
  completeness: 0.2
  conflict_resolution: 0.3
  assumption_clarity: 0.2
weight: 1.0
---

Adversarial: vague input with conflicting constraints (enterprise positioning + no sales capacity + fast growth demand). Guards against rubber-stamping generic recommendations and ensures the skill can navigate ambiguity, ask for clarification, and surface misalignment between product/market/team realities.

