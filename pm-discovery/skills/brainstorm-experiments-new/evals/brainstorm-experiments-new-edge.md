---
id: brainstorm-experiments-new-edge
skill: brainstorm-experiments-new
input:
  prompt: "We're thinking about a platform for freelance marketers. But we're not sure if they need project management, portfolio tools, or client matching. What experiments should we run?"
  context: "Founder has done 5 customer interviews, but each freelancer described a different pain point. Team is bootstrapped and can't spend more than 1 week validating."
expected:
  - "Skill acknowledges ambiguity and clarifies which customer segment + problem hypothesis to anchor first"
  - "Experiments test which problem (project mgmt vs. portfolio vs. matching) is most urgent/valuable"
  - "Portfolio includes 2–3 experiments that can run in parallel within a 1-week constraint"
  - "At least one experiment quickly validates which problem tier ranks highest (e.g., email survey or concierge call)"
  - "Clear go/no-go threshold: if most experiments show low engagement, recommend narrowing or pivoting"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

This edge case tests the skill's ability to handle an ambiguous product scope with competing hypotheses.
Rather than proposing experiments for all three problems, the skill should help clarify which assumption to test first,
and propose lean experiments that fit a tight 1-week window. Guards against paralysis or overly broad portfolios.
