---
id: competitive-intel-watch-edge
skill: competitive-intel-watch
input:
  prompt: "Weekly competitive watch for Acme, Bolt, Cinder. Last check 2026-08-01, today 2026-08-08. Slow week — I don't think much happened."
  context: "Short window over a holiday week. Only Bolt shipped a minor changelog note; the others were quiet."
expected:
  - "Explicitly marks competitors with no material moves as 'No material moves' rather than omitting them or padding"
  - "Does not fabricate moves or inflate a minor changelog note into a High threat"
  - "Correctly rates the single minor move as Low or Noise with a one-line justification"
  - "Still produces a well-formed digest (header, moves table, watchlist state) even when the digest is nearly empty"
  - "Keeps the window scoped to the quiet week and carries the watchlist forward"
rubric:
  scoping_discipline: 0.35
  correctness: 0.30
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge: a quiet period. Guards against the failure mode of padding an empty digest
with manufactured or exaggerated moves, and confirms the skill can cleanly report
"nothing material" while still triaging the one minor signal correctly.
