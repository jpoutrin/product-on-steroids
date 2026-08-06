import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))   # import skillkit
sys.path.insert(0, str(ROOT / "tests"))      # import validate_plugins in-tree
