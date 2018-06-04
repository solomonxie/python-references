# $ python learn/dataclass/07_inheritance.py
# + subclassing a dataclass: the subclass's fields are appended after the parent's.
# Step 7: extend Circle with an extra field.

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


@dataclass(frozen=True, order=True)     # Step 7: inherits every Circle field, then adds its own
class DashedCircle(Circle):
    dash_pattern: str = "dashed"        # Step 7: must have a default since parent fields already do


if __name__ == "__main__":
    c1 = Circle(radius=5)
    d1 = DashedCircle(radius=5, color="red")
    print(c1)
    print(d1)
    print(isinstance(d1, Circle))
