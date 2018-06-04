# $ python learn/dataclass/06_ordering.py
# + order=True: generates __lt__/__le__/__gt__/__ge__ from field order.
# Step 6: make circles sortable by their field order (radius first).

from dataclasses import dataclass, field, FrozenInstanceError
import math
import itertools

_counter = itertools.count(1)


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True, order=True)   # Step 6: order=True compares fields left-to-right
class Circle:
    radius: float
    center: Point = field(default_factory=lambda: Point(0, 0))
    color: str = "black"
    area: float = field(init=False)
    id: int = field(default_factory=lambda: next(_counter), repr=False, compare=False)
    units: str = field(default="cm", metadata={"unit_system": "metric"})

    def __post_init__(self):
        object.__setattr__(self, "area", math.pi * self.radius ** 2)


if __name__ == "__main__":
    p1 = Point(1, 2)
    print(p1, hash(p1))

    c1 = Circle(radius=5)
    c2 = Circle(radius=3, color="red")
    print(c1 > c2)             # Step 6: radii differ (5 > 3), so later fields never get compared
    print(sorted([c1, c2]))    # Step 6: sorts ascending by radius
