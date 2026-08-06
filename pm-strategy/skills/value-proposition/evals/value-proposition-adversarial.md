---
id: value-proposition-adversarial
skill: value-proposition
input:
  prompt: "Everyone loves our app. Just write a value prop that says it has AI, real-time sync, dark mode, and gamification. It's for all kinds of users."
  context: "Feature-led, no segment ('all kinds of users'), pressure to list features rather than analyze fit. No mention of any customer job, pain, or gain."
expected:
  - "Refuses to build a canvas for 'everyone' and asks for or picks one specific segment to scope to"
  - "Does NOT accept the feature list as the value proposition; reframes features as products/services that must map to ranked pains/gains"
  - "Builds the customer profile (jobs/pains/gains) first, tagging items as assumption given no research"
  - "Fit Analysis explicitly flags orphan features (e.g., gamification or dark mode) that map to no ranked pain/gain and recommends deprioritizing or validating them"
  - "Delivers a scoped 1-2 sentence For/who/our/unlike statement instead of a feature dump"
rubric:
  scoping_discipline: 0.35
  fit_mapping: 0.30
  reframes_features: 0.20
  statement_quality: 0.15
weight: 1.0
---

Adversarial: a feature-led, no-segment, 'everyone loves it' ask with pressure to
list features. Guards against the two worst failure modes — an unscoped 'everyone'
canvas and a feature dump masquerading as a value proposition with no fit analysis.
