# Audit: Intended vs. Implemented — <System / Feature Name>

## Audit Scope

- **System / Feature audited:** <subsystem name and version>
- **Source-of-truth documents:** <list docs and their locations, e.g., permissions.md (line 12–45), architecture.md (section 3.2), feature spec v2.1>
- **Code reviewed:** <file paths and commit SHAs or date range>
- **Date of audit:** <date>
- **Auditor:** <name>

## Methodology

- **How intent was established:** <e.g., extracted documented claims from permissions.md as numbered rules; treated all docs as claims to verify, not as proof>
- **How implementation evidence was gathered:** <e.g., traced code paths from endpoint → guard → enforcement for each claim; cited file and line for every enforcement or absence>
- **Verification approach:** <e.g., followed unauthenticated requests through the full stack to confirm guards apply on every path>
- **Limitations and blind spots:** <e.g., did not test runtime behavior, only reviewed code; did not audit database-level constraints; did not test third-party library behavior>

## Findings Summary

| Documented Rule | Enforcement in Code | Status | Impact |
|-----------------|---------------------|--------|--------|
| <rule from docs> | <yes/no/partial + citation> | <enforced/gap/undocumented> | <none/cosmetic/boundary-crossing> |
| <...> | <...> | <...> | <...> |

## Detailed Gaps

### Gap 1: <Short Title>

**Documented intent** (from `<file>`, line <N>):
> <quote the exact requirement from the docs>

**Implemented reality** (file: `<path>`, lines <N–M>):
<describe what the code actually does; include a code snippet if it clarifies the gap>

**Impact:** <who is the attacker, who is the victim, what boundary is crossed (data / money / infrastructure / tenant), or is this cosmetic?>

**Concrete fix:** <what must change — code, docs, or both?>

---

### Gap 2: <Short Title>

...

## Undocumented-but-enforced Rules

- <rule the code enforces that the docs are silent on — indicates stale docs>

## Sign-off

**Summary:** <N> findings identified:
- <M> cross a boundary (access / data / tenant / cost) and require code changes.
- <K> require documentation updates only.
- <L> are cosmetic or internal inconsistencies.

**Next steps:** <what should happen to each gap — fix now, defer, deprioritize, or investigate further?>
