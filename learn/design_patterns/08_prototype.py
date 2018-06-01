"""
The Prototype pattern creates new objects by copying an existing instance, also known as a prototype.
This approach is beneficial when creating a new instance is more costly than cloning an existing one.
"""

import copy


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


# Usage
p1 = Prototype([1, 2, 3])
p2 = p1.clone()
print(f"Original: {p1.value}, Clone: {p2.value}")
print(f"Are they the same object? {p1 is p2}")
