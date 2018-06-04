# $ python learn/dataclass/01_basic_fields.py
# Plain @dataclass: typed fields get auto __init__/__repr__/__eq__.
# Step 1: define a dataclass with typed fields.

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    print(p1)               # auto __repr__
    print(p1 == p2)          # auto __eq__, compares field values
