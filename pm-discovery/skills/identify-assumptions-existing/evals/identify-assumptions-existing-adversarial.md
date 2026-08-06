---
id: identify-assumptions-existing-adversarial
skill: identify-assumptions-existing
input:
  prompt: >
    We want to launch an AI copilot that helps our users write better emails.
    It will use LLMs to suggest subject lines, auto-complete paragraphs,
    and detect tone issues. Our product is an email client for teams.
    What assumptions should we validate?
  context: >
    Product: B2B email client, 5 years old, 50k users. Revenue: $2M ARR.
    Market: crowded (Superhuman, Gmail). Competition: intense.
    Technical: no LLM experience in-house, no ML infrastructure.
    Business: pressure to ship an AI feature "ASAP" (investor/board request).
expected:
  - "Skill identifies this as a major feature request that risks product direction and asks scope/resource questions before surfacing assumptions."
  - "Skill flags existential/strategic risks: technical debt, market positioning, user retention (disrupting existing workflow), technical learning curve, cost structure (LLM inference costs)."
  - "Desirability assumptions go beyond 'users like AI' to specifics: do users trust AI-generated suggestions? Will it reduce email quality? Tone detection accuracy."
  - "Viability assumptions cover LLM cost structure (revenue vs. inference cost burn), GTM differentiation, and brand risk (bad suggestions = reputational damage)."
  - "Feasibility assumptions cover LLM model selection, privacy/security (emails to third-party API), infrastructure, and integration into existing client."
  - "Skill does NOT assume this is low-risk or easy. Risk ranking puts top-uncertainty items (user trust, inference cost, model hallucination) at the top."
  - "Summary is candid: surfaces the magnitude of assumptions and suggests a phased approach (small user cohort, cost modeling, private on-device model exploration)."
rubric:
  accuracy: "Assumptions are grounded in reality, not hype. Acknowledges LLM-specific risks (hallucination, latency, cost, privacy) that generic feature analysis would miss. Flags strategic risks (market positioning, product direction)."
  completeness: "All three categories covered, with honest acknowledgment of HIGH uncertainty across all. Top 5 risks clearly named and ranked. Summary includes go/no-go guidance (e.g., 'Do NOT ship without validating cost structure and model accuracy on production data')."
  actionability: "Tests are LLM-specific and phased: prototype with off-the-shelf models, run accuracy tests on 1k production emails, cost-model inference pricing, run willingness-to-pay survey. Mitigation: start with smaller user cohort, private on-device models if cost is an issue."
weight: 1.0
---

Adversarial scenario: overly ambitious feature request (LLM copilot) that could disrupt product direction
and strategy. Skill must challenge scope, surface existential risks (cost, brand, technical debt, market position),
and distinguish between feature risk and strategic risk. This guards against the skill treating every feature
as equivalent and prevents it from being bullied by "ship fast" pressure into assuming low risk.
