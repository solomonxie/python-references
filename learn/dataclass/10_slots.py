# $ python learn/dataclass/10_slots.py
# + slots=True: drop the per-instance __dict__ to save memory (and, without frozen, block new attributes).
# Step 10: needs Python 3.10+.

from dataclasses import dataclass, field, FrozenInstanceError, asdict, astuple, replace
import math
import itertools

_counter = itertools.count(1)


@dataclass(frozen=True, slots=True)              # Step 10
class Point:
    x: int
    y: int


@dataclass(frozen=True, order=True, slots=True)  # Step 10
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
    def from_dict(cls, data: dict) -> "Circle":
        raw_center = data.pop("center", None)
        center = Point(**raw_center) if raw_center else Point(0, 0)
        return cls(center=center, **data)


@dataclass(frozen=True, order=True, slots=True)
class DashedCircle(Circle):
    dash_pattern: str = "dashed"


if __name__ == "__main__":
    c = Circle(radius=4, center=Point(1, 1))
    print(c)
    print(hasattr(c, "__dict__"))     # Step 10: False -> no per-instance dict

    try:
        c.color = "red"               # Step 10: still frozen, so this is still blocked
    except FrozenInstanceError as e:
        print(f"blocked: {e}")
