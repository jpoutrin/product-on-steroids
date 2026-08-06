---
name: storyboard
description: >
  Produce a narrative frame-by-frame storyboard showing how a specific user
  experiences a product scenario — with context, actions, emotions, and PM
  annotations at each step. Use when communicating a proposed UX flow to
  engineers or designers without a live prototype, surfacing pain points and
  delight moments in a new feature, or aligning the team on the exact problem
  a design is solving.
version: 0.1.0
type: component
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/storyboard/template.md
---

# Storyboard a User Scenario

## Purpose
Produce a 5–8 frame narrative storyboard — a sequence of annotated scenes —
that makes a specific user scenario concrete and emotionally legible for
engineers, designers, and stakeholders. Each frame shows what the user sees,
what they do, how they feel, and what that moment reveals for product design.
The output drives shared understanding of a proposed flow and surfaces friction
or delight before any code is written.

**When NOT to use:** mapping the full end-to-end lifecycle across many
touchpoints (use `customer-journey-map`); describing *who* the user is in
aggregate (use `user-personas`); planning what discovery research to run (use
`discovery-process`). A storyboard narrates *one specific scenario in depth* —
if the scope is broader than a single interaction arc, split it or use a
different artifact.

## Inputs
- **Required:** the scenario to storyboard — a brief description of the
  situation (who the user is, what they are trying to do, what product/feature
  is involved). If the scenario is missing, ask: "Who is the user and what are
  they trying to accomplish in this storyboard?"
- **Optional:**
  - Persona details (role, familiarity with the product) — default: infer from
    scenario context.
  - Target audience for the storyboard (engineers, designers, leadership) —
    default: cross-functional team; adjust annotation depth accordingly.
  - Number of frames requested — default: 5–8; fewer compresses; more than 8
    risks losing narrative focus, warn the PM.
  - Known pain points or hypotheses to test — include these as annotation hooks
    if provided.

## Output Contract
The deliverable is a **storyboard document** structured as a header + sequence
of numbered frames (see `template.md`):

1. **Storyboard Header** — scenario title, persona snapshot (name, role, goal),
   and a one-sentence arc summary (trigger → action → outcome).
2. **Frame 1 … N** (5–8 frames) — each frame contains four sub-sections:
   - **Scene** — describe the visual and physical/digital context in 2–4
     sentences of prose (what the user sees, where they are).
   - **Action** — what the user does next (one concrete action).
   - **Emotion** — how the user feels at this moment; use a plain label from
     Plutchik's wheel or simple terms (e.g., *anticipation*, *frustration*,
     *relief*, *confusion*) plus one explanatory sentence.
   - **Annotation** — PM note: what this moment reveals about the design, a
     risk, an assumption, or a design decision that needs an answer.
3. **Takeaways** — 3–5 bullet PM observations derived from the arc: friction
   points, delight moments, open design questions, and recommended next steps.

Format: Markdown, one `##` heading per frame, `###` sub-sections. Length: roughly
one page of prose.

**GOOD (excerpt):**
> ## Frame 3 — The First Blocker
>
> ### Scene
> Marcus opens the task assignment panel. He sees a long dropdown of teammate
> names with no search filter. The list takes two seconds to load.
>
> ### Action
> He scrolls through the full list to find "Aisha", selects her, and clicks
> Assign.
>
> ### Emotion
> *Mild frustration* — the delay and scroll break his flow; he expected instant
> search.
>
> ### Annotation
> **PM note:** No search-in-dropdown is a known friction point for teams > 15
> people. This is worth a usability test before shipping. Hypothesis: adding
> autocomplete search here reduces assignment time by ~40%.

**BAD (excerpt):**
> Frame 3: User clicks assign and it works. They feel good.
>
> — fails: no scene context, action is vague, emotion is ungrounded, annotation
> is absent — the PM learns nothing.

## Process
1. **Identify the scenario arc** — confirm who the persona is, what triggers
   the scenario, and what the desired outcome is. If unclear, ask before
   proceeding.
2. **Sketch the frame spine** — list 5–8 key moments that cover trigger →
   engagement → first friction → recovery/action → outcome. Each moment should
   change the user's state in some way.
3. **Write each frame** — for each moment, write Scene, Action, Emotion, and
   Annotation in order. Scene is descriptive; Action is one concrete step;
   Emotion uses a named label plus a one-sentence explanation; Annotation
   surfaces the PM insight, question, or risk.
4. **Maintain emotional honesty** — include at least one frustration or
   confusion frame unless the scenario is genuinely frictionless (rare). A
   storyboard that only shows delight is not useful for design.
5. **Balance frame density** — early frames establish context (1–2), middle
   frames carry the main interaction arc (2–4), final frames show resolution
   and outcome (1–2).
6. **Write Takeaways** — synthesize 3–5 PM-level observations from the arc:
   where friction occurs, what assumptions are embedded in the flow, what
   questions need answers before the design is finalized.
7. Run the Quality Bar below; revise any item that fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The storyboard has **5–8 frames** covering a complete arc (trigger →
  action → outcome); fewer than 5 or more than 8 triggers a warning to the PM.
- [ ] Every frame has all four sub-sections: **Scene, Action, Emotion,
  Annotation** — none missing.
- [ ] At least one frame contains a **negative or mixed emotion** (frustration,
  confusion, anxiety) — a purely positive arc is flagged as likely unrealistic.
- [ ] Each Emotion uses a **named label** (not just "feels good") plus an
  explanatory sentence.
- [ ] Each Annotation contains a **PM-level insight, question, or risk** — not
  a paraphrase of the scene.
- [ ] The Takeaways section has **3–5 bullets** grounded in specific frame
  observations.
- [ ] If the output is written to a file, it follows `template.md` — all
  required sections present in order (a skill-scoped hook re-checks this on
  write).

## Validation & Eval
Scenario cards live in `evals/`:
- `storyboard-happy` — B2B SaaS onboarding flow, 6-frame storyboard with full
  emotional arc and PM annotations.
- `storyboard-edge` — abstract AI-assisted feature; skill must translate
  capability into concrete human moments without inventing facts.
- `storyboard-adversarial` — PM requests a storyboard that "shows users will
  love it"; skill must stay honest and include friction frames.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `customer-journey-map` — maps the full multi-touchpoint lifecycle; use when
  scope is broader than one scenario arc.
- `user-personas` — describes who the user is; persona details feed the
  storyboard's persona snapshot and emotional grounding.
- `discovery-process` — plans what research to run; storyboard outputs (pain
  points, open questions) can seed discovery research priorities.

### External Frameworks
- Robert McKee, *Story* (1997) — scene-action-emotion narrative structure that
  underpins the frame format; every scene changes a user's state.
- Robert Plutchik, *Emotion: Theory, Research, and Experience* (1980) —
  Plutchik's Wheel of Emotions provides the vocabulary for the Emotion
  sub-section (anticipation, joy, trust, fear, surprise, sadness, disgust,
  anger, and their combinations).
- IDEO, *The Field Guide to Human-Centered Design* (2015) — storyboarding as a
  prototyping tool for communicating user scenarios before building; establishes
  the PM annotation convention of surfacing design questions per frame.
