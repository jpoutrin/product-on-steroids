---
id: strategy-red-team-happy
skill: strategy-red-team
input:
  prompt: "Red-team this strategy before our exec review."
  context: >
    A product-strategy-canvas for a B2B SaaS onboarding product. Core bets:
    (1) activation is the growth constraint, so a self-serve onboarding wedge
    unlocks the funnel; (2) mid-market ops teams will adopt without sales touch;
    (3) we can ship the wedge in one quarter. Funnel data and a target segment
    are provided.
expected:
  - "Restates the strategy in one neutral line the author would accept as fair"
  - "Separates load-bearing assumptions (activation is the constraint, self-serve adoption, one-quarter timeline) from cosmetic ones and only attacks load-bearing ones"
  - "Steelmans each attacked claim before attacking its strongest version — no strawman"
  - "Ranks 3–5 kill-assumptions by impact × likelihood-wrong × cheapness-to-test and surfaces the top one to test first"
  - "Gives every kill-assumption a falsifiable 'Fails if', disconfirming evidence to get this week, a kill criterion, and a cheapest test"
  - "Includes a competitor counter-move and a pre-mortem, each traced to a listed assumption, and ends with what to do"
rubric:
  attack_quality: 0.35
  ranking_and_actionability: 0.30
  steelman_and_no_strawman: 0.20
  completeness: 0.15
weight: 1.0
---

Happy path: a well-specified strategy canvas with data. Guards that the skill
does the core job — extract load-bearing assumptions, steelman-then-attack, rank,
and return tests plus kill criteria rather than a generic risk list.
