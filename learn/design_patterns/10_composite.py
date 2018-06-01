"""
The Composite pattern allows you to compose objects into tree structures to represent part-whole hierarchies.
It lets clients treat individual objects and compositions of objects uniformly.
"""


class Graphic:
    def draw(self): pass


class Shape(Graphic):
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f"Drawing shape: {self.name}")


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def draw(self):
        for g in self.graphics:
            g.draw()


# Usage
circle = Shape("Circle")
square = Shape("Square")
composite = CompositeGraphic()
composite.add(circle)
composite.add(square)
composite.draw()
