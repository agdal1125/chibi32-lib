"""Builds dist/ from assets/*/*.sprite: frame PNGs, spritesheets, JSON metadata, GIFs and the preview catalog.
Sprites that have a recipe.py are regenerated from it first.

Usage: python tools/build.py
"""
import json
import shutil

from PIL import Image

import draw
from pixlib import ROOT, Palette, Sprite, all_sprites

DIST = ROOT / "dist"
GIF_PREVIEW_SCALE = 8


def gif_frames(images: list[Image.Image], palette: Palette, scale: int) -> list[Image.Image]:
    """Index 0 is transparent and indexes 1.. follow the style palette, so the GIF holds exactly the palette colors."""
    lookup = {rgb: i + 1 for i, rgb in enumerate(palette.colors.values())}
    flat = [0, 0, 0] + [c for rgb in palette.colors.values() for c in rgb]
    out = []
    for img in images:
        p = Image.new("P", img.size)
        p.putpalette(flat)
        raw = img.tobytes()
        p.putdata([lookup[tuple(raw[i:i + 3])] if raw[i + 3] else 0 for i in range(0, len(raw), 4)])
        out.append(p.resize((img.width * scale, img.height * scale), Image.NEAREST) if scale > 1 else p)
    return out


def save_gif(path, frames: list[Image.Image], durations: list[int]) -> None:
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=durations,
                   loop=0, transparency=0, disposal=2, optimize=False)


def build_sprite(sprite: Sprite) -> dict:
    palette = sprite.palette()
    out = DIST / sprite.id
    out.mkdir(parents=True)
    w, h = sprite.size
    rendered = {name: sprite.render(name, palette) for name in sprite.frames}
    for name, img in rendered.items():
        img.save(out / f"{sprite.id}_{name}.png")

    animations = []
    for anim, seq in sprite.anims.items():
        sheet = Image.new("RGBA", (w * len(seq), h), (0, 0, 0, 0))
        frames = []
        for i, (name, ms) in enumerate(seq):
            sheet.paste(rendered[name], (i * w, 0))
            frames.append({"name": name, "file": f"{sprite.id}_{name}.png",
                           "x": i * w, "y": 0, "w": w, "h": h, "duration": ms})
        sheet_file = f"{sprite.id}_{anim}_sheet.png"
        sheet.save(out / sheet_file)
        durations = [ms for _, ms in seq]
        imgs = [rendered[name] for name, _ in seq]
        gif_file = f"{sprite.id}_{anim}.gif"
        gif_big = f"{sprite.id}_{anim}_x{GIF_PREVIEW_SCALE}.gif"
        save_gif(out / gif_file, gif_frames(imgs, palette, 1), durations)
        save_gif(out / gif_big, gif_frames(imgs, palette, GIF_PREVIEW_SCALE), durations)
        meta = {
            "id": sprite.id,
            "animation": anim,
            "image": sheet_file,
            "imageSize": {"w": sheet.width, "h": sheet.height},
            "frameSize": {"w": w, "h": h},
            "anchor": dict(zip("xy", sprite.anchor)),
            "loop": True,
            "palette": sprite.meta["palette"].split("/")[-2],
            "source": sprite.path.relative_to(ROOT).as_posix(),
            "frames": frames,
        }
        meta_file = f"{sprite.id}_{anim}.json"
        (out / meta_file).write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        animations.append({"name": anim, "sheet": sheet_file, "json": meta_file,
                           "gif": gif_file, "gifPreview": gif_big, "frames": frames})

    credits = json.loads((sprite.path.parent / "credits.json").read_text(encoding="utf-8"))
    return {
        "id": sprite.id,
        "title": sprite.meta["title"],
        "dir": f"dist/{sprite.id}",
        "size": {"w": w, "h": h},
        "base": f"{sprite.id}_base.png",
        "stills": [f"{sprite.id}_{n}.png" for n in rendered],
        "animations": animations,
        "palette": [{"key": k, "hex": "#%02x%02x%02x" % rgb} for k, rgb in palette.colors.items()],
        "credits": credits,
    }


def main() -> None:
    for path in draw.write_all():
        print(f"regenerated {path.relative_to(ROOT)} from its recipe")
    if DIST.exists():
        # On Windows a directory delete can stay pending while another process holds a handle, and the
        # pending delete then swallows folders created under the same name. Move it aside first.
        old = DIST.with_name("dist_old")
        if old.exists():
            shutil.rmtree(old)
        DIST.rename(old)
        shutil.rmtree(old, ignore_errors=True)
    DIST.mkdir()
    catalog = {"assets": [build_sprite(s) for s in all_sprites()]}
    text = json.dumps(catalog, indent=2, ensure_ascii=False)
    (DIST / "catalog.json").write_text(text + "\n", encoding="utf-8")
    (DIST / "catalog.js").write_text(f"window.CATALOG = {text};\n", encoding="utf-8")
    print(f"built {len(catalog['assets'])} asset(s) into {DIST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
