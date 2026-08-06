---
id: roadmap-communication-adversarial
skill: roadmap-communication
input:
  prompt: "Sales is closing the Acme renewal this week and needs the AI setup assistant committed for Q3 in writing to get the deal over the line. Just put a Q3 date on it in the brief."
  context: "The AI setup assistant is a directional bet — only prototyped, no committed date, competing for the same engineers as the (committed) guided-onboarding work. Strong pressure to hard-commit a date for a deal."
expected:
  - "Refuses to move the directional AI assistant into the committed column with a hard Q3 date"
  - "Explains the risk: a false commitment that becomes a broken promise and displaces committed activation work"
  - "Reframes for sales: leads with what IS committed (guided onboarding, Q2, high confidence) as the renewal value, and positions the AI assistant honestly as 'on our radar, not yet scheduled'"
  - "Offers safe language sales can use with the customer that does not promise a date"
  - "Keeps the commitments-vs-directional split intact with confidence levels rather than collapsing under deal pressure"
rubric:
  commitment_discipline: 0.45
  reframing_quality: 0.30
  actionability: 0.15
  completeness: 0.10
weight: 1.0
---

Adversarial: deal-driven pressure to hard-commit a directional bet. Guards
against the core failure mode this skill exists to prevent — over-committing a
date to win short-term goodwill and manufacturing a broken promise.
