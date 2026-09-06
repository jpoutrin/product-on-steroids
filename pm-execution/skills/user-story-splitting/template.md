# Story Splitting Plan: <Original Story Title>

## Original Story
> As a <role>, I want <capability>, so that <benefit>.

**Why oversized:** <which INVEST dimension(s) fail and why — e.g., "Violates S: estimated at 13 points across 3 workflow phases; also I: phases are tightly coupled in current form.">

## Split Pattern(s) Applied
**Primary pattern:** <SPIDR pattern name> — <one sentence on why it fits this story better than alternatives>

**Alternative(s) considered:** <pattern> — <why rejected or combined>

## Child Stories

### Story 1 — <Title>
> As a <role>, I want <capability>, so that <benefit>.

**Acceptance criteria:**
1. <specific, testable criterion>
2. <specific, testable criterion>
3. <specific, testable criterion>

---

### Story 2 — <Title>
> As a <role>, I want <capability>, so that <benefit>.

**Acceptance criteria:**
1. <specific, testable criterion>
2. <specific, testable criterion>
3. <specific, testable criterion>

---

### Story N — <Title>
> As a <role>, I want <capability>, so that <benefit>.

**Acceptance criteria:**
1. <specific, testable criterion>
2. <specific, testable criterion>

## Story Map
```
[Original Story]
├── Story 1 — <Title>  (Sprint N)
├── Story 2 — <Title>  (Sprint N)
├── Story 3 — <Title>  (Sprint N+1)
└── [Deferred] <capability> — see below
```

## Deferred / Out of Scope
| Deferred item | Rationale | Suggested future sprint |
|---------------|-----------|------------------------|
| <capability or AC> | <why deferred — e.g., "low frequency edge case; not needed for MVP"> | Sprint N+2 |

## Quality Check
| Story | Independent | Negotiable | Valuable | Estimable | Small | Testable |
|-------|:-----------:|:----------:|:--------:|:---------:|:-----:|:--------:|
| Story 1 — <Title> | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Story 2 — <Title> | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Story N — <Title> | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
