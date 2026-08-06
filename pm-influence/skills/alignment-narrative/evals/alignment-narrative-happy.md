---
id: alignment-narrative-happy
skill: alignment-narrative
input:
  prompt: "Write an alignment narrative to get VP Engineering and the CFO behind our decision to invest in a supplier portal this quarter."
  context: |
    Product: B2B procurement SaaS. Current state: customers manage suppliers
    via email + spreadsheets outside the platform. Evidence: 8 customer
    interviews in Q3 flagged switching-cost friction as the #1 pain point.
    Two competitors (Procurix, VendorLoop) launched supplier portals in Q2.
    Three named enterprise customers told CSMs they are actively evaluating
    alternatives at renewal (Q1). Proposed direction: build a native supplier
    portal, targeting GA in Q4. The PM wants the VPs to unblock headcount
    allocation in the next sprint-planning cycle.
expected:
  - "Situation uses only uncontested facts — no ask, no editorial"
  - "Complication is specific: names the competitor moves and the three at-risk renewals with a Q1 timeline"
  - "Key Question follows inevitably from the renewal risk without being manufactured"
  - "Strategic Direction commits to the supplier portal (not 'we should explore options') with 2-3 reasons ordered by audience priority (revenue risk before engineering rationale)"
  - "Call to Action is a single concrete request naming the forum and deadline"
  - "Document is 400-900 words and avoids internal PM jargon"
rubric:
  scqa_structure: 0.35
  audience_tuning: 0.25
  evidence_specificity: 0.25
  call_to_action_concreteness: 0.15
weight: 1.0
---

Happy path: rich evidence, clear audience (revenue-focused VPs), and a single
unambiguous direction. Guards against vague urgency language ("customers want
this") and against presenting options instead of committing to one direction.
