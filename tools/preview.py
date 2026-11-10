"""Builds the README gallery: preview/<category>.png sheets, preview/banner.png, preview/walk.gif
and docs/catalog.md (every asset id with its English title and description, grouped like the sheets).
Run after tools/build.py.

Usage: python tools/preview.py
"""
import json

from PIL import Image, ImageDraw

import kit32
from pixlib import ROOT, Palette

DIST = ROOT / "dist"
OUT = ROOT / "preview"
SCALE = 4
COLS = 10
CELL = 32 * SCALE
LABEL = 14
PAD = 6
BG, CARD, INK = (34, 36, 46, 255), (200, 205, 215, 255), (225, 228, 236, 255)

ORDER = ["characters", "monsters", "animals", "items", "props", "nature", "buildings", "effects", "ui", "tiles"]
NAMES = {"characters": "Characters", "monsters": "Monsters", "animals": "Animals", "items": "Items and equipment",
         "props": "Props and furniture", "nature": "Nature", "buildings": "Buildings", "effects": "Effects",
         "ui": "UI and status icons", "tiles": "Tiles"}
HAND_DRAWN = {  # the first eleven sprites were typed as .sprite grids, before the kit32 templates existed
    "hero": "characters", "slime": "monsters", "bat": "monsters", "coin": "items", "potion": "items",
    "key": "items", "scroll": "items", "chest": "props", "torch": "props", "tile_grass": "tiles", "tile_stone": "tiles",
}
BANNER = ("mage_f slime_healer knight archer_f witch dragon_red priestess wolf treant samurai "
          "house tree_cherry waterfall chest_gold fireball portal skeleton_mage fairy golem shop").split()
WALKERS = ("hero mage_f knight archer_f witch priestess barbarian bard king princess ninja dwarf "
           "samurai wizard_old fairy goblin").split()


def load() -> dict:
    return {a["id"]: a for a in json.loads((DIST / "catalog.json").read_text(encoding="utf-8"))["assets"]}


def category(aid: str) -> str:
    return HAND_DRAWN.get(aid) or kit32.CATEGORY.get(aid, "props")


def frame(asset: dict, name: str | None = None) -> Image.Image:
    card = Image.new("RGBA", (32, 32), CARD)
    card.alpha_composite(Image.open(ROOT / asset["dir"] / (name or asset["base"])).convert("RGBA"))
    return card.resize((CELL, CELL), Image.NEAREST)


def sheet(assets: list[dict], labels: bool = True) -> Image.Image:
    rows = (len(assets) + COLS - 1) // COLS
    h = CELL + (LABEL if labels else 0)
    img = Image.new("RGBA", (PAD + COLS * (CELL + PAD), PAD + rows * (h + PAD)), BG)
    draw = ImageDraw.Draw(img)
    for i, a in enumerate(assets):
        x, y = PAD + (i % COLS) * (CELL + PAD), PAD + (i // COLS) * (h + PAD)
        img.paste(frame(a), (x, y))
        if labels:
            draw.text((x + 2, y + CELL + 2), a["id"][:21], fill=INK)
    return img


def walk_gif(assets: dict) -> None:
    walkers = [assets[w] for w in WALKERS if w in assets]
    cols = 8
    rows = (len(walkers) + cols - 1) // cols
    frames = []
    for i in range(4):
        img = Image.new("RGBA", (PAD + cols * (CELL + PAD), PAD + rows * (CELL + PAD)), BG)
        for j, a in enumerate(walkers):
            img.paste(frame(a, f"{a['id']}_walk_{i}.png"), (PAD + (j % cols) * (CELL + PAD), PAD + (j // cols) * (CELL + PAD)))
        frames.append(img.convert("RGB").quantize(colors=128, method=Image.Quantize.MEDIANCUT))
    frames[0].save(OUT / "walk.gif", save_all=True, append_images=frames[1:], duration=150, loop=0, optimize=False)


def palette_strip() -> None:
    colors = Palette.load(ROOT / "styles" / "chibi32" / "palette.txt").colors
    sw = 24
    img = Image.new("RGBA", (PAD + len(colors) * (sw + 2), sw + 2 * PAD + LABEL), BG)
    draw = ImageDraw.Draw(img)
    for i, (key, rgb) in enumerate(colors.items()):
        x = PAD + i * (sw + 2)
        draw.rectangle((x, PAD, x + sw - 1, PAD + sw - 1), fill=(*rgb, 255))
        draw.text((x + 8, PAD + sw + 2), key, fill=INK)
    img.save(OUT / "palette.png")


def main() -> None:
    assets = load()
    OUT.mkdir(exist_ok=True)
    groups = {c: [] for c in ORDER}
    for aid in sorted(assets):
        groups[category(aid)].append(assets[aid])
    for c, items in groups.items():
        sheet(items).save(OUT / f"{c}.png")
        print(f"{c}: {len(items)}")
    sheet([assets[a] for a in BANNER], labels=False).save(OUT / "banner.png")
    walk_gif(assets)
    palette_strip()

    lines = ["# Asset catalog", "", f"{len(assets)} assets. Descriptions are in Korean, the language the set was "
             "briefed in; titles are in English. Files for each id are in `dist/<id>/`.", ""]
    for c, items in groups.items():
        lines += [f"## {NAMES[c]} ({len(items)})", "", f"![{NAMES[c]}](../preview/{c}.png)", "",
                  "| id | title | description |", "|---|---|---|"]
        for a in items:
            desc = kit32.SPECS.get(a["id"], ("",))[0]
            lines.append(f"| `{a['id']}` | {a['title']} | {desc} |")
        lines.append("")
    (ROOT / "docs" / "catalog.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"total: {len(assets)}")


if __name__ == "__main__":
    main()
