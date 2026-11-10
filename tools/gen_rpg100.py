"""Writes assets/<id>/recipe.py and credits.json for every id in kit32.SPECS, . Descriptions and the gallery are written by tools/preview.py.
Usage: python tools/gen_rpg100.py
"""
import json
from pathlib import Path

import kit32
from pixlib import ROOT

RECIPE = '''"""{aid}: {desc}
Generated from tools/kit32.py; edit the spec there."""
from kit32 import make


def build():
    return make("{aid}")
'''

for aid, (desc, _) in kit32.SPECS.items():
    d = ROOT / "assets" / aid
    d.mkdir(exist_ok=True)
    (d / "recipe.py").write_text(RECIPE.format(aid=aid, desc=desc), encoding="utf-8", newline="\n")
    credits = {
        "id": aid,
        "authors": [
            {"name": "Project owner", "role": "art direction (asked for 100 fantasy RPG assets in the chibi32 style)"},
            {"name": "Claude (Anthropic) via Claude Code; Opus 5.5, Fable 5.1 and Fable 5.2 models were used across sessions", "role": "wrote the pixel grids and templates in tools/kit32.py"}],
        "created": "2026-11-08",
        "tools": ["tools/kit32.py (shared grids and recolor templates)", "tools/build.py (Python 3 + Pillow)"],
        "ai_usage": {"used": True,
                     "kind": "A language model wrote every pixel as text in shared templates, rendered them, and revised after looking at the render. No image-generation model was used.",
                     "terms_checked": False,
                     "note": "The owner has not yet reviewed whether the AI tool's terms allow distribution under the chosen license."},
        "references": [],
        "license": "UNDECIDED",
        "license_note": "See LICENSING.md. The owner picks the art license before the first release."}
    (d / "credits.json").write_text(json.dumps(credits, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(len(kit32.SPECS), "specs")
