---
id: competitive-intel-watch-happy
skill: competitive-intel-watch
input:
  prompt: "Run our monthly competitive watch. Watchlist: Acme, Bolt, Cinder. Last check was 2026-07-01; today is 2026-08-01. Our product is a mid-market billing platform; Q3 renewals are our priority."
  context: "Sources to watch: product changelog, pricing page, hiring, funding/press, messaging. This is an established monthly watch."
expected:
  - "Reports only moves within the window since 2026-07-01, stated explicitly as since <date> to today"
  - "Presents moves in a table with competitor, signal type, what changed, a dated source, threat level, and a recommended response per row"
  - "Assigns a justified threat level (High/Medium/Low/Noise) to each material move rather than a bare label"
  - "Gives a concrete owner-ready recommended response for High/Medium moves, not 'keep an eye on it'"
  - "Carries the watchlist state forward so the next run can diff against it"
rubric:
  correctness: 0.30
  actionability: 0.30
  completeness: 0.25
  scoping_discipline: 0.15
weight: 1.0
---

Happy path: an established monthly watch over a known list. Guards that the digest
diffs against the last check, cites dated sources, triages threat, and produces
owner-ready responses tied to our stated priority (Q3 renewals).
