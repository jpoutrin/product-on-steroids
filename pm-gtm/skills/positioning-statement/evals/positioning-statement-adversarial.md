---
id: positioning-statement-adversarial
skill: positioning-statement
input:
  prompt: "Polish this positioning statement so it's ready to use."
  context: |
    Draft statement submitted by the user:
    "Nexus empowers modern revenue teams to leverage AI-powered synergies across
    the entire customer journey to unlock best-in-class outcomes and drive
    sustainable growth at scale."

    Product background (provided separately):
    Nexus is a B2B revenue intelligence tool that ingests CRM data and call
    recordings, then surfaces which deals are at risk of slipping based on
    engagement signals — targeted at RevOps managers at mid-market SaaS companies
    (100–1000 employees) that run Salesforce and Gong.
    The key differentiator is that Nexus auto-categorizes deal risk without manual
    CRM hygiene — competing products (Clari, People.ai) require reps to keep
    Salesforce fields clean for the model to work.
    The team wants the statement "polished" — but the draft is so vague it is
    functionally meaningless.
expected:
  - "Skill rewrites the statement from scratch rather than making cosmetic edits to the jargon-heavy draft"
  - "Rewritten statement names a specific target customer (RevOps manager or equivalent role) not 'revenue teams'"
  - "Rewritten statement declares a category (revenue intelligence, deal risk detection, or equivalent) — not 'AI-powered synergies'"
  - "Jargon terms 'empower', 'leverage', 'synergies', 'best-in-class', 'unlock', 'sustainable growth at scale' are absent from the final statement"
  - "Reason to believe is concrete: references the no-CRM-hygiene-required differentiator specifically"
  - "Rationale or a brief note explains why the original draft was insufficient and what made it non-distinctive"
  - "Three test questions cover distinct dimensions: comprehension, differentiation, purchase relevance"
rubric:
  correctness: 0.50
  completeness: 0.25
  actionability: 0.25
weight: 1.0
---

Adversarial case: the user submits a classic "corporate word salad" positioning
statement and asks only for polish. The skill must not rubber-stamp it. With
sufficient product context available (ICP, differentiator, named competitors),
a full rewrite is warranted and expected. The test guards against the failure
mode where the skill makes minor wording tweaks and returns a slightly less
jargony version of the same undifferentiated statement. The correctness weight
is elevated because the core task here is the diagnosis — recognizing the draft
is non-distinctive — before writing.
