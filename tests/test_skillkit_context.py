import skillkit

TASK_IMPORT = {"skill": "product-vision", "plugin": "pm-strategy",
               "disposition": "IMPORT", "priority": "P1", "status": "todo", "line_no": 4}
TASK_GEN = {"skill": "roadmap-planning", "plugin": "pm-strategy",
            "disposition": "GENERATE", "priority": "P1", "status": "todo", "line_no": 5}

def test_build_pack_import_includes_source():
    pack = skillkit.build_pack(TASK_IMPORT, "BRIEF-BODY", "PHURYN-SOURCE-TEXT")
    assert "BRIEF-BODY" in pack
    assert "product-vision" in pack
    assert "PHURYN-SOURCE-TEXT" in pack
    assert "IMPORT" in pack

def test_build_pack_generate_has_reminder_no_source():
    pack = skillkit.build_pack(TASK_GEN, "BRIEF-BODY", None)
    assert "original" in pack.lower()
    assert "deanpeters" in pack.lower()

def test_alias_resolves_product_strategy_canvas():
    # even without the work/ repo present, the resolver applies the alias to the name
    assert skillkit.SOURCE_ALIAS["product-strategy-canvas"] == "product-strategy"
