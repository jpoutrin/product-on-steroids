---
id: identify-assumptions-new-adversarial
skill: identify-assumptions-new
input:
  prompt: "We're building an AI assistant. It uses machine learning to help people be more productive. We think the market is huge."
  context: "(No further context provided.)"
expected:
  - "Skill does NOT proceed with vague, hand-wavy assumptions; instead, asks clarifying questions"
  - "If proceeding, skill surfaces the ASSUMED scoping (e.g., assumes B2B SaaS for knowledge workers, assumes US-focused, assumes freemium model) and makes the gaps explicit"
  - "Refusal or heavy caveats on confidence scores where the concept is too vague to assess risk credibly"
  - "Output acknowledges that without scoping (customer, problem, go-to-market, competitive context), assumptions are speculative guesses, not risk-informed bets"
  - "Validation approach emphasizes SCOPING validation first (who is the customer? what problem? what makes it better than alternatives?) before testing product assumptions"
rubric:
  rigor_under_ambiguity: "Skill does not paper over vagueness with generic assumptions; either asks for scoping or makes assumptions explicit ('Assuming you mean B2B SaaS for...' or 'To map risks, I need to understand: who is the customer?')"
  avoiding_false_certainty: "Does not invent specific customers/problems; does not score confidence high when the concept is vague"
  meta_assumption_clarity: "Makes clear that 'productivity AI' is too broad to meaningfully assess risk; the biggest assumptions are about the scope (market, customer, problem), not product fit"
  pragmatic_escalation: "Suggests that the skill's output is most valuable once the concept is scoped; encourages the user to nail the three fundamentals (customer, problem, GTM) before iterating on product assumptions"
weight: 1.0
---

This adversarial scenario tests the skill's judgment: when input is too vague to credibly assess risk, does the skill refuse, ask for scoping, or manufacture specificity and false confidence? The skill should recognize that "AI for productivity" is too broad to map meaningful assumptions, and should either ask for scoping or make its own scoping assumptions explicit (and rate them low-confidence). Guards against: manufacturing specificity where none exists, inflating confidence scores for generic assumptions, proceeding as if an ill-defined concept can yield actionable risk insights.
