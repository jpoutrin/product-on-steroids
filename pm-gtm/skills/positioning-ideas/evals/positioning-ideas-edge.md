---
id: positioning-ideas-edge
skill: positioning-ideas
input:
  prompt: "We need positioning ideas for our new product."
  context: |
    Product: Draftly — an AI writing assistant for internal business documents
    (memos, reports, project updates).
    Core capability: generates first drafts from bullet points; supports a
    company's house style guide.
    Target audience: knowledge workers at Fortune 500 companies — unclear whether
    to focus on comms teams, ops managers, or all employees.
    Competitors: ChatGPT (broad, not enterprise-safe), Microsoft Copilot (bundled
    with M365, not standalone), Notion AI (doc-editing context only),
    Jasper (marketing copy focus).
    Differentiation: honestly unclear — house style support is a feature, not a
    clear frame; enterprise data security is table-stakes for the category.
    No current positioning.
expected:
  - "Context Summary explicitly surfaces the differentiation tension — no clear white space yet — rather than glossing over it"
  - "Output contains at least 5 positioning concepts despite the ambiguity"
  - "At least one concept proposes a specific audience reframe (e.g., comms teams vs. all-employee) as a way to manufacture differentiation"
  - "At least one concept flags that it depends on a strategic choice the team has not yet made (e.g., audience focus)"
  - "Trade-offs for each concept are honest about the undifferentiated baseline risk"
  - "Recommendation names a concept and explains what evidence would validate it, rather than claiming false certainty"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge scenario: product with no obvious differentiation and an unresolved audience
question. Guards against the skill papering over strategic ambiguity with confident-
sounding but hollow positioning concepts. The skill must surface the tension honestly,
generate ideas that help the team make the missing strategic choices, and flag
assumptions rather than hiding them in the recommendation.
