# $ python learn/dataclass/04_field_options.py
# + field() options: repr=False, compare=False, and metadata.
# Step 4: fine-tune which fields show up in __repr__/__eq__.

from dataclasses import dataclass, field
import math
import itertools

_counter = itertools.count(1)


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Circle:
    radius: float
    center: Point = field(default_factory=lambda: Point(0, 0))
    color: str = "black"
    area: float = field(init=False)
    id: int = field(default_factory=lambda: next(_counter), repr=False, compare=False)  # Step 4: hidden from repr/eq
    units: str = field(default="cm", metadata={"unit_system": "metric"})                 # Step 4: arbitrary metadata

    def __post_init__(self):
        self.area = math.pi * self.radius ** 2


if __name__ == "__main__":
    p1 = Point(1, 2)
    print(p1)

    c1 = Circle(radius=5)
    c2 = Circle(radius=5, color="black")  # Step 4: differs only in id -> still equal, since id has compare=False
    print(c1)
    print(c1 == c2)
    print(f"id: {c1.id}, metadata: {Circle.__dataclass_fields__['units'].metadata}")
