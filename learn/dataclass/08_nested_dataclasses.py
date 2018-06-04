# $ python learn/dataclass/08_nested_dataclasses.py
# + building a nested dataclass tree from plain dicts (there is no auto-conversion).
# Step 8: Circle.center is already a nested Point; add a from_dict that builds it explicitly.

from dataclasses import dataclass, field, FrozenInstanceError
import math
import itertools

_counter = itertools.count(1)


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True, order=True)
class Circle:
    radius: float
    center: Point = field(default_factory=lambda: Point(0, 0))
    color: str = "black"
    area: float = field(init=False)
    id: int = field(default_factory=lambda: next(_counter), repr=False, compare=False)
    units: str = field(default="cm", metadata={"unit_system": "metric"})

    def __post_init__(self):
        object.__setattr__(self, "area", math.pi * self.radius ** 2)

    @classmethod
    def from_dict(cls, data: dict) -> "Circle":   # Step 8: dataclasses don't nest-convert dicts on their own
        raw_center = data.pop("center", None)
        center = Point(**raw_center) if raw_center else Point(0, 0)
        return cls(center=center, **data)


@dataclass(frozen=True, order=True)
class DashedCircle(Circle):
    dash_pattern: str = "dashed"


if __name__ == "__main__":
    raw = {"radius": 4, "color": "blue", "center": {"x": 1, "y": 1}}
    c = Circle.from_dict(dict(raw))          # Step 8: copy since from_dict pops from it
    print(c)

    bare = Circle(radius=4, center={"x": 1, "y": 1})    # Step 8: passing a dict directly bypasses Point entirely
    print(f"center type without from_dict: {type(bare.center).__name__}")
