---
id: build-vs-buy-core-differentiator-edge
skill: build-vs-buy
input:
  prompt: "There's an off-the-shelf recommendation engine we could license for €80k/yr and ship in a month. Should we buy it instead of building our own?"
  context: "We're a discovery-first shopping app. Our recommendation quality IS the product — it's the top reason users say they stay. Building in-house is ~€600k over 18 months."
expected:
  - "Runs the core-differentiation test and finds the recommendation engine IS the core differentiator"
  - "Uses the core-test verdict to override the fact that Buy is cheaper and faster to value"
  - "Still shows a like-for-like TCO and a weighted scorecard where strategic fit/control carries heavy weight"
  - "Recommends Build (or a build-around-a-bought-core hybrid) with reasons tied to differentiation and lock-in on a core capability"
  - "States flip conditions (e.g. if the vendor allows deep customization/data ownership and quality parity, Buy could win)"
rubric:
  correctness: 0.35
  completeness: 0.20
  assumptions_explicit: 0.20
  actionability: 0.25
weight: 1.0
---

Edge case: the cheaper, faster option (Buy) is the wrong call because the capability
is the core differentiator. Guards against a naive cost-only recommendation and tests
that the core-differentiation test can override raw TCO/time-to-value.
