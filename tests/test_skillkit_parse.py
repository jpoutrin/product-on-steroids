import skillkit

FIXTURE = """\
## pm-strategy — Product Strategy

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| market-sizing | IMPORT | P1 | done |
| product-vision | IMPORT | P1 | todo |
| roadmap-planning | GENERATE | P1 | todo |
| lean-canvas | IMPORT | P2 | todo |

## pm-discovery — Customer Insight

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| interview-script | IMPORT | P1 | todo |

## Cross-cutting

| Item | Disposition | Priority | Status |
|------|-------------|----------|--------|
| workshop-facilitation (shared) | GENERATE | P1 | todo |
"""

def test_load_tasks_extracts_plugin_rows_only():
    tasks = skillkit.load_tasks(FIXTURE)
    names = [t["skill"] for t in tasks]
    assert names == [
        "market-sizing", "product-vision", "roadmap-planning",
        "lean-canvas", "interview-script",
    ]  # Cross-cutting row excluded (no pm- plugin)
    ms = tasks[0]
    assert ms["plugin"] == "pm-strategy"
    assert ms["disposition"] == "IMPORT"
    assert ms["priority"] == "P1"
    assert ms["status"] == "done"

def test_select_next_skips_done_and_respects_priority():
    tasks = skillkit.load_tasks(FIXTURE)
    nxt = skillkit.select_next(tasks)
    assert nxt["skill"] == "product-vision"  # first todo, P1, pm-strategy

def test_progress_report_counts():
    report = skillkit.progress_report(skillkit.load_tasks(FIXTURE))
    assert "pm-strategy" in report
    assert "1/4 done" in report  # 1 done of 4 pm-strategy skills
