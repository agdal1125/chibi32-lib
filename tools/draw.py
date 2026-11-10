"""Generates assets/<id>/<id>.sprite from assets/<id>/recipe.py. tools/build.py runs this first.

Usage: python tools/draw.py
"""
import importlib.util
from pathlib import Path

from pixlib import ROOT

ASSETS = ROOT / "assets"


def recipes(assets: Path = ASSETS) -> list[Path]:
    return sorted(assets.glob("*/recipe.py"))


def generate(recipe_path: Path) -> tuple[Path, str]:
    spec = importlib.util.spec_from_file_location(f"recipe_{recipe_path.parent.name}", recipe_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    recipe = module.build()
    out = recipe_path.parent / f"{recipe.meta['id']}.sprite"
    return out, recipe.to_text(f"assets/{recipe_path.parent.name}/{recipe_path.name}")


def write_all(assets: Path = ASSETS) -> list[Path]:
    written = []
    for path in recipes(assets):
        out, text = generate(path)
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            out.write_text(text, encoding="utf-8", newline="\n")
            written.append(out)
    return written


def stale(assets: Path = ASSETS) -> list[str]:
    """Sprites that no longer match their recipe, for example after a hand edit that the next build would erase."""
    errors = []
    for path in recipes(assets):
        out, text = generate(path)
        if not out.exists() or out.read_text(encoding="utf-8") != text:
            errors.append(f"{path.parent.name}/{out.name} differs from {path.name}; edit the recipe and run tools/build.py")
    return errors


def main() -> None:
    written = write_all()
    print(f"{len(recipes())} recipe(s), {len(written)} sprite(s) rewritten")


if __name__ == "__main__":
    main()
