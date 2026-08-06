---
id: value-prop-statements-happy
skill: value-prop-statements
input:
  prompt: "Create value proposition statements for our design SaaS platform (Canva-like) targeting three audience segments: social media marketers, small business owners, and content creators."
  context: "Core value: create professional-quality designs without design expertise or expensive software. Key features: drag-and-drop editor, 10k+ pre-designed templates, pre-sized for social platforms, built-in brand kit. Alternative: Photoshop or hiring a designer. Time savings: 80% reduction in design time per asset."
expected:
  - "Produces exactly 3 value propositions, one per segment, each named and distinct"
  - "Each statement embeds the feature-benefit-outcome-differentiation chain; none is generic positioning-only"
  - "Each segment's value prop is tailored to that segment's job and pain point (e.g., marketers care about speed + brand consistency, small business owners care about professionalism without expertise, creators care about volume at scale)"
  - "Statements include concrete proof points or metrics (e.g., '80% faster', 'no design expertise needed', 'create in minutes instead of hours')"
  - "Alternatives and key limitations are named for each segment (Photoshop requires expertise, hiring designers is expensive, manual tools are slow)"
  - "Tone is benefit-focused and action-ready; statements could be used directly in marketing or sales decks"
rubric:
  segment_tailoring: 0.35
  feature_benefit_chain: 0.30
  proof_points: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: all required inputs provided (segments, core value, features, alternatives, metrics).
Guards against generic positioning-only language and ensures value props are segment-specific,
measurable, and ready for GTM execution (sales pitch or marketing copy).

