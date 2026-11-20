"""The character rig gives every character the same sheet: four animations in four directions."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import kit32  # noqa: E402
from drawkit import dotted, lumps  # noqa: E402
from pixlib import DIRECTIONS  # noqa: E402

FRAMES = {"idle": 2, "walk": 4, "attack": 3, "hurt": 2}


class CharacterSheetTest(unittest.TestCase):
    def test_every_character_has_each_animation_in_each_direction(self):
        ids = [aid for aid, category in kit32.CATEGORY.items() if category == "characters"]
        self.assertGreater(len(ids), 70)
        for aid in ids:
            anims = kit32.make(aid).anims
            got = {name: len(seq) for name, seq in anims.items()}
            want = {f"{kind}_{d}": n for kind, n in FRAMES.items() for d in DIRECTIONS}
            self.assertEqual(got, want, aid)

    def test_neighbouring_frames_differ(self):
        # A GIF merges identical neighbours, so a repeated frame would shorten the animation.
        for aid in ("hero", "monk", "zombie", "archer_f", "bard"):
            recipe = kit32.make(aid)
            for name, seq in recipe.anims.items():
                shown = [tuple(recipe.frames[frame]) for frame, _ in seq]
                for a, b in zip(shown, shown[1:]):
                    self.assertNotEqual(a, b, f"{aid}/{name}")


class LumpsTest(unittest.TestCase):
    def test_grid_is_rectangular_and_uses_only_its_tones(self):
        rows = lumps([(6, 5, 5, 4), (10, 6, 4, 3)], "Eeq", (0.3, -0.2), floor=7).split("\n")
        self.assertEqual(len({len(r) for r in rows}), 1)
        self.assertLessEqual(set("".join(rows)), set("Eeq."))
        self.assertLessEqual(len(rows), 8)

    def test_dots_land_only_on_painted_cells(self):
        self.assertEqual(dotted("E.\nEE", "R", [(1, 0), (1, 1)]), "E.\nER")


if __name__ == "__main__":
    unittest.main()
