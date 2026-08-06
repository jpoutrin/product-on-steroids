---
id: sentiment-analysis-happy
skill: sentiment-analysis
input:
  prompt: "Analyze sentiment from these 50 app store reviews for our mobile fitness app and create a sentiment report."
  context: "The reviews span January–March 2025; mix of 1–5 star ratings; from iOS and Android; we're an early-stage health startup. I want to understand what's working and what's breaking trust."
expected:
  - "Overall sentiment score computed and clearly stated (positive, negative, neutral %, or -1 to +1 scale)."
  - "At least 5 distinct themes identified (e.g., UI clarity, workout effectiveness, social features, battery drain, onboarding)."
  - "Each theme includes ≥2 direct quotes from the feedback and frequency (# mentions or %)."
  - "Business impact stated for top themes (e.g., churn risk, feature opportunity, retention lever)."
  - "At least 3 prioritized, actionable recommendations tied to specific themes."
  - "No high-frequency issue (>5% of feedback) left unaddressed."
rubric:
  correctness: "Score correctly identifies sentiment polarity distribution and theme patterns from the feedback; themes map to customer needs, not analyst interpretation."
  completeness: "All 6 sections from template present; no major theme is missing; every top-frequency issue has a recommendation."
  actionability: "Recommendations are specific, tied to customer evidence (quotes + frequency), and ranked by effort or impact; a PM can act on them immediately."
weight: 1.0
---

This scenario guards against the skill overfitting to vocal outliers, skipping low-frequency themes, or failing to prioritize. A well-formed dataset with clear themes tests the skill's ability to synthesize large feedback at scale and surface actionable insights tied to business impact.
