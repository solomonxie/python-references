"""
The Visitor pattern represents an operation to be performed on the elements of an object structure.
It lets you define a new operation without changing the classes of the elements on which it operates.
"""


class Element:
    def accept(self, visitor): pass


class ConcreteElement(Element):
    def accept(self, visitor):
        visitor.visit(self)


class Visitor:
    def visit(self, element):
        print(f"Visiting {element.__class__.__name__}")


# Usage
el = ConcreteElement()
v = Visitor()
el.accept(v)
