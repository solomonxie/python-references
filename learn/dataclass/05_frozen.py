# $ python learn/dataclass/05_frozen.py
# + frozen=True: immutable instances, and hashable once every field is hashable.
# Step 5: freeze both dataclasses; mutating raises, hashing works.

from dataclasses import dataclass, field, FrozenInstanceError
import math
import itertools

_counter = itertools.count(1)


@dataclass(frozen=True)          # Step 5: frozen -> immutable + auto __hash__
class Point:
    x: int
    y: int


@dataclass(frozen=True)          # Step 5: every field must be hashable for Circle itself to be hashable
class Circle:
    radius: float
    center: Point = field(default_factory=lambda: Point(0, 0))
    color: str = "black"
    area: float = field(init=False)
    id: int = field(default_factory=lambda: next(_counter), repr=False, compare=False)
    units: str = field(default="cm", metadata={"unit_system": "metric"})

    def __post_init__(self):
        object.__setattr__(self, "area", math.pi * self.radius ** 2)  # Step 5: frozen blocks self.x = ...


if __name__ == "__main__":
    p1 = Point(1, 2)
    print(p1, hash(p1))

    c1 = Circle(radius=5)
    print(c1)
    print(hash(c1))

    try:
        c1.color = "red"
    except FrozenInstanceError as e:
        print(f"mutation blocked: {e}")
