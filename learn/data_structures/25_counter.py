"""
25. Counter: Dictionary subclass for counting hashable objects.
Useful for frequency counting and basic set-like operations.
"""

from collections import Counter

# Create a Counter from an iterable
c = Counter("abracadabra")
print(f"Original Counter: {c}")

# Most common elements
print(f"Top 2 most common: {c.most_common(2)}")

# Counts can be updated or accessed
print(f"Count for 'a': {c['a']}")
c.update("aaa")
print(f"After updating 'aaa': {c}")

# Counter arithmetic
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"Counter 1: {c1}")
print(f"Counter 2: {c2}")
print(f"Sum: {c1 + c2}")
print(f"Difference: {c1 - c2}")
print(f"Intersection: {c1 & c2}")
print(f"Union: {c1 | c2}")
