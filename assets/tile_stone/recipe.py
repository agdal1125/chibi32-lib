"""tile_stone: seamless 32x32 dungeon stone-brick floor or wall tile.

Bricks are 16x8 with 1 px black mortar, every other row shifted by 8 px. Each brick is lit from the upper
left: light top row and left column, dark bottom row and right column, plus a few cracks and moss in the
mortar. The pattern divides 32 evenly, so the tile repeats without seams. No outline.
Edit this file and run tools/build.py; tile_stone.sprite is generated from it.
"""
import random

from drawkit import Layer, Recipe

N, BW, BH = 32, 16, 8


def key_at(x: int, y: int) -> str:
    row = y // BH
    bx = (x + (BW // 2) * (row % 2)) % BW  # column inside the brick, offset on odd rows
    by = y % BH
    if by == BH - 1 or bx == BW - 1:
        return "K"
    if by == 0 or bx == 0:
        return "M"
    if by == BH - 2 or bx == BW - 2:
        return "d"
    return "m"


def build() -> Recipe:
    rng = random.Random(3)
    stone = Layer("stone", outline=False)
    stone.fill(((x, y) for x in range(N) for y in range(N)), key_at)
    inner = [(x, y) for x in range(N) for y in range(N) if key_at(x, y) == "m"]
    for x, y in rng.sample(inner, 7):  # short cracks: one pixel and its right neighbour when it is also stone face
        stone.set((x, y), "d")
        if key_at((x + 1) % N, y) == "m":
            stone.set(((x + 1) % N, y), "d")
    mortar = [(x, y) for x in range(N) for y in range(N) if key_at(x, y) == "K"]
    for p in rng.sample(mortar, 6):
        stone.set(p, "e")
    meta = {"id": "tile_stone", "title": "Stone brick tile (seamless)", "size": "32 32",
            "anchor": "16 31", "margin": "0", "palette": "../../styles/chibi32/palette.txt"}
    return Recipe(meta=meta, layers=[stone], frames={"base": [("stone", 0, 0)]})
