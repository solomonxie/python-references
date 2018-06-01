"""
The Decorator pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.
In Python, this is often implemented using class-based wrappers that augment the functionality of a base object.
"""


class Component:
    def operation(self):
        return "Base Component"


class Decorator:
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Decorated({self._component.operation()})"


# Usage
base = Component()
decorated = Decorator(base)
print(decorated.operation())
