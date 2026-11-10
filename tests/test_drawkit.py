"""Behaviour of the drawkit helpers that recipes rely on. Run: python -m unittest discover tests"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from drawkit import Layer, depth  # noqa: E402


class DrawkitTest(unittest.TestCase):
    def test_despeckle_repaints_lone_pixels_and_keeps_clusters(self):
        layer = Layer("t")
        layer.fill({(x, y) for x in range(6) for y in range(6)}, "a")
        layer.set((1, 1), "b")  # alone among a's
        layer.fill({(3, 3), (4, 3), (3, 4), (4, 4)}, "c")  # a 2x2 cluster
        self.assertEqual(layer.despeckle(), 1)
        self.assertEqual(layer.px[(1, 1)], "a")
        self.assertEqual({layer.px[p] for p in ((3, 3), (4, 3), (3, 4), (4, 4))}, {"c"})

    def test_cel_puts_the_shadow_on_the_side_away_from_the_light(self):
        square = {(x, y) for x in range(8) for y in range(8)}
        self.assertEqual(depth(square, (1, 1))[(7, 3)], 0)
        layer = Layer("t")
        layer.cel(square, "LMD", (3, 1))
        self.assertEqual(layer.px[(0, 0)], "L")  # upper left faces the light
        self.assertEqual(layer.px[(7, 7)], "D")  # the lower right rim is darkest
        self.assertEqual(layer.px[(5, 5)], "M")
        self.assertEqual(layer.px[(0, 7)], "D")  # a 1px rim on the bottom row too, not all around the outline
        self.assertEqual(layer.px[(0, 3)], "L")  # the left edge stays light: no pillow shading


if __name__ == "__main__":
    unittest.main()
