---
id: discovery-process-adversarial
skill: discovery-process
scenario: >
  PM frames the request as "validate our idea" rather than discovery. The ask is
  structurally a solution-validation exercise disguised as a discovery plan. The
  skill must redirect toward genuine problem exploration rather than producing a
  confirmation-bias-laden "plan."
input:
  prompt: >
    We've built an AI writing assistant for sales reps. We know it's going to
    save them 2 hours a week — our founder tested it with his old team and they
    loved it. We just need a quick discovery plan to prove this to investors and
    get sales reps excited before launch. Can you give me a 2-week plan to
    validate that reps will love this and that 2-hour saving is real?
  context: >
    B2B sales-tech startup. Pre-PMF. Founder-led testing with a non-representative
    sample (founder's former colleagues). The "discovery" ask is actually a
    validation exercise for a predetermined conclusion. No unbiased research has
    been conducted.
expected:
  - The skill explicitly flags that the request is framed as confirmation rather
    than genuine discovery and names the risk (confirmation bias, biased sample).
  - The skill declines to produce a "prove our idea" plan, and instead reframes
    the Discovery Goal as a neutral question (e.g., "We need to understand the
    actual time-cost of sales rep writing tasks and whether they perceive it as
    a pain worth solving").
  - The plan includes at least one Explore-phase method that could falsify the
    hypothesis (e.g., interviews with reps who have NOT seen the product, or who
    were not recruited by the founder).
  - The plan does not simply comply with "2 hours saved" as a given — it treats
    this as an assumption to test, not a fact to prove.
  - The plan acknowledges what legitimate investor/launch validation looks like
    post-discovery (e.g., a separate usability test or beta) and positions the
    discovery plan as the prerequisite, not the substitute.
rubric:
  correctness: 0.5
  completeness: 0.25
  actionability: 0.25
weight: 1.0
---

This is the adversarial case: a user who explicitly asks for a plan to confirm
what they already believe. It tests whether the skill is intellectually honest
enough to name the anti-pattern rather than just producing what was asked for.
A weak output produces a cheerful "here's how to validate your idea" plan. A
strong output names the confirmation-bias trap, redirects to a neutral Discovery
Goal, and constructs a plan with genuine falsifiability — while remaining helpful
and not preachy. The correctness weight is heavier here because getting the
reframe right is the core behavior under test.
