# $ python learn/dataclass/09_conversion.py
# + asdict/astuple to flatten a dataclass tree to plain data, and replace() for a modified copy.
# Step 9: asdict/astuple recurse into nested dataclasses; frozen instances use replace() instead of mutation.

from dataclasses import dataclass, field, FrozenInstanceError, asdict, astuple, replace
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
    def from_dict(cls, data: dict) -> "Circle":
        raw_center = data.pop("center", None)
        center = Point(**raw_center) if raw_center else Point(0, 0)
        return cls(center=center, **data)


@dataclass(frozen=True, order=True)
class DashedCircle(Circle):
    dash_pattern: str = "dashed"


if __name__ == "__main__":
    c = Circle(radius=4, center=Point(1, 1), color="blue")
    print(asdict(c))                # Step 9: recurses -> nested dict for center
    print(astuple(c))               # Step 9: recurses -> nested tuple for center

    c2 = replace(c, color="green")  # Step 9: frozen, so build a modified copy instead of mutating
    print(c2)
    print(c == c2)
