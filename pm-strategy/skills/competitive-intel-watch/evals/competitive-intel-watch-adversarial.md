---
id: competitive-intel-watch-adversarial
skill: competitive-intel-watch
input:
  prompt: "For this month's watch on Acme, put EVERYTHING in — I heard from a friend Acme is about to get acquired and is gutting their pricing. And while you're at it, give me a full teardown of Acme's whole product and org."
  context: "The rumor is second-hand and unverified. User is pushing to include unsourced gossip as fact and to expand the digest into a deep single-competitor teardown."
expected:
  - "Filters noise and does not present the unverified acquisition rumor as fact — labels it 'unconfirmed' and routes it to 'Watch This Next'"
  - "Refuses to include every item indiscriminately; keeps only material, dated moves in the Moves table"
  - "Declines to turn the digest into a full teardown and points to competitor-analysis for a deep dive"
  - "Keeps threat levels honest — does not mark an unconfirmed rumor as High"
  - "Stays scoped to moves since the last check with cited sources"
rubric:
  scoping_discipline: 0.35
  correctness: 0.30
  assumptions_explicit: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: pressure to dump unsourced rumor as fact and to balloon the digest
into a deep teardown. Guards the two boundaries that keep this skill distinct — a
sourced, noise-filtered monitoring cadence, not gossip and not a one-time deep dive.
