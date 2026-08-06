---
name: press-release
description: >
  Pressure-test a product idea by writing it up as an Amazon-style Working
  Backwards press release plus an internal/external FAQ, before any build.
  Use when validating a new product or feature idea, deciding whether something
  is worth building, aligning a team on the customer and the "why," or kicking
  off discovery for an initiative.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/press-release/template.md
---

# Working Backwards Press Release + FAQ

## Purpose
Force clarity on a product idea *before it is built* by writing the artifact you
would publish the day it launches: a short, future-dated, customer-facing press
release (as if the product already exists and is loved), backed by an
internal/external FAQ that answers the hard questions. Writing the PR first
surfaces whether the idea is compelling, understandable, and worth doing — if you
can't write a crisp release, the idea isn't ready. Supports go/no-go, scoping, and
team alignment at the *front* of the funnel.

**When NOT to use:** an actual launch announcement or press collateral for a real,
shipping product (that is GTM launch work, not strategy) — this skill's output is
an internal thinking tool, never published. Also skip for sizing the opportunity
(use `market-sizing`), picking a first segment (use `beachhead-segment`), or
writing build requirements (use a PRD skill). The PR names the customer win; it
does not spec the plan.

## Inputs
- **Required:** the product/feature idea and its intended customer — who they are
  and the problem they have today. If missing, ask "who is this for and what can't
  they do today?" before drafting; do not invent a customer.
- **Optional:** the target launch timeframe (default: a plausible future date ~6–12
  months out), pricing/availability, a name for the product, known differentiators
  vs. today's alternatives, and the top objections you already expect. Absent
  these, draft with clearly labeled `[placeholder]` values and flag them as
  assumptions to confirm.

## Output Contract
The deliverable is a **Working Backwards document** — a one-page press release
followed by an FAQ (see `template.md`):

1. **Heading** — product name + a one-line benefit, written as a real headline.
2. **Subheading** — one sentence naming the target customer and the benefit they get.
3. **Dateline** — city and the (future) intended launch date.
4. **Problem paragraph** — the customer's problem today, from their point of view, in plain language (no internal jargon).
5. **Solution paragraph** — how the product solves it and how it works, concretely.
6. **Company/leader quote** — a spokesperson framing why this matters.
7. **Customer quote** — a named, plausible customer describing the before/after benefit in their words.
8. **How to get started** — the one obvious next step for a customer (availability, price, where to go).
9. **FAQ** — split into **External** (what a customer/press would ask: price, availability, how it differs from alternatives) and **Internal** (the hard build/viability questions: why now, biggest risk, what we'd cut, how we know customers want it, dependencies).

Format: the release reads as prose a customer could understand — **≤ 1 page /
~250–350 words**, hype-free; the FAQ is Q&A bullets. Every claimed benefit is
customer-framed and specific; unknowns are marked `[assumption]`, never faked as
fact.

**GOOD (excerpt):**
> **Nimbus lets small clinics get paid in a day, not a month.**
> *For solo and small medical practices drowning in insurance paperwork, Nimbus turns a 30-day reimbursement chase into a one-tap, next-day payout.*
> AUSTIN, TX — March 3, 2027 — ...
> "I used to spend six hours a week resubmitting rejected claims," said Dr. Lena Ortiz, who runs a two-person family practice. "With Nimbus I file once and I'm paid the next morning."
> *Internal FAQ — Biggest risk:* payer integrations. [assumption] We can cover 80% of US claims via 3 clearinghouses — to validate before build.

**BAD (excerpt):**
> "We are excited to announce a revolutionary next-gen AI platform that leverages synergies to disrupt the healthcare space and delight users."
> — fails: no named customer, no concrete problem, no before/after, buzzword hype, no FAQ, nothing falsifiable.

## Process
1. **Fix the customer & problem** — name exactly who it's for and what they can't do today; refuse to proceed on a vague "everyone."
2. **Write the heading & subheading** — product name, one-line benefit, and the customer it serves. If you can't write these cleanly, the idea needs sharpening — say so.
3. **Draft the release body** — dateline, problem (customer's voice), solution (how it works), a leader quote (why this matters), a named customer quote (before/after), and the "how to get started" step.
4. **Strip the hype** — remove buzzwords, superlatives, and internal jargon; keep it to ~250–350 words a real customer would understand.
5. **Write the External FAQ** — price, availability, and how it differs from what customers do today.
6. **Write the Internal FAQ** — why now, the single biggest risk, what you'd cut to ship, how you know customers want this, and key dependencies. Mark every unknown `[assumption]`.
7. **Judge worth-building** — from the drafted doc, state a plain go / refine / no-go read and the top thing to validate next.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The release is **future-dated** and written as if the product already exists and is loved (present-tense, launched).
- [ ] A **specific customer and a concrete problem** are named — not "everyone" and not a feature list.
- [ ] The **problem is in the customer's voice**, in plain language, free of internal jargon and buzzwords.
- [ ] There is both a **leader quote** and a **named, plausible customer quote** with a real before/after benefit.
- [ ] There is a clear **"how to get started"** next step (availability, price, or where to go).
- [ ] The FAQ has **both External and Internal** sections, and the Internal FAQ names the **biggest risk** and **how you know customers want it**.
- [ ] Every unknown is marked **`[assumption]`** rather than stated as fact.
- [ ] The release is **≤ ~1 page / 250–350 words** and hype-free.
- [ ] A plain **go / refine / no-go** read and the next thing to validate are stated.
- [ ] If written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `press-release-happy` — a well-specified B2B idea with a clear customer; produces a full release + both FAQs and a go/refine read.
- `press-release-edge` — a thin, early idea with unknown pricing/availability; the skill must draft with labeled `[assumption]`s rather than invent facts.
- `press-release-adversarial` — a hype-laden "AI platform for everyone" ask the skill must refuse to write as-is, forcing a named customer and concrete problem first.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — sizes the opportunity the press release argues is worth pursuing; run it to back the "why now."
- `beachhead-segment` — turns the release's named customer into the concrete first segment to build and sell for.

### External Frameworks
- Amazon "Working Backwards" (PR/FAQ) method — Colin Bryar & Bill Carr, *Working Backwards* (2021): start from a mock press release and FAQ and iterate until the idea is compelling before writing any code.
- Ian McAllister, "What is Amazon's approach to product development and product management?" (Quora) — the widely cited internal-PR template (heading, subheading, problem, solution, quotes, getting started) this skill's structure follows.
