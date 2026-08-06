---
id: build-vs-buy-commodity-auth
skill: build-vs-buy
input:
  prompt: "Should we build our own authentication/SSO or buy a vendor like Auth0?"
  context: "B2B SaaS. Customers never mention login as a reason to buy. Rough build estimate 2 eng x 9 months. Auth0 quote ~€45k/yr license. Team is small; roadmap is full."
expected:
  - "Runs an explicit core-differentiation test and finds auth is commodity/context, not a differentiator"
  - "Compares TCO like-for-like over a stated horizon, and the Build side includes ongoing maintenance, not just build cost"
  - "Addresses time-to-value, lock-in/switching risk, and opportunity cost for each live option"
  - "Presents a weighted scorecard with criteria, weights summing to 1.0, 1-5 scores, and weighted totals"
  - "Recommends Buy with 2-3 reasons and explicit flip conditions"
rubric:
  correctness: 0.35
  completeness: 0.25
  assumptions_explicit: 0.20
  actionability: 0.20
weight: 1.0
---

Happy path: a textbook commodity capability with cost and vendor anchors. Guards
against skipping the core test, ignoring build's maintenance cost, and recommending
without a scorecard or flip conditions.
