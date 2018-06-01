"""
The Facade pattern provides a simplified interface to a larger body of code, such as a class library.
It hides the complexities of the system and provides an interface to the client from which they can access the system.
"""


class SubsystemA:
    def operation_a(self): return "Subsystem A ready"


class SubsystemB:
    def operation_b(self): return "Subsystem B ready"


class Facade:
    def __init__(self):
        self.s_a = SubsystemA()
        self.s_b = SubsystemB()

    def start(self):
        return f"{self.s_a.operation_a()} and {self.s_b.operation_b()}"


# Usage
facade = Facade()
print(facade.start())
