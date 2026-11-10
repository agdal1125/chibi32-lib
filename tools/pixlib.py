"""Reads palette and .sprite sources and composes frames. Shared by build.py and check.py."""
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUTLINE_KEY = "K"


@dataclass(frozen=True)
class Palette:
    colors: dict[str, tuple[int, int, int]]

    @classmethod
    def load(cls, path: Path) -> "Palette":
        colors = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            key, hexcode = line.split()[:2]
            if len(key) != 1 or key == "." or key in colors:
                raise ValueError(f"{path}: bad or duplicate key {key!r}")
            colors[key] = tuple(int(hexcode[i:i + 2], 16) for i in (0, 2, 4))
        if OUTLINE_KEY not in colors:
            raise ValueError(f"{path}: palette needs outline key {OUTLINE_KEY}")
        return cls(colors)


@dataclass(frozen=True)
class Placement:
    part: str
    x: int
    y: int
    outline: bool


@dataclass
class Sprite:
    path: Path
    meta: dict[str, str]
    parts: dict[str, list[str]] = field(default_factory=dict)
    frames: dict[str, list[Placement]] = field(default_factory=dict)
    anims: dict[str, list[tuple[str, int]]] = field(default_factory=dict)

    @property
    def id(self) -> str:
        return self.meta["id"]

    @property
    def size(self) -> tuple[int, int]:
        w, h = self.meta["size"].split()
        return int(w), int(h)

    @property
    def anchor(self) -> tuple[int, int]:
        x, y = self.meta["anchor"].split()
        return int(x), int(y)

    @property
    def margin(self) -> int:
        """Transparent pixels required along the frame border (meta `margin`, default 1)."""
        return int(self.meta.get("margin", 1))

    @property
    def bbox(self) -> tuple[int, int] | None:
        """Exact size of the opaque area of every frame (meta `bbox`), when the asset fixes one."""
        if "bbox" not in self.meta:
            return None
        w, h = self.meta["bbox"].split()
        return int(w), int(h)

    def palette(self) -> Palette:
        return Palette.load((self.path.parent / self.meta["palette"]).resolve())

    def render(self, frame: str, palette: Palette) -> Image.Image:
        """Each placement is outlined on its own before being drawn, so overlapping parts get a separating line."""
        w, h = self.size
        grid = [["."] * w for _ in range(h)]
        for p in self.frames[frame]:
            cells = [(p.x + cx, p.y + cy, key)
                     for cy, row in enumerate(self.parts[p.part])
                     for cx, key in enumerate(row) if key != "."]
            for x, y, _ in cells:
                if not (0 <= x < w and 0 <= y < h):
                    raise ValueError(f"{self.id}/{frame}: part {p.part} leaves the canvas at {x},{y}")
            if p.outline:
                filled = {(x, y) for x, y, _ in cells}
                for x, y in filled:
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if (nx, ny) in filled:
                            continue
                        if not (0 <= nx < w and 0 <= ny < h):
                            raise ValueError(f"{self.id}/{frame}: outline of {p.part} leaves the canvas")
                        grid[ny][nx] = OUTLINE_KEY
            for x, y, key in cells:
                grid[y][x] = key
        img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        px = img.load()
        for y, row in enumerate(grid):
            for x, key in enumerate(row):
                if key != ".":
                    px[x, y] = (*palette.colors[key], 255)
        return img


def load_sprite(path: Path) -> Sprite:
    sprite = Sprite(path=path, meta={})
    section, name, buf = None, None, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section, _, name = line[1:-1].partition(" ")
            if section == "part":
                buf = sprite.parts.setdefault(name, [])
            elif section == "frame":
                sprite.frames[name] = []
            elif section == "anim":
                sprite.anims[name] = []
            elif section != "meta":
                raise ValueError(f"{path}: unknown section {section}")
            continue
        if not line.strip():
            continue
        if section == "meta":
            k, _, v = line.partition("=")
            sprite.meta[k.strip()] = v.strip()
        elif section == "part":
            buf.append(line.strip())
        elif section == "frame":
            bits = line.split()
            sprite.frames[name].append(Placement(bits[0], int(bits[1]), int(bits[2]), "nooutline" not in bits[3:]))
        elif section == "anim":
            frame, ms = line.split()
            sprite.anims[name].append((frame, int(ms)))
    for part, rows in sprite.parts.items():
        if len({len(r) for r in rows}) != 1:
            raise ValueError(f"{path}: part {part} has rows of different widths")
    for frame, placements in sprite.frames.items():
        for p in placements:
            if p.part not in sprite.parts:
                raise ValueError(f"{path}: frame {frame} uses missing part {p.part}")
    for anim, seq in sprite.anims.items():
        for frame, _ in seq:
            if frame not in sprite.frames:
                raise ValueError(f"{path}: anim {anim} uses missing frame {frame}")
    return sprite


def all_sprites() -> list[Sprite]:
    return [load_sprite(p) for p in sorted((ROOT / "assets").glob("*/*.sprite"))]
