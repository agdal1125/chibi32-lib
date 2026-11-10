"""Checks dist/ against the sources. Covers sizes, palette, transparency, frame coordinates, file references and credits.
It does not judge whether the art looks good.

Usage: python tools/check.py [dist_dir]
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageSequence

import draw
from pixlib import ROOT, all_sprites

CREDIT_FIELDS = ("id", "authors", "created", "tools", "ai_usage", "references", "license")


def same_pixels(a: Image.Image, b: Image.Image) -> bool:
    return a.size == b.size and a.convert("RGBA").tobytes() == b.convert("RGBA").tobytes()


def check_png(img: Image.Image, size, colors: set, label: str, margin: int = 1) -> list[str]:
    errors = []
    if img.size != size:
        errors.append(f"{label}: size {img.size}, expected {size}")
    if img.mode != "RGBA":
        errors.append(f"{label}: mode {img.mode}, expected RGBA")
        return errors
    w, h = img.size
    px = img.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a not in (0, 255):
                errors.append(f"{label}: semi-transparent pixel at {x},{y}")
                return errors
            if a and (r, g, b) not in colors:
                errors.append(f"{label}: color #{r:02x}{g:02x}{b:02x} at {x},{y} is not in the palette")
                return errors
    fw, fh = size
    for y in range(h):
        for x in range(w):
            cx, cy = x % fw, y % fh
            if px[x, y][3] and min(cx, cy, fw - 1 - cx, fh - 1 - cy) < margin:
                errors.append(f"{label}: pixel {x},{y} is inside the {margin}px frame border that must stay transparent")
                return errors
    return errors


def lowest_opaque_row(img: Image.Image) -> int:
    bbox = img.getchannel("A").getbbox()
    return bbox[3] - 1 if bbox else -1


def check(dist: Path) -> tuple[list[str], list[str]]:
    errors, notes = draw.stale(), []
    catalog_path = dist / "catalog.json"
    if not catalog_path.exists():
        return [f"{catalog_path} missing, run tools/build.py"], notes
    catalog = {a["id"]: a for a in json.loads(catalog_path.read_text(encoding="utf-8"))["assets"]}
    sprites = all_sprites()
    if set(catalog) != {s.id for s in sprites}:
        errors.append(f"catalog lists {sorted(catalog)}, sources are {sorted(s.id for s in sprites)}")

    for sprite in sprites:
        palette = sprite.palette()
        colors = set(palette.colors.values())
        size = sprite.size
        out = dist / sprite.id
        for part, rows in sprite.parts.items():
            bad = {k for row in rows for k in row if k != "." and k not in palette.colors}
            if bad:
                errors.append(f"{sprite.id}: part {part} uses keys {sorted(bad)} missing from the palette")

        for name in sprite.frames:
            f = out / f"{sprite.id}_{name}.png"
            if not f.exists():
                errors.append(f"{f.name}: missing")
                continue
            img = Image.open(f)
            errors += check_png(img, size, colors, f.name, sprite.margin)
            if not same_pixels(img, sprite.render(name, palette)):
                errors.append(f"{f.name}: differs from {sprite.path.name}, rebuild dist")
            if sprite.bbox:
                box = img.getchannel("A").getbbox() or (0, 0, 0, 0)
                got = (box[2] - box[0], box[3] - box[1])
                if got != sprite.bbox:
                    errors.append(f"{f.name}: character box {got[0]}x{got[1]}, expected {sprite.bbox[0]}x{sprite.bbox[1]}")
                elif name == "base":
                    notes.append(f"{sprite.id}: character box {got[0]}x{got[1]} at x {box[0]}..{box[2] - 1}, "
                                 f"y {box[1]}..{box[3] - 1} in a {size[0]}x{size[1]} frame")

        for anim, seq in sprite.anims.items():
            meta_path = out / f"{sprite.id}_{anim}.json"
            if not meta_path.exists():
                errors.append(f"{meta_path.name}: missing")
                continue
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            sheet_path = out / meta["image"]
            if not sheet_path.exists():
                errors.append(f"{meta_path.name}: image {meta['image']} missing")
                continue
            sheet = Image.open(sheet_path)
            errors += check_png(sheet, (size[0] * len(seq), size[1]), colors, sheet_path.name, sprite.margin)
            if (meta["imageSize"]["w"], meta["imageSize"]["h"]) != sheet.size:
                errors.append(f"{meta_path.name}: imageSize disagrees with {sheet_path.name}")
            ax, ay = meta["anchor"]["x"], meta["anchor"]["y"]
            if not (0 <= ax < size[0] and 0 <= ay < size[1]):
                errors.append(f"{meta_path.name}: anchor outside the frame")
            if [fr["name"] for fr in meta["frames"]] != [n for n, _ in seq]:
                errors.append(f"{meta_path.name}: frame order differs from the source")
            baselines = set()
            for fr in meta["frames"]:
                box = (fr["x"], fr["y"], fr["x"] + fr["w"], fr["y"] + fr["h"])
                if (fr["w"], fr["h"]) != size or box[2] > sheet.width or box[3] > sheet.height or min(box) < 0:
                    errors.append(f"{meta_path.name}: frame {fr['name']} rect {box} is wrong")
                    continue
                if not isinstance(fr["duration"], int) or fr["duration"] <= 0:
                    errors.append(f"{meta_path.name}: frame {fr['name']} duration {fr['duration']!r}")
                frame_file = out / fr["file"]
                if not frame_file.exists():
                    errors.append(f"{meta_path.name}: file {fr['file']} missing")
                    continue
                crop = sheet.crop(box)
                if not same_pixels(crop, Image.open(frame_file)):
                    errors.append(f"{meta_path.name}: sheet cell {fr['name']} differs from {fr['file']}")
                baselines.add(lowest_opaque_row(crop))
            if baselines != {ay + 1}:
                errors.append(f"{meta_path.name}: lowest outline rows {sorted(baselines)}, expected {ay + 1} (anchor y + outline)")
            notes.append(f"{sprite.id}/{anim}: {len(seq)} frames, {sum(ms for _, ms in seq)} ms per loop, feet on row {sorted(baselines)}")

            for gif_name, scale in ((f"{sprite.id}_{anim}.gif", 1), (f"{sprite.id}_{anim}_x8.gif", 8)):
                gif_path = out / gif_name
                if not gif_path.exists():
                    errors.append(f"{gif_name}: missing")
                    continue
                gif = Image.open(gif_path)
                gframes = [fr.convert("RGBA") for fr in ImageSequence.Iterator(gif)]
                if len(gframes) != len(seq):
                    errors.append(f"{gif_name}: {len(gframes)} frames, expected {len(seq)}")
                    continue
                for i, (name, ms) in enumerate(seq):
                    gif.seek(i)
                    if gif.info.get("duration") != ms:
                        errors.append(f"{gif_name}: frame {i} lasts {gif.info.get('duration')} ms, expected {ms}")
                    want = Image.open(out / f"{sprite.id}_{name}.png").resize((size[0] * scale, size[1] * scale), Image.NEAREST)
                    if not same_pixels(gframes[i], want):
                        errors.append(f"{gif_name}: frame {i} pixels differ from {sprite.id}_{name}.png")

        credits_path = sprite.path.parent / "credits.json"
        if not credits_path.exists():
            errors.append(f"{sprite.id}: credits.json missing")
        else:
            credits = json.loads(credits_path.read_text(encoding="utf-8"))
            missing = [k for k in CREDIT_FIELDS if k not in credits]
            if missing:
                errors.append(f"{sprite.id}: credits.json lacks {missing}")
            if credits.get("license") == "UNDECIDED":
                notes.append(f"{sprite.id}: art license is UNDECIDED, which blocks release but not this check")

        entry = catalog.get(sprite.id)
        if entry:
            refs = [entry["base"], *entry["stills"]]
            for a in entry["animations"]:
                refs += [a["sheet"], a["json"], a["gif"], a["gifPreview"], *(f["file"] for f in a["frames"])]
            for ref in refs:
                if not (out / ref).exists():
                    errors.append(f"catalog {sprite.id}: {ref} missing")
    return errors, notes


def main() -> int:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    errors, notes = check(dist)
    for n in notes:
        print(f"note  {n}")
    for e in errors:
        print(f"FAIL  {e}")
    print("PASS" if not errors else f"{len(errors)} failure(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
