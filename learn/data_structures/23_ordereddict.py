"""
23. OrderedDict: Dictionary subclass that remembers the order entries were added.
From Python 3.7+, dictionaries are ordered by default, but OrderedDict has unique properties.
Time complexity: O(1) for operations, but with higher memory overhead.
"""

from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(f"Original OrderedDict: {od}")

# Change value of a key
od["a"] = 10
print(f"After updating 'a': {od}")

# Move an item to the end
od.move_to_end("b")
print(f"After moving 'b' to the end: {od}")

# Move an item to the beginning
od.move_to_end("c", last=False)
print(f"After moving 'c' to the beginning: {od}")

# OrderedDict vs regular dict (Python 3.7+)
# dict preserves order, but doesn't have move_to_end or popitem(last=False)
d = dict(a=1, b=2, c=3)
print(f"Regular dict: {d}")
