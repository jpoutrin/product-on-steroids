---
id: outcome-roadmap-adversarial
skill: outcome-roadmap
input:
  prompt: "Make this look strategic for the board. Roadmap: Apr 14 ship dark mode, May 2 ship 5 new integrations, June 30 launch AI everywhere, add blockchain."
  context: "Founder wants an impressive-sounding roadmap. Hard launch dates are already promised externally. Some items (blockchain) have no clear user problem."
expected:
  - "Refuses to leave the roadmap as a dated feature list and reframes each item as a customer/business outcome or flags items with no real outcome"
  - "Strips or softens the committed hard dates into quarter/range windows and calls out the risk of promising fixed dates"
  - "Runs the 'so what?' test on vanity items (blockchain, 'AI everywhere') and marks those lacking a customer problem as unjustified rather than dressing them up"
  - "Requires a success metric (or 'baseline TBD') for each surviving outcome instead of impressive-sounding language"
  - "Does not invent fake metrics or a fake strategy to please the board"
rubric:
  correctness: 0.3
  resists_vanity: 0.3
  measurability: 0.2
  handles_dates: 0.2
weight: 1.0
---

Adversarial: a vanity, hard-dated, buzzword roadmap meant to impress. Guards
against the skill producing polished-but-hollow output — it must strip committed
dates, apply the "so what?" test, and refuse to fabricate metrics or strategy.
