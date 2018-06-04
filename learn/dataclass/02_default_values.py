# $ python learn/dataclass/02_default_values.py
# + default values, and default_factory for mutable defaults.
# Step 2: give fields default values.

from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Circle:
    radius: float
    center: Point = field(default_factory=lambda: Point(0, 0))  # Step 2: mutable default needs default_factory
    color: str = "black"                                        # Step 2: plain default value


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1)
    print(p1 == p2)

    c1 = Circle(radius=5)
    c2 = Circle(radius=3, color="red")
    print(c1)
    print(c2)
