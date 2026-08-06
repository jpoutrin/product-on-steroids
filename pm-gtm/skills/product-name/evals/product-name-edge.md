---
id: product-name-edge
skill: product-name
input:
  prompt: "Help me name my new product. It's kind of like Slack but for a specific industry — think Slack meets X-industry-specific-thing. Target users are medium-sized companies. We want something catchy but also professional. Don't make it too weird or hard to spell. We're launching in Q2."
  context: "User provided minimal positioning detail; 'Slack but for X' is vague; tone guidance is conflicting ('catchy but professional'); no competitors named; geographic markets not specified; timeline provided but not relevant to naming."
expected:
  - "Skill probes for missing context (product value proposition, specific industry/segment, brand tone, concrete differentiation goals)"
  - "Despite incomplete input, skill still generates 8–12 reasonable candidates across naming styles"
  - "Rationale for each candidate includes assumptions made ('assuming enterprise-focused tone', 'assuming tech-forward industry')"
  - "Candidates span a range of styles, including some professional options and some modern/catchy options to address the tension"
  - "Recommendation section notes the ambiguity and suggests revisiting names once positioning clarifies"
  - "Scores are present but include caveats (e.g., 'memorability scored as 7 for finance-sector audience; may differ for other segments')"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge case: under-specified input with conflicting or vague requirements. Guards against skill accepting the request without probing, generating generic names without stated assumptions, or failing to hedge around incomplete context.
