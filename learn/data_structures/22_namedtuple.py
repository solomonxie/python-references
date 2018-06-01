"""
22. Namedtuple: Factory function for creating tuple subclasses with named fields.
A way to create data objects that are more readable than regular tuples.
"""

from collections import namedtuple

# Define a Point namedtuple
Point = namedtuple("Point", ["x", "y"])

# Create a Point instance
p = Point(10, 20)
print(f"Point: {p}")
print(f"x: {p.x}, y: {p.y}")

# Standard tuple operations work too
print(f"Index access: p[0] = {p[0]}, p[1] = {p[1]}")
print(f"Iterable: {[x for x in p]}")

# Use unpack
x, y = p
print(f"Unpacked: x={x}, y={y}")
