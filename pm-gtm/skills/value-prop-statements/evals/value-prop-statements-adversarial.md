---
id: value-prop-statements-adversarial
skill: value-prop-statements
input:
  prompt: "Just write me some value propositions for our product."
  context: "No product name. No core value. No segments named. No features. No alternatives. User is asking for a generic output with minimal direction."
expected:
  - "Does NOT return generic template-filling or placeholder text (e.g., 'We help <segment> <job> so they can <outcome>')."
  - "Asks explicitly for required inputs before proceeding: product name, core value/capability, target segments, and key features or proof points."
  - "Explains that value propositions are only useful when segment-specific and tied to concrete outcomes; generic language is not actionable."
  - "If it must proceed (e.g., user pushes back), it clarifies what assumptions it is making and flags them as unvalidated before writing any statements."
  - "Does NOT confuse value propositions with positioning or marketing campaign ideas; clarifies the scope if the user's intent is misaligned."
rubric:
  scoping_discipline: 0.40
  input_elicitation: 0.30
  clarity_of_limitation: 0.20
  no_placeholder_output: 0.10
weight: 1.0
---

Adversarial: vague, minimal-input ask with no direction. Guards against the most common failure
mode — returning generic, template-filled output that is not actionable. Ensures the skill
actively elicits required inputs and refuses to generate placeholder text.

