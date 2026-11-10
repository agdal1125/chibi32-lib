"""Proves check.py catches broken output, so a PASS means something. Run: python -m unittest discover tests"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import build  # noqa: E402
import check  # noqa: E402
import draw  # noqa: E402


class CheckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        build.main()

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.dist = self.tmp / "dist"
        shutil.copytree(build.DIST, self.dist)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def errors(self):
        return check.check(self.dist)[0]

    def test_clean_build_passes(self):
        self.assertEqual(self.errors(), [])

    def test_off_palette_pixel_fails(self):
        f = self.dist / "hero" / "hero_walk_1.png"
        img = Image.open(f)
        img.putpixel((16, 16), (255, 0, 255, 255))
        img.save(f)
        self.assertTrue(any("not in the palette" in e for e in self.errors()))

    def test_semi_transparent_pixel_fails(self):
        f = self.dist / "hero" / "hero_base.png"
        img = Image.open(f)
        img.putpixel((16, 16), (26, 20, 32, 128))
        img.save(f)
        self.assertTrue(any("semi-transparent" in e for e in self.errors()))

    def test_wrong_frame_rect_fails(self):
        f = self.dist / "hero" / "hero_walk.json"
        meta = json.loads(f.read_text(encoding="utf-8"))
        meta["frames"][2]["x"] = 40
        f.write_text(json.dumps(meta), encoding="utf-8")
        self.assertTrue(any("differs from hero_walk_2.png" in e for e in self.errors()))

    def test_missing_file_fails(self):
        (self.dist / "hero" / "hero_walk_x8.gif").unlink()
        self.assertTrue(any("hero_walk_x8.gif" in e for e in self.errors()))

    def test_wrong_size_fails(self):
        f = self.dist / "hero" / "hero_walk_0.png"
        Image.open(f).crop((0, 0, 31, 32)).save(f)
        self.assertTrue(any("size" in e for e in self.errors()))

    def test_hand_edited_sprite_is_reported(self):
        assets = self.tmp / "assets"
        shutil.copytree(build.ROOT / "assets" / "slime_healer", assets / "slime_healer")
        self.assertEqual(draw.stale(assets), [])
        sprite = assets / "slime_healer" / "slime_healer.sprite"
        sprite.write_text(sprite.read_text(encoding="utf-8") + "# hand edit\n", encoding="utf-8")
        self.assertTrue(any("differs from recipe.py" in e for e in draw.stale(assets)))


if __name__ == "__main__":
    unittest.main()
