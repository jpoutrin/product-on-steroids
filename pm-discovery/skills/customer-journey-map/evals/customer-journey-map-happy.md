---
id: customer-journey-map-happy
skill: customer-journey-map
scenario: >
  Well-scoped B2C SaaS product with a clear persona and partial research.
  The user provides a persona, a product URL, and three interview excerpts
  showing onboarding friction and positive Aha Moment signals.
input:
  prompt: >
    Map the customer journey for Focusly, a B2C habit-tracking app. Persona:
    freelance knowledge workers, 25–40, who struggle to maintain consistent
    daily routines. JTBD: build and track sustainable work habits without
    feeling overwhelmed by complex productivity systems. Stages: Awareness
    through Retention. We have 3 interview excerpts attached — please use them.
  context: >
    Interview excerpt 1: "I found Focusly through a Twitter thread about
    simple habit stacks. Signed up immediately, but the onboarding had so many
    options I didn't know where to start." Interview excerpt 2: "The moment I
    completed my first 7-day streak and saw the streak animation — that was when
    I got it. That felt good." Interview excerpt 3: "I cancelled after 3 months.
    The app kept nagging me with notifications even after I turned them off in
    settings. That was the deal-breaker."
expected:
  - All six stages (Awareness through Retention) are present in the journey table with all six columns populated per row.
  - The Aha Moment explicitly references the 7-day streak animation, grounded in interview evidence.
  - The notification bug is called out as a top Churn Trigger with [evidence] label.
  - Onboarding complexity is identified as a pain point linked to a concrete improvement opportunity.
  - Pain points and opportunities are labeled [evidence] or [inference] correctly.
  - Prioritized Improvements are ranked by impact × effort with quick-win vs. strategic labels.
rubric:
  accuracy: Evidence from the three interviews is correctly attributed and not contradicted by the map.
  completeness: All required output sections are present (Persona & Scope, Journey Stage Table, Critical Moments, Prioritized Improvements).
  actionability: At least two improvements are specific enough to write a ticket from (touchpoint + mechanism named).
weight: 1.0
---

Guards the baseline happy-path output: a research-informed CJM for a B2C SaaS
product where interview evidence is available. Verifies that the skill correctly
synthesizes qualitative data into the stage table, properly calls out the Aha
Moment and Churn Triggers, and produces actionable, ranked improvements.
The notification churn signal is a deliberate edge within the happy path —
it should be flagged as [evidence], not buried or generalized.
