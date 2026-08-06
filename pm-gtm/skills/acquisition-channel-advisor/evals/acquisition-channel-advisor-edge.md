---
id: acquisition-channel-advisor-edge
skill: acquisition-channel-advisor
input:
  prompt: "We run a B2C consumer fitness app (iOS/Android). We have $15,000/month to spend. The problem: every obvious paid channel is now saturated for fitness apps — Meta Ads CPIs have tripled in two years, Apple Search Ads is crowded, TikTok influencers convert poorly for us. Our organic content gets decent impressions but almost no downloads. We're in early-traction stage with 12,000 MAU but struggling to grow. ICP: women aged 25–40, urban, interested in strength training, likely already using one fitness app."
  context: "Paid channels have already been tried and are underperforming. Organic has some signal but weak conversion. Budget exists but prior spend was inefficient. ICP is crowded demographic in a mature category."
expected:
  - "The skill acknowledges channel saturation explicitly and does not blindly recommend Meta Ads or Apple Search Ads as top picks without noting the saturation context"
  - "The scorecard includes non-obvious channels for this scenario — e.g., influencer/micro-influencer partnerships, community-led (Reddit, niche Facebook groups), referral/viral loops, content SEO (YouTube), or offline/events"
  - "ICP Fit scores reflect the specific persona (women 25–40, strength training) — not generic fitness-app reasoning"
  - "The Test Protocol proposes a channel the team has NOT yet exhausted, with a test budget that is proportionate to the $15k/month constraint"
  - "The Next Review Trigger is data-driven (a specific milestone), not just a calendar date"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge-case scenario: a B2C consumer app where the most commonly recommended paid channels
are already saturated and underperforming. Guards against the skill defaulting to obvious
channel recommendations without accounting for saturation signals the user has provided.
Also tests that the scoring adapts to a crowded ICP (urban women into strength training)
and surfaces less-obvious channels (micro-influencers, community, referral loops, YouTube
SEO) that are underexplored for this product. The scenario has a real budget, so the skill
should not eliminate paid entirely — it must thoughtfully re-score saturated channels.
