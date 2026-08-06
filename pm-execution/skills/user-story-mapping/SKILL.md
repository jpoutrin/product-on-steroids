---
name: user-story-mapping
description: >
  Build a 2-D user story map that arranges the product backlog as a grid of
  activities (columns) × user steps (rows) with horizontal swim lanes for
  releases. Use when organizing a new or existing backlog around the user
  journey, deciding what to ship in each release, aligning a cross-functional
  team on scope, or preparing a story-mapping workshop.
version: 0.1.0
type: workflow
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/user-story-mapping/template.md
---

# Build a User Story Map

## Purpose
Produce a structured user story map — the 2-D visual backlog technique invented
by Jeff Patton — that organizes work as a grid:

- **Backbone (top row):** high-level activities users perform, left to right in
  journey order.
- **User tasks (walking skeleton):** the minimal set of tasks under each activity
  that complete an end-to-end flow.
- **Story slices (release rows):** detailed stories grouped into horizontal swim
  lanes, each lane representing one release or iteration.

The map makes the whole user journey visible at once so the team can make
deliberate release scope decisions — trading breadth vs. depth — rather than
prioritizing a flat list.

**When NOT to use:**
- Writing individual user stories from scratch → use `user-stories`.
- Splitting an oversized story into smaller ones → use `user-story-splitting`.
- Testing a strategic product bet → use `epic-hypothesis`.
- Simple sprint-level task ordering (no journey structure needed) → use
  `sprint-plan`.

## Inputs
- **Required:** a product or feature description that has a recognizable user
  journey — what a user is trying to accomplish end-to-end. If absent, ask:
  "Who is the primary user and what does a complete end-to-end session look like
  for them?"
- **Required:** a rough list of stories, epics, or features to map. If none
  provided, derive them from the journey description (and call this out
  explicitly).
- **Optional:** target releases or iterations (e.g. MVP, v1, v2). If not
  provided, infer a sensible 3-tier slice (Walking Skeleton / MVP / Later) and
  ask the user to confirm.
- **Optional:** explicit user personas or roles. If multiple users exist and
  none are specified, surface the primary actor and note secondary actors.
- **Optional:** a time horizon or team capacity context (helpful for realistic
  slice sizing). Default: no capacity constraint assumed.

## Output Contract
The deliverable is a **user story map document** structured as (see
`template.md`):

1. **Map Overview** — one-sentence goal, primary user(s), and scope boundaries
   (what is in and out of this map).
2. **Backbone — Activities** — the ordered list of top-level activities (column
   headers) the user performs across the full journey, each with a brief
   description.
3. **Walking Skeleton** — for each activity, the single minimal task that must
   exist in any viable release; together these tasks form the thinnest end-to-end
   experience.
4. **Release Slices** — numbered swim lanes (Release 1, Release 2, …) listing
   the stories assigned to each lane under each activity, with a one-line scope
   statement per release.
5. **Deferred / Out-of-Scope Stories** — stories explicitly excluded from all
   releases, with a one-line rationale.
6. **Open Questions** — unresolved assumptions or gaps the team must answer
   before implementation begins.

Format: structured markdown with a table or structured list per section. Length:
1–3 pages depending on map depth. Every story is placed in exactly one swim lane
or in the Deferred section — no story is left unplaced.

**GOOD (excerpt):**
> **Activity 3 — Search & Discover**
> *Walking skeleton:* As a buyer, I can search for items by keyword so I get
> relevant results.
>
> **Release 1 (MVP):**
> - Keyword search with basic relevance ranking
> - Filter by category
>
> **Release 2:**
> - Faceted filters (price range, rating)
> - Saved searches

**BAD (excerpt):**
> "User can search, filter, and get recommendations."
> — fails: no backbone decomposition, stories not split into releases, no
> walking skeleton identified, output is a flat bullet not a map.

## Process
1. **Identify the primary user and the narrative** — confirm who the user is and
   write the one-sentence goal: "As a <user>, I want to <accomplish goal>."
2. **Build the backbone** — list 4–8 high-level activities that span the full
   journey left to right. Activities are verb phrases at the user's level
   (e.g. "Sign Up", "Search & Discover", "Purchase", "Track Order").
3. **Lay the walking skeleton** — under each activity, identify the single
   minimal task a user must be able to perform for the journey to be viable.
   These tasks form one horizontal band across the map.
4. **Collect and place stories** — take all input stories/epics and assign each
   under the relevant activity column. If an input is an epic, decompose it
   into story-sized tasks.
5. **Slice releases** — draw horizontal swim lanes by grouping stories into
   releases. Apply the "would the user be stuck without this?" test: stories
   that block the minimal journey → Release 1; enhancements → later releases.
6. **Identify deferred work** — explicitly list stories left out of all planned
   releases and note why.
7. **Surface open questions** — note any assumption gaps, unclear scope, or
   dependencies that must be resolved before build.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The backbone has 4–8 activities in narrative (journey) order, not
  alphabetical or technical order.
- [ ] Every activity has at least one user task in the walking skeleton.
- [ ] Every input story is placed in exactly one release swim lane or explicitly
  deferred — no story is orphaned or double-placed.
- [ ] Release 1 (or the first slice) can stand alone as a usable, end-to-end
  experience, however minimal — it is not just a subset of features.
- [ ] Release swim lanes are named with a meaningful scope statement (not just
  "Phase 1").
- [ ] Deferred stories are listed separately with a rationale, not silently
  omitted.
- [ ] Open questions are surfaced rather than silently assumed away.
- [ ] If the map is written to a file, it follows `template.md` — all 6 sections
  present, in order, headings matching (a skill-scoped hook re-checks this on
  write).

## Validation & Eval
Scenario cards in `evals/`:
- `user-story-mapping-happy` — well-specified e-commerce product with a backlog
  of epics; tests full backbone + 3-release slice structure.
- `user-story-mapping-edge` — single-feature scope with no existing stories;
  tests story derivation from journey description and minimal 2-slice output.
- `user-story-mapping-adversarial` — request to map a backlog with no user
  journey context; tests whether the skill asks clarifying questions instead of
  producing a meaningless flat list.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-stories` — writes individual user stories; user story mapping organizes
  those stories into a release structure.
- `user-story-splitting` — splits large stories into smaller ones; the map
  identifies which stories need splitting before slicing.
- `epic-hypothesis` — validates whether an epic is worth building; maps the
  stories once the bet is confirmed.
- `sprint-plan` — assigns map-sliced stories to sprint iterations.

### External Frameworks
- Jeff Patton, *User Story Mapping* (O'Reilly, 2014) — the canonical source for
  the backbone/walking-skeleton/release-slice structure this skill implements.
- Jeff Patton & Peter Economy, *User Story Mapping* (2014), Chapter 3 — "the
  big picture" activity decomposition and narrative flow.
- Jared Spool, "The Anatomy of a User Story Map" — practical guidance on
  backbone granularity and slice thickness.
