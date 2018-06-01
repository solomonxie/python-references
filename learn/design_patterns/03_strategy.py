"""
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
It allows the algorithm to vary independently from clients that use it, enabling dynamic switching of behaviors at runtime.
"""


class Strategy:
    def execute(self, a, b): pass


class AddStrategy(Strategy):
    def execute(self, a, b): return a + b


class MultiplyStrategy(Strategy):
    def execute(self, a, b): return a * b


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def run(self, a, b):
        return self.strategy.execute(a, b)


# Usage
calc = Context(AddStrategy())
print(calc.run(5, 3))
calc.strategy = MultiplyStrategy()
print(calc.run(5, 3))
