---
id: sentiment-analysis-edge
skill: sentiment-analysis
input:
  prompt: "I have ~15 NPS comments from our SaaS product. Most are very short (1–3 sentences). A couple mention features in a language that's not English. Analyze sentiment and themes."
  context: "Small dataset; sparse signal; mixed quality. We ship monthly, so any signal is useful—but I need to know the confidence limits."
expected:
  - "Sentiment score is computed and confidence level is stated (e.g., 'limited dataset; interpret with caution')."
  - "Themes are identified despite small size; if only 2–3 themes emerge, skill acknowledges the sample is too small to generalize."
  - "Non-English feedback is either translated, excluded with explanation, or flagged as low-confidence."
  - "Skill does not over-interpret small sample; no theme is claimed to represent >X% if the data is sparse."
  - "Recommendations account for small sample size; quick wins are favored over large bets."
rubric:
  correctness: "Themes reflect the actual feedback without extrapolation; translated or unclear pieces are handled transparently."
  completeness: "All sections present; confidence limits and limitations are stated; no illusion of certainty from a small dataset."
  actionability: "Recommendations are feasible with a small signal; skill suggests validation (follow-up survey, user interviews) before large investment."
weight: 1.0
---

This scenario guards against the skill over-claiming confidence on thin data or failing to flag data-quality issues. Edge cases (small samples, mixed languages, vague feedback) are common in real practice; skill must acknowledge uncertainty and recommend follow-up.
