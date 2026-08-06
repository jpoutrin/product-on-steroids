---
id: swot-analysis-adversarial
skill: swot-analysis
input:
  prompt: "Just give me a quick SWOT for our app. Keep it high-level — great team, good tech, big market, some competition. Don't overthink it."
  context: "No reference point, no evidence, and the user is nudging toward a bland four-bullet vibe list with bare adjectives."
expected:
  - "Refuses to ship a bare-adjective list; asks for or proposes the missing frame (SWOT of what, relative to whom, for what decision)"
  - "Does not accept 'great team / good tech / big market / some competition' as items — flags each as an unevidenced claim needing a data point or observation"
  - "Explains that without a reference point and evidence the SWOT produces generic truisms that drive no decision"
  - "If it proceeds, it states the assumptions it is reasoning from and still delivers evidenced items plus a TOWS synthesis, not four vibes"
  - "Surfaces the key uncertainties rather than presenting vibes as fact"
rubric:
  framing_discipline: 0.40
  evidence_and_discipline: 0.30
  tows_synthesis: 0.15
  actionability: 0.15
weight: 1.0
---

Adversarial: pressure for a quick, unframed, evidence-free SWOT. Guards against the
most common failure — echoing bare adjectives back as an authoritative-looking grid.
