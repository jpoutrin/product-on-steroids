---
id: voice-of-customer-miner-edge
skill: voice-of-customer-miner
input:
  prompt: "Mine the voice of the customer from these 60 reviews of our new calendar integration feature."
  context: "30 reviews praise the calendar sync as seamless and time-saving. 30 reviews call the same sync broken, laggy, and unusable. The split is roughly 50/50 positive vs negative on the identical feature."
expected:
  - "Tags the calendar-sync theme as Mixed sentiment — does NOT report it as Positive or Negative"
  - "Surfaces the contradiction explicitly: states that the corpus is split ~50/50 positive/negative on the same feature"
  - "Includes verbatim quotes from BOTH sides of the split to illustrate the contradiction"
  - "Does NOT average away the contradiction into a neutral summary or a net sentiment score"
  - "Hypothesizes at least one possible cause for the split (e.g., platform difference, account type, data volume) in Notable Gaps or JTBD Signals"
  - "Recommended Actions acknowledge the need to investigate the root cause of the divergence before shipping a fix"
rubric:
  correctness: 0.40
  verbatim_fidelity: 0.25
  contradiction_handling: 0.25
  actionability: 0.10
weight: 1.0
---

Edge case: perfectly contradictory signals on the same feature. The most common
failure mode here is averaging the contradiction into a "Mixed but mostly fine"
summary that erases actionable information. This card guards against sentiment
averaging and forces the skill to surface the split faithfully.
