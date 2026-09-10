"""Each plugin ships its own copy of the hook scripts in scripts/skel/.

A drifted copy means one plugin silently enforces different rules than the
others. This test is the guard that keeps the six copies in lockstep.
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ["pm-strategy", "pm-discovery", "pm-gtm", "pm-execution", "pm-influence"]

# canonical file in scripts/skel/  ->  its path inside each plugin
COPIES = {
    "check_output_conformance.py": "scripts/check_output_conformance.py",
    "md_shape.py": "scripts/md_shape.py",
    "output_language.py": "hooks/output_language.py",
    "hooks.json": "hooks/hooks.json",
}


def _digest(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def test_every_plugin_copy_matches_skel():
    for src_name, rel in COPIES.items():
        src = ROOT / "scripts" / "skel" / src_name
        assert src.is_file(), f"canonical source missing: {src}"
        want = _digest(src)
        for plugin in PLUGINS:
            dst = ROOT / plugin / rel
            assert dst.is_file(), f"missing: {dst} — copy it from {src}"
            assert _digest(dst) == want, (
                f"{dst} has drifted from {src}. Re-copy it:\n"
                f"  for p in pm-*/; do cp {src.relative_to(ROOT)} "
                f"\"$p\"{rel}; done")
