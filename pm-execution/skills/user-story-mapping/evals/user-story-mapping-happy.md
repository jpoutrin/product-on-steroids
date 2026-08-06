---
id: user-story-mapping-happy
skill: user-story-mapping
input:
  prompt: "Create a user story map for our e-commerce marketplace MVP."
  context: >
    Primary user: online buyer. The team has identified these epics: Account
    Registration, Product Search, Product Detail Page, Shopping Cart, Checkout
    (payment + address), Order Confirmation, Order Tracking, Returns & Refunds.
    We want to ship three releases: MVP (end-to-end purchase flow), v1 (discovery
    enhancements), v2 (post-purchase). No capacity constraints given.
expected:
  - "Backbone has 4-8 activities in journey order (e.g. Discover, Evaluate, Purchase, Track)"
  - "Each activity has at least one walking skeleton task forming a thin end-to-end flow"
  - "All input epics are decomposed and placed in exactly one release swim lane or deferred"
  - "Release 1 (MVP) supports a complete end-to-end purchase as a standalone experience"
  - "Each release swim lane has a meaningful scope statement, not just a phase number"
  - "Deferred stories are listed with a one-line rationale"
  - "Open questions are surfaced (e.g. payment provider, guest checkout decision)"
rubric:
  backbone_quality: 0.25
  walking_skeleton: 0.20
  release_slicing: 0.30
  completeness: 0.15
  open_questions: 0.10
weight: 1.0
---

Happy path: sufficient epics and a clear user journey provided. Guards against
flat list output (no backbone) and against Release 1 being a partial,
non-end-to-end experience. Also checks that deferred work is made explicit.
