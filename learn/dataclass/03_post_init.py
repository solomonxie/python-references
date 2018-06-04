# $ python learn/dataclass/03_post_init.py
# + __post_init__ for fields computed after the generated __init__ runs.
# Step 3: derive a field from the others once __init__ has set them.

from dataclasses import dataclass, field
import math


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Circle:
    radius: float
    center: Point = field(default_factory=lambda: Point(0, 0))
    color: str = "black"
    area: float = field(init=False)   # Step 3: computed, so excluded from __init__

    def __post_init__(self):          # Step 3: runs right after the generated __init__
        self.area = math.pi * self.radius ** 2


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1)
    print(p1 == p2)

    c1 = Circle(radius=5)
    c2 = Circle(radius=3, color="red")
    print(c1)
    print(c2)
    print(f"area: {c1.area:.2f}")
