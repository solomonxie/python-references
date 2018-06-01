"""
The Flyweight pattern minimizes memory usage by sharing as much data as possible with similar objects.
It is particularly useful when dealing with a large number of objects that have many common attributes.
"""


class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state


class FlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, shared_state):
        if shared_state not in cls._flyweights:
            cls._flyweights[shared_state] = Flyweight(shared_state)
        return cls._flyweights[shared_state]


# Usage
f1 = FlyweightFactory.get_flyweight("common")
f2 = FlyweightFactory.get_flyweight("common")
print(f"Are they the same flyweight? {f1 is f2}")
