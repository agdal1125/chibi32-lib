"""tile_grass: seamless 32x32 grass ground tile for top-down maps.

Mid green base with light blade tufts, dark speckles and two small flowers. Every mark wraps around the
tile edge (x and y mod 32), so the tile repeats without seams. No outline: tiles sit edge to edge.
Edit this file and run tools/build.py; tile_grass.sprite is generated from it.
"""
import random

from drawkit import Layer, Recipe

N = 32
TUFT = ["E.E", "qEq"]
FLOWER = [".M.", "MGM", ".M."]


def stamp(layer: Layer, x0: int, y0: int, rows: list[str]) -> None:
    for dy, row in enumerate(rows):
        for dx, key in enumerate(row):
            if key != ".":
                layer.set(((x0 + dx) % N, (y0 + dy) % N), key)


def build() -> Recipe:
    rng = random.Random(7)
    ground = Layer("ground", outline=False)
    ground.fill(((x, y) for x in range(N) for y in range(N)), "e")
    for _ in range(40):
        ground.set((rng.randrange(N), rng.randrange(N)), "q")
    for _ in range(14):
        stamp(ground, rng.randrange(N), rng.randrange(N), TUFT)
    for x, y in ((6, 20), (23, 5)):
        stamp(ground, x, y, FLOWER)
    meta = {"id": "tile_grass", "title": "Grass ground tile (seamless)", "size": "32 32",
            "anchor": "16 31", "margin": "0", "palette": "../../styles/chibi32/palette.txt"}
    return Recipe(meta=meta, layers=[ground], frames={"base": [("ground", 0, 0)]})
