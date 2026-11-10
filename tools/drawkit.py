"""Drawing helpers for assets/<id>/recipe.py.

A recipe paints palette keys into layers with shapes, sphere or cylinder shading and tapered hair locks.
Recipe.to_text() turns the layers into a .sprite file: one part per layer, cropped to its pixels.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable, Iterable

Pixel = tuple[int, int]
Vec3 = tuple[float, float, float]
Normal = Callable[[int, int], Vec3]


def normalize(v: Vec3) -> Vec3:
    n = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]) or 1.0
    return (v[0] / n, v[1] / n, v[2] / n)


LIGHT = normalize((-0.55, -0.7, 0.45))  # from the upper left, a little toward the viewer


def lit(n: Vec3) -> float:
    """Cosine between a surface normal and the light: 1 faces the light, -1 faces away."""
    n = normalize(n)
    return n[0] * LIGHT[0] + n[1] * LIGHT[1] + n[2] * LIGHT[2]


def pick(value: float, tones: str, cuts: Iterable[float]) -> str:
    """Tones run from light to dark; cuts are the descending thresholds between neighbouring tones."""
    for key, cut in zip(tones, cuts):
        if value > cut:
            return key
    return tones[-1]


def sphere(cx: float, cy: float, r: float) -> Normal:
    def normal(x: int, y: int) -> Vec3:
        nx, ny = (x + .5 - cx) / r, (y + .5 - cy) / r
        d = nx * nx + ny * ny
        if d >= 1:
            s = math.sqrt(d)
            return (nx / s, ny / s, 0.0)
        return (nx, ny, math.sqrt(1 - d))
    return normal


def cylinder(cx: float, r: float, tilt: float = -0.3) -> Normal:
    """Upright cylinder; a negative tilt turns the surface up toward the light."""
    def normal(x: int, y: int) -> Vec3:
        nx = max(-1.0, min(1.0, (x + .5 - cx) / r))
        return (nx, tilt, math.sqrt(1 - nx * nx))
    return normal


def ellipse(cx: float, cy: float, rx: float, ry: float) -> set[Pixel]:
    return {(x, y)
            for y in range(math.floor(cy - ry), math.ceil(cy + ry) + 1)
            for x in range(math.floor(cx - rx), math.ceil(cx + rx) + 1)
            if ((x + .5 - cx) / rx) ** 2 + ((y + .5 - cy) / ry) ** 2 <= 1}


def polygon(points: list[tuple[float, float]]) -> set[Pixel]:
    """Pixels whose centers fall inside the polygon."""
    out: set[Pixel] = set()
    ys = [p[1] for p in points]
    for y in range(math.floor(min(ys)), math.ceil(max(ys)) + 1):
        cy = y + .5
        xs = sorted(x1 + (cy - y1) * (x2 - x1) / (y2 - y1)
                    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])
                    if (y1 <= cy < y2) or (y2 <= cy < y1))
        for a, b in zip(xs[::2], xs[1::2]):
            out.update((x, y) for x in range(math.ceil(a - .5), math.floor(b - .5) + 1))
    return out


@dataclass(frozen=True)
class Sample:
    t: float  # 0 at the root of the stroke, 1 at its tip
    side: float  # -1 to 1 across the stroke
    perp: tuple[float, float]  # unit vector across the stroke


def stroke(p0, p1, p2, w0: float, w1: float = 0.5, steps: int = 400) -> dict[Pixel, Sample]:
    """Pixels covered by a quadratic Bezier from p0 to p2 whose width tapers from w0 to w1."""
    best: dict[Pixel, float] = {}
    out: dict[Pixel, Sample] = {}
    for i in range(steps + 1):
        t = i / steps
        a, b, c = (1 - t) ** 2, 2 * (1 - t) * t, t * t
        x = a * p0[0] + b * p1[0] + c * p2[0]
        y = a * p0[1] + b * p1[1] + c * p2[1]
        dx = 2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
        dy = 2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
        length = math.hypot(dx, dy) or 1.0
        perp = (-dy / length, dx / length)
        half = max((w0 + (w1 - w0) * t) / 2, 0.3)
        for py in range(math.floor(y - half), math.ceil(y + half) + 1):
            for px in range(math.floor(x - half), math.ceil(x + half) + 1):
                ox, oy = px + .5 - x, py + .5 - y
                d = math.hypot(ox, oy)
                if d <= half and d < best.get((px, py), math.inf):
                    best[(px, py)] = d
                    out[(px, py)] = Sample(t, (ox * perp[0] + oy * perp[1]) / half, perp)
    return out


def depth(pixels: Iterable[Pixel], away: tuple[float, float] = (1.0, 1.0), limit: int = 12) -> dict[Pixel, int]:
    """Steps of `away` each pixel can take before it leaves the shape: 0 on the rim facing that way.
    With `away` pointing from the light, banding on depth stacks lighter copies of the shape shifted toward the light,
    so shadow collects as a crescent on the far side instead of hugging the whole outline."""
    shape = set(pixels)
    out = {}
    for x, y in shape:
        k = 1
        while k <= limit and (x + round(k * away[0]), y + round(k * away[1])) in shape:
            k += 1
        out[(x, y)] = k - 1
    return out


def strands(p0, p1, p2, w: float, offsets: tuple[float, ...] = (-0.22, 0.22)) -> list[Pixel]:
    """1px lines inside a lock, shifted across it by offset * width, so the lock splits into strands."""
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    n = math.hypot(dx, dy)
    ox, oy = -dy / n, dx / n
    lines = []
    for k in offsets:
        shifted = [(x + ox * k * w, y + oy * k * w) for x, y in (p0, p1, p2)]
        lines += [p for p, s in stroke(*shifted, 1.0, 1.0).items() if 0.25 < s.t < 0.85]
    return lines


class Layer:
    """One .sprite part. Pixels painted later replace earlier ones; '.' erases."""

    def __init__(self, name: str, outline: bool = True):
        self.name, self.outline = name, outline
        self.px: dict[Pixel, str] = {}
        self.owner: dict[Pixel, int] = {}
        self._locks = 0

    def set(self, p: Pixel, key: str) -> None:
        self.owner.pop(p, None)
        if key == ".":
            self.px.pop(p, None)
        else:
            self.px[p] = key

    def fill(self, pixels: Iterable[Pixel], key: str | Callable[[int, int], str]) -> None:
        for x, y in pixels:
            self.set((x, y), key(x, y) if callable(key) else key)

    def shade(self, pixels: Iterable[Pixel], normal: Normal, tones: str, cuts: Iterable[float]) -> None:
        cuts = tuple(cuts)
        self.fill(pixels, lambda x, y: pick(lit(normal(x, y)), tones, cuts))

    def rows(self, x0: int, y0: int, text: str) -> None:
        """A block of keys with its top-left at x0, y0. A space leaves the pixel alone; '.' erases it."""
        for dy, row in enumerate(text.strip("\n").split("\n")):
            for dx, key in enumerate(row):
                if key != " ":
                    self.set((x0 + dx, y0 + dy), key)

    def lock(self, samples: dict[Pixel, Sample], normal: Normal, tones: str, cuts: Iterable[float],
             bend: float = 0.8, shine: tuple[float, float, float, str] | None = None) -> None:
        """A hair lock: the head's normal tilted across the stroke, so each lock is lit on one side.
        shine = (t_from, t_to, min_light, key) paints a highlight band; bands of neighbouring locks line up into a ring."""
        cuts = tuple(cuts)
        self._locks += 1
        for p, s in samples.items():
            nx, ny, nz = normal(*p)
            v = lit((nx + bend * s.side * s.perp[0], ny + bend * s.side * s.perp[1], nz))
            key = pick(v, tones, cuts)
            if shine and shine[0] <= s.t <= shine[1] and v > shine[2]:
                key = shine[3]
            self.px[p] = key
            self.owner[p] = self._locks

    def cel(self, pixels: Iterable[Pixel], tones: str, cuts: Iterable[int], away: tuple[float, float] = (1.0, 1.0)) -> None:
        """Hard-edged bands from depth(): tones run light to dark, cuts are the descending depths between them."""
        cuts = tuple(cuts)
        for p, k in depth(pixels, away).items():
            self.set(p, next((key for key, cut in zip(tones, cuts) if k >= cut), tones[-1]))

    def despeckle(self) -> int:
        """Repaints every pixel that shares its key with none of its eight neighbours in the majority key around it.
        Shading thresholds leave such single pixels at band borders; at 1x they read as dirt. Run it before
        adding deliberate single pixels such as eye glints. Returns how many pixels it changed."""
        changed = {}
        for (x, y), key in self.px.items():
            around = [self.px[q] for q in ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy)
                      if q in self.px]
            if around and key not in around:
                changed[(x, y)] = max(sorted(set(around)), key=around.count)  # sorted: ties break the same way every run
        for p, key in changed.items():
            self.px[p] = key
        return len(changed)

    def edge(self) -> list[Pixel]:
        """Painted pixels with an empty side: the ones the automatic outline will touch."""
        return [(x, y) for x, y in self.px
                if any(q not in self.px for q in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))]

    def darken(self, pixels: Iterable[Pixel], darker: str) -> None:
        """Moves each painted pixel one step along `darker`, a light-to-dark run of keys."""
        for p in list(pixels):
            i = darker.find(self.px.get(p, "."))
            if 0 <= i < len(darker) - 1:
                self.px[p] = darker[i + 1]

    def lock_lines(self, darker: str) -> None:
        """Darkens a pixel one step when a lock painted later sits right above or left of it,
        so each lock casts a thin line on what lies under it."""
        under = [(x, y) for x, y in self.px
                 if any(q in self.px and self.owner.get(q, 0) > self.owner.get((x, y), 0)
                        for q in ((x, y - 1), (x - 1, y)))]
        self.darken(under, darker)

    def crop(self) -> tuple[int, int, list[str]]:
        xs = [x for x, _ in self.px]
        ys = [y for _, y in self.px]
        x0, y0 = min(xs), min(ys)
        return x0, y0, ["".join(self.px.get((x, y), ".") for x in range(x0, max(xs) + 1))
                        for y in range(y0, max(ys) + 1)]


@dataclass
class Recipe:
    meta: dict[str, str]
    layers: list[Layer]
    frames: dict[str, list[tuple[str, int, int]]]  # per frame: layer name and offset, back to front
    anims: dict[str, list[tuple[str, int]]] = field(default_factory=dict)

    def to_text(self, source: str) -> str:
        lines = [f"# generated from {source} by tools/draw.py; edit the recipe, not this file", "[meta]"]
        lines += [f"{k} = {v}" for k, v in self.meta.items()]
        origin = {}
        for layer in self.layers:
            x0, y0, grid = layer.crop()
            origin[layer.name] = (x0, y0, layer.outline)
            lines += ["", f"[part {layer.name}]", *grid]
        for frame, items in self.frames.items():
            lines += ["", f"[frame {frame}]"]
            for name, dx, dy in items:
                x0, y0, outline = origin[name]
                lines.append(f"{name} {x0 + dx} {y0 + dy}" + ("" if outline else " nooutline"))
        for anim, seq in self.anims.items():
            lines += ["", f"[anim {anim}]", *(f"{frame} {ms}" for frame, ms in seq)]
        return "\n".join(lines) + "\n"
